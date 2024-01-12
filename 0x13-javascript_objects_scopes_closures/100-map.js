#!/usr/bin/node

const impList = require('./100-data.js').list

const nwList = impList.map((val, index) => val * index);
console.log(impList);
console.log(nwList);
