/*ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.*/

// My solution
function validatePIN (pin) {
    if (pin.length == 4 || pin.length == 6) 
        {
          for (let i = 0; i < pin.length; i++)
            {
              if (pin[i] == "0" ||
                  pin[i] == "1" ||
                  pin[i] == "2" ||
                  pin[i] == "3" ||
                  pin[i] == "4" ||
                  pin[i] == "5" ||
                  pin[i] == "6" ||
                  pin[i] == "7" ||
                  pin[i] == "8" ||
                  pin[i] == "9") ;
              else return false;
            }
          return true;
        }
      else return false;
    }

    //other solutions
    function validatePIN (pin) {
  
        var pinlen = pin.length;
        var isCorrectLength = (pinlen == 4 || pinlen == 6);
        var hasOnlyNumbers = pin.match(/^\d+$/);
          
        if(isCorrectLength && hasOnlyNumbers){
          return true;
        }
        
        return false;
      
      }

      //for good measure
      const validatePIN = pin => /^(\d{4}$|\d{6}$)/.test(pin);