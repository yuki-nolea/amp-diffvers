<template>
  <div class="my-auto mx-0 ml-2">
    <UButton color="black" variant="solid" @click="props.signOut">Sign Out</UButton>
  </div>
</template>

<script setup lang="ts">
  const props = defineProps<{signOut: any}>();
</script>


<style scoped>

</style>