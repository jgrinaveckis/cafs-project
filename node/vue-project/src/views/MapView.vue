<script setup lang="ts">
import * as am5 from '@amcharts/amcharts5';
import * as am5map from "@amcharts/amcharts5/map";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import Navigation from '../components/Navigation.vue';
import { onMounted, ref, shallowRef } from 'vue'
import type { Root } from "@amcharts/amcharts5";
import { createGlobe } from "../services/globe"

let root: Root;
const chartdiv = shallowRef();
const ws = new WebSocket('ws://localhost:3003');


onMounted(() => {
  root = am5.Root.new(chartdiv.value);
  root.setThemes([am5themes_Animated.new(root)]);

  let globe = createGlobe(root, am5map);
  
  let pointSeries = globe.series.push(
      am5map.MapPointSeries.new(root, {
      })
  );
  pointSeries.bullets.push(function() {
      return am5.Bullet.new(root, {
          sprite: am5.Circle.new(root, {
              radius: 5,
              fill: am5.color(0xff0000)
          })
      });
  });

  globe.animate({
      key: "rotationX",
      from: 0,
      to: 360,
      duration: 40000,
      loops: Infinity
  });

  ws.onmessage = function message(data) {
      let obj = JSON.parse(data.data);
      pointSeries.pushDataItem({ latitude: obj.data.lat, longitude: obj.data.lon });
  }
})

</script>

<template>
    <Navigation></Navigation>
    <div class="d-flex justify-content-center">
        <div class="hello" ref="chartdiv"></div>
    </div>
</template>

<style>
.hello {
  width: 750px;
  height: 750px;
  align-items: center;
  display: inline-block;
}
</style>