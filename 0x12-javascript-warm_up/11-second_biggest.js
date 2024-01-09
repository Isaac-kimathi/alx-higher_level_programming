#!/usr/bin/node
const ac = process.argv.map(Number);

if (ac.length > 3) {
	const sortedAc = ac.slice(2).sort((a, b) => a - b);
	console.log(sortedAc[sortedAc.length - 2]);
}
else {
	console.log(0);
}
