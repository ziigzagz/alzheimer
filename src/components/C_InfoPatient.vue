<template>
  <div class="container">
    <button class="btn btn-info" @click="edit">แก้ไข</button>

    <!-- ข้อมูลส่วนตัว -->
    <div class="row">
      <div class="col text-center">
        <h1>ข้อมูลส่วนตัว</h1>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">หมายเลขผู้ป่วย</label>
        <input
          type="text"
          id="hn"
          class="form-control"
          value="6030301195"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">ชื่อ-สกุล ผู้ป่วย</label>
        <input
          type="text"
          class="form-control"
          value="นายอิฟฟาน หะยีอิสมาแอ"
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
          value="22 ปี"
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
          value="4/11/2541"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">น้ำหนัก</label>
        <input
          type="text"
          id="w"
          class="form-control"
          value="60 กก."
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">ส่วนสูง</label>
        <input
          type="text"
          id="h"
          class="form-control"
          value="175 ซม."
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">หมู่เลือด</label>
        <input
          type="text"
          id="bloodgroup"
          class="form-control"
          value="-"
          readonly
        />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">ที่อยู่บ้านเลขที่</label>
        <input type="text" id="home" class="form-control" value="-" readonly />
      </div>
      <div class="col">
        <label class="form-label">หมู่ที่</label>
        <input type="text" id="moo" class="form-control" value="-" readonly />
      </div>
      <div class="col">
        <label class="form-label">ตรอก/ซอย</label>
        <input type="text" id="alley" class="form-control" value="-" readonly />
      </div>
      <div class="col">
        <label class="form-label">ถนน</label>
        <input type="text" id="road" class="form-control" value="-" readonly />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">อำเภอ</label>
        <input type="text" id="amper" class="form-control" value="-" readonly />
      </div>
      <div class="col">
        <label class="form-label">จังหวัด</label>
        <input
          type="text"
          id="provice"
          class="form-control"
          value="-"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">รหัสไปรษณีย์</label>
        <input
          type="text"
          id="zipcode"
          class="form-control"
          value="-"
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
          value="0971512922"
          readonly
        />
      </div>
      <div class="col">
        <label class="form-label">การศึกษาสูงสุด</label>
        <input type="text" id="edu" class="form-control" value="-" readonly />
      </div>
      <div class="col">
        <label class="form-label">สาขาวิชา</label>
        <input type="text" id="สาขา" class="form-control" value="-" readonly />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">อาชีพ</label>
        <input type="text" id="job" class="form-control" value="ข้าราชการ" readonly />
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
        <input type="text" class="form-control" value="-" readonly />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">ประวัติการผ่าตัด</label>
        <input type="text" class="form-control" value="-" readonly />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">โรคประจำตัว</label>
        <input type="text" class="form-control" value="-" readonly />
      </div>
    </div>
    <div class="row">
      <div class="col">
        <label class="form-label">ยาที่รับประทานประจำ</label>
        <input type="text" class="form-control" value="-" readonly />
      </div>
      <div class="col">
        <label class="form-label">แพ้ยา/แพ้อาหาร</label>
        <input type="text" class="form-control" value="-" readonly />
      </div>
    </div>
    <!-- การสูบบุหรี่ / ยาเส้น // การดื่มเครื่องดื่มที่มีส่วนผสมของแอลกอฮอล์ (เช่น สุรา เบียร์ ยาดองเหล้า -->
    <div class="row">
      <div class="col">
        การสูบบุหรี่ / ยาเส้น
        <input type="text" class="form-control" value="-" readonly />
      </div>
      <div class="col">
        การดื่มเครื่องดื่มที่มีส่วนผสมของแอลกอฮอล์ (เช่น สุรา เบียร์ ยาดองเหล้า
        <input type="text" class="form-control" value="-" readonly />
      </div>
    </div>
    <!-- การออกกำลังกาย -->
    <div class="row">
      <div class="col-6">
        การออกกำลังกาย
        <input type="text" class="form-control" value="-" readonly />
      </div>
    </div>
    <!-- การนอนหลับ -->
    <div class="row">
      <div class="col">
        การนอนหลับ
        <input type="text" class="form-control" value="หลับได้ปกติ" readonly />
      </div>
      <div class="col">
        เวลาเข้านอน
        <input type="text" class="form-control" value="22:00 น." readonly />
      </div>
      <div class="col">
        เวลาตื่นนอน
        <input type="text" class="form-control" value="6:00 น." readonly />
      </div>
    </div>
    <!-- การรับประทานอาหาร -->
    <div class="row">
      <div class="col">
        การรับประทานอาหาร
        <input type="text" class="form-control" value="ทานได้ปกติ" readonly />
      </div>
      <div class="col">
        งานอดิเรก
        <input type="text" class="form-control" value="วาดรูป" readonly />
      </div>
      <div class="col">
        เวลาตื่นนอน
        <input type="text" class="form-control" value="6:00 น." readonly />
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
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาด้านการได้ยิน</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาด้านการเคลื่อนไหว</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
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
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาด้านสมาธิ</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาด้านการจัดการ</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">หลงทาง จำทางไม่ได้</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">มีปัญหาการเขียน/อ่าน</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
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
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">การสร้างสัมพันธภาพ</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">การรอคอย ความอดทน</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">การนึกคำพูด สื่อสาร</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
          </div>
        </div>
        <div class="row">
          <div class="col-2">การเข้าใจในการสื่อสาร</div>
          <div class="col-2">
            <input type="text" class="form-control" value="ปกติ" readonly />
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
export default {
  mounted() {
    var x = document.getElementById("savebtn");
    x.style.display = "none";
  },
  methods: {
    print() {
      window.print();
    },
    save() {
      location.reload();
    },
    edit() {
      document.getElementById("name").removeAttribute("readonly");
      document.getElementById("bd").removeAttribute("readonly");
      document.getElementById("bloodgroup").removeAttribute("readonly");
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