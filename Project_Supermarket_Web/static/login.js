window.addEventListener("load",redirect); 

function redirect()
{
	document.getElementById("submit").addEventListener("click",checkinfo); 
}
function checkinfo()
{
	var username = document.getElementById("username").value; 
	var pass = document.getElementById("password").value; 
	if(username == "" || pass == "")
	{
		alert("There are missing inputs!!")
		document.getElementById("username").focus();
	}
}
