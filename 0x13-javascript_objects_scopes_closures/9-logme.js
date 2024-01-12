#!/usr/bin/node

let iteration = 0;

exports.logMe = function (item) {
	console.log(`${iteration}:${item}`);
	iteration += 1;
}
