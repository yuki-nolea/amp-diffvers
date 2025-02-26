<template>
  <ul class="nav navbar-nav pull-xs-right">
    <li class="nav-item">
      <!-- <nuxt-link to="/" class="nav-link"> Home </nuxt-link> -->
    </li>
    <li class="nav-item">
      <!-- <nuxt-link to="/signout" class="nav-link"> Sign out </nuxt-link> -->
       <UButton color="black" variant="solid" @click="props.signOut">Sign Out</UButton>
      <!-- <button @click="props.signOut">Sign Out</button> -->
    </li>
  </ul>
</template>

<script setup lang="ts">
  const props = defineProps<{signOut: any}>();
</script>


<style scoped>
.nav {
  list-style: none;
  margin: auto 0 auto 0;
}

.navbar-nav .nav-link {
  color: rgba(0, 0, 0, 0.3);
}
.navbar-nav .nav-link:focus,
.navbar-nav .nav-link:hover {
  color: rgba(0, 0, 0, 0.6);
}
.navbar-nav .open > .nav-link,
.navbar-nav .open > .nav-link:focus,
.navbar-nav .open > .nav-link:hover,
.navbar-nav .active > .nav-link,
.navbar-nav .active > .nav-link:focus,
.navbar-nav .active > .nav-link:hover,
.navbar-nav .nav-link.open,
.navbar-nav .nav-link.open:focus,
.navbar-nav .nav-link.open:hover,
.navbar-nav .nav-link.active,
.navbar-nav .nav-link.active:focus,
.navbar-nav .nav-link.active:hover {
  color: rgba(0, 0, 0, 0.8);
}

.pull-xs-right {
  float: right !important;
}

.navbar-nav .nav-item {
  float: left;
}
.navbar-nav .nav-link {
  display: block;
}
.navbar-nav .nav-link + .nav-link {
  margin-left: 1rem;
}
.navbar-nav .nav-item + .nav-item {
  margin-left: 1rem;
}
</style>