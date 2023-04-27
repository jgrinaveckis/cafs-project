import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/Login/LoginView.vue'
import MapView from '../views/MapView.vue'
import About from '../views/AboutView.vue'
import Aggregations from '../views/AggregationsView.vue'
import Register from '../views/Register/RegisterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: LoginView
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
    },
    {
      path: '/register',
      component: Register
    }
  ]
})

export default router
