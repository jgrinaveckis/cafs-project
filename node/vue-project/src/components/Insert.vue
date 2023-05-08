<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { roles } from '../composables/roles'
import { reactive, ref } from 'vue'

const { isAdmin } = roles()
const authStore = useAuthStore()
const isBusy = ref(false)
const pasted = ref(false)
const errMsg = ref<string | null>();
const errors = ref({})

const leadForm = reactive({
    ip: ""
});

const generateIp = () => {
    pasted.value = true;
    leadForm.ip = (Math.floor(Math.random() * 255) + 1) + "."
        + (Math.floor(Math.random() * 255)) + "."
        + (Math.floor(Math.random() * 255)) + "."
        + (Math.floor(Math.random() * 255)
        );
    setTimeout(submit, 3000);
}
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
        .then(() => {
            isBusy.value = false
            pasted.value = false;
        });
}
</script>


<template>
    <div class="form-outline form-white d-flex justify-content-center " v-if="isAdmin">
        <div class="container transparent">
            <label class="form-label mt-2" for="ip">Test IP address</label>
            <input type="ip" id="ip" class="form-control form-control-md mb-2" v-model.trim="leadForm.ip" ref="ip"
                :disabled="pasted" />
            <div class="form-text text-danger" v-if="errors.ip">
                {{ errors.ip.join(' ') }}
            </div>
            <button class="btn btn-outline-dark me-2" @click="submit" :disabled="isBusy">
                <div class="spinner-border spinner-border-sm" v-if="isBusy"></div>
                Send
            </button>
            <button class="btn btn-outline-dark" @click="generateIp" :disabled="isBusy">
                <div class="spinner-border spinner-border-sm" v-if="isBusy"></div>
                Generate
            </button>
        </div>
    </div>
</template>

<style lang="scss">
.transparent {
    background-color: transparent;
}

#ip {
    width: 15%;
}
</style>