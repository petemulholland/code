/*var main = function () {
	"use strict";
	
	var $newUL = $("<ul>");
	var $newPara = $("<p>");
	
	$newPara.text("scripted para");
	
	$("footer").append($newPara);
	
	var $li1 = $("<li>").text("item 1");
	var $li2 = $("<li>").text("item 2");
	var $li3 = $("<li>").text("item 3");

	$newUL.append($li1);
	$newUL.append($li2);
	$newUL.append($li3);
	
	$("main").append($newUL);
	
	
	var $ftr1stChild = $("<p>").text("scripted first child");
	//$("footer").prepend($ftr1stChild);
	
	//$ftr1stChild.appendTo($("footer"));
	$ftr1stChild.prependTo($("footer"));
	
	$("ul li:first-child").remove();
	
	$("footer p:first-child").fadeOut(1000, function() {
        $("footer").remove();
    });
	
}*/

/*
var main = function () {
    // demonstrate call backs/asynchronicity
    $(document).ready(function () {
        console.log("this will pritn when the doc is ready");
    });
    
    setTimeout(function () {
        console.log("this will print after 3 secs");
    }, 3000);
    
    // 
    console.log("this prints first");
}
*/

/*var add = function (num1, num2) {
    var sum = num1 + num2;
    return sum;
}

var main = function () {
    "use strcit";
    
    var $content = $("<div>Hello World!</div>").hide();
    var $moreContent = $("<div>Goodbye World!</div>").hide();
    
    $("body").append($content);
    $content.slideDown(2000, function () {
        $("body").append($moreContent);
        $moreContent.fadeIn();
    });
    
    add(5,2);
};*/

var main = function () {
    "use strcit";
    
    var cardSuits = [];
    cardSuits.push("clubs");
    console.log(cardSuits);
    
    cardSuits.push("diamonds");
    console.log(cardSuits);

    cardSuits.push("hearts");
    cardSuits.push("spades");
    console.log(cardSuits);
    
    cardSuits.forEach(function (element) {
        console.log(element);
    });
    
};


$(document).ready(main);