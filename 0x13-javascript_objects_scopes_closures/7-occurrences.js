#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let index = 0;

	for (let x = 0; x < list.length; x++) {
		index = (list[x] === searchElement ? index + 1 : index);
	}

	return index;
};
