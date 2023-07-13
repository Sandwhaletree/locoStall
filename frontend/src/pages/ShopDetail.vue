<script setup>
import axios from 'axios';
import { reactive, ref, computed, onMounted } from 'vue';
import { useStore } from "vuex";
import { useRouter, useRoute } from "vue-router";

const shops = ref([])

const route = useRoute()
const router = useRouter()
const store = useStore()

const lang = route.params.lang;
const id = route.params.id;

onMounted(()=>{
  var url = `http://localhost:5000/api/${lang}/shop/${id}`

  axios.get(url).then(function (response) {
    shops.value = response.data
    
    for(let i=0; i<shops.value[0].menu.length; i++){
      shops.value[0].menu[i].buy = 0;
    }

  }).catch(function (response) {
      console.log(response);
  })
})

const total = ref(0)
const valChange = () => {
    total.value = 0
    for(let i=0; i<shops.value[0].menu.length; i++){
      total.value += Number(shops.value[0].menu[i].buy) * shops.value[0].menu[i].price;
    }
}

const goPayment = () => {
  console.log('goPayment');
  // 把訂單內容存進 store
  store.dispatch("order", shops.value[0].menu);

  router.push({ name: 'Payment', params: { lang: lang } })

}


</script>

<template>
  <div class="_shopDetail">
    <div v-for="item,idx in shops" :key="idx">
      <h1 class="_shopDetail_name">{{ item.name }}</h1>
      <ul class="_shopDetail_menu">
        <li class="_shopDetail_menu__item" v-for="i,index in item.menu" :key="index">
          <div class="_shopDetail_menu__left">
            <img class="_shopDetail_menu__img" v-if="!item.img" alt="" src="@/assets/default.jpg" />
          </div>
          <div class="_shopDetail_menu__right">
            <p class="_shopDetail_menu__name">{{ i.name }}</p>
            <!-- {{ i.description }} -->
            <div class="_shopDetail_order">
              <div class="_shopDetail_order__price">
                <span class="_shopDetail_order__currency">NTD</span>
                <span class="_shopDetail_order__num">{{ i.price }}</span>
              </div>
              
              <div class="_shopDetail_count">
                <a-input-group compact>
                  <a-select class="_shopDetail_count__num" v-model:value="i.buy" @change="valChange()">
                    <a-select-option value="0">0</a-select-option>
                    <a-select-option v-for="n in 20" :value="n">{{ n }}</a-select-option>
                  </a-select>
                </a-input-group>
              </div>
            </div>
          </div>
        </li>
      </ul>

      <a-button class="_bigBtn" @click="goPayment" type="primary" block>
       <div class="_bigBtn_wrap">
          <div>Total<span class="_bigBtn_total">{{ total }}</span></div>
          Continue
        </div>
      </a-button>
    </div>
  </div>
</template>

<style scoped lang="scss">
._bigBtn{
  position: fixed;
  left: 0;
  bottom: 0;
  height: 3.5rem;
}
._bigBtn_wrap{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
._bigBtn_total{
  font-size: 1.5rem;
  margin-left: .25rem;
  font-weight: bold;
}
._shopDetail_name{
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
}
._shopDetail_menu__item{
  display: flex;
  border-bottom: 1px solid $color-gray-2;
  padding: .75rem 0;
}
._shopDetail_menu__left{
  flex: 1;
}
._shopDetail_menu__right{
  flex: 3;
  padding-left: 1rem;
  box-sizing: border-box;
}
._shopDetail_menu__img{
  width: 100%;
}
._shopDetail_menu__name{
  font-size: 1rem;
  font-weight: bold;
}
._shopDetail_order{
  display: flex;
  align-items: center;
}
._shopDetail_count{
  display: flex;

  input{
    color: $color-blue;
    font-weight: bold;
    max-width: 3rem;
    text-align: center;
    border: none;
    font-size: 1.5rem;
  }
}
._shopDetail_count__num{
    font-size: 1.2rem;
}
._shopDetail_order__currency{
  transform: translateY(-5px);
}
._shopDetail_order__price{
  display: flex;
  align-items: end;
  flex: auto;
}
._shopDetail_order__num{
  font-size: 1.5rem;
  font-weight: bold;
  margin-left: .5rem;
}
</style>
