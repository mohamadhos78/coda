  
  /**************** fix-width ****************/
  function resize() {
  if ( $(window).width() > 1370) {     
    $("#main").addClass('container');
    $("#main").removeClass('container-fluid');
  }
  else
  {
    $("#main").addClass('container-fluid');
    $("#main").removeClass('container');
  }
  }
  $(window).on("resize", resize);
  resize();
  /**************** fix-width ****************/
  
  
  