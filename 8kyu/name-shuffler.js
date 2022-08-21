/*The problem
Write a function that returns a string in which firstname is swapped with last name.*/

// My Solution

function nameShuffler(str){
    return str.split(" ").reverse().join(" ");
    }

// other solutions
const nameShuffler = str => str.split(' ').reverse().join(' ');


//for good measure...
function nameSuffle(str){
    var arr = str.split(" ");
    return arr[1] + ' ' + arr[0]
  }