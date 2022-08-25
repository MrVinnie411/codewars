/*Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"*/

//My Solution

function bmi(weight, height) {if(weight / height**2 <= 18.5){return "Underweight"}
                              else if(weight / height**2 <= 25.0){return "Normal"}
                              else if(weight / height**2<= 30.0 ){return "Overweight"}
                              else if(weight / height**2 > 30){return "Obese"}

}

//Other solutions

const bmi = (w, h, bmi = w/h/h) =>  bmi <= 18.5 ? "Underweight" :
                                    bmi <= 25 ? "Normal" :
                                    bmi <= 30 ? "Overweight" : "Obese";

//For good measure...

function bmi(weight, height) {
    var formula = (weight / Math.pow(height, 2));  // another method of conducting if else if statment
    switch (true) {
      case formula <=18.5:
      return 'Underweight';
      case formula <=25.0:
      return 'Normal';
      case formula <=30:
      return 'Overweight';
      default:
      return 'Obese';
      
    }
  }

