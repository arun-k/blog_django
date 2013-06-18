
$(document).ready(function(){
  $("#signin").click(function(){
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;
    $.post("/",{usrname:username,passwrd:password},function(data,status){
      if(status=='success'){
        window.location.href=data;
      }
    });
  });
});
