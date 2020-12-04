// run in Google Earth Engine Code editor to view forest loss between 2000 and 2015

var gfc2014 = ee.Image('UMD/hansen/global_forest_change_2015');
var treeCover = gfc2014.select(['treecover2000']);
var lossImage = gfc2014.select(['loss']);
var gainImage = gfc2014.select(['gain']);

// existing forest in green
Map.addLayer(treeCover.updateMask(treeCover),
    {palette: ['000000', '00FF00'], max: 100}, 'Forest Cover');

// lost forest in red
Map.addLayer(lossImage.updateMask(lossImage),
            {palette: ['FF0000']}, 'Loss');

// new forest in blue
Map.addLayer(gainImage.updateMask(gainImage),
            {palette: ['0000FF']}, 'Gain');