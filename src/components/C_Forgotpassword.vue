<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-6 mx-auto text-center">
       
            <p class="h4 mb-4">ลืมรหัสผ่าน</p>
            <!-- Email -->
            <input
              type="email"
              id="email"
              class="form-control mb-4"
              placeholder="E-mail"
              v-model="email"
            />
            <p>
กรุณาใส่รหัสผ่าน ระบบจะทำการส่งลิงค์รีเซ็ตรหัสผ่านให้คุณทางอีเมลล์ดังกล่าว
            </p>
            <!-- Sign in button -->
            <button class="btn btn-info btn-block my-4" @click="sendemail">
              Send
            </button>
          </form>
        </div>
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
      email: "",
    };
  },
  methods: {
    sendemail(e) {
      Swal.fire({
        title: "ยืนยัน",
        text: "คุณต้องการยืนยันการทำตามคำแนะนำใช่หรือไม่?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "ใช่",
        cancelButtonText: "ไม่",
      }).then((result) => {
        if (result.isConfirmed) {
          var auth = firebase.auth();
          var emailAddress = document.getElementById("email").value;
          auth
            .sendPasswordResetEmail(emailAddress)
            .then(() => {
              //   alert("ระบบส่งลิงค์สำหรับรีเซ็ทรหัสผ่านไปใน Email ของคุณแล้ว !");
              Swal.fire({
                position: "top-end",
                icon: "success",
                title: "ระบบส่งลิงค์สำหรับรีเซ็ทรหัสผ่านไปใน Email ของคุณแล้ว !",
                showConfirmButton: false,
                timer: 3000,
              });
            }).then(()=>{
                window.location.href = "/login"
            })
            .catch(function (error) {
              // An error happened.
            });
        //   Swal.fire({
        //     position: "center",
        //     icon: "success",
        //     title: "ยืนยันสำเร็จ!",
        //     showConfirmButton: false,
        //     timer: 1500,
        //   }).then(() => {
        //     location.reload();
        //   });
          // Swal.fire("ยืนยันสำเร็จ!", "ทำการอัปเดตเรียบร้อย", "success");
        }
      });
    },
  },
};
</script>

<style>
</style>