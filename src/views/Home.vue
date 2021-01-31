<template>
  <div class="home">
  
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <div class="container">
      <div class="row">
        <div class="col">
          <ul uk-accordion>
            <li>
              <a class="uk-accordion-title bg-danger text-right" href="#"
                >123</a
              >
              <div class="uk-accordion-content bg-info text-right">123</div>
            </li>
            <li>
              <a class="uk-accordion-title" href="#">456</a>
              <div class="uk-accordion-content">456</div>
            </li>
            <li>
              <a class="uk-accordion-title" href="#">789</a>
              <div class="uk-accordion-content">789</div>
            </li>
          </ul>
        </div>
      </div>


    
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
    HelloWorld,
  },
};
</script>
