<script setup>
  import { Authenticator } from "@aws-amplify/ui-vue";
  import "@aws-amplify/ui-vue/styles.css";
</script>

<template>
  <div>
    <authenticator :hide-sign-up="true" class="flex pt-8">
      <template v-slot="{ user, signOut }">
        <UApp>
          <NuxtLayout :signOut="signOut">
            <NuxtPage />
          </NuxtLayout>
      </UApp>
      </template>
    </authenticator>
  </div>
</template>

<style lang="css">
</style>