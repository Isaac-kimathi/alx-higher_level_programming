#!/usr/bin/node

exports.esrever = function (list) {
	const listReserved = [];
	for (let x = list.length - 1; x >= 0; x--)
	{
		listReserved.push(list[x]);
	}
	return listReserved;
}
