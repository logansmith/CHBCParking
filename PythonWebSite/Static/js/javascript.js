
var modal = ''

window.onload = function() {
	// Get the modal
	modal = document.getElementById('myModal');

	// Get the <span> element that closes the modal
	var span = document.getElementsByClassName("close")[0];

	// When the user clicks on <span> (x), close the modal
	span.onclick = function() {
	    modal.style.display = "none";
	}

  	var d = new Date();
	document.getElementById('date').innerHTML=d.getMonth()+1+'/'+d.getDate()+"/"+d.getFullYear();
	

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	    if (event.target == modal) {
	        modal.style.display = "none";
	    }
	}
}

function loadmodal(id) {
	 
	 if(document.getElementById('lnum'+id) !=null &&
	 	 document.getElementById('pnum' +id) != null){
			var lnum=document.getElementById('lnum'+id).innerHTML
	 		var pnum= document.getElementById('pnum' +id).innerHTML
	 		document.getElementById('notetext').value=lnum;
	 		document.getElementById('phonenumber').value=pnum;
	 }
	 

	 document.getElementById('parkingid').value = id;
	 modal.style.display = "block";
}


