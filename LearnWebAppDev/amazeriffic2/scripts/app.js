var main = function() {
    "use strict";
    
    $(".tabs span").toArray().forEach(function (element) {
        // create click handler for the element:
        $(element).on("click", function() {
            $(".tabs span").removeClass("active");
            $(element).addClass("active");
            $("main .content").empty();
            
            // figure out which tab has been clicked
            if ($(element).parent().is(":nth-child(1)")) {
                console.log("FIRST TAB CLICKED!");
            } else if ($(element).parent().is(":nth-child(2)")) {
                console.log("SECOND TAB CLICKED!");
            } else if ($(element).parent().is(":nth-child(3)")) {
                console.log("THIRD TAB CLICKED!");
            }
            
            
            return false;
        });
    });
    
};

$(document).ready(main);