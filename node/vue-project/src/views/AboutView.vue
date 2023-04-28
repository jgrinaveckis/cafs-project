<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Navigation from '../components/Navigation.vue'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
onMounted(() => {
  authStore.loadUserInfo()
})
</script>

<template>
  <Navigation></Navigation>
  <div>
    <h3>Current user</h3>
      <div>Name: {{ authStore.user?.name }}</div>
      <div>Email: {{ authStore.user?.email }}</div>
      <div>Role: {{ authStore.user?.role  }}</div>
  </div>
</template>

<style>
</style>
