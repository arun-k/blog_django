
$(document).ready(function(){
  $("#postblog").click(function(){
    var topic=document.getElementById("topic").value;
    var content=document.getElementById("content").value;
    var date=document.getElementById("created").value;
    url=window.location.href;
    $.post(url,{topic:topic,content:content,date:date},function(data,status){
      if(status=='success'){
        alert("Blog Posted!!!");
	window.location.href=data;
      }
    });
  });
});
