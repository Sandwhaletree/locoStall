<script setup>
import Logo from "../assets/locoStall_logo.vue";
</script>

<template>
  <ul class="_nav">
    <li>
      <router-link :to="`/${currLang}`"><Logo class="_logo"/></router-link>
    </li>
  </ul>

</template>

<style scoped lang="scss">
._nav{
  padding: 1rem;
}
._logo{
  max-width: 200px;
}
</style>
