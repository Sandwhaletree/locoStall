import { createRouter, createWebHistory } from 'vue-router'

import ShopDetail from '../pages/ShopDetail.vue';
import Index from '../pages/Index.vue';
import Payment from '../pages/Payment.vue';
import NotFound from '../pages/NotFound.vue';

let history = createWebHistory();

let routes = [
  {
    path: '/:lang',
    name: 'Index',
    component: Index
  },
  {
    // /zh/shop/1
    path: '/:lang/shop/:id',
    name: 'Shop',
    component: ShopDetail
  },
  {
    path: '/:lang/payment',
    name: 'Payment',
    component: Payment
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound
  },
  
]

const router = createRouter({ history, routes });

export default router