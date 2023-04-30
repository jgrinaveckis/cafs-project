<script setup lang="ts">

import * as am5 from '@amcharts/amcharts5';
import * as am5map from "@amcharts/amcharts5/map";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import Navigation from '../../components/Navigation.vue';
import { onMounted, ref, shallowRef } from 'vue'
import type { Root } from "@amcharts/amcharts5";
import { createGlobe } from "../../services/globe"

let root: Root;
const chartdiv = shallowRef();
const ws = new WebSocket('ws://localhost:3003');


onMounted(()  => {
    root = am5.Root.new(chartdiv.value);
    root.setThemes([am5themes_Animated.new(root)]);
    let globe = createGlobe(root, am5map);
  
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