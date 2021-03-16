<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div class="col-4">
          <label for="exampleFormControlInput1" class="form-label"
            >ชื่อการบ้าน</label
          >
          <input
            type="text"
            class="form-control"
            id="exampleFormControlInput1"
            placeholder=""
            v-model="homeworkName.Homework_name"
            readonly
          />
        </div>
      </div>
      <div class="row">
        <div class="col text-center">
          <button
            type="button"
            :id="'btncolorplt' + j"
            class="btn btn-default mx-auto"
            @click="setStateColor(j)"
            v-for="j in 17"
            v-bind:key="j"
          ></button>
          <div class="row mt-5">
            <div class="col text-center">
              <button class="btnc btn-warning mr-3" @click="reset">
                reset
              </button>
              <button class="btnc btn-success" @click="check">ส่ง</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <!-- โจทย์ -->
        <div class="col-6 m-0" id="eight">
          <div class="row">
            <div v-for="i in 8" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btnprop8' + i + '/' + j"
                class="btn btn-default"
                v-for="j in 8"
                @click="testColor(i, j)"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
        <div class="col-6 m-0" id="ten">
          <div class="row">
            <div v-for="i in 10" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btnprop10' + i + '/' + j"
                class="btn btn-default"
                v-for="j in 10"
                @click="testColor(i, j)"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
        <div class="col-6 m-0" id="fourteen">
          <div class="row">
            <div v-for="i in 14" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btnprop14' + i + '/' + j"
                class="btn btn-default"
                v-for="j in 14"
                @click="testColor(i, j)"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
        <div class="col-6 m-0" id="eightteen">
          <div class="row">
            <div v-for="i in 18" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btnprop18' + i + '/' + j"
                class="btn btn-default"
                v-for="j in 18"
                @click="testColor(i, j)"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
        <div class="col-6 m-0" id="twenty">
          <div class="row">
            <div v-for="i in 20" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btnprop20' + i + '/' + j"
                class="btn btn-default"
                v-for="j in 20"
                @click="testColor(i, j)"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
        <!-- คำตอบ -->
        <div class="col-6 m-0" id="eight_ans">
          <div class="row">
            <div v-for="i in 8" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btn8' + i + '/' + j"
                class="btn btn-default"
                @click="changeColor(i, j)"
                v-for="j in 8"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
         <div class="col-6 m-0" id="ten_ans">
          <div class="row">
            <div v-for="i in 10" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btn10' + i + '/' + j"
                class="btn btn-default"
                @click="changeColor(i, j)"
                v-for="j in 10"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
         <div class="col-6 m-0" id="fourteen_ans">
          <div class="row">
            <div v-for="i in 14" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btn14' + i + '/' + j"
                class="btn btn-default"
                @click="changeColor(i, j)"
                v-for="j in 14"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
         <div class="col-6 m-0" id="eightteen_ans">
          <div class="row">
            <div v-for="i in 18" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btn18' + i + '/' + j"
                class="btn btn-default"
                @click="changeColor(i, j)"
                v-for="j in 18"
                v-bind:key="j"
              ></button>
            </div>
          </div>
        </div>
         <div class="col-6 m-0" id="twenty_ans">
          <div class="row">
            <div v-for="i in 20" v-bind:key="i" class="text-center">
              <button
                type="button"
                :id="'btn20' + i + '/' + j"
                class="btn btn-default"
                @click="changeColor(i, j)"
                v-for="j in 20"
                v-bind:key="j"
              ></button>
            </div>
          </div>
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
      eight: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      eight_ans: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      ten: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      ten_ans: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      foueteen: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      foueteen_ans: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      eightteen: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      eightteen_ans: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      twenty: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      twenty_ans: [
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
        [
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
          "#ffffff",
        ],
      ],
      colorlist: [
        "#79661e", //น้ำตาล
        "#ffec1F", //เหลืองเข้ม
        "#f6ff78", //เหลืองอ่อน
        "#21e83f", //เขียวอ่อน
        "#148f27", //เขียวเข้ม
        "#1f26ff", //น้ำเงิน
        "#a12dcf", //ม่วง
        "#f00800", //แดง
        "#ff892e", //ส้ม
        "#f007ff", //ชมพู
        "#ef9090", //เนื้อ
        "#6eddff", //ฟ้า
        "#b0fff4", //ฟ้าอ่อน
        "#ffffff", //ขาว
        "#c2c2c2", //เทาอ่อน
        "#878787", //เทาเข้ม
        "#000000", //ดำ
      ],
      homeworktemplatelist: [],
      homeworkName: "",
    };
  },
  mounted() {
    var db = firebase.firestore();
    var timer = 0;
    // first view page set color
    this.timer();
    var i, j, txtid;
    var lst = [];
    for (i = 0; i < 17; i++) {
      txtid = "btncolorplt" + (i + 1);
      // console.log(txtid);
      document.getElementById(txtid).style.backgroundColor = this.colorlist[i];
      // console.log(this.colorlist[i], txtid);
    }

    var docRef = db
      .collection("HomeworkTemplate")
      .doc(localStorage.getItem("id_hwTemplate").toString());
    docRef.get().then((doc) => {
      // console.log(doc.data().Homework_data);
      // console.log(element.data());
      this.homeworkName = doc.data();
      var tmp = doc.data().Homework_data.split("*");
      // tmp = tmp.pop()
      // console.log(tmp[0].split("/"));
      var txtid;
      i = 0;
      j = 0;
      var x = doc.data().Homework_size;
      localStorage.setItem("Hw_size", x);
      console.log(x);
      if (x == "8") {
        x = document.getElementById("eight");
        x.style.display = "block";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
        x = document.getElementById("eight_ans");
        x.style.display = "block";
        x = document.getElementById("ten_ans");
        x.style.display = "none";
        x = document.getElementById("fourteen_ans");
        x.style.display = "none";
        x = document.getElementById("eightteen_ans");
        x.style.display = "none";
        x = document.getElementById("twenty_ans");
        x.style.display = "none";
        for (i = 0; i < 8; i++) {
          // console.log(tmp[i].split("/"))
          for (j = 0; j < 8; j++) {
            // console.log(tmp[i].split("/")[j]);
            txtid = "btnprop8" + (i + 1) + "/" + (j + 1);
            this.eight[i][j] = tmp[i].split("/")[j];
            document.getElementById(txtid).style.backgroundColor = tmp[i].split(
              "/"
            )[j];
          }
        }
      } else if (x == "10") {
        x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "block";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
        x = document.getElementById("eight_ans");
        x.style.display = "none";
        x = document.getElementById("ten_ans");
        x.style.display = "block";
        x = document.getElementById("fourteen_ans");
        x.style.display = "none";
        x = document.getElementById("eightteen_ans");
        x.style.display = "none";
        x = document.getElementById("twenty_ans");
        x.style.display = "none";
        for (i = 0; i < 10; i++) {
          // console.log(tmp[i].split("/"))
          for (j = 0; j < 10; j++) {
            // console.log(tmp[i].split("/")[j]);
            txtid = "btnprop10" + (i + 1) + "/" + (j + 1);
            this.ten[i][j] = tmp[i].split("/")[j];
            document.getElementById(txtid).style.backgroundColor = tmp[i].split(
              "/"
            )[j];
          }
        }
      } else if (x == "14") {
        x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "block";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "none";
        x = document.getElementById("eight_ans");
        x.style.display = "none";
        x = document.getElementById("ten_ans");
        x.style.display = "none";
        x = document.getElementById("fourteen_ans");
        x.style.display = "block";
        x = document.getElementById("eightteen_ans");
        x.style.display = "none";
        x = document.getElementById("twenty_ans");
        x.style.display = "none";
        for (i = 0; i < 14; i++) {
          // console.log(tmp[i].split("/"))
          for (j = 0; j < 14; j++) {
            // console.log(tmp[i].split("/")[j]);
            txtid = "btnprop14" + (i + 1) + "/" + (j + 1);
            this.fourteen[i][j] = tmp[i].split("/")[j];
            document.getElementById(txtid).style.backgroundColor = tmp[i].split(
              "/"
            )[j];
          }
        }
      } else if (x == "18") {
        x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "block";
        x = document.getElementById("twenty");
        x.style.display = "none";
        x = document.getElementById("eight_ans");
        x.style.display = "none";
        x = document.getElementById("ten_ans");
        x.style.display = "none";
        x = document.getElementById("fourteen_ans");
        x.style.display = "none";
        x = document.getElementById("eightteen_ans");
        x.style.display = "block";
        x = document.getElementById("twenty_ans");
        x.style.display = "none";
        for (i = 0; i < 18; i++) {
          // console.log(tmp[i].split("/"))
          for (j = 0; j < 18; j++) {
            // console.log(tmp[i].split("/")[j]);
            txtid = "btnprop18" + (i + 1) + "/" + (j + 1);
            this.eightteen[i][j] = tmp[i].split("/")[j];
            document.getElementById(txtid).style.backgroundColor = tmp[i].split(
              "/"
            )[j];
          }
        }
      } else if (x == "20") {
        x = document.getElementById("eight");
        x.style.display = "none";
        x = document.getElementById("ten");
        x.style.display = "none";
        x = document.getElementById("fourteen");
        x.style.display = "none";
        x = document.getElementById("eightteen");
        x.style.display = "none";
        x = document.getElementById("twenty");
        x.style.display = "block";
        x = document.getElementById("eight_ans");
        x.style.display = "none";
        x = document.getElementById("ten_ans");
        x.style.display = "none";
        x = document.getElementById("fourteen_ans");
        x.style.display = "none";
        x = document.getElementById("eightteen_ans");
        x.style.display = "none";
        x = document.getElementById("twenty_ans");
        x.style.display = "block";
        for (i = 0; i < 20; i++) {
          // console.log(tmp[i].split("/"))
          for (j = 0; j < 20; j++) {
            // console.log(tmp[i].split("/")[j]);
            txtid = "btnprop20" + (i + 1) + "/" + (j + 1);
            this.twenty[i][j] = tmp[i].split("/")[j];
            document.getElementById(txtid).style.backgroundColor = tmp[i].split(
              "/"
            )[j];
          }
        }
      }
    });
    // const cityRef = db.collection("HomeworkTemplate").doc("Fn0shgkIBuukMLUhxgBa");
    // const doc = cityRef.get().then((val)=>{
    // console.log(val.data())
    // });

    // console.log(this.homeworktemplatelist[0]);
    // });
    //  document.getElementById("btnprop1/3").style.backgroundColor = "#F00800";
    // document.getElementById("btnprop24").style.backgroundColor = "#F00800";
    // document.getElementById("btnprop35").style.backgroundColor = "#F00800";
    // document.getElementById("btnprop26").style.backgroundColor = "#F00800";
  },
  methods: {
    timer() {
      // var s = 1,
      //   m = 0,
      //   h = 0,
      //   ms = 0;
      // var timer;
      // var interval = setInterval(function () {
      //   timer = h.toString() + ":" + m.toString() + ":" + s.toString();
      //   localStorage.setItem("timer", timer);
      //   localStorage.setItem("timer_ms", ms++);
      //   console.log(h, m, s);
      //   s++;
      //   if (s % 60 == 0 || s > 59) {
      //     s = 0;
      //     m++;
      //   }
      //   if (m % 60 == 0 && m > 59) {
      //     s = 0;
      //     m = 0;
      //     h++;
      //   }
      // }, 1000);
    },
    testColor(i, j) {
      console.log(i, j);
    },
    async check() {
      var count_correct = 0;
      var count_error = 0;
      var i = 0;
      var j = 0;
      var error = [];
      // console.log(document.getElementById("btn1/2").style.backgroundColor);
      // console.log(document.getElementById("btnprop1/2").style.backgroundColor);
      var Hw_size = localStorage.getItem("Hw_size");
      if (Hw_size == "8") {
        this.eight.forEach((element_i, i) => {
          element_i.forEach((element_j, j) => {
            if (element_j == this.eight_ans[i][j]) {
              count_correct++;
            } else {
              count_error++;
              // console.log(i, j);
              error.push([i, j]);
            }
          });
        });
        localStorage.setItem("Error", JSON.stringify(error));

        if (100 - (count_error / 324) * 100 > 80) {
          localStorage.setItem("isHomeworkPass", "pass");
        } else {
          localStorage.setItem("isHomeworkPass", "not pass");
        }
        var str = "";
        localStorage.setItem("count_correct", count_correct);
        localStorage.setItem("count_error", count_error);
        this.eight_ans.forEach((element_i) => {
          element_i.forEach((element_j) => {
            str += element_j.toString() + "/";
          });
          str += "*";
        });
      }
      if (Hw_size == "10") {
        this.ten.forEach((element_i, i) => {
          element_i.forEach((element_j, j) => {
            if (element_j == this.ten_ans[i][j]) {
              count_correct++;
            } else {
              count_error++;
              // console.log(i, j);
              error.push([i, j]);
            }
          });
        });
        localStorage.setItem("Error", JSON.stringify(error));

        if (100 - (count_error / 324) * 100 > 80) {
          localStorage.setItem("isHomeworkPass", "pass");
        } else {
          localStorage.setItem("isHomeworkPass", "not pass");
        }
        var str = "";
        localStorage.setItem("count_correct", count_correct);
        localStorage.setItem("count_error", count_error);
        this.ten_ans.forEach((element_i) => {
          element_i.forEach((element_j) => {
            str += element_j.toString() + "/";
          });
          str += "*";
        });
      }
      if (Hw_size == "14") {
        this.fourteen.forEach((element_i, i) => {
          element_i.forEach((element_j, j) => {
            if (element_j == this.fourteen_ans[i][j]) {
              count_correct++;
            } else {
              count_error++;
              // console.log(i, j);
              error.push([i, j]);
            }
          });
        });
        localStorage.setItem("Error", JSON.stringify(error));

        if (100 - (count_error / 324) * 100 > 80) {
          localStorage.setItem("isHomeworkPass", "pass");
        } else {
          localStorage.setItem("isHomeworkPass", "not pass");
        }
        var str = "";
        localStorage.setItem("count_correct", count_correct);
        localStorage.setItem("count_error", count_error);
        this.fourteen_ans.forEach((element_i) => {
          element_i.forEach((element_j) => {
            str += element_j.toString() + "/";
          });
          str += "*";
        });
      }
      if (Hw_size == "18") {
        this.eightteen.forEach((element_i, i) => {
          element_i.forEach((element_j, j) => {
            if (element_j == this.eightteen_ans[i][j]) {
              count_correct++;
            } else {
              count_error++;
              // console.log(i, j);
              error.push([i, j]);
            }
          });
        });
        localStorage.setItem("Error", JSON.stringify(error));

        if (100 - (count_error / 324) * 100 > 80) {
          localStorage.setItem("isHomeworkPass", "pass");
        } else {
          localStorage.setItem("isHomeworkPass", "not pass");
        }
        var str = "";
        localStorage.setItem("count_correct", count_correct);
        localStorage.setItem("count_error", count_error);
        this.eightteen_ans.forEach((element_i) => {
          element_i.forEach((element_j) => {
            str += element_j.toString() + "/";
          });
          str += "*";
        });
      }
      if (Hw_size == "20") {
        this.twenty.forEach((element_i, i) => {
          element_i.forEach((element_j, j) => {
            if (element_j == this.twenty_ans[i][j]) {
              count_correct++;
            } else {
              count_error++;
              // console.log(i, j);
              error.push([i, j]);
            }
          });
        });
        localStorage.setItem("Error", JSON.stringify(error));

        if (100 - (count_error / 324) * 100 > 80) {
          localStorage.setItem("isHomeworkPass", "pass");
        } else {
          localStorage.setItem("isHomeworkPass", "not pass");
        }
        var str = "";
        localStorage.setItem("count_correct", count_correct);
        localStorage.setItem("count_error", count_error);
        this.twenty_ans.forEach((element_i) => {
          element_i.forEach((element_j) => {
            str += element_j.toString() + "/";
          });
          str += "*";
        });
      }

      // check firsttime
      var isFirsttime;
      var db = firebase.firestore();
      var docRef = await db
        .collection("Homework")
        .doc(localStorage.getItem("id_hw"));
      docRef
        .get()
        .then((data) => {
          console.log(data.data());
          if (data.data().timer_first == "0") {
            isFirsttime = 1;
            console.log(isFirsttime);
          } else {
            isFirsttime = 0;
            console.log(isFirsttime);
          }
        })
        .then(() => {
          console.log(str, 1);
          if (isFirsttime == 1) {
            if (localStorage.getItem("isHomeworkPass") == "pass") {
              localStorage.setItem("ans", str);
              console.log(str, 1);
              // console.log(str.split("*"));
              var db = firebase.firestore();
              const up = db
                .collection("Homework")
                .doc(localStorage.getItem("id_hw"));
              up.update({
                ans: str.split("*"),
                timer_first: localStorage.getItem("timer_ms"),
                status: 1,
              }).then(() => {
                localStorage.setItem("ans", str);
                window.location.href = "/CheckHomework";
              });
            } else {
              localStorage.setItem("ans", str);
              window.location.href = "/CheckHomework";
            }
          } else {
            if (localStorage.getItem("isHomeworkPass") == "pass") {
              localStorage.setItem("ans", str);
              console.log(str, 2);
              console.log(str.split("*"));
              var db = firebase.firestore();
              const up = db
                .collection("Homework")
                .doc(localStorage.getItem("id_hw"));
              up.update({
                ans: str.split("*"),
                timer_release: localStorage.getItem("timer_ms"),
                status: 1,
              }).then(() => {
                localStorage.setItem("ans", str);
                window.location.href = "/CheckHomework";
              });
            } else {
              localStorage.setItem("ans", str);
              window.location.href = "/CheckHomework";
            }
          }
        });
      // Insert hw to firebase
    },
    changeColor(i, j) {
      // console.log(i, j);
      var Hw_size = localStorage.getItem("Hw_size");
      if (Hw_size == "8") {
        var txtid = "btn8" + i + "/" + j;
        document.getElementById(txtid).style.backgroundColor = this.colorlist[
          localStorage.getItem("color") - 1
        ];
        this.eight_ans[i - 1][j - 1] = this.colorlist[
          localStorage.getItem("color") - 1
        ];
      }
      if (Hw_size == "10") {
        var txtid = "btn10" + i + "/" + j;
        document.getElementById(txtid).style.backgroundColor = this.colorlist[
          localStorage.getItem("color") - 1
        ];
        this.ten_ans[i - 1][j - 1] = this.colorlist[
          localStorage.getItem("color") - 1
        ];
      }
      if (Hw_size == "14") {
        var txtid = "btn14" + i + "/" + j;
        document.getElementById(txtid).style.backgroundColor = this.colorlist[
          localStorage.getItem("color") - 1
        ];
        this.fourteen_ans[i - 1][j - 1] = this.colorlist[
          localStorage.getItem("color") - 1
        ];
      }
      if (Hw_size == "18") {
        var txtid = "btn18" + i + "/" + j;
        document.getElementById(txtid).style.backgroundColor = this.colorlist[
          localStorage.getItem("color") - 1
        ];
        this.eightteen_ans[i - 1][j - 1] = this.colorlist[
          localStorage.getItem("color") - 1
        ];
      }
      if (Hw_size == "20") {
        var txtid = "btn20" + i + "/" + j;
        document.getElementById(txtid).style.backgroundColor = this.colorlist[
          localStorage.getItem("color") - 1
        ];
        this.twenty_ans[i - 1][j - 1] = this.colorlist[
          localStorage.getItem("color") - 1
        ];
      }
    },
    setStateColor(i) {
      localStorage.setItem("color", i);
      // console.log(i)
    },
    reset() {
      var i, j, txtid;
      for (i = 0; i < 18; ++i) {
        for (j = 0; j < 18; ++j) {
          txtid = "btn" + (i + 1) + "/" + (j + 1);
          this.eightteen_ans[i][j] = "#ffffff";
          document.getElementById(txtid).style.backgroundColor = "#ffffff";
        }
      }
    },
  },
};
</script>

<style>
@import url("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css");

.btn.btn-default {
  width: 45px;
  height: 45px;
  margin: 0 0;
  border-color: black;
}

.btnc {
  color: black;
  font-size: 1.5em;
  width: 70px;
  height: 45px;
  margin: 0 0;
}
</style>