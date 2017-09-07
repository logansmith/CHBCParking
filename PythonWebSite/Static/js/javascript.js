
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
	var pnum = ''
	 var lnum = ''
	/*for (var i = 0; i <= notes.length; i++) {
	 	if(notes[i].parkingid==id)
	 	{
	 		 var lnum = note.lnum
	 		 var pnum = note.pnum
	 	}

	 }*/
	 
	 document.getElementById('parkingid').value = id;
	 document.getElementById('notetext').value = lnum;
	 modal.style.display = "block";
}


