<script setup lang="ts">
import * as am5 from '@amcharts/amcharts5';
import * as am5map from "@amcharts/amcharts5/map";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import Navigation from '../../components/Navigation.vue';
import Insert from '../../components/Insert.vue';
import { onMounted, shallowRef } from 'vue'
import type { Root } from "@amcharts/amcharts5";
import { createGlobe } from "../../services/globe"
import { useAuthStore } from '@/stores/auth';

let root: Root;
const chartdiv = shallowRef();
const ws = new WebSocket('ws://localhost:3003');
const authStore = useAuthStore()

onMounted(() => {
    authStore.loadUserInfo()
    root = am5.Root.new(chartdiv.value);
    root.setThemes([am5themes_Animated.new(root)]);

    let glb = createGlobe(root, am5map);
    let globe = glb[0];
    let pointSeries = globe.series.push(
        am5map.MapPointSeries.new(root, {
        })
    );

    pointSeries.bullets.push(function () {
        let container = am5.Container.new(root, {});
        let circle = container.children.push(
            am5.Circle.new(root, {
                radius: 4,
                fill: am5.color(0xff0000),
                strokeOpacity: 0
            })
        );

        circle.animate({
            key: "scale",
            from: 0.5,
            to: 2,
            duration: 1200,
            easing: am5.ease.out(am5.ease.cubic),
            loops: 30
        });
        circle.animate({
            key: "opacity",
            from: 1,
            to: 0,
            duration: 1200,
            easing: am5.ease.out(am5.ease.cubic),
            loops: 30
        });

        return am5.Bullet.new(root, {
            sprite: container
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
        pointSeries.pushDataItem({ latitude: obj.lat, longitude: obj.lon });

        // check and clear list
        if (pointSeries.bullets.length > 100) {
            pointSeries.bullets.clear()
        }
    }
})

</script>

<template>
    <Navigation></Navigation>
    <Insert></Insert>
    <div class="d-flex justify-content-center mt-1">
        <div class="map" ref="chartdiv"></div>
    </div>
</template>

<style>
.map {
    width: 100%;
    height: 700px;
}
</style>