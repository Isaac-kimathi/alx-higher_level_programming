#!/usr/bin/node
const n = parseInt(process.argv[2]);

if(!isNaN(n)) {
	for (let u = 0; u < n; u++) {
		let v = 0;
		let strVar = '';
		while (v < n) {
			strVar = strVar + 'X';
			v++;
		}
		console.log(strVar);
	}
}
else {
	console.log('Missing size');
}
