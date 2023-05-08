<script setup lang="ts">
import { useAuthStore } from '../stores/auth'
import { roles } from '../composables/roles'

const authStore = useAuthStore()
const { isAdmin } = roles()

</script>

<template>
    <nav class="navbar navbar-expand navbar-dark bg-dark">
        <div class="container-fluid option">
            <router-link class="nav-link px-2" to="/map">LiveOrderMap</router-link>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                        <router-link class="nav-link" to="/map">Home</router-link>
                    </li>
                    <li class="nav-item" v-if="isAdmin">
                        <router-link class="nav-link" to="/aggregations">Aggregations</router-link>
                    </li>
                    <li class="nav-item" v-if="isAdmin">
                        <router-link class="nav-link" to="/about">About</router-link>
                    </li>
                </ul>
            </div>
            <div class="logout d-flex flex-row-reverse px-2" v-if="authStore.user">
                <router-link class="nav-link" to="/" @click.prevent="authStore.logout">Logout</router-link>
                <router-link class="nav-link" to="/person">Welcome, {{ authStore.user.name }}</router-link>
                <div> </div>
            </div>
        </div>
    </nav>
</template>

<style lang="scss">
.option {
    color: white;
}

.logout {
    color: white;
    gap: 20px;
}
</style>