<script setup lang="ts">

import * as am5 from '@amcharts/amcharts5';
import * as am5map from "@amcharts/amcharts5/map";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import Navigation from '../../components/Navigation.vue';
import { onMounted, ref, shallowRef } from 'vue'
import type { Root } from "@amcharts/amcharts5";
import { createGlobe } from "../../services/globe"
import { useAuthStore } from '@/stores/auth';

let root: Root;
const chartdiv = shallowRef();
const ws = new WebSocket('ws://localhost:3003');
const authStore = useAuthStore()
const leadsByCountry = ref([])
const leadsByState = ref({})
const errors = ref({})
const errMsg = ref<string | null>()

onMounted(() => {
    root = am5.Root.new(chartdiv.value);
    root.setThemes([am5themes_Animated.new(root)]);
    let globe = createGlobe(root, am5map);

    authStore.httpClient?.get('http://localhost/leads/bycountry')
        .then((res) => {
            res.data.forEach(d => {
                console.log(d)
            });
        })
        .catch((err) => {
            errMsg.value = err.response.data.message
            errors.value = err.response.data.errors
        })

});
</script>
<template>
    <Navigation></Navigation>
    <div class="d-flex justify-content-center px-2">
        <div class="aggregations" ref="chartdiv"></div>
    </div>
</template>

<style>
.aggregations {
    width: 600px;
    height: 800px;
    align-items: center;
    display: inline-block;
}
</style>