import 'vite/modulepreload-polyfill'; // required for vite entrypoints

import { createApp, defineComponent } from 'vue';
import DemoCounter from '@/js/components/DemoCounter.vue';

const RootComponent = defineComponent({
  delimiters: ['[[', ']]'],
  components: {
    demoCounter: DemoCounter,
  },
});

const app = createApp(RootComponent);
app.mount('#vue-experiment-1');

export {};
