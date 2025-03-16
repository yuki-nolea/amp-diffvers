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
[data-amplify-authenticator] {
  --amplify-components-authenticator-router-box-shadow: 0 0 16px var(--amplify-colors-overlay-10);
  --amplify-components-authenticator-router-border-width: 0;
  --amplify-components-authenticator-form-padding: var(--amplify-space-medium) var(--amplify-space-xl) var(--amplify-space-xl);
  --amplify-components-button-primary-background-color: var(--amplify-colors-neutral-100);
  --amplify-components-fieldcontrol-focus-box-shadow: 0 0 0 2px var(--amplify-colors-purple-60);
  --amplify-components-tabs-item-active-border-color: var(--amplify-colors-neutral-100);
  --amplify-components-tabs-item-color: var(--amplify-colors-neutral-80);
  --amplify-components-tabs-item-active-color: var(--amplify-colors-purple-100);
  --amplify-components-button-link-color: var(--amplify-colors-purple-80);
}
</style>