<script setup>
  import { Authenticator } from "@aws-amplify/ui-vue";
  import "@aws-amplify/ui-vue/styles.css";
</script>

<template>
  <div>
    <authenticator>
      <template v-slot="{ user, signOut }">
        <UApp>
          <!--
          <h1>Hello {{user?.signInDetails?.loginId}}'s todos</h1>
          <Todos />
          <button @click="signOut">Sign Out</button>
          -->
          <NuxtLayout :signOut="signOut">
            <NuxtPage />
          </NuxtLayout>
      </UApp>
      </template>
    </authenticator>
  </div>
</template>