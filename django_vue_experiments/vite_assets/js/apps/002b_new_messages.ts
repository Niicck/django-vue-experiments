import 'vite/modulepreload-polyfill'; // required for vite entrypoints

import { createApp, defineComponent } from 'vue';
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import { VAlert } from 'vuetify/components';
import { aliases, mdi } from 'vuetify/iconsets/mdi-svg';

const vuetify = createVuetify({
  components: {
    VAlert,
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
  ssr: true,
});

const RootComponent = defineComponent({
  delimiters: ['[[', ']]'],
});

const app = createApp(RootComponent);
app.use(vuetify).mount('#vue-experiment-2b');

export {};
