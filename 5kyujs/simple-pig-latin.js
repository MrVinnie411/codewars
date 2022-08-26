/*Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !*/

// My solution
function pigIt(str){
    const arr= str.split(' ')
    return arr
      .map((word) => {
        return word.match(/[A-z]/i)                            
          ? `${word.substr(1)}${word.substr(0, 1)}ay`
          : word
      })
    .join(' ')
  } // //Here we are iterating over the strings with map and at each iteration, we remove the first character with substr(1) which will return us a substring from character 1 to the end of the string, then we add the first letter and finally we append ay at the end of it.

  // we also implement a regex function to verify that only letters a-z will be taken into account

  //other solutions
  function pigIt(str){
    return str.replace(/(\w)(\w*)(\s|$)/g, "\$2\$1ay\$3")
  }

  //for good measure..
  function pigIt(str) {
    var arrayWord = str.split(' ');
    return arrayWord.map(function(word) {
      var firstLetter = word.charAt(0);
      return word.slice(1) + firstLetter + 'ay';
    }).join(' ');
  }
