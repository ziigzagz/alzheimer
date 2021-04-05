import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import firebase from 'firebase/app'
import * as $ from 'jquery'
Vue.config.productionTip = false
// app.use(VueSweetalert2);
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDZwOxmdmAKKLlXK2lix66k_tlSSBW9WAY",
  authDomain: "alzeimer-4a47b.firebaseapp.com",
  projectId: "alzeimer-4a47b",
  storageBucket: "alzeimer-4a47b.appspot.com",
  messagingSenderId: "361460881993",
  appId: "1:361460881993:web:145e2bd4dd8cd977737d98",
  measurementId: "G-BHZRR8PJT5"
};
// var db = firebase.firestore();
firebase.initializeApp(firebaseConfig)
export function somethingWithjQuery() {
  console.log(123123123)
  $(document).ready(function () {
    $('#example').DataTable();
  });
}
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app');
