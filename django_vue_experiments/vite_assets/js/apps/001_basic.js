import 'vite/modulepreload-polyfill'; // required for vite entrypoints

import { createApp, defineComponent } from 'vue';
import BasicBlock from '@/js/components/BasicBlock.vue';

const RootComponent = defineComponent({
  delimiters: ['[[', ']]'],
  components: {
    'basic-block': BasicBlock,
  },
});

const app = createApp(RootComponent);
app.mount('#vue-experiment-1');

export {};
