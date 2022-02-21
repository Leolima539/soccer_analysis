(function() {
    var csv_path = "../Resources/transfers.csv",

    var renderCSVDropdown = function (csv) {
        var dropdown = $('selDataset');
        for(var i = 0; i < csv.length; i++) {
            var record = csv[i];
            var entry = $('').attr('value', record.someProperty);
            dropdown.append(entry);

        }
    };
    $.get(csv_path, function (data) {
        var csv = CSVToArray(data);
        renderCSVDropdown(csv);
    });
}());