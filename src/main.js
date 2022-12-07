import Vue from 'vue'
import App from './App.vue'
import {initRouter} from './router'
import './theme/index.less'
import Antd from 'ant-design-vue'
import Viser from 'viser-vue'
import '@/mock'
import store from './store'
import 'animate.css/source/animate.css'
import Plugins from '@/plugins'
import {initI18n} from '@/utils/i18n'
import bootstrap from '@/bootstrap'
import 'moment/locale/zh-cn'
import * as echarts from 'echarts'
import axios from 'axios'

const router = initRouter(store.state.setting.asyncRoutes)
const i18n = initI18n('CN', 'US')

// 挂载一个自定义属性$http
// Vue.prototype.$http = axios
// 全局配置axios请求根路径(axios.默认配置.请求根路径)
Vue.prototype.$axios = axios
axios.defaults.baseURL = 'http://127.0.0.1:7000/'
Vue.use(Antd)
Vue.config.productionTip = false
Vue.use(Viser)
Vue.use(Plugins)
Vue.prototype.$echarts = echarts;

bootstrap({router, store, i18n, message: Vue.prototype.$message})


new Vue({
  router,
  store,
  i18n,
  render: h => h(App),
}).$mount('#app')
