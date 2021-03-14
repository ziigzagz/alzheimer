<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="text-center">
          <iframe
            id="player"
            @click="testvideo"
            width="1280"
            height="720"
            :src="vlist[count]"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col text-center">
        <p id="display"></p>
        <button class="btn btn-success" id="btn" @click="next">ถัดไป</button>
      </div>
    </div>
  </div>
</template>

<script>
var player,
  timer,
  timeSpent = [],
  display = document.getElementById("display");

function onYouTubeIframeAPIReady() {
  player = new YT.Player("player", {
    events: { onStateChange: onPlayerStateChange },
  });
}

function onPlayerStateChange(event) {
  if (event.data === 1) {
    // Started playing
    if (!timeSpent.length) {
      for (var i = 0, l = parseInt(player.getDuration()); i < l; i++)
        timeSpent.push(false);
    }
    timer = setInterval(record, 100);
  } else {
    clearInterval(timer);
  }
}

function record() {
  timeSpent[parseInt(player.getCurrentTime())] = true;
  showPercentage();
}

function showPercentage() {
  var percent = 0;
  for (var i = 0, l = timeSpent.length; i < l; i++) {
    if (timeSpent[i]) percent++;
  }
  percent = Math.round((percent / timeSpent.length) * 100);
  display.innerHTML = percent + "%";
  console.log(percent);
}
import firebase from "firebase";
export default {
  data() {
    return {
      vlist: [],
      count: 0,
    };
  },
  mounted() {
    var db = firebase.firestore();
    var docRef = db.collection("Exam").doc(localStorage.getItem("ID_Exam"));
    docRef.get().then((doc) => {
      // console.log(doc.data().v);
      doc.data().v.forEach((element) => {
        this.vlist.push(
          "https://www.youtube.com/embed/" +
            element.text.split("/")[3].split("=")[1].split("&")[0]
        );
        console.log(element.text.split("/")[3].split("=")[1].split("&")[0]);
      });
    });
  },
  methods: {
    testvideo() {
      console.log(123);
    },
    async next() {
      var db = firebase.firestore();
      document.getElementById("btn").innerHTML = "สำเร็จ";
      if (this.count < this.vlist.length - 1) {
        this.count++;
      } else {
        const cityRef = db
          .collection("Exam")
          .doc(localStorage.getItem("ID_Exam"));
        await cityRef.update({
          status: 1,
        });
        console.log("จบแล้ว");
        window.location.href = "/Patient";
      }
    },
  },
};
</script>

<style>
</style>