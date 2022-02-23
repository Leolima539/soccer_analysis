// function buildMetadata(sample) {
//   d3.json("samples.json").then((data) => {
//     var metadata= data.metadata;
//     var resultsarray= metadata.filter(sampleobject => 
//       sampleobject.country == sample);
//     var result= resultsarray[0]
//     var panel = d3.select("#sample-metadata");
//     panel.html("");
//     Object.entries(result).forEach(([key, value]) => {
//       panel.append("h6").text(`${key}: ${value}`);
//     });


//   });
// }
// function chartBuild(sample) {
// d3.json("samples.json").then(data => {
//   console.log(data);
//   let samples = data.country;

//   let resultArray = samples.filter(sampleObj => sampleObj.country == sample);
//   console.log("resultArray: " + resultArray);
//   let result = resultArray[0];

//   let otu_ids = result.country;
//   let sample_values = result.country.count;
//   let otu_labels = result.country;

//   // Bar Chart
// // Selecting only the OTU to be shown
//   let yValues = otu_ids.map(yValue => `OTU ${yValue}`)

//   let barTrace = [
//   {
//     x: sample_values,
//     y: yValues.slice(0,10),
//     orientation: "h",
//     text: otu_labels,
//     type: "bar"
//   }
// ];


//   let barLayout = {
//     showlegend: false,
//     title: `Top 10 OTU IDs for ${sample}`,
//     margin: { t: 30, l: 150 }
//   };
//   //plot bar plot
//   Plotly.newPlot("bar", barTrace, barLayout);

// // Bubble Chart
//     let bubbleData = [
//       {
//         x: otu_ids,
//         y: sample_values,
//         orientation: "h",
//         text: otu_labels,
//         mode: "markers",
//         marker: {
//           color: otu_ids,
//           size: sample_values,
//         }
//       }
//     ];

//     //build layout
//     let bubbleLayout = {
//       title: `Top Ten Measurements for Sample ${sample}`
//     };

//     //build plot
//     Plotly.newPlot("bubble", bubbleData, bubbleLayout);
//   });
// }

//Initialize function
function init() {
  let dropdown = $('#locality-dropdown');

  dropdown.empty();
  
  dropdown.append('<option selected="true" disabled>Choose State/Province</option>');
  dropdown.prop('selectedIndex', 0);
  
  const url = 'samples.json';
  
  // Populate dropdown with list of provinces
  $.getJSON(url, function (data) {
    $.each(data, function (key, entry) {
      dropdown.append($('<option></option>').attr('value', entry.abbreviation).text(entry.name));
    })
  });}
init();