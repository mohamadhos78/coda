/**************** hamburger-menu ****************/
function openNav() {
  document.getElementById("side-nav").style.width = "350px";
  document.getElementById("Main").style.marginLeft = "50px";
  document.getElementById("side-nav").style.backgroundColor = "rgb(255, 233, 233, 0.5)";
  document.getElementById("header").style.opacity = "80%";
}

function closeNav() {
  document.getElementById("header").style.opacity = "100%";
  document.getElementById("side-nav").style.width = "0";
  document.getElementById("Main").style.marginLeft= "0";
}
/**************** hamburger-menu ****************/

/**************** page-loader ****************/
var myVar;

function myFunction() {
myVar = setTimeout(showPage, 1000);
}

function showPage() {
document.getElementById("loader").style.display = "none";
document.getElementById("Main").style.display = "block";
document.getElementById("main").style.opacity = "100%";
}
/**************** page-loader ****************/


$('[data-toggle="tooltip"]').tooltip({
delay: {
    show: 10000,
    hide: 0
}
});


/**************** navbar-scroll ****************/
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
if (document.body.scrollTop > 900 || document.documentElement.scrollTop > 900) {
  document.getElementById("navbar-scroll").style.top = "0";
}
else {
  document.getElementById("navbar-scroll").style.top = "-80px";
}
}
/**************** navbar-scroll ****************/

/*************** css range slider **************/




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



function acardeon1() {
  document.getElementById("acardeon-tabs-main").style.backgroundColor = "rgba(46, 139, 86, 0.274)";
  document.getElementById("acardeon-tabs-main").style.borderColor = "seagreen";
  document.getElementById("acardeon-buttons-1").style.zIndex = 2;
  document.getElementById("acardeon-buttons-2").style.zIndex = 1;
  document.getElementById("acardeon-buttons-3").style.zIndex = 0;
  document.getElementById("acardeon-tabs-main").style.zIndex = 2;
  $("#text3").addClass('d-none');
  $("#text2").addClass('d-none');
  $("#text1").removeClass('d-none');
}

function acardeon2() {
  document.getElementById("acardeon-tabs-main").style.backgroundColor = "rgba(255, 99, 71, 0.28)";
  document.getElementById("acardeon-tabs-main").style.borderColor = "tomato";
  document.getElementById("acardeon-buttons-1").style.zIndex = 1;
  document.getElementById("acardeon-buttons-2").style.zIndex = 2;
  document.getElementById("acardeon-buttons-3").style.zIndex = 1;
  document.getElementById("acardeon-tabs-main").style.zIndex = 2;
  $("#text3").addClass('d-none');
  $("#text1").addClass('d-none');
  $("#text2").removeClass('d-none');
}

function acardeon3() {
  document.getElementById("acardeon-tabs-main").style.backgroundColor = "rgba(255, 179, 0, 0.274)";
  document.getElementById("acardeon-tabs-main").style.borderColor = "rgb(255, 179, 0)";
  document.getElementById("acardeon-buttons-1").style.zIndex = 0;
  document.getElementById("acardeon-buttons-2").style.zIndex = 1;
  document.getElementById("acardeon-buttons-3").style.zIndex = 2;
  document.getElementById("acardeon-tabs-main").style.zIndex = 2;
  $("#text2").addClass('d-none');
  $("#text1").addClass('d-none');
  $("#text3").removeClass('d-none');
}

////////

