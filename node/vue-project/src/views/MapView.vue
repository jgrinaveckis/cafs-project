<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import WebSocket from 'isomorphic-ws';

    let dataMsg = ref();
    let messages = ref([]);
    const ws = new WebSocket('ws://localhost:3003');

    function addMessage(dataMsg) {
        console.log("New message ", dataMsg.data.ip)
        messages.value.push(dataMsg.data.ip)
    }

    onMounted(() => {
      ws.onmessage = function message(data) {
        addMessage(data);
        console.log(data.data.ip);
      }
    })

</script>

<template>

  <h1>
    Hello
  </h1>

    <div id="messages">
      <div id="message-box" v-for="(message, index) in messages">
        <div>
          <p>{{ message }}</p>
        </div>
      </div>
    </div>
</template> 