<template>
  <nav class="navbar navbar-light">
    <div class="content">
      <nuxt-link to="/" class="navbar-brand">DiffVers</nuxt-link>
      <div class="gap"></div>
      <CommonNavigationBar :signOut="props.signOut"/>
    </div>
  </nav>
</template>
  
<script setup lang="ts">
  const props = defineProps<{signOut: any}>();
</script>


<style scoped>
  .content
  {
    display: grid;
    grid-template-columns: max-content 1fr max-content;
    grid-template-rows: 1fr;
    padding: 0 20px 0 20px;
  }
  .navbar
  {
    height: max-content;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  }

  .navbar-brand {
    color: rgba(0, 0, 0, 0.8);
  }
  .navbar-brand {
    font-family: 'Vidaloka', serif;
    font-weight:normal;
    color:#444;
    display:block;
    font-size:32px;
    line-height:48px;
    letter-spacing:-2px;
    text-shadow:3px 3px 6px #888;
  }
  .navbar-brand:focus,
  .navbar-brand:hover {
    color: rgba(0, 0, 0, 0.8);
  }

</style>