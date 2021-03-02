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
            v-model="Name"
            readonly
          />
        </div>
      </div>

      <div class="row">
        <ul class="nav nav-tabs " id="myTab" role="tablist">
          <li class="nav-item text-danger" role="presentation">
            <a
              class="nav-link "
              id="home-tab"
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
              class="nav-link active"
              id="profile-tab"
              data-bs-toggle="tab"
              href="#exam"
              role="tab"
              aria-controls="profile"
              aria-selected="false"
              >แบบฝึกหัด</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              class="nav-link"
              id="contact-tab"
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
              class="nav-link"
              id="contact-tab"
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
              class="nav-link"
              id="contact-tab"
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
            class="tab-pane fade  show active"
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
            class="tab-pane fade"
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
  data(){
    return {
      HN:"",
      Name:""
    }
  },
  mounted() {
    var db = firebase.firestore();
    var dataset = {};
    var docRef = db.collection("InfoPatient").doc(localStorage.getItem("uid"));
     docRef.get().then((snapshot) => {
      this.HN = snapshot.data().ID;
      this.Name = snapshot.data().Name;
      this.Email = snapshot.data().Email;
      this.Age = snapshot.data().Age;
      this.Birthday = snapshot.data().Birthday;
      // console.log(snapshot.data())
    });
  },
  components: {
    Navdraw,
    Homework,
    Advice,
    Diary,
    ExamList,
    InfoPatient
  },
};
</script>

<style>
</style>