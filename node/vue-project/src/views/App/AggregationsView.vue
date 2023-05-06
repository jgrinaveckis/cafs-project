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
const authStore = useAuthStore();
let leadsByCountry = ref([]);
let leadsByState = ref([]);
const errors = ref({});
const errMsg = ref<string | null>();

onMounted(() => {
    root = am5.Root.new(chartdiv.value);
    root.setThemes([am5themes_Animated.new(root)]);
    let globe = createGlobe(root, am5map);
    let chart = globe[0];
    let states = globe[1];
    let countries = globe[2];

    countries.mapPolygons.template.setAll({
        tooltipText: "{id}: {value}"
    });
    countries.set("heatRules", [{
        target: countries.mapPolygons.template,
        dataField: "value",
        min: am5.color(0xff621f),
        max: am5.color(0x661f00),
        key: "fill"
    }]);

    states.mapPolygons.template.setAll({
        tooltipText: "{id}: {value}"
    });
    states.set("heatRules", [{
        target: states.mapPolygons.template,
        dataField: "value",
        max: am5.color(0xff621f),
        min: am5.color(0x661f00),
        key: "fill"
    }]);
    authStore.httpClient?.get('http://localhost/leads/bycountry')
        .then((res) => {
            res.data.forEach(e => {
                if (e.iso_country !== 'US') {
                    leadsByCountry.value.push({ id: e.iso_country, value: e.count });
                }
                countries.data.setAll(leadsByCountry.value);
            });
        })
        .catch((err) => {
            errMsg.value = err.response.data.message
            errors.value = err.response.data.errors
        });

    authStore.httpClient?.get('http://localhost/leads/bystate')
        .then((res) => {
            res.data.forEach(e => {
                leadsByState.value.push({ id: `${e.iso_country}-${e.iso_state}`, value: e.count }
                );
                states.data.setAll(leadsByState.value);
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
    width: 100%;
    height: 800px;
    align-items: center;
    display: inline-block;
}
</style>