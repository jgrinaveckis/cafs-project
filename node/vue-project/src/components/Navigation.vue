<script setup lang="ts">
</script>

<template>
    <nav class="navbar navbar-expand navbar-dark bg-dark">
    <div class="container-fluid">
        <router-link class="nav-link" to="/map">LiveOrderMap</router-link>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <router-link class="nav-link" to="/map">Home</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/aggregations">Aggregations</router-link>
            </li>
        </ul>
        <router-link class="nav-link" to="/logout">Logout</router-link>
        </div>
    </div>
    </nav>
</template>