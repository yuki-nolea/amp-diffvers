<template>
  <div class="flex flex-col">
    <div class="h-full overflow-hidden">
      <UTabs :items="items" :ui="{ container: 'w-full h-full', wrapper: 'space-y-0 flex flex-col', base: 'h-full' }" class="w-full h-full">
        <template #diff-version class="h-full">
          <ViewDiffVersions/>
        </template>
        <template #note class="h-full">
          this is note
        </template>
      </UTabs>
    </div>
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