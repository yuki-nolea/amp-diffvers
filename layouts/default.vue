<template>
  <div class="content">
    <CommonAppHeader class="header" :signOut="props.signOut"/>
    <slot class="body"/>
    <CommonAppFooter class="footer" />
  </div>
</template>

<script setup lang="ts">
  const props = defineProps<{signOut: any}>();
</script>

<style scoped>
  .content 
  {
    display: grid;
    width: 100%;
    height: 100%;
    grid-template-rows: max-content 1fr max-content;
    grid-template-columns: 1fr;
    min-height: 100vh;
  }

  .header
  {

  }

  .body
  {

  }

  .footer
  {

  }

</style>