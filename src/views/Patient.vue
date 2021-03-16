<template>
  <v-card class="mx-auto" height="100%">
    <Navdraw />
    <div class="container">
      <div class="row">
        <div class="col-4">
          <label for="exampleFormControlInput1" class="form-label"
            >หมายเลขผู้ป่วย</label
          >
          <input
            type="email"
            class="form-control"
            id="exampleFormControlInput1"
            v-model="HN"
            readonly
          />
        </div>
        <div class="col-8">
          <label for="exampleFormControlInput2" class="form-label"
            >ชื่อ-สกุล ผู้ป่วย</label
          >
          <input
            type="email"
            class="form-control"
            id="exampleFormControlInput2"
            v-model="ชื่อ"
            readonly
          />
        </div>
      </div>

      <div class="row">
        <ul class="nav nav-tabs" id="myTab" role="tablist">
          <li class="nav-item text-danger" role="presentation">
            <a
              @click="setMode(1)"
              class="nav-link"
              id="tab1"
              data-bs-toggle="tab"
              href="#profile"
              role="tab"
              aria-controls="home"
              aria-selected="true"
              >ข้อมูลส่วนตัว</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              @click="setMode(2)"
              class="nav-link"
              id="tab2"
              data-bs-toggle="tab"
              href="#exam"
              role="tab"
              aria-controls="profile"
              aria-selected="false"
              >ออกกำลังกาย</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              @click="setMode(3)"
              class="nav-link active"
              id="tab3"
              data-bs-toggle="tab"
              href="#homework"
              role="tab"
              aria-controls="contact"
              aria-selected="false"
              >การบ้าน</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              @click="setMode(4)"
              class="nav-link"
              id="tab4"
              data-bs-toggle="tab"
              href="#diary"
              role="tab"
              aria-controls="contact"
              aria-selected="false"
              >บันทึก</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              @click="setMode(5)"
              class="nav-link"
              id="tab5"
              data-bs-toggle="tab"
              href="#advice"
              role="tab"
              aria-controls="contact"
              aria-selected="false"
              >คำแนะนำ</a
            >
          </li>
        </ul>
        <div class="tab-content" id="myTabContent">
          <!-- ข้อมูลส่วนตัว -->
          <div
            class="tab-pane fade "
            id="profile"
            role="tabpanel"
            aria-labelledby="home-tab"
          >
            <InfoPatient />
          </div>
          <!-- แบบฝึกหัด -->
          <div
            class="tab-pane fade"
            id="exam"
            role="tabpanel"
            aria-labelledby="profile-tab"
          >
            <ExamList />
          </div>
          <!-- การบ้าน -->
          <div
            class="tab-pane fade show active"
            id="homework"
            role="tabpanel"
            aria-labelledby="contact-tab"
          >
            <Homework />
          </div>
          <!-- บันทึก -->
          <div
            class="tab-pane fade"
            id="diary"
            role="tabpanel"
            aria-labelledby="contact-tab"
          >
            <Diary />
          </div>
          <!-- คำแนะนำ -->
          <div
            class="tab-pane fade"
            id="advice"
            role="tabpanel"
            aria-labelledby="contact-tab"
          >
            <Advice />
          </div>
        </div>
      </div>
    </div>
  </v-card>
</template>

<script>
import firebase from "firebase";
import Navdraw from "@/components/Navdraw.vue";
import Homework from "@/components/C_Homework.vue";
import Advice from "@/components/C_Advice.vue";
import Diary from "@/components/C_Diary.vue";
import ExamList from "@/components/C_ExamList.vue";
import InfoPatient from "@/components/C_InfoPatient.vue";

