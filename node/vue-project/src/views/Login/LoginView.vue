<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import LoginForm from './LoginForm.vue'
const authStore = useAuthStore()
const router = useRouter()

onMounted(() => {
    if (authStore.isLoggedIn) {
        router.push('/map')
    }
})
</script>

<template>
    <div class="container">
        <router-view></router-view>
        <login-form> </login-form>
    </div>
</template>