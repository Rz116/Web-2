window.addEventListener("load",redirect); 

function redirect()
{
	document.getElementById("signup").addEventListener("click",direction); 
}
function direction()
{
	window.location.href = "/templates/signup.html"
}
