<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { roles } from '../composables/roles'
import { reactive, ref } from 'vue'

const { isAdmin } = roles()
const authStore = useAuthStore()
const isBusy = ref(false)
const errMsg = ref<string | null>();
const errors = ref({})

const leadForm = reactive({
    ip: ""
});

const submit = () => {
    isBusy.value = true
    authStore.httpClient?.post('http://localhost/test/insert', leadForm)
        .then(() => {
            leadForm.ip = "";
            errMsg.value = "";
            errors.value = "";
        })
        .catch((err) => {
            errMsg.value = err.response.data.message
            errors.value = err.response.data.errors
        })
        .then(() => (isBusy.value = false));
}
</script>


<template>
    <div class="form-outline form-white d-flex justify-content-center" v-if="isAdmin">
        <div class="container">
            <label class="form-label mt-2" for="ip">Test IP address</label>
            <input type="ip" id="ip" class="form-control form-control-md mb-2" v-model.trim="leadForm.ip" ref="ip" />
            <div class="form-text text-danger" v-if="errors.ip">
                {{ errors.ip.join(' ') }}
            </div>
            <button class="btn btn-outline-dark btn-lg" @click="submit" :disabled="isBusy">
                <div class="spinner-border spinner-border-sm" v-if="isBusy"></div>
                Send
            </button>
        </div>
    </div>
</template>

<style lang="scss">
#ip {
    width: 15%;
}
</style>