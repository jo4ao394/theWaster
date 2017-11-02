$(document).ready(function(){
  $(window).resize(function(){
  	var mainHeight = $("body").height() - $("#logo").height();
  	$("#mainform").height(mainHeight);
  	$("#bullectin").height(mainHeight);
  	
  	var margin ="";
  	margin += ($('#mainform').height() - $("form").height())/2;
  	margin += "px";
  	$('form').css({"position":"relative","top":margin});
  });

  var mainHeight = $("body").height() - $("#logo").height();
  $("#mainform").height(mainHeight);
  $("#bullectin").height(mainHeight);
  
  var margin ="";
  margin += ($('#mainform').height() - $("form").height())/2;
  margin += "px";
  $('form').css({"position":"relative","top":margin});
});