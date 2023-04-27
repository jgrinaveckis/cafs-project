<script setup lang="ts">
import axios from 'axios';
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

const regForm = reactive({
    email: "",
    name: "",
    password: "",
    confirmPassword: ""
})

const errors = ref({})
const errMsg = ref<string | null>()
const isBusy = ref(false)
const router = useRouter()
const emailElement = ref<HTMLInputElement | null>(null)

const submit = () => {
    isBusy.value = true
    axios
        .post('http://localhost/register', regForm)
        .then((res) => {
            router.push('/')
        })
        .catch((err) => {
            errMsg.value = err.response.data.message
            errors.value = err.response.data.errors
        })
        .then(() => (isBusy.value = false))
}

onMounted(() => emailElement.value?.focus())
</script>

<template>
    <section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card bg-dark text-white">

            <div class="card-body p-5 text-center">

                <div class="mb-md-5 mt-md-4 pb-5">

                    <h2 class="fw-bold mb-2 text-uppercase">Register</h2>

                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="username">Username</label>
                        <input 
                            type="username" 
                            id="username" 
                            class="form-control form-control-lg"
                            v-model.trim="regForm.name"
                            ref="username"
                             />
                        <p></p>
                        <div class="form-text text-danger" v-if="errors.name">
                            {{ errors.name.join(' ') }}
                        </div>

                    </div>

                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="email">Email</label>
                        <input 
                            type="email" 
                            id="email" 
                            class="form-control form-control-lg"
                            v-model.trim="regForm.email"
                            ref="emailElement"
                             />
                        <p></p>
                        <div class="form-text text-danger" v-if="errors.email">
                            {{ errors.email.join(' ') }}
                        </div>

                    </div>

                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="password">Password</label>
                        <input 
                            type="password"
                            id="password"
                            class="form-control form-control-lg"
                            v-model.trim="regForm.password" />
                        <p class="text-white-50">Password have to be longer than 5 symbols</p>
                        <div class="form-text text-danger" v-if="errors.password">
                            {{ errors.password.join(' ') }}
                        </div>

                    </div>

                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="confirmPassword">Confirm Password</label>
                        <input 
                            type="password"
                            id="confirmPassword"
                            class="form-control form-control-lg"
                            v-model.trim="regForm.confirmPassword" />
                        <div class="form-text text-danger" v-if="errors.password_confirmation">
                            {{ errors.password_confirmation.join(' ') }}
                        </div>

                    </div>

                    <button 
                        class="btn btn-outline-light btn-lg px-5" 
                        @click="submit"
                        :disabled="isBusy"
                    >
                    <div class="spinner-border spinner-border-sm" v-if="isBusy"></div>
                        Register
                    </button>

                </div>

            </div>
            </div>
        </div>
        </div>
    </div>
    </section>
</template>

<style lang="scss">
</style>