#!/usr/bin/node
const impDict = require('./101-data').dict

const nwDct = {};

Object.getOwnPropertyNames(impDict).forEach(occurrences => {
	if (nwDct[impDict[occurrences]] === undefined) {
		nwDct[impDict[occurrences]] = [occurrences];
	}
	else {
		nwDct[impDict[occurrences]].push(occurrences);
	}
});
console.log(nwDct);
