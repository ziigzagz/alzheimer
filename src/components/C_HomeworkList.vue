<template>
  <div class="container">
    <div class="row">
      <div class="col-1">
        <button class="btn btn-info" @click="CreateHomework">เพิ่ม</button>
        <v-row justify="center"> </v-row>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <input
          type="text"
          id="myInput"
          @keyup="myFunction"
          placeholder="Search for names.."
          title="Type in a name"
        />
        <table class="table table-striped text-center" id="myTable">
          <tr>
            <th scope="col">#</th>
            <th scope="col">การบ้าน</th>
            <th scope="col">#</th>
          </tr>
          <tr v-for="(item, index) in homeworkTemplate" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item }}</td>
            <td>
        <button class="border btn btn-info bg-info">แก้ไข</button>
        <button class="border btn btn-danger bg-danger">ลบ</button>
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";
import Swal from "sweetalert2";
export default {
  data() {
    return {
      homeworkTemplate: [],
      dialog: false,
    };
  },
  mounted() {
    var db = firebase.firestore();
    var docRef = db.collection("HomeworkTemplate");
    docRef.get().then((doc) => {
      doc.forEach((element) => {
        console.log(element.data());
        this.homeworkTemplate.push(element.data().Homework_name);
      });
    });
  },
  methods: {
    myFunction() {
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }
      }
    },
    CreateHomework() {
      window.location.href = "/CreateHomework";
    },
  },
};
</script>

<style>
#myInput {
  background-image: url('/css/searchicon.png');
  background-position: 10px 10px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}
</style>