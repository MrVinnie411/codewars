/*In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.*/

// My solution
function filter_list(l) {
    // Return a new array with the strings filtered out
  return l.filter( str => typeof str != 'string');
  }

  //other solutions
  const filter_list = l => l.filter(c => typeof c === 'number');

  //for good measure
  function filter_list(l) {
    // Return a new array with the strings filtered out
    var filteredList = [];
    for (var i = 0; i < l.length; i++){
      if (l[i].constructor.name !== "String"){
        filteredList.push(l[i]);
      }
    }
    return filteredList;
  }