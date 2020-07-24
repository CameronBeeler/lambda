exports.handler = (event, context, callback) => {
	const age = event.PersonsAge;
	const msg = `function input data is ${age}`;
	console.log(msg);

callback(null, event);
}
