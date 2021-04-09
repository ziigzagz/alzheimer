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
            <td>{{ item.data.Homework_name }}</td>
            <td>
              <button class="border btn btn-info bg-info"
              @click="EditHomework(item.data,item.id)">แก้ไข</button>
              <button
                class="border btn btn-danger bg-danger"
                @click="Delete(item.id,item.data.Homework_name)"
              >
                ลบ
              </button>
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
    var docRef = db.collection("HomeworkTemplate")
    .where("statusdel", "==", 0)
    .orderBy("Homework_name", "asc");
    docRef.get().then((doc) => {
      doc.forEach((element) => {
        // console.log(element.data());
        // console.log(doc);
        // console.log(element.id);
        this.homeworkTemplate.push({ data: element.data(), id: element.id });
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
    Delete(id,HW_name) {
      var db = firebase.firestore();
      Swal.fire({
        title: "คุณต้องการลบการบ้าน \n \'"+HW_name+"\' ใช่หรือไม่",
        showCancelButton: true,
        icon: "question",
        confirmButtonText: `ยืนยัน`,
        cancelButtonText: "ยกเลิก",
      }).then((result) => {
        if (result.isConfirmed) {
          const update = db.collection("HomeworkTemplate").doc(id);
          update.update({
            statusdel: 1,
          });
          console.log("Document successfully deleted!");
          Swal.fire({
            position: "center",
            icon: "success",
            title: "ลบสำเร็จ!",
            showConfirmButton: false,
            timer: 1500,
          }).then(() => {
            window.location.reload();
          });
        } else if (result.isDenied) {
          Swal.fire("Changes are not saved", "", "info");
        }
      });
    },
    CreateHomework() {
      localStorage.removeItem('Hw_size');
      window.location.href = "/CreateHomework";
    },
    EditHomework(item,id){
      localStorage.setItem("EditHomework",item.Homework_data)
      localStorage.setItem("Hw_size",item.Homework_size)
      localStorage.setItem("Hw_name",item.Homework_name)
      localStorage.setItem("id_hwTemplate",id)
      // console.log(item.Homework_data)
      // console.log(id)
      window.location.href = "/CreateHomework"
    }
  },
};
</script>

<style>
#myInput {
  background-image: url("/css/searchicon.png");
  background-position: 10px 10px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}
</style>