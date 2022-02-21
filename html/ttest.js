// function buildMetadata(sample) {
//     d3.csv("../Resources/transfers.csv").then((data) => {
//       var names= data.name;
//       var resultsarray= metadata.filter(sampleobject => 
//         sampleobject.id == sample);
//       var result= resultsarray[0]
//       var panel = d3.select("#sample-metadata");
//       panel.html("");
//       Object.entries(result).forEach(([key, value]) => {
//         panel.append("h6").text(`${key}: ${value}`);
//       });
  
//     //buildGauge(result.wfreq)
  
  
  
//     });
//   }
  
  //function buildGauge(wfreq) {}
  
  function buildCharts(sample) {
  
  // Use `d3.json` to fetch the sample data for the plots
  d3.csv("../Resources/transfers.csv").then((data) => {
    var samples= data.index;
    var resultsarray= samples.filter(sampleobject => 
        sampleobject.id == sample);
    var result= resultsarray[0]
  
    var ids = result.otu_ids;
    var labels = result.otu_labels;
    var values = result.sample_values;
  
  //------------------------------------------------------//
  //------------------------------------------------------//
            // Build a BUBBLE Chart 
  //------------------------------------------------------//
  //------------------------------------------------------//
  
    var LayoutBubble = {
      margin: { t: 0 },
      xaxis: { title: "OTU ID" },
      hovermode: "closest",
      };
  
      var DataBubble = [ 
      {
        x: ids,
        y: values,
        text: labels,
        mode: "markers",
        marker: {
          color: ids,
          size: values,
          }
      }
    ];
  
    Plotly.newPlot("bubble", DataBubble, LayoutBubble);
  
  
  //---------------------------------------------------------//
  //---------------------------------------------------------//
                //  Build a BAR Chart
  //---------------------------------------------------------//  
  //---------------------------------------------------------// 
    var bar_data =[
      {
        y:ids.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse(),
        x:values.slice(0,10).reverse(),
        text:labels.slice(0,10).reverse(),
        type:"bar",
        orientation:"h"
  
      }
    ];
  
    var barLayout = {
      title: "Top 10 Bacteria Cultures Found",
      margin: { t: 30, l: 150 }
    };
  
    Plotly.newPlot("bar", bar_data, barLayout);
  });
  }
   
  
  function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  
  // Use the list of sample names to populate the select options
//   d3.csv("../Resources/transfers.csv").then((data) => {
//     var sampleNames = data.Name;
//     sampleNames.forEach((sample) => {
//       selector
//         .append("option")
//         .text(sample)
//         .property("value", sample);
//     });

    d3.csv("../Resources/transfers.csv", function(d) {
        return {
            sampleNames: d.Name, // convert "Year" column to Date
        //   make: d.Make,
        //   model: d.Model,
        //   length: +d.Length // convert "Length" column to number
        };
      }, function(error, rows) {
        console.log(rows);
      });
  
    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[1];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  }
  
  function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
  }
  
  
  
  // Initialize the dashboard
  init();







//   d3.csv("../Resources/transfers.csv", function(d) {
//     return {
//         playerChoice: new Date(+d.Name, 0, 1), // convert "Year" column to Date
//     //   make: d.Make,
//     //   model: d.Model,
//     //   length: +d.Length // convert "Length" column to number
//     };
//   }, function(error, rows) {
//     console.log(rows);
//   });