$(document).ready(function(){
  $("#part").mouseover(function(){
    $(".partson").fadeIn(0);
  });
  
  $("#part").mouseout(function(){
    $(".partson").fadeOut();
    $(".partson").mouseover(function(){
      $(".partson").stop(true);
      $(".partson").fadeIn(0);
    });
  });
  
  $(".partson").mouseout(function(){
    $(".partson").fadeOut(0);
  });
  
  
  
  $("#game").mouseover(function(){
    $(".gameson").fadeIn(0);
  });
  
  $("#game").mouseout(function(){
    $(".gameson").fadeOut();
    $(".gameson").mouseover(function(){
      $(".gameson").stop(true);
      $(".gameson").fadeIn(0);
    });
  });
  
  $(".gameson").mouseout(function(){
    $(".gameson").fadeOut(0);
  });
});