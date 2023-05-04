<script setup lang="ts">
import { useAuthStore } from '@/stores/auth';
import LoginForm from './LoginForm.vue'
import { watchEffect } from 'vue'
import { useRouter } from 'vue-router';

const authStore = useAuthStore()
const router = useRouter()

watchEffect(() => {
    if (authStore.isInitializing) return;
    if (authStore.isLoggedIn) router.push('/map')
})

</script>

<template>
    <div class="container">
        <login-form> </login-form>
    </div>
</template>