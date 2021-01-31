<template>
  <div>
    <v-app-bar color="indigo darken-2" dark>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-toolbar-title class="tz">Staff</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
      class="bg-dark text-dark"
    >
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-img
            class="mx-auto"
            max-height="150"
            max-width="120"
            :src="this.imageprofile"
          ></v-img>
          <div class="row">
            <div class="col text-white text-center mx-auto">
              {{ this.users }}
            </div>
          </div>
          <div class="row">
            <div class="col text-center">
              <button class="btn btn-danger" @click="logout">Logout</button>
            </div>
          </div>
          <hr />
          <v-list-item class="mt-3 m-h">
            <v-list-item-title color="deep-orange darken-2">
              <img
                src="https://www.flaticon.com/svg/static/icons/svg/609/609803.svg"
                width="20"
                height="20"
                alt=""
                srcset=""
              />
              <a class="text-white ml-5" href="/"> หน้าแรก</a>
            </v-list-item-title>
          </v-list-item>

          <v-list-item class="mt-3 m-h">
            <v-list-item-title color="deep-orange darken-2">
              <img
                src="https://www.flaticon.com/svg/static/icons/svg/2750/2750657.svg"
                width="20"
                height="20"
                alt=""
                srcset=""
              />
              <a class="text-white ml-5" href="/PatientList"> ผู้ป่วย</a>
            </v-list-item-title>
          </v-list-item>
          
          <v-list-item class="mt-3 m-h">
            <v-list-item-title color="deep-orange darken-2">
              <img
                src="@/assets/icon/homework.png"
                width="20"
                height="20"
                alt=""
                srcset=""
              />
              <a class="text-white ml-5" href="/HomeworkList"> การบ้าน</a>
            </v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script >
import firebase from "firebase";
export default {
  data: () => ({
    drawer: false,
    group: null,
    users: "",
    imageprofile: "",
    isAdmin: localStorage.getItem("isAdmin"),
  }),

  async mounted() {
    await firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.users = user.displayName;
        this.imageprofile = user.photoURL;
      } else {
        // No user is signed in.
      }
    });
  },
  methods: {
    logout() {
      this.$router.replace("/logout");
    },
  },
};
</script>

<style scoped>
.tz{
  font-size: 1.8em;
}
a {
  color: white;
  font-size: 15px;
  text-decoration: none;
  transition: font-size 0.2s;
}
a:hover {
  color: white;
  text-decoration: none;
  font-size: 20px;
}

</style>