<template>
  <div class="container">
    <div class="row">
      <div class="col-1">
        <v-row justify="center">
          <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark v-bind="attrs" v-on="on">
                เพิ่ม
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">เพิ่มบันทึกประจำวัน</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col>
                      <v-text-field
                        label="ชื่อบันทึก*"
                        id="name"
                        hint=""
                        persistent-hint
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>

                <v-textarea
                  outlined
                  name=""
                  id="textarea"
                  label="รายละเอียด"
                  value=""
                ></v-textarea>
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
              <th scope="col">วันที่</th>
              <th scope="col">หัวข้อ</th>
              <th>รายละเอียด</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="i in diary" v-bind:key="i">
              <th scope="row">{{ i.date }}</th>
              <th scope="row">{{ i.diary_name }}</th>
              <th scope="row">
                <a href="">
                  <img
                    src="https://www.flaticon.com/svg/vstatic/svg/1086/1086933.svg?token=exp=1610709723~hmac=097bbbae75c7f7eff800850f3cc9bd2b"
                    height="20"
                    width="20"
                    alt=""
                  />
                </a>
              </th>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>