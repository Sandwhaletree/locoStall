import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
// import Components from 'unplugin-vue-components/vite'
// import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // Components({
      // resolvers: [AntDesignVueResolver({ importStyle: "less" })],
    // })
  ],
  // 路徑別名設置
  resolve: {
    alias: {
      '@': path.resolve(__dirname, '../frontend/src')
    }
  },
  css: {
    devSourcemap:true,
    preprocessorOptions: {
      less: {
        javascriptEnabled: true,
      },
      scss: {
        additionalData: `@import "@/assets/scss/shared/_var.scss";`
      },
    },
  },
})
