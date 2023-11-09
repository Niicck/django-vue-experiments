<template>
  <div
    class="relative flex items-center space-x-3 rounded-lg border-4 border-green-600 bg-emerald-100 px-6 py-5 shadow-sm ring-green-600 hover:ring hover:ring-offset-2"
  >
    <div class="my-5 text-base leading-7 space-y-3">
      <p>This is a Vue component that has been loaded into a Django Template!</p>
      <div>
        {{ counter }}
      </div>
      <div @click="increment">Click me</div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
const counter = ref(0);

const increment = () => {
  counter.value += 1;
};
</script>
