import { createStore } from 'vuex'
import { ref,reactive } from "vue";

export const store = createStore({
    state () {
        return {
            currLang: 'zh',
            login: ref(false),
            order: []
        }
    },
    getters:{
        currLang:state => {
            return state.currLang
        },
        order:state => {
            return state.order
        }
    },
    actions:{
        order: ({commit}, order) => {
            commit("order", order)
        }
    },
    mutations:{
        order:(state, val)=>{
            state.order = val;
        }
    }
})