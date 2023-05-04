import type { AxiosInstance } from 'axios'
import axios from 'axios'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import type { IUser } from '../interfaces'
import CONFIG from '../config.json'
import { useRouter } from 'vue-router'

const TOKEN = 'token'

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()
  const httpClient = ref<AxiosInstance | null>(null)
  const user = ref<IUser | null>(null)
  const isInitializing = ref(true)
  const isLoggedIn = computed(() => user.value !== null)

  const loadHttpClient = (): Promise<any> => {
    const token = window.localStorage.getItem(TOKEN)

    httpClient.value = axios.create({
      baseURL: CONFIG.api.address,
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    return loadUserInfo()
  }

  const registerToken = (token: string): Promise<any> => {
    window.localStorage.setItem(TOKEN, token)
    return loadHttpClient()
  }

  const checkTokenStorage = () => {
    const token = window.localStorage.getItem(TOKEN)
    if (token !== null) {
      loadHttpClient().then(() => isInitializing.value = false)
    }
    else {
      isInitializing.value = false;
    }
  }

  const loadUserInfo = (): Promise<any> =>
    (httpClient.value) ? httpClient.value?.get('/auth/user')
      .then((res) => (user.value = res.data))
      .catch(logout) : Promise.resolve()

  const logout = () => {
    window.localStorage.removeItem(TOKEN)
    httpClient.value = null
    user.value = null
    router.push('/')
  }


  return {
    httpClient,
    user,
    isLoggedIn,
    isInitializing,
    registerToken,
    checkTokenStorage,
    logout,
    loadUserInfo
  }
})