
$(document).ready(function(){
  $("#post").click(function(){
    var name=document.getElementById("name").value;
    var body=document.getElementById("body").value;
    url=window.location.href;
    $.post(url,{name:name,body:body},function(data,status){
      window.location.href=data;
    });
  });
});
