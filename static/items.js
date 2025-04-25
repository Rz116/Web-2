window.addEventListener("load",add); 

function add()
{
	document.getElementById("Submit").addEventListener("click", checkvalue)
}
function checkvalue() 
{
	let quantity = document.getElementById("quantity").value; 
	let check1 = quantity/1; 
	let check2 = parseInt(quantity)/1;
	switch(true)
	{
		case quantity == "":
			document.getElementById("quantity").focus(); 
			alert("Please type in a quantity");
			break; 
		case check1 != check2: 
			document.getElementById("quantity").focus(); 
			alert("Please type in a number for the quantity of this item");
			break; 
		default: 
			alert("Item has been added to your cart")
			break;
	}
}

	