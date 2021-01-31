<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="text-center">
          <iframe
            width="1280"
            height="720"
            src="https://www.youtube.com/embed/TyaIHBmzYl8"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col text-center">
        <button class="btn btn-success" id="btn" @click="next">สำเร็จ</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    next() {
      document.getElementById("btn").innerHTML = "สำเร็จ";
    },
  },
};
</script>

<style>
</style>