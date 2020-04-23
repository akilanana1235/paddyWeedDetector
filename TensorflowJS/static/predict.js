$("#image-selector").change(function () {
  let reader = new FileReader();
  reader.onload = function () {
    let dataURL = reader.result;
    $("#selected-image").attr("src", dataURL);
    $("#prediction-list").empty();
  }    
  let file = $("#image-selector").prop("files")[0];
  reader.readAsDataURL(file);
});

// let model;
// const tf = require('@tensorflow/tfjs');
// const tfnode = require('@tensorflow/tfjs-node');
// (async function () {
//     const handler = tfnode.io.fileSystem('http://localhost:81/tsf-models/1/model.json');
//     const model = await tf.loadModel(handler);
//     console.log("Model Loaded");
//    const model = await tf.loadModel('http://localhost:81/tsf-models/1/model.json');
//   $(".progress-bar").hide();
// })();       

let model;
(async function () {
    model = await tf.loadModel("http://localhost:81/tfjs-models/paddy2/model.json");
    console.log("Model added");
    $(".progress-bar").hide();
})();



$("#predict-button").click(async function () {
  let image = $("#selected-image").get(0);
  let tensor = tf
    .fromPixels(image)
    .resizeNearestNeighbor([ 50, 50])
    .toFloat()
    .expandDims();

  let predictions = await model.predict(tensor).data();
  let top5 = Array.from(predictions)
    .map(function (p, i) {
      return {
        probability: p,
        className: image_classes[i],
      };
    })
    .sort(function (a, b) {
      return b.probability - a.probability;
    })
    .slice(0, 5);

  $("#prediction-list").empty();
  top5.forEach(function (p) {
    $("#prediction-list").append('<li>${p.className}: ${p.probability.toFixed(6)}</li>');
  });
});