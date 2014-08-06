var main = function() {
    "use strict";
    
    var toDos = [
        "finish chapter 4",
        "take indie to the beach", 
        "answer emails", 
        "Prep for mondays class", 
        "Make up some new Todos", 
        "Get Groceries"
    ];
    
    $(".tabs span").toArray().forEach(function (element) {
        // create click handler for the element:
        $(element).on("click", function() {
            var $element = $(element),
                $content;
                
            $(".tabs span").removeClass("active");
            $element.addClass("active");
            $("main .content").empty();
            
            // figure out which tab has been clicked
            if ($element.parent().is(":nth-child(1)")) {
                // TODO: populate contents with array in reverse
                console.log("FIRST TAB CLICKED!");
            } else if ($element.parent().is(":nth-child(2)")) {
                $content = $("<ul>");
                toDos.forEach(function (todo) {
                    $content.append($("<li>").text(todo));
                });
                $("main .content").append($content);
                //console.log("SECOND TAB CLICKED!");
            } else if ($element.parent().is(":nth-child(3)")) {
                // TODO add controls to add content to array
                console.log("THIRD TAB CLICKED!");
            }
            
            
            return false;
        });
    });
    
    // trigger fake click on first tab to load dynamic data:
    $(".tabs a:first-child span").trigger("click");
    
};

$(document).ready(main);