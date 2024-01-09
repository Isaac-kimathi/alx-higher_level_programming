#!/usr/bin/node
const nx = parseInt(process.argv[2]);
console.log(!isNaN(nx) ? `My number: ${nx}` : 'Not a number');
