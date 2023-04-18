<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import WebSocket, { WebSocketServer } from 'ws';

    let dataMsg = ref();
    let messages = ref([]);
    const ws = new WebSocket("ws://localhost:3005")

    function addMessage(dataMsg) {
        console.log("New message ", dataMsg)
        messages.value.push(dataMsg)
    }

    onMounted(() => {
      ws.onmessage = function(e) {
        dataMsg.value = e.data;
        addMessage(dataMsg.value);
      }
    })

  </script>

<template>
    <div id="messages">
      <div id="message-box" v-for="(message, index) in messages">
        <div>
          <p>{{ message }}</p>
        </div>
      </div>
    </div>
  </template> 