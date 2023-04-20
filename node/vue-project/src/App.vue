<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Navigation from './components/Navigation.vue';
</script>

<template>
  <Navigation></Navigation>
  <div class="container pt-4"></div>
  <router-view></router-view>
</template>

<style lang="scss">
@use '../node_modules/bootstrap/scss/bootstrap.scss';
</style>
