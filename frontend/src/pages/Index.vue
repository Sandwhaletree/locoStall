<script setup>
import axios from 'axios';
import { reactive, ref, computed, onMounted } from 'vue';
// import { useStore } from "vuex";
import { useRouter, useRoute } from "vue-router";

const shopList = ref([])
const route = useRoute()
const lang = route.params.lang;

onMounted(()=>{
  var url = `http://localhost:5000/api/${lang}/shops`

  axios.get(url).then(function (response) {
    shopList.value = response.data
  }).catch(function (response) {
      console.log(response);
  })
})
</script>

<template>
  <h1>SHOP LIST</h1>
  
  <ul class="_shopList">
    <li class="_shopList_item" v-for="shop,idx in shopList" :key="idx">
      <router-link class="_shopList_item__a" :to="`/${lang}/shop/${shop.shop_id}`">{{ shop.name }}</router-link>
    </li>
  </ul>

</template>

<style scoped lang="scss">
._shopList_item{
  padding: .5rem 0;
}
._shopList_item__a{
  color: $color-gray-1;
  transition: .2s;
  
  &:hover{
    color: $color-blue;
  }
}
</style>
