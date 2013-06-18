
$(document).ready(function(){
  $("#register").click(function(){
    var usrname=document.getElementById("username").value;
    var passwrd=document.getElementById("password").value;
    var email=document.getElementById("email").value;
    var conf_passwrd=document.getElementById("conf_password").value;
    var firstname=document.getElementById("firstname").value;
    var lastname=document.getElementById("lastname").value;
    if(conf_passwrd!=passwrd){
      alert("Oops!!! Passwords doesn't match!!!");
    }
    else{
      $.post("/register/",{usrname:usrname,email:email,passwrd:passwrd,firstname:firstname,lastname:lastname},function(data,status){
        if(status=='success'){
	  alert("Successfully Registered!!!");
	  window.location.href="/";
	}
      });
    }
  });
});
