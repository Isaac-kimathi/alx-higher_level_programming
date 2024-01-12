#!/usr/bin/node

const prevSquare = require('./5-square');

class Square extends prevSquare {
	charPrint(c) {
		const strChar = c === undefined ? 'X' : c ;
		for (let x = 0; x < this.height; x++) {
			let strVar = '';
			for (let y = 0; y < this.width; y++) {
				strVar += strChar;
			}
			console.log(strVar);
		}
	}
}

module.exports = Square;
