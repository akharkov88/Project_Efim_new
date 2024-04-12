// let value = 153
// let str = 0
// value = value.toString()
// for (let i = 0; i < value.toString().length; i++) {
//     str += Number(Math.pow(value[i], value.length))
//     console.log('value[i]=' + value[i])
//     console.log('value.length  ' + value.length)
//     console.log(Number(Math.pow(value[i], value.length)))
//     console.log(str)
// }
// if (str == value) {
//     console.log(true)
// } else {
//     console.log(false)
// }
// let arr =['a', 'e', 'i', 'o', 'u']
// let str = 'ahsdjoisajfiadljklsakc'
// count = 0
// for (i of str) if (arr.indexOf(i)!=-1) count++
// console.log(count)

//output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
// input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
//
// console.log(input.map((e)=> { if (e[0]>=55 && e[1]>7){
// return 'Senior' }
// else return 'Open'}))

// function digPow(n, p){
// n = n.toString().split('')
//     var sum = (n.map((e)=> {
//         let step = Math.pow(Number(e),Number(p))
//         p++
//         return step
//     })).reduce(function(a, b){
//     return a + b;
// }, 0);
//
//  if (Number.isInteger(sum/n.join(''))){
//     return sum/n.join('')
//  } else return -1
// }
//
// console.log(digPow(46288, 3))

