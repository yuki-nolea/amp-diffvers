<template>
  <div class="flex flex-col overflow-hidden">
    <UTabs :items="items" :ui="{ wrapper: 'space-y-0 w-full h-full flex flex-col', container: 'w-full h-full', base: 'h-full' }">
      <template #diff-version>
        <ViewDiffVersions/>
      </template>
      <template #note>
        this is note
      </template>
    </UTabs>
  </div>
</template>

<script setup lang="ts">
  const items = ref(
  [{
    label: 'Diff Versions',
    icon: 'icon-park-twotone:difference-set',
    slot: 'diff-version'
  }, {
    label: 'Note',
    icon: 'gridicons:notice-outline',
    slot: 'note'
  }]);

</script>

<style scoped>

</style>