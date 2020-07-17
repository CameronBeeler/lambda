//  /Users/cam/dev/lambda/compare-store-data/$
exports.handler = (event, context, callback) => {
    console.log(event);
/*
    input data {
    "name":"Cameron",
    "age":52,
    "EyeColor":"blue"
  }
  therefore...
  const name = event.name; // results in name=="Cameron"
*/
    callback(null, event);
};
