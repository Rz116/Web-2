window.addEventListener("load",add); 

function add()
{
	document.getElementById("submit").addEventListener("click", checkvalue)
}
function checkvalue() 
{
	let creditcard = document.getElementById("credit").value; 
	let ccv = document.getElementById("ccv").value; 
	let name = document.getElementById("name").value;
	let phone = document.getElementById("phone").value; 
	let length = creditcard.length;
	let check1 = creditcard/1; 
	let check2 = parseInt(creditcard)/1;
	let check3 = ccv/1;
	let check4 = parseInt(ccv)/1;
	let length2 = ccv.length;
	let check5 = phone/1 
	let check6 = parseInt(phone)/1; 
	let length3 = phone.length;
	switch(true)
	{
		case creditcard == "":
			document.getElementById("credit").focus(); 
			alert("Please type in a credit card number");
			break; 
		case check1 != check2: 
			document.getElementById("credit").focus(); 
			alert("Please type in a 16 digit number for your credit card");
			break; 
		case length < 16 || length > 16:
			document.getElementById("credit").focus(); 
			alert("Please type in a 16 digit number for your credit card");
			break;
		case ccv == "":
			document.getElementById("ccv").focus();
			alert("Type in a ccv number"); 
			break;
		case check3 != check4: 
			document.getElementById("ccv").focus();
			alert("Type in a 3 digit number for your ccv"); 
			break;			
		case length2 < 3 || length2 > 3: 
			document.getElementById("ccv").focus();
			alert("Type in a 3 digit number for your ccv"); 
			break;	
		case name == "":
			document.getElementById("name").focus(); 
			alert("Please input your name"); 
			break; 
		case phone == "":
			document.getElementById("phone").focus(); 
			alert("Please type in your phone number")
			break; 
		case check5 != check6: 
			document.getElementById("phone").focus(); 
			alert("Please type in a 10 digit number for your phone number")
			break; 		
		case length3 < 10 || length3 > 10: 
			document.getElementById("phone").focus(); 
			alert("Please type in a 10 digit number for your phone number")
			break; 			
		default: 
			alert("You have successfully paid for all your items!!")
			break;
	}
}