export default {
  data() {
    return {
      HN: "",
      ชื่อ: "",
    };
  },

  mounted() {
    var tmp = localStorage.getItem("Tab_mode");
    if (tmp == 1) {
      document.getElementById("tab1").classList.add("active");
      document.getElementById("tab2").classList.remove("active");
      document.getElementById("tab3").classList.remove("active");
      document.getElementById("tab4").classList.remove("active");
      document.getElementById("tab5").classList.remove("active");
      // ------------------------------------------------------------
      document.getElementById("profile").classList.add("show");
      document.getElementById("profile").classList.add("active");
      document.getElementById("exam").classList.remove("show");
      document.getElementById("exam").classList.remove("active");
      document.getElementById("homework").classList.remove("show");
      document.getElementById("homework").classList.remove("active");
      document.getElementById("diary").classList.remove("show");
      document.getElementById("diary").classList.remove("active");
      document.getElementById("advice").classList.remove("show");
      document.getElementById("advice").classList.remove("active");
    } else {
      if (tmp == 2) {
        document.getElementById("tab2").classList.add("active");
        document.getElementById("tab1").classList.remove("active");
        document.getElementById("tab3").classList.remove("active");
        document.getElementById("tab4").classList.remove("active");
        document.getElementById("tab5").classList.remove("active");
        // ------------------------------------------------------------
        document.getElementById("profile").classList.remove("show");
        document.getElementById("profile").classList.remove("active");
        document.getElementById("exam").classList.add("show");
        document.getElementById("exam").classList.add("active");
        document.getElementById("homework").classList.remove("show");
        document.getElementById("homework").classList.remove("active");
        document.getElementById("diary").classList.remove("show");
        document.getElementById("diary").classList.remove("active");
        document.getElementById("advice").classList.remove("show");
        document.getElementById("advice").classList.remove("active");
      } else {
        if (tmp == 3) {
          document.getElementById("tab3").classList.add("active");
          document.getElementById("tab2").classList.remove("active");
          document.getElementById("tab1").classList.remove("active");
          document.getElementById("tab4").classList.remove("active");
          document.getElementById("tab5").classList.remove("active");
          // ------------------------------------------------------------
          document.getElementById("profile").classList.remove("show");
          document.getElementById("profile").classList.remove("active");
          document.getElementById("exam").classList.remove("show");
          document.getElementById("exam").classList.remove("active");
          document.getElementById("homework").classList.add("show");
          document.getElementById("homework").classList.add("active");
          document.getElementById("diary").classList.remove("show");
          document.getElementById("diary").classList.remove("active");
          document.getElementById("advice").classList.remove("show");
          document.getElementById("advice").classList.remove("active");
        } else {
          if (tmp == 4) {
            document.getElementById("tab4").classList.add("active");
            document.getElementById("tab2").classList.remove("active");
            document.getElementById("tab3").classList.remove("active");
            document.getElementById("tab1").classList.remove("active");
            document.getElementById("tab5").classList.remove("active");
            // ------------------------------------------------------------
            document.getElementById("profile").classList.remove("show");
            document.getElementById("profile").classList.remove("active");
            document.getElementById("exam").classList.remove("show");
            document.getElementById("exam").classList.remove("active");
            document.getElementById("homework").classList.remove("show");
            document.getElementById("homework").classList.remove("active");
            document.getElementById("diary").classList.add("show");
            document.getElementById("diary").classList.add("active");
            document.getElementById("advice").classList.remove("show");
            document.getElementById("advice").classList.remove("active");
          } else {
            if (tmp == 5) {
              document.getElementById("tab5").classList.add("active");
              document.getElementById("tab2").classList.remove("active");
              document.getElementById("tab3").classList.remove("active");
              document.getElementById("tab4").classList.remove("active");
              document.getElementById("tab1").classList.remove("active");
              // ------------------------------------------------------------
              document.getElementById("profile").classList.remove("show");
              document.getElementById("profile").classList.remove("active");
              document.getElementById("exam").classList.remove("show");
              document.getElementById("exam").classList.remove("active");
              document.getElementById("homework").classList.remove("show");
              document.getElementById("homework").classList.remove("active");
              document.getElementById("diary").classList.remove("show");
              document.getElementById("diary").classList.remove("active");
              document.getElementById("advice").classList.add("show");
              document.getElementById("advice").classList.add("active");
            } else {
            }
          }
        }
      }
    }
    // document.getElementById("tab1").classList.add("active");
    var db = firebase.firestore();
    var dataset = {};
    var docRef = db.collection("InfoPatient").doc(localStorage.getItem("uid"));
    docRef.get().then((snapshot) => {
      this.HN = snapshot.data().ID;
      this.ชื่อ = snapshot.data().ชื่อ;
      // console.log(snapshot.data())
    });
  },
  methods: {
    setMode(i) {
      localStorage.setItem("Tab_mode", i);
    },
  },
  components: {
    Navdraw,
    Homework,
    Advice,
    Diary,
    ExamList,
    InfoPatient,
  },
};
</script>

<style>
</style>