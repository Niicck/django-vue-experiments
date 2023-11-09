/* eslint-disable @typescript-eslint/no-var-requires */
import { defineConfig, loadEnv } from 'vite';
import { resolve, join } from 'path';
import vue from '@vitejs/plugin-vue';

const INPUT_DIR = './django_vue_experiments/vite_assets';
const OUTPUT_DIR =
  './django_vue_experiments/vite_assets_dist/django_vue_experiments/vite';

const postcssConfig = {
  plugins: [
    require('postcss-import')(),
    require('postcss-simple-vars')(),
    require('tailwindcss/nesting')(),
    require('tailwindcss')(),
    require('autoprefixer')(),
  ],
};

export default defineConfig((mode) => {
  const env = loadEnv(mode, process.cwd(), '');
  return {
    plugins: [vue()],
    resolve: {
      alias: {
        '@': resolve(INPUT_DIR),
        'vue': 'vue/dist/vue.esm-bundler.js',
      },
    },
    root: resolve(INPUT_DIR),
    base: '/static/',
    css: {
      postcss: postcssConfig,
    },
    server: {
      host: '0.0.0.0',
      port: env.DJANGO_VITE_DEV_SERVER_PORT,
    },
    build: {
      manifest: true,
      emptyOutDir: true,
      target: 'es2015',
      outDir: resolve(OUTPUT_DIR),
      rollupOptions: {
        input: {
          css: join(INPUT_DIR, '/css/main.css.js'),
        },
        output: {
          chunkFileNames: undefined,
        },
      },
    },
  };
});
