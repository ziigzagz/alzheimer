<template>
  <div class="container">
    <div class="row">
      <div class="col-1">
        <v-row justify="center">
          <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark v-bind="attrs" v-on="on" v-if="isAdmin">
                เพิ่ม
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">เพิ่มการออกกำลังกาย</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col>
                      <v-text-field
                        label="ชื่อการออกกำลังกาย*"
                        id="nameExam"
                        hint=""
                        persistent-hint
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-container style="max-width: 500px">
                      <v-text-field
                        v-model="newTask"
                        label="กรอกลิงค์ออกกำลังกาย (Youtube)"
                        solo
                        @keydown.enter="create"
                      >
                      </v-text-field>

                      <h2 class="display-1 success--text pl-4">
                        จำนวนลิงค์:&nbsp;
                        <v-fade-transition leave-absolute>
                          <span :key="`tasks-${tasks.length}`">
                            {{ tasks.length }}
                          </span>
                        </v-fade-transition>
                      </h2>
                      <v-card v-if="tasks.length > 0">
                        <v-slide-y-transition class="py-0" group tag="v-list">
                          <template v-for="(task, i) in tasks">
                            <v-divider
                              v-if="i !== 0"
                              :key="`${i}-divider`"
                            ></v-divider>

                            <v-list-item :key="`${i}-${task.text}`">
                              <div class="ml-4" v-text="task.text"></div>
                            </v-list-item>
                          </template>
                        </v-slide-y-transition>
                      </v-card>
                    </v-container>
                  </v-row>
                </v-container>
                div
                <small>*indicates required field</small>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close"> ปิด </v-btn>
                <v-btn color="blue darken-1" text @click="save"> บันทึก </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <table class="table table-striped text-center">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">ชื่อออกกำลังกาย</th>
              <th scope="col">เวลา</th>
              <th scope="col">สถานะ</th>
              <th scope="col">ดู</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in test" :key="index">
              <th scope="row">{{ index + 1 }}</th>
              <td>
                {{ item.data.ID }}
              </td>
              <td>{{ item.data.date }}</td>
              <td v-if="item.data.status == 1">
                <span class="badge bg-success">สำเร็จ</span>
              </td>
              <td v-else><span class="badge bg-danger">ไม่สำเร็จ</span></td>
              <td>
                <button class="btn btn-info" @click="viewInfo(item.ID)" v-if="item.data.status == 0">
                  ดูข้อมูล
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";
import Advice from "@/components/C_Advice.vue";
export default {
  data: () => ({
    dialog: false,
    tasks: [],
    newTask: null,
    video: [],
    test: [],
    isAdmin: Boolean(parseInt(localStorage.getItem("isAdmin"))),
  }),
  components: {
    Advice,
  },
  computed: {
    completedTasks() {
      return this.tasks.filter((task) => task.done).length;
    },
    progress() {
      return (this.completedTasks / this.tasks.length) * 100;
    },
    remainingTasks() {
      return this.tasks.length - this.completedTasks;
    },
  },

  async mounted() {
    var db = firebase.firestore();
    if (!localStorage.getItem("isAdmin")) {
      var docRef = db
        .collection("Exam")
        .where("user", "==", localStorage.getItem("uid"));
    } else {
      var docRef = db
        .collection("Exam")
        .where("user", "==", localStorage.getItem("uid"));
    }

    var dataset = {};
    var video;
    var videolink;
    var data = [];
    var videolinkset = [];
    var i = 0;
    docRef
      .get()
      .then((doc) => {
        doc.docs.forEach((element) => {
          // console.log(element.id);
        });
        // console.log(doc.docs[0]);
        var tmp = []; // list data exam
        doc.docs.forEach((element) => {
          // console.log(element.data());
          this.test.push({
            ID: element.id,
            data: element.data(),
          });
        });
      })
      .catch(function (error) {
        console.log("Error getting document:", error);
      });
  },

  methods: {
    viewInfo(uid) {
      console.log(uid)
      localStorage.setItem("ID_Exam",uid);
      window.location.href = "/Exam"
    },
    create() {
      this.tasks.push({
        text: this.newTask,
      });
      this.newTask = null;
      console.log();
    },

    close() {
      this.dialog = false;
    },
    save() {
      var d = new Date();
      var date = d.getDate();
      var month = d.getMonth();
      var year = d.getFullYear();
      var hours = d.getHours();
      var minutes = d.getMinutes();
      var db = firebase.firestore();
      if (minutes < 10) {
        minutes = "0" + minutes;
      }
      month += 1;
      db.collection("Exam")
        .add({
          ID: document.getElementById("nameExam").value,
          status: 0,
          user: localStorage.getItem("uid"),
          v: this.tasks,
          date:
            date +
            "/" +
            month +
            "/" +
            year +
            " " +
            hours +
            ":" +
            minutes +
            "น.",
        })
        .then((res) => {
          location.reload();
        })
        .catch(function (error) {
          console.error("Error adding document: ", error);
        });
      console.log(document.getElementById("name").value);
    },
  },
};
</script>

<style>
</style>