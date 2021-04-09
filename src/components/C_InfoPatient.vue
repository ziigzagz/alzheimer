<template>
  <div class="container">
    <button class="btn btn-info" @click="edit" v-if="isAdmin" id="edit">แก้ไข</button>

    <!-- ข้อมูลส่วนตัว -->
    <div class="row">
      <div class="col text-center">
        <h1>ข้อมูลส่วนตัว</h1>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">หมายเลขผู้ป่วย</label>
        <input type="text" id="hn" class="form-control" v-model="ID" readonly />
      </div>
      <div class="col">
        <label class="form-label">ชื่อ-สกุล</label>
        <input
          type="text"
          class="form-control"
          v-model="ชื่อ"
          id="name"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">อายุ</label>
        <input
          type="text"
          id="age"
          class="form-control"
          v-model="อายุ"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">วัน-เดือน-ปีเกิด</label>
        <input
          type="text"
          id="bd"
          class="form-control"
          v-model="วันเกิด"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">น้ำหนัก</label>
        <input
          type="text"
          id="w"
          class="form-control"
          v-model="น้ำหนัก"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">ส่วนสูง</label>
        <input
          type="text"
          id="h"
          class="form-control"
          v-model="ส่วนสูง"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">ที่อยู่บ้านเลขที่</label>
        <input
          type="text"
          id="home"
          class="form-control"
          v-model="บ้านเลขที่"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">หมู่ที่</label>
        <input
          type="text"
          id="moo"
          class="form-control"
          v-model="หมู่"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">ตรอก/ซอย</label>
        <input
          type="text"
          id="alley"
          class="form-control"
          v-model="ตรอกซอย"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">ถนน</label>
        <input
          type="text"
          id="road"
          class="form-control"
          v-model="ถนน"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">อำเภอ</label>
        <input
          type="text"
          id="amper"
          class="form-control"
          v-model="อำเภอ"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">จังหวัด</label>
        <input
          type="text"
          id="provice"
          class="form-control"
          v-model="จังหวัด"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">รหัสไปรษณีย์</label>
        <input
          type="text"
          id="zipcode"
          class="form-control"
          v-model="รหัสไปรษณีย์"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">โทรศัพท์</label>
        <input
          type="text"
          id="tel"
          class="form-control"
          v-model="เบอร์"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">การศึกษาสูงสุด</label>
        <input
          type="text"
          id="edu"
          class="form-control"
          v-model="การศึกษา"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">สาขาวิชา</label>
        <input
          type="text"
          id="สาขา"
          class="form-control"
          v-model="สาขาวิชา"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">อาชีพ</label>
        <input
          type="text"
          id="job"
          class="form-control"
          v-model="อาชีพ"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">ผู้ให้ข้อมูล</label>
        <input
          type="text"
          id="job"
          class="form-control"
          v-model="ผู้ให้ข้อมูล"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">เบอร์ผู้ให้ข้อมูล</label>
        <input
          type="text"
          id="job"
          class="form-control"
          v-model="เบอร์ผู้ให้ข้อมูล"
          readonly
        />
      </div>
    </div>
    <!-- ข้อมูลสุขภาพ -->
    <div class="row">
      <div class="col text-center">
        <h1>ข้อมูลสุขภาพ</h1>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">ประวัติการเจ็บป่วยในอดีต</label>
        <input
          type="text"
          class="form-control"
          v-model="ประวัติการเจ็บป่วยในอดีต"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">ประวัติการผ่าตัด</label>
        <input
          type="text"
          class="form-control"
          v-model="ประวัติการผ่าตัด"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">โรคประจำตัว</label>
        <input
          type="text"
          class="form-control"
          v-model="โรคประจำตัว"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">ยาที่รับประทานประจำ</label>
        <input
          type="text"
          class="form-control"
          v-model="ยาที่รับประทานประจำ"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">แพ้ยา/แพ้อาหาร</label>
        <input type="text" class="form-control" v-model="แพ้ยาอาหาร" readonly />
      </div>
    </div>
    <!-- การสูบบุหรี่ / ยาเส้น // การดื่มเครื่องดื่มที่มีส่วนผสมของแอลกอฮอล์ (เช่น สุรา เบียร์ ยาดองเหล้า -->
    <div class="row">
      <div class="col">
        การสูบบุหรี่ / ยาเส้น
        <input type="text" class="form-control" v-model="สูบบุหรี่" readonly />
      </div>
      <div class="col">
        การดื่มเครื่องดื่มที่มีส่วนผสมของแอลกอฮอล์ (เช่น สุรา เบียร์ ยาดองเหล้า
        <input
          type="text"
          class="form-control"
          v-model="การดื่มแอลกอฮอล"
          readonly
        />
      </div>
    </div>
    <!-- การออกกำลังกาย -->
    <div class="row">
      <div class="col-6">
        การออกกำลังกาย
        <input
          type="text"
          class="form-control"
          v-model="ออกกำลังกาย"
          readonly
        />
      </div>
    </div>
    <!-- การนอนหลับ -->
    <div class="row">
      <div class="col">
        การนอนหลับ
        <input type="text" class="form-control" v-model="การนอนหลับ" readonly />
      </div>
      <div class="col">
        เวลาเข้านอน
        <input
          type="text"
          class="form-control"
          v-model="เวลาเข้านอน"
          readonly
        />
      </div>
      <div class="col">
        เวลาตื่นนอน
        <input
          type="text"
          class="form-control"
          v-model="เวลาตื่นนอน"
          readonly
        />
      </div>
    </div>
    <!-- การรับประทานอาหาร -->
    <div class="row">
      <div class="col">
        การรับประทานอาหาร
        <input
          type="text"
          class="form-control"
          v-model="การรับประทานอาหาร"
          readonly
        />
      </div>
      <div class="col">
        งานอดิเรก
        <input type="text" class="form-control" v-model="งานอดิเรก" readonly />
      </div>
    </div>
    <hr />
    <!-- ความสามารถด้านร่างกาย -->
    <div class="row">
      <div class="col">
        <ul>
          <li>ความสามารถด้านร่างกาย</li>
        </ul>
        <div class="row">
          <div class="col-2">มีปัญหาด้านการมองเห็น</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="มีปัญหาการมองเห็น"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาด้านการได้ยิน</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="มีปัญหาด้านการได้ยิน"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาด้านการเคลื่อนไหว</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="มีปัญหาด้านการเคลื่อนไหว"
              readonly
            />
          </div>
        </div>
      </div>
    </div>
    <!-- ความสามารถด้านความคิดความจำ -->
    <div class="row">
      <div class="col">
        <ul>
          <li>ความสามารถด้านความคิดความจำ</li>
        </ul>
        <div class="row">
          <div class="col-2">มีปัญหาด้านความจำ</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="มีปัญหาด้านความจำ"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาด้านสมาธิ</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="มีปัญหาด้านสมาธิ"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาด้านการจัดการ</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="มีปัญหาด้านการจัดการ"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">หลงทาง จำทางไม่ได้</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="หลงทางจำทางไม่ได้"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาการเขียน/อ่าน</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="มีปัญหาด้านการอ่านเขียน"
              readonly
            />
          </div>
        </div>
      </div>
    </div>
    <!-- ความสามารถด้านอารมณ์/ภาษา -->
    <div class="row">
      <div class="col">
        <ul>
          <li>ความสามารถด้านอารมณ์/ภาษา</li>
        </ul>
        <div class="row">
          <div class="col-2">หงุดหงิด โมโหง่าย</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="หงุดหงิดโมโหง่าย"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">การสร้างสัมพันธภาพ</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="การสร้างสัมพันธภาพ"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">การรอคอย ความอดทน</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="การรอคอยความอดทน"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">การนึกคำพูด สื่อสาร</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="การนึกคำพูดสื่อสาร"
              readonly
            />
          </div>
        </div>
        <div class="row">
          <div class="col-2">การเข้าใจในการสื่อสาร</div>
          <div class="col-2">
            <input
              type="text"
              class="form-control"
              v-model="ความเข้าใจในการสื่อสาร"
              readonly
            />
          </div>
        </div>
      </div>
    </div>
    <button id="savebtn" class="btn btn-success ml-1" @click="save">
      บันทึก
    </button>
  </div>
</template>

<script>
import firebase from "firebase";
import Swal from "sweetalert2";
export default {
  data() {
    return {
      isAdmin: Boolean(parseInt(localStorage.getItem("isAdmin"))),
      Status: 0,
      ID: "",
      คำนำหน้าชื่อ: "",
      ชื่อ: "",
      วันเกิด: "",
      อายุ: "",
      น้ำหนัก: "",
      ส่วนสูง: "",
      คนดูแล: "",
      ผู้ให้ข้อมูล:"",
      เบอร์ผู้ให้ข้อมูล:"",
      Email: "",
      บ้านเลขที่: "",
      หมู่: "",
      ตรอกซอย: "",
      ถนน: "",
      อำเภอ: "",
      จังหวัด: "",
      รหัสไปรษณีย์: "",
      เบอร์: "",
      การศึกษา: "",
      สาขาวิชา: "",
      อาชีพ: "",
      ประวัติการเจ็บป่วยในอดีต: "",
      ประวัติการผ่าตัด: "",
      โรคประจำตัว: "",
      ยาที่รับประทานประจำ: "",
      แพ้ยาอาหาร: "",
      สูบบุหรี่: "",
      การดื่มแอลกอฮอล: "",
      ออกกำลังกาย: "",
      การนอนหลับ: "",
      เวลาเข้านอน: "",
      เวลาตื่นนอน: "",
      การรับประทานอาหาร: "",
      งานอดิเรก: "",
      มีปัญหาการมองเห็น: "",
      มีปัญหาด้านการได้ยิน: "",
      มีปัญหาด้านการเคลื่อนไหว: "",
      มีปัญหาด้านความจำ: "",
      มีปัญหาด้านสมาธิ: "",
      มีปัญหาด้านการจัดการ: "",
      หลงทางจำทางไม่ได้: "",
      มีปัญหาด้านการอ่านเขียน: "",
      หงุดหงิดโมโหง่าย: "",
      การสร้างสัมพันธภาพ: "",
      การรอคอยความอดทน: "",
      การนึกคำพูดสื่อสาร: "",
      ความเข้าใจในการสื่อสาร: "",
    };
  },
  mounted() {
    var x = document.getElementById("savebtn");
    x.style.display = "none";
    var db = firebase.firestore();
    var dataset = {};
    var docRef = db.collection("InfoPatient").doc(localStorage.getItem("uid"));
    docRef.get().then((snapshot) => {
      var dob = new Date(snapshot.data().วันเกิด.seconds);
      //calculate month difference from current date in time
      var month_diff = Date.now() - dob.getTime();
      // var date1 = new Date(time);
      // console.log(snapshot.data().วันเกิด.toDate());
      var yearbd = parseInt(snapshot.data().วันเกิด.toString().split("/")[2]);
      if(yearbd-543 >= 1378 && yearbd-543
       <= 1578){
        yearbd = yearbd+543
        console.log(yearbd,yearbd+543*2,"IF")
      }
      console.log(yearbd+543,yearbd)
      var birthday =
        snapshot.data().วันเกิด.toString().split("/")[1] +
        "/" +
        snapshot.data().วันเกิด.toString().split("/")[0] +
        "/" +
        yearbd;
        // console.log(snapshot.data().วันเกิด.split("/")[2])
      this.ID = snapshot.data().ID;
      this.คำนำหน้าชื่อ = snapshot.data().คำนำหน้าชื่อ;
      this.ชื่อ = snapshot.data().ชื่อ;
      this.วันเกิด = birthday;
      // this.วันเกิด = 99;
      this.อายุ = snapshot.data().อายุ;
      this.น้ำหนัก = snapshot.data().น้ำหนัก;
      this.ส่วนสูง = snapshot.data().ส่วนสูง;
      this.คนดูแล = snapshot.data().คนดูแล;
      this.Email = snapshot.data().Email;
      this.บ้านเลขที่ = snapshot.data().บ้านเลขที่;
      this.หมู่ = snapshot.data().หมู่;
      this.ตรอกซอย = snapshot.data().ตรอกซอย;
      this.ถนน = snapshot.data().ถนน;
      this.อำเภอ = snapshot.data().อำเภอ;
      this.จังหวัด = snapshot.data().จังหวัด;
      this.รหัสไปรษณีย์ = snapshot.data().รหัสไปรษณีย์;
      this.เบอร์ = snapshot.data().เบอร์;
      this.การศึกษา = snapshot.data().การศึกษา;
      this.สาขาวิชา = snapshot.data().สาขาวิชา;
      this.อาชีพ = snapshot.data().อาชีพ;
      this.ผู้ให้ข้อมูล = snapshot.data().ผู้ให้ข้อมูล;
      this.เบอร์ผู้ให้ข้อมูล = snapshot.data().เบอร์ผู้ให้ข้อมูล;
      this.ประวัติการเจ็บป่วยในอดีต = snapshot.data().ประวัติการเจ็บป่วยในอดีต;
      this.ประวัติการผ่าตัด = snapshot.data().ประวัติการผ่าตัด;
      this.โรคประจำตัว = snapshot.data().โรคประจำตัว;
      this.ยาที่รับประทานประจำ = snapshot.data().ยาที่รับประทานประจำ;
      this.แพ้ยาอาหาร = snapshot.data().แพ้ยาอาหาร;
      this.สูบบุหรี่ = snapshot.data().สูบบุหรี่;
      this.การดื่มแอลกอฮอล = snapshot.data().การดื่มแอลกอฮอล;
      this.ออกกำลังกาย = snapshot.data().ออกกำลังกาย;
      this.การนอนหลับ = snapshot.data().การนอนหลับ;
      this.เวลาเข้านอน = snapshot.data().เวลาเข้านอน;
      this.เวลาตื่นนอน = snapshot.data().เวลาตื่นนอน;
      this.การรับประทานอาหาร = snapshot.data().การรับประทานอาหาร;
      this.งานอดิเรก = snapshot.data().งานอดิเรก;
      this.มีปัญหาการมองเห็น = snapshot.data().มีปัญหาการมองเห็น;
      this.มีปัญหาด้านการได้ยิน = snapshot.data().มีปัญหาด้านการได้ยิน;
      this.มีปัญหาด้านการเคลื่อนไหว = snapshot.data().มีปัญหาด้านการเคลื่อนไหว;
      this.มีปัญหาด้านความจำ = snapshot.data().มีปัญหาด้านความจำ;
      this.มีปัญหาด้านสมาธิ = snapshot.data().มีปัญหาด้านสมาธิ;
      this.มีปัญหาด้านการจัดการ = snapshot.data().มีปัญหาด้านการจัดการ;
      this.หลงทางจำทางไม่ได้ = snapshot.data().หลงทางจำทางไม่ได้;
      this.มีปัญหาด้านการอ่านเขียน = snapshot.data().มีปัญหาด้านการอ่านเขียน;
      this.หงุดหงิดโมโหง่าย = snapshot.data().หงุดหงิดโมโหง่าย;
      this.การสร้างสัมพันธภาพ = snapshot.data().การสร้างสัมพันธภาพ;
      this.การรอคอยความอดทน = snapshot.data().การรอคอยความอดทน;
      this.การนึกคำพูดสื่อสาร = snapshot.data().การนึกคำพูดสื่อสาร;
      this.ความเข้าใจในการสื่อสาร = snapshot.data().ความเข้าใจในการสื่อสาร;
      // console.log(snapshot.data())
    });
  },
  methods: {
    print() {
      window.print();
    },
    save() {
      // location.reload();
      var db = firebase.firestore();
      const update = db
        .collection("InfoPatient")
        .doc(localStorage.getItem("uid"));
      update
        .update({
          ชื่อ: this.ชื่อ,
          น้ำหนัก: this.น้ำหนัก,
          ส่วนสูง: this.ส่วนสูง,
          คนดูแล: this.คนดูแล,
          Email: this.Email,
          บ้านเลขที่: this.บ้านเลขที่,
          หมู่: this.หมู่,
          ตรอกซอย: this.ตรอกซอย,
          ถนน: this.ถนน,
          อำเภอ: this.อำเภอ,
          จังหวัด: this.จังหวัด,
          รหัสไปรษณีย์: this.รหัสไปรษณีย์,
          เบอร์: this.เบอร์,
        })
        .then(() => {
          Swal.fire({
            position: "top-end",
            icon: "success",
            title: "อัพเดตข้อมูลสำเร็จ",
            showConfirmButton: false,
            timer: 3000,
          }).then(()=>{
            location.reload();
          });
        });
    },
    edit() {
      document.getElementById("name").removeAttribute("readonly");
      document.getElementById("home").removeAttribute("readonly");
      document.getElementById("moo").removeAttribute("readonly");
      document.getElementById("alley").removeAttribute("readonly");
      document.getElementById("road").removeAttribute("readonly");
      document.getElementById("amper").removeAttribute("readonly");
      document.getElementById("provice").removeAttribute("readonly");
      document.getElementById("zipcode").removeAttribute("readonly");
      document.getElementById("tel").removeAttribute("readonly");
      document.getElementById("edu").removeAttribute("readonly");
      document.getElementById("สาขา").removeAttribute("readonly");
      var x = document.getElementById("savebtn");
      var y = document.getElementById("edit");
      y.style.display = "none";
      if (x.style.display === "block") {
        x.style.display = "none";
      } else {
        x.style.display = "block";
      }
    },
  },
};
</script>

<style>
</style>