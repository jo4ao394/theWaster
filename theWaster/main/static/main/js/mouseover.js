$(document).ready(function(){
  $("#part").mouseover(function(){
    $("#son").fadeIn(0);
  });
  
  $("#part").mouseout(function(){
    $("#son").fadeOut();
    $("#son").mouseover(function(){
      $("#son").stop(true);
      $("#son").fadeIn(0);
    });
  });
  
  $("#son").mouseout(function(){
    $("#son").fadeOut(0);
  });
});