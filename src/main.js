import './assets/main.css'
import 'primevue/resources/themes/aura-light-indigo/theme.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';
import App from './App.vue'
import Router from './router'


const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(Router)
app.use(PrimeVue)

app.mount('#app')
