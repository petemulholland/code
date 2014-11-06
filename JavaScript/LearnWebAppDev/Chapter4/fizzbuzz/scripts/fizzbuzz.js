var main = function () {
    "use strict"
    
    var i;
    for (i = 1; i <= 100; ++i) {
        var isFizz = (i % 3) == 0;
        var isBuzz = (i % 5) == 0;
        
        if (isFizz && isBuzz) {
            $("body").append($("<p>").text("FizzBuzz"));
        }
        else if (isFizz) {
            $("body").append($("<p>").text("Fizz"));
        }
        else if (isBuzz) {
            $("body").append($("<p>").text("Buzz"));
        }
        else  {
            $("body").append($("<p>").text(i));
        }
    }
}

$(document).ready(main);