var main = function () {
    "use strict"
    
    $(".relevant p:not(.a)").css("color","red");
}

$(document).ready(main);