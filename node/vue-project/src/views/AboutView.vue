<script setup lang="ts">
import { roles } from '@/composables/roles';
import Navigation from '../components/Navigation.vue'

const { isAdmin } = roles()
</script>

<template>
    <Navigation></Navigation>
    <div class="container">
        <h2>About</h2>
        <h4> This is Live Order Map project </h4>
        <p>
            If you want to see live orders go to <router-link class="nav-link display-inline" to="/">Home</router-link>
        </p>
        <p>
            If you want to see order aggregations go to <router-link class="nav-link display-inline"
                to="/aggregations">Aggregations</router-link>
        </p>
        <p v-if="isAdmin">
            If you want to see currently logged in person info press <router-link class="nav-link display-inline"
                to="/person"><a>here</a></router-link>
        </p>
        <p>
            Source code can be seen in <a href="https://github.com/jgrinaveckis/cafs-project">in Github repo here</a>
        </p>
    </div>
</template>

<style>
.display-inline {
    display: inline;
    font-weight: bold;
}
</style>