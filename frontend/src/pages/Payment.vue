<script setup>
import axios from 'axios';
import { reactive, ref, computed, onMounted } from 'vue';
import { useStore } from "vuex";
import { useRouter, useRoute } from "vue-router";

const store = useStore()
const order = computed(() => store.getters.order);
console.log('order.value',order.value);

onMounted(()=>{
})
</script>

<template>
  <div class="_payment">
    <h1>Order list</h1>
    
    <div class="_payment_items" v-for="item,idx in order" :key="idx">
      <div class="_payment_item">
        <span class="_payment_item__buy">{{ item.buy }}</span>
        <span class="_payment_item__name">{{ item.name }}</span>
        <span class="_payment_item__subtotal">{{ item.buy * item.price }}</span>
      </div>
    </div>

    <div>Total {{ total }}</div>
  </div>
</template>

<style scoped lang="scss">
._payment_item{
  display: flex;
  align-items: center;

  * {
    font-weight: bold;
  }
}
._payment_item__buy{
  color: $color-blue;
  font-size: 2rem;
  flex: 1;
}
._payment_item__name{
  font-size: 1rem;
  flex: 5;
}
._payment_item__subtotal{
  font-size: 1.5rem;
  flex: 1;
  text-align: right;
}
</style>
