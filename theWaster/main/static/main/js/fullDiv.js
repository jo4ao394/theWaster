$(document).ready(function(){
  $(window).resize(function(){
  	var mainHeight = $("body").height() - $("#logo").height();
  	$("#mainform").height(mainHeight);
  	$("#toolIcon").height(mainHeight);
  	
  	var margin ="";
  	margin += ($('#mainform').height() - $("form").height())/2;
  	margin += "px";
  	$('form').css({"position":"relative","top":margin});
  	$('ul').css({"position":"relative","top":margin}); 
  });

  var mainHeight = $("body").height() - $("#logo").height();
  $("#mainform").height(mainHeight);
  $("#toolIcon").height(mainHeight);
  
  var margin ="";
  margin += ($('#mainform').height() - $("form").height())/2;
  margin += "px";
  $('form').css({"position":"relative","top":margin});
  $('ul').css({"position":"relative","top":margin}); 
});