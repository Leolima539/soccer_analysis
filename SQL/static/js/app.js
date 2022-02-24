
// function chartBuild(sample) {
// d3.json("samplesm.json").then(data => {
//   console.log(data);
//   let samples = data.samples;

//   let resultArray = samples.filter(sampleObj => sampleObj.id == sample);
//   console.log("resultArray: " + resultArray);
//   let result = resultArray[0];

//   let otu_ids = result.otu_ids;
//   let sample_values = result.sample_values;
//   let otu_labels = result.otu_labels;

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
    d3.json("seasons.json").then(function(data) {
      let names = data.seasons;
      //grab a reference to the dropdown select
      let selector = d3.select("#selDataset");
  
      //use the list of sample names to populate the select options
      names.forEach(rob => {
        selector
          .append("option")
          .text(rob)
          .property("value", rob);
      });
  
      //use the first sample from list to build the initial plots
      let firstSample = names[0];
      chartBuild(firstSample);
      // buildMetadata(firstSample);
    });
  }
  //function to change charts when a new sample is selected
  function optionChanged(newSample) {
    console.log(`sample changed to ${newSample}`);
    //fetch new data and build charts
    chartBuild(newSample);
    // buildMetadata(newSample);
  }
  
  init();