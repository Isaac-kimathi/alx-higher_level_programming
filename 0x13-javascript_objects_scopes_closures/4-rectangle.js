#!/usr/bin/node
class Rectangle {
	constructor(w, h) {
		if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
	print () {
		for (let x = 0; x < this.height; x++) {
			let strChr = '';
			let y = 0;
			for (let y = 0; y < this.width; y++) {
				strChr += 'X';
			}
			console.log(strChr);
		}
	}
	rotate () {
		let temp = 0;
		temp = this.width;
		this.width = this.height;
		this.height = temp;
	}
	double () {
		this.width *= 2;
		this.height *= 2;
	}
}
module.exports = Rectangle;
