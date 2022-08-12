/*Given a random non-negative number, you have to return the digits of this number within an array in reverse order.*/

//My Solution
function digitize(n) {
    return String(n).split('').map(Number).reverse()
    
  }

  //other solutions
  function digitize(n) {
    return String(n).split('').map(Number).reverse()
  }

  //for good measure
  function digitize(n) {
    //code here
    let numArr = [];
    
    while(n > 0){
      numArr.push(n % 10);
      
      n = Math.floor(n/10);
    }
    
    return numArr;
  }