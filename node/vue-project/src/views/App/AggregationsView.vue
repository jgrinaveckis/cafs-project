<script setup lang="ts">

import * as am5 from '@amcharts/amcharts5';
import * as am5map from "@amcharts/amcharts5/map";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import Navigation from '../../components/Navigation.vue';
import { onMounted, reactive, ref, shallowRef } from 'vue'
import type { Root } from "@amcharts/amcharts5";
import { createGlobe } from "../../services/globe"
import { useAuthStore } from '@/stores/auth';

let root: Root;
const chartdiv = shallowRef();
const ws = new WebSocket('ws://localhost:3003');
const authStore = useAuthStore();
const leadsByCountry = [];
const leadsByState = ref({});
const errors = ref({});
const errMsg = ref<string | null>();

onMounted(() => {
    root = am5.Root.new(chartdiv.value);
    root.setThemes([am5themes_Animated.new(root)]);
    let globe = createGlobe(root, am5map);

    let countries = globe[1];
    let states = globe[2];

    countries.valueField = "value";
    countries.calculateAggregates = true;
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

    states.valueField = "count";
    states.mapPolygons.template.setAll({
        tooltipText: "{id}: {value}"
    });
    states.set("heatRules", [{
        target: states.mapPolygons.template,
        dataField: "value",
        min: am5.color(0xff621f),
        max: am5.color(0x661f00),
        key: "fill"
    }]);

    authStore.httpClient?.get('http://localhost/leads/bycountry')
        .then((res) => {
            // console.log(res.data[0]);
            // console.log(res.data[0].iso_country);
            res.data.forEach(e => {
                leadsByCountry.push({ id: e.iso_country, value: e.count }
                );
            });
        })
        .catch((err) => {
            // errMsg.value = err.response.data.message
            // errors.value = err.response.data.errors
        })
    countries.data.setAll(leadsByCountry);

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