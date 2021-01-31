<template>
  <div class="col-4 mx-auto">
    <br /><br />
    <div class="card">
      <form class="text-center border border-light p-5" @submit="login">
        <p class="h4 mb-4">Sign in</p>

        <!-- Email -->
        <input
          type="email"
          id="defaultLoginFormEmail"
          class="form-control mb-4"
          placeholder="E-mail"
          v-model="email"
        />

        <!-- Password -->
        <input
          type="password"
          id="defaultLoginFormPassword"
          class="form-control mb-4"
          placeholder="Password"
          v-model="password"
        />

        <div class="d-flex justify-content-around">
          <div>
            <!-- Forgot password -->
            <a href="/Forgetpass">Forgot password?</a>
          </div>
        </div>

        <!-- Sign in button -->
        <button class="btn btn-info btn-block my-4" type="submit">
          Sign in
        </button>

        <!-- Register -->
        <!-- Social login -->
        <p>or sign in with:</p>

        <a @click="loginWithProvider" class="mx-5" role="button">
          <img
            src="../assets/icon/google.png"
            alt=""
            width="20"
            height="20"
          />
        </a>
      </form>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";
import Swal from "sweetalert2";
export default {
  name: "Login",
  data: function () {
    return { email: "", password: "" };
  },
  methods: {
    login(e) {
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then(
          (user) => {
            var user = firebase.auth().currentUser;
            console.log(user);
            if (user != null) {
              this.$router.replace("/home");
              user.providerData.forEach((profile) => {
                console.log(profile);
                console.log(user.uid);
                localStorage.setItem("uid", user.uid);
                localStorage.setItem("User", profile.email);
                localStorage.setItem("StatusLogin", 1);
                if (profile.uid == "zigzagzaczax@gmail.com") {
                  localStorage.setItem("isAdmin", true);
                }
              });
            }
            this.$router.replace("/");
          },
          (err) => {
            alert(err.message);
          }
        );
      e.preventDefault();
    },
    loginWithProvider(e) {
      var provider = new firebase.auth.GoogleAuthProvider();
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(
          (user) => {
            var user = firebase.auth().currentUser;
            if (user != null) {
              user.providerData.forEach((profile) => {
                console.log(profile);
                console.log(user.uid);
                localStorage.setItem("uid", user.uid);
                localStorage.setItem("User", profile.email);
                localStorage.setItem("StatusLogin", 1);
                // console.log("Sign-in provider: " + profile.providerId);
                // console.log("  Provider-specific UID: " + profile.uid);
                // console.log("  Name: " + profile.displayName);
                // console.log("  Email: " + profile.email);
                // console.log("  Photo URL: " + profile.photoURL);
                if (profile.email == "zigzagzaczax@gmail.com") {
                  localStorage.setItem("isAdmin", true);
                }
                Swal.fire({
                  position: "center",
                  icon: "success",
                  title: "ลงชื่อเข้าใช้สำเร็จ",
                  showConfirmButton: false,
                  timer: 1500,
                }).then(() => {
                  this.$router.replace("/");
                });
              });
            }
          },
          (err) => {
            alert(err.message);
          }
        )
        .then(() => {});
    },
  },
};
</script>

<style></style>