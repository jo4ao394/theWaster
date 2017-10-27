$(document).ready(function(){
	var mainHeight = $("body").height() - $("#logo").height();
	alert(mainHeight);
	$("#mainform").height(mainHeight);
	$("#toolIcon").height(mainHeight);
});