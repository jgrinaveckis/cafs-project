import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MapView from '../views/MapView.vue'
import About from '../views/AboutView.vue'
import Aggregations from '../views/AggregationsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      component: About
    },
    {
      path: '/map',
      component: MapView
    },
    {
      path: '/aggregations',
      component: Aggregations
    }
  ]
})

export default router
