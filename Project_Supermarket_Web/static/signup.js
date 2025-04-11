window.addEventListener("load",redirect); 

function redirect()
{
	document.getElementById("submit").addEventListener("click",checkinfo); 
}
function checkinfo()
{
	var username = document.getElementById("username").value; 
	var pass = document.getElementById("password").value; 
	var email = document.getElementById("email").value; 
	var length = pass.length
	let check1 = email/1; 
	let check2 = parseInt(email)/1; 
	switch(true) 
	{
		case username == "" || pass == "" || email == "":
			alert("There are missing inputs!!")
			document.getElementById("username").focus(); 
			break; 
		case length < 6:
			alert("Your password must be more than 6 digits long")
			document.getElementById("username").focus(); 
			break; 
		case check1 == check2:
			alert("You cannot type in just numbers for your email")
			document.getElementById("username").focus(); 
			break; 
		default:
			break;
	}
}