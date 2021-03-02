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
            <a href="/Forgotpassword">Forgot password?</a>
          </div>
        </div>

        <!-- Sign in button -->
        <button class="btn btn-info btn-block my-4" type="submit">
          Sign in
        </button>
      </form>
    </div>
  </div>
</template>

<script>
// numrow = 0 is Admin 1 is not admin
import firebase from "firebase";
import Swal from "sweetalert2";
export default {
  name: "Login",
  data: function () {
    return { email: "", password: "", numrow: 0 };
  },
  mounted() {
    firebase.auth.OAuthProvider;
  },
  methods: {
    login(e) {
      var db = firebase.firestore();
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then(
          (user) => {
            // console.log(user.user.email);
            // var docRef = db
            //   .collection("InfoPatient")
            //   .where("Email", "==", user.user.email);
            // docRef
            //   .get()
            //   .then((doc) => {
            //     doc.forEach((element) => {
            //       console.log(element.id);
            //       localStorage.setItem("uid", element.id);
            //       window.location.href = "/dashboard";
            //     });
            //   })
            //   .catch(function (error) {
            //     console.log("Error getting document:", error);
            //   });

            var docRef = db
              .collection("InfoPatient")
              .where("Email", "==", user.user.email);
            docRef
              .get()
              .then((doc) => {
                this.numrow = doc.size;
                if (this.numrow == 0) {
                  localStorage.setItem("isAdmin", 1);
                } else {
                  doc.forEach((element) => {
                    localStorage.setItem("uid", element.id);
                    localStorage.setItem("isAdmin", 0);
                  });
                }
                window.location.href = "/dashboard";
              })
              .catch(function (error) {
                console.log("Error getting document:", error);
              });
            // localStorage.setItem("isAdmin", true);
            // window.location.href = "/dashboard";
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
                  localStorage.setItem("isAdmin", 1);
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