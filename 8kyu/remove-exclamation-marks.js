/*Write function RemoveExclamationMarks which removes all exclamation marks from a given string.*/
// My solution
function removeExclamationMarks(s) {
    return s.replace(/!/gi, '');
  }

  //other solutions
  const removeExclamationMarks = s => s.replace(/!/g,"") ;

  //for good measure
  function removeExclamationMarks(s) {
    return s.split('!').join('');
  }