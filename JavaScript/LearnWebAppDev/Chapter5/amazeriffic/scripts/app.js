var toDos = [];
/*    "finish chapter 4",
    "take indie to the beach", 
    "answer emails", 
    "Prep for mondays class", 
    "Make up some new Todos", 
    "Get Groceries"
];*/
    
    
var toDosJSON = [ 
    { 
        "description" : "Get groceries", 
        "tags" : [ "shopping", "chores" ] 
    }, 
    { 
        "description" : "Make up some new ToDos", 
        "tags" : [ "writing", "work" ] 
    }, 
    { 
        "description" : "Prep for Monday's class", 
        "tags" : [ "work", "teaching" ] 
    }, 
    { 
        "description" : "Answer emails", 
        "tags" : [ "work" ] 
    }, 
    { 
        "description" : "Take Gracie to the park", 
        "tags" : [ "chores", "pets" ] 
    }, 
    { 
        "description" : "Finish writing this book", 
        "tags" : [ "writing", "work" ] 
    } 
];

    
var onOldest = function () {
    var $content;

    $content = $("<ul>");
    toDos.forEach(function (todo) {
        $content.append($("<li>").text(todo));
    });
    
    $("main .content").append($content);
}

var onNewest = function () {
    var $content;

    var $content;

    $content = $("<ul>");
    toDos.forEach(function (todo) {
        $content.prepend($("<li>").text(todo));
    });
    
    $("main .content").append($content);
}

var addTodoFromInputBox = function() {
    var $new_comment;
    
    if ($("main .content input").val() !== "") {
        toDos.push($("main .content input").val());
        $("main .content input").val("");
    }
}

var onAdd = function () {
    var $content;

    //<input type="text"><button>+</button>
    $content = $("<p>"); // cause p & ul have 30px margin applied in css.
    
    $content.append($('<input type="text">'));
    $content.append($('<button>+</button>'));
    
    $("main .content").append($content);

    // add the functionality for the controls.
    $("main .content button").on("click", function(event) {
        addTodoFromInputBox();
    });

    $("main .content input").on("keypress", function (event) {
        if (event.keyCode === 13) {
            addTodoFromInputBox();
        }
    });

}

var onClick = function (element) {
   // create click handler for the element:
    $(element).on("click", function() {
        var $element = $(element);
            
        $(".tabs span").removeClass("active");
        $element.addClass("active");
        $("main .content").empty();
        
        // figure out which tab has been clicked
        if ($element.parent().is(":nth-child(1)")) {
            onNewest();
        } else if ($element.parent().is(":nth-child(2)")) {
            onOldest();
        } else if ($element.parent().is(":nth-child(3)")) {
            onAdd();
        }
        
        return false;
    });
}

var main = function(toDoObjects) {
    "use strict";
    
    // create array of toDos string from array of toDoObjects.
    // so that old code works.
    toDos = toDoObjects.map(function (toDo) {
        return toDo.description;
    });
    
    $(".tabs span").toArray().forEach(function (element) {
        onClick(element);
    });
    
    // trigger fake click on first tab to load dynamic data:
    $(".tabs a:first-child span").trigger("click");
    
};

$(document).ready(main(toDosJSON));