<script setup>
export default {
    name: 'Message',
    components: {},
    mounted() {
      this.ws = new WebSocket('ws://localhost:3005');
      this.ws.addEventListener('open', () => {
        this.status = "Connection established"
        this.canSendMessage = true;
      });
      // Listen for messages
      this.ws.addEventListener('message', (event) => {
        try {
          const data = JSON.parse(event.data);
          this.addMessage(data);
        } catch (err) {
          console.log(err)
        }
      });
      this.ws.addEventListener('error', (event) => {
        this.status = "Connection lost"
        console.log("Error connecting to server ", event);
      })
    },
    data: function () {
      return {
        messages: [],
        userInput: "",
        ws: null,
        canSendMessage: false,
        status: "",
        username: "Anonymous"
      }
    },
    computed: {},
    methods: {
      addMessage(data) {
        console.log("New message ", data)
        this.messages.push({
          message: data.message
        })
      }
    }
  }
  </script>
<template>
    <div id="messages">
      <div id="message-box" v-for="message in messages">
        <div>
          <p>{{ message.message }}</p>
        </div>
      </div>
    </div>
  </template> 