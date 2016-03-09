$(document).ready(function () {
$("#about-btn").click( function(event) {
		alert("You clicked the button using JQuery!");
	});
$(".ouch").click( function(event) {
           alert("You clicked me! ouch!");
});
$("#about-btn").click( function(event) {
msgstr = $("#msg").html()
        msgstr = msgstr + "o"
        $("#msg").html(msgstr)
 });
	})