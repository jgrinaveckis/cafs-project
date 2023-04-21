<script setup lang="ts">

import Map from '../components/Map.vue';

const props = defineProps({
    lat: Number,
    lon: Number
});

</script>
<template>
    <Map></Map>
</template>