from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class CSPFrameAncestorsMiddleware(MiddlewareMixin):
    """
    Middleware to set the Content Security Policy (CSP) 'frame-ancestors' directive.

    This middleware adds a CSP header to HTTP responses to control which sources
    can embed the current application within a <frame>, <iframe>, <embed>, or <object>.

    The default value is set to "'self'", which only allows framing by the same origin
    as the response.

    Additional frame-ancestors can be set by the EXTRA_CSP_FRAME_ANCESTORS settings
    variable, which should be a list of URLs.

    Example:
        EXTRA_CSP_FRAME_ANCESTORS = ["https://example.com"]
        {'Content-Security-Policy': "frame-ancestors 'self' https://example.com;}

    This will allow the current application to be framed by itself and 'https://example.com'.
    """

    def process_response(self, request, response):
        csp_frame_ancestors = ["'self'"]

        extra_frame_ancestors = getattr(settings, "EXTRA_CSP_FRAME_ANCESTORS", [])
        csp_frame_ancestors += extra_frame_ancestors

        csp_policy = f"frame-ancestors {' '.join(csp_frame_ancestors)};"
        response["Content-Security-Policy"] = csp_policy
        return response
