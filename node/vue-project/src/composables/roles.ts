import { computed } from 'vue'
import { useAuthStore } from '../stores/auth'
import { Role } from '../interfaces'

export const roles = () => {
  const authStore = useAuthStore()

  const isAdmin = computed<boolean>(
    () => authStore.user?.role === Role.admin
  )
  const isRegular = computed<boolean>(
    () => authStore.user?.role === Role.regular
  )

  return {
    isAdmin,
    isRegular
  }
}