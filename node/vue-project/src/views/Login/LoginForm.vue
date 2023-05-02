<script setup lang="ts">
import axios from 'axios';
import { onMounted, reactive, ref } from 'vue'
import { useAuthStore } from '../../stores/auth'
import { createRouter, useRouter } from 'vue-router'

const loginForm = reactive({
    email: "",
    password: ""
})

const errors = ref({})
const errMsg = ref<string | null>()
const isBusy = ref(false)
const authStore = useAuthStore()
const router = useRouter()
const emailElement = ref<HTMLInputElement | null>(null)

const submit = () => {
    isBusy.value = true
    axios
        .post('http://localhost/login', loginForm)
        .then((res) => {
            authStore.registerToken(res.data.token)
                .then(() => router.push('/map'))
        })
        .catch((err) => {
            errMsg.value = err.response.data.message
            errors.value = err.response.data.errors
        })
        .then(() => (isBusy.value = false))
}

onMounted(() => {
    emailElement.value?.focus()
})
</script>

<template>
    <section class="vh-100 gradient-custom">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div class="card bg-dark text-white">

                        <div class="card-body p-5 text-center">

                            <div class="mb-md-5 mt-md-4 pb-5">

                                <h2 class="fw-bold mb-2 text-uppercase">Login</h2>

                                <p class="text-white-50 mb-5">Please enter your login and password!</p>

                                <div class="form-outline form-white mb-4">
                                    <label class="form-label" for="email">Email</label>
                                    <input type="email" id="email" class="form-control form-control-lg"
                                        v-model.trim="loginForm.email" ref="emailElement" />

                                </div>

                                <div class="form-outline form-white mb-4">
                                    <label class="form-label" for="password">Password</label>
                                    <input type="password" id="password" class="form-control form-control-lg"
                                        v-model.trim="loginForm.password" />
                                    <div class="form-text text-danger" v-if="errMsg">{{ errMsg }}</div>
                                </div>


                                <button class="btn btn-outline-light btn-lg px-5" @click="submit" :disabled="isBusy">
                                    <div class="spinner-border spinner-border-sm" v-if="isBusy"></div>
                                    Login
                                </button>

                            </div>

                            <div>
                                <p class="mb-0">Don't have an account? <router-link to="/register">Sign Up</router-link>
                                </p>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="scss"></style>