<script setup lang="ts">
</script>

<template>
    <nav class="navbar navbar-expand navbar-dark bg-dark">
    <div class="container-fluid option">
        <router-link class="nav-link px-2" to="/map">LiveOrderMap</router-link>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <router-link class="nav-link" to="/map">Home</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/aggregations">Aggregations</router-link>
            </li>
        </ul>
        </div>
        <div class="logout d-flex flex-row-reverse px-2">
            <router-link class="nav-link" to="/logout">Logout</router-link>
        </div>
    </div>
    </nav>
</template>

<style lang="scss">
.option {
    color:white;
}

.logout {
    color:white;
}
</style>