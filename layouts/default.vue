<template>
  <div class="grid grid-rows-[max-content_auto_max-content] grid-cols-[1fr] min-h-screen w-full h-screen">
    <CommonAppHeader class="header" :signOut="props.signOut"/>
    <slot />
    <CommonAppFooter class="footer" />
  </div>
</template>

<script setup lang="ts">
  const props = defineProps<{signOut: any}>();
</script>

<style scoped>


</style>