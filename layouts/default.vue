<template>
  <div class="grid grid-rows-[max-content_1fr_max-content] grid-cols-[1fr] min-h-screen w-full h-full">
    <CommonAppHeader class="header" :signOut="props.signOut"/>
    <slot class="body"/>
    <CommonAppFooter class="footer" />
  </div>
</template>

<script setup lang="ts">
  const props = defineProps<{signOut: any}>();
</script>

<style scoped>


</style>