
import App from './App.vue'
import HelloWorld from './components/HelloWorld.ce.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { defineCustomElement } from 'vue'


const capp = defineCustomElement(App)
const HelloWorldElement = defineCustomElement(HelloWorld)

customElements.define('o-search-logo', capp)
customElements.define('o-search', HelloWorldElement)