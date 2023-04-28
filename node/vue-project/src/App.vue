<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

import { onMounted } from 'vue'
import { useAuthStore } from './stores/auth'

// Adding auth globally in Vue app
const authStore = useAuthStore()
onMounted(() => authStore.checkTokenStorage())
</script>

<template>
  <Navigation></Navigation>
    <div class="container"></div>
  <router-view></router-view>
</template>

<style lang="scss">
@use '../node_modules/bootstrap/scss/bootstrap.scss';
</style>
