var main = function () {
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
	
	$("footer p:first-child").fadeOut();
}

$(document).ready(main);