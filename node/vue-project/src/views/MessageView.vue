<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import WebSocket from 'isomorphic-ws';

    let dataMsg = ref();
    let messages = ref([]);
    let connections = [];
    const ws = new WebSocket('ws://localhost:3003');

    function addMessage(dataMsg) {
        console.log("New message ", dataMsg)
        messages.value.push(dataMsg.data)
    }

    onMounted(() => {

      // ws.onopen = function open() {
      //   console.log("New connection added", ws);
      //   connections.push(ws);
      // };
      // ws.onclose = function close() {
      //   console.log("New connection removed", ws);
      //   let index = 
      //   connections.pop(ws);
      // }
      ws.onmessage = function message(data) {
        addMessage(data);
        console.log(data.data);
      }
    })

</script>

<template>
  <h1>
    Hello
  </h1>
    <div id="messages">
      <button class="btn btn-danger">aaa</button>
      <div id="message-box" v-for="(message, index) in messages">
        <div>
          <p>{{ message }}</p>
        </div>
      </div>
    </div>
</template> 