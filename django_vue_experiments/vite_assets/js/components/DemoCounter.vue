<template>
  <div
    class="relative flex items-center space-x-3 rounded-lg border-4 border-amber-600 bg-yellow-100 px-6 py-5 shadow-sm w-fit"
  >
    <div class="my-5 text-base leading-7 space-y-3 flex flex-col">
      <p class="pb-5">
        This is a Vue component that has been loaded into a Django Template!
      </p>
      <div class="flex flex-row mx-auto">
        <button class="button rounded-l bg-red-500 hover:bg-red-700" @click="decrement">
          -
        </button>
        <div class="count-display">{{ count }}</div>
        <button
          class="button rounded-r bg-green-500 hover:bg-green-700"
          @click="increment"
        >
          +
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
const count = ref(0);

const decrement = () => {
  count.value -= 1;
};

const increment = () => {
  count.value += 1;
};
</script>

<style>
.button {
  @apply text-white font-bold py-2 px-4;
}

.count-display {
  @apply px-4 py-2 text-lg font-semibold text-gray-700;
}
</style>
