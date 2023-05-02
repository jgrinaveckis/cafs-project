import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/Login/LoginView.vue'
import MapView from '../views/App/MapView.vue'
import About from '../views/AboutView.vue'
import Aggregations from '../views/App/AggregationsView.vue'
import Register from '../views/Register/RegisterView.vue'
import Auth from '../views/Auth.vue'

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
      path: '/register',
      component: Register
    },
    {
      path: '/auth',
      component: Auth,
      children: [
        {
          path: '/map',
          component: MapView
        },
        {
          path: '/aggregations',
          component: Aggregations
        },
      ]
    }
  ],
  linkActiveClass: 'active',
  linkExactActiveClass: 'active'
})

export default router
