$(document).ready(function(){
  var $left1 = $("#part").position();
  $left1 = $left1.left ;
  $("div.partson").css({
    "position": "fixed",
    "left":$left1
  });
  
  var $left = $("#game").position();
  $left = $left.left ;
  $("div.gameson").css({
    "position": "fixed",
    "left":$left
  });
});