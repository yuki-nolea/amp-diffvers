<template>
  <div class="home-page">
    <div class="content">
      <UTabs :items="items" class="w-full" />
    </div>
  </div>
</template>

<script setup lang="ts">
  const items = 
  ref([{
    label: 'Diff Versions',
    icon: 'icon-park-twotone:difference-set',
    content: 'This is the content shown for Tab1'
  }, {
    label: 'Note',
    icon: 'gridicons:notice-outline',
    content: 'And, this is the content for Tab2'
  }]);


</script>

<style scoped>
.home-page
{
  display: flex;
  flex-direction: column;
}

.content
{
  overflow: hidden;
}

</style>