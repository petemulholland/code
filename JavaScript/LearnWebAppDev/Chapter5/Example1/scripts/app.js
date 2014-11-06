var main = function () {
	"use strict";
	
	var card = JSON.parse('{"rank":"ace","suit":"spades"}');
	
	var $cardPara = $("<p>");
	$cardPara.text(card.rank + " of " + card.suit);
	$("main").append($cardPara);

	
	var hand = JSON.parse('[ { "suit" : "spades", "rank" : "ace" }, { "suit" : "hearts", "rank" : "ten" }, { "suit" : "spades", "rank" : "five" }, { "suit" : "clubs", "rank" : "three" }, { "suit" : "diamonds", "rank" : "three" } ]');

	var $list = $("<ul>");
	hand.forEach(function (card) {
		var $card = $("<li>");
		$card.text(card.rank + " of " + card.suit);
		$list.append($card);
	});

	$("main").append($list);
}

$(document).ready(main);