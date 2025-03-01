<template>
  <footer>
    <div class="content">
      <nuxt-link to="/" class="logo-font">DiffVers</nuxt-link>
    </div>
  </footer>
</template>

<script setup lang="ts">

</script>

<style scoped>
  .content
  {
    height: max-content;
    border-top: 1px solid rgba(0, 0, 0, 0.3);
    padding: 0 20px 0 20px;
  }
  .logo-font
  {
    font-family: 'Vidaloka', serif;
    font-weight:normal;
    color:#444;
    display:block;
    font-size:24px;
    line-height:32px;
    letter-spacing:-2px;
    text-shadow:3px 3px 6px #888;
  }
</style>