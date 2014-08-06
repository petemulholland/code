var main = function() {
    "use strict";
    
    $(".tabs span").toArray().forEach(function (element) {
        // create click handler for the element:
        $(element).on("click", function() {
            $(".tabs span").removeClass("active");
            $(element).addClass("active");
            $("main .content").empty();
        });
    });
    
};

$(document).ready(main);