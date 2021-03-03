import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import firebase from "firebase";
Vue.use(VueRouter);

const routes = [
  {
    path: "/dashboard",
    name: "Home",
    component: () => import("../views/Dashboard.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Dashboard.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/about",
    name: "About",
    component: () =>  import("../views/About.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/Dashboard",
    name: "Dashboard",
    component: () =>  import("../views/Dashboard.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/Patient",
    name: "Patient",
    component: () => import("../views/Patient.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/PatientList",
    name: "PatientList",
    component: () => import("../views/PatientList.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },

  {
    path: "/Diary-Info",
    name: "Diary-Info",
    component: () => import("../views/Diary_Info.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },

  {
    path: "/Advice-info",
    name: "Advice-info",
    component: () => import("../views/Advice_Info.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },

  {
    path: "/Test",
    name: "Test",
    component: () => import("../views/Test.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/InfoHomework",
    name: "InfoHomework",
    component: () => import("../views/InfoHomework.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/ExamList",
    name: "ExamList",
    component: () => import("../views/ExamList.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  }
  ,
  {
    path: "/Exam",
    name: "Exam",
    component: () => import("../views/Exam.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  }, {
    path: "/Homework",
    name: "Homework",
    component: () => import("../views/Homework.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/Login",
    name: "Login",
    component: () => import("../views/Login.vue"),

  },
  {
    path: "/Logout",
    name: "Logout",
    component: () => import("../views/Logout.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  ,
  {
    path: "/CheckHomework",
    name: "CheckHomework",
    component: () => import("../views/CheckHomework.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },

  {
    path: "/HomeworkList",
    name: "HomeworkList",
    component: () => import("../views/HomeworkList.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/CreateHomework",
    name: "CreateHomework",
    component: () => import("../views/CreateHomework.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
  {
    path: "/Forgotpassword",
    name: "Forgotpassword",
    component: () => import("../views/Forgotpassword.vue"),
    beforeEnter(to, from, next) {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          window.location.href = "/login"
        } else {
          next();
        }
      });
    }
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
