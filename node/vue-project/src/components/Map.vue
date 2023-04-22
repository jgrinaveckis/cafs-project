<script setup lang="ts">
import * as am5 from '@amcharts/amcharts5';
import * as am5map from "@amcharts/amcharts5/map";
import am4geodata_worldLow from "@amcharts/amcharts4-geodata/worldLow";
import am4geodata_usaStatesLow from "@amcharts/amcharts4-geodata/usaHigh";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import { shallowRef, onMounted } from 'vue';

let root: any;
const chartdiv = shallowRef();
let radius = 0.5;
const props = defineProps<{
    ip: string,
    iso_state: string,
    iso_country: string,
    lat: number,
    lon: number,
}>()
const geoPoint = {
      latitude: 38.8951,
      longitude: -77.0364
    };

onMounted(()  => {
    root = am5.Root.new(chartdiv.value);
    root.setThemes([am5themes_Animated.new(root)]);

    let chart = root.container.children.push(
        am5map.MapChart.new(root, {
            panX: "rotateX",
            panY: "rotateY",
            projection: am5map.geoOrthographic()
        })
    );

    let backgroundSeries = chart.series.push(
        am5map.MapPolygonSeries.new(root, {})
    );
    backgroundSeries.mapPolygons.template.setAll({
        fill: root.interfaceColors.get("alternativeBackground"),
        fillOpacity: 0.1,
        strokeOpacity: 0
    });
    backgroundSeries.data.push({
        geometry:
            am5map.getGeoRectangle(90, 180, -90, -180)
    });

    // Country series polygon
    let countrySeries = chart.series.push(
        am5map.MapPolygonSeries.new(root, {
            geoJSON: am4geodata_worldLow 
        }
    ));
    countrySeries.mapPolygons.template.setAll({
        fill: root.interfaceColors.get("alternativeBackground"),
        fillOpacity: 0.15,
        strokeWidth: 0.5,
        stroke: root.interfaceColors.get("background")
    });

    let stateSeries = chart.series.push(
        am5map.MapPolygonSeries.new(root, {
            geoJSON: am4geodata_usaStatesLow 
        }
    ));
    stateSeries.mapPolygons.template.setAll({
        fill: root.interfaceColors.get("alternativeBackground"),
        fillOpacity: 0.05,
        strokeWidth: 0.5,
        stroke: root.interfaceColors.get("background")
    });

    let pointSeries = chart.series.push(
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
    pointSeries.pushDataItem({ latitude: 40.641312, longitude: -73.778137 });

    chart.animate({
        key: "rotationX",
        from: 0,
        to: 360,
        duration: 40000,
        loops: Infinity
    });
});

</script>

<template>
    <div class="d-flex justify-content-center">
        <div class="hello" ref="chartdiv"></div>
    </div>

</template>

<style>
.hello {
  width: 800px;
  height: 800px;
  align-items: center;
  display: inline-block;
}
</style>