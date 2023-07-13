import { createApp } from 'vue'
// import './style.css'
import App from './App.vue'
import router from '../src/router'
import Vuex from 'vuex';
import { store } from './store/store'
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

let app = createApp(App);

app.use(router)
.use(Antd)
.use(store)
.use(Vuex)
// .use(i18n)
.mount('#app')