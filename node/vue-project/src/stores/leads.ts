import { computed, onMounted, ref } from 'vue'
import { defineStore } from 'pinia'
import WebSocket from 'isomorphic-ws';
import type { ILead } from '../interfaces';

export const leadsStore = defineStore('leads', () => {
    let leads = ref<ILead | null>(null);
    let messages = ref([]);


    
})