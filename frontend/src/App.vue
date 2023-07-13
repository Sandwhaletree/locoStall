<script setup>
import Navigation from "../src/components/Navigation.vue";
import { useRouter, useRoute } from "vue-router";
import { reactive, ref, computed, onMounted } from 'vue';
import { useStore } from "vuex";

// vuex
const store = useStore();
const currLang = computed(() => store.getters.currLang);
// console.log('currLang',currLang.value);

const router = useRouter()
router.beforeEach((to, from) => {
  // console.log('to',to);
  // console.log('from',from);
  if ( !from.name ){
    console.log('跳轉到有語系的網址');
  }
});
</script>

<template>
  <Navigation />
  <div class="_body">
    <router-view/>
  </div>
</template>

<style lang="scss">
@import "../src/assets/scss/style.scss";

._body{
  padding: 1rem;
}
</style>
