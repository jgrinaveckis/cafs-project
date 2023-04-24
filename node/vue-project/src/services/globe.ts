import type { Root } from "@amcharts/amcharts5";
import am4geodata_worldLow from "@amcharts/amcharts4-geodata/worldLow";
import am4geodata_usaStatesLow from "@amcharts/amcharts4-geodata/usaHigh";

export function createGlobe(root: Root, am5map: any) {
    let chrt = createChart(root, am5map);
    let backgroundSeries = setBackgroundSeries(chrt, am5map, root);
    let countriesAndStates = setCountriesAndStates(backgroundSeries, am5map, root, am4geodata_worldLow, am4geodata_usaStatesLow);

    return countriesAndStates;
};

function createChart(root: Root, am5map: any) {
    let chart = root.container.children.push(
        am5map.MapChart.new(root, {
            panX: "rotateX",
            panY: "rotateY",
            projection: am5map.geoOrthographic()
        })
    );
    return chart;
}
function setBackgroundSeries(chart: any, am5map:any, root:Root) {

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

    return chart;
};

function setCountriesAndStates(chart: any, am5map:any, root: Root, world: any, states: any) {
    // Country series polygon
    let countrySeries = chart.series.push(
        am5map.MapPolygonSeries.new(root, {
            geoJSON: world 
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
            geoJSON: states 
        }
    ));
    stateSeries.mapPolygons.template.setAll({
        fill: root.interfaceColors.get("alternativeBackground"),
        fillOpacity: 0.05,
        strokeWidth: 0.5,
        stroke: root.interfaceColors.get("background")
    });
    return chart;
}
