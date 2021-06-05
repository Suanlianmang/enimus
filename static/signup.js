function CheckPassword(){
	var psw1 = document.getElementById('id_password1').value;
	var psw2 = document.getElementById('id_password2').value;
	if(psw1 == psw2){
		if (document.getElementById('check').checked) {
            document.getElementById('signup_butt').click();
           
        } else {
            alert("Pleas agree to our terms and services first!");
            return;
        }
	}
	else{
		alert("The psswords are not same");
		return;
	}
}
var psw = document.getElementById('id_password1');

psw.onkeyup = function() {
	var letter = document.getElementById("upper");
	var capital = document.getElementById("lower");
	var number = document.getElementById("number");
	var length = document.getElementById("length");
		// Validate lowercase letters
		var lowerCaseLetters = /[a-z]/g;
  	if(psw.value.match(lowerCaseLetters)) {
    	letter.classList.remove("invalid");
    	letter.classList.add("valid");
  	} 
  	else {
    	letter.classList.remove("valid");
    	letter.classList.add("invalid");
}
  // Validate capital letters
	var upperCaseLetters = /[A-Z]/g;
	if(psw.value.match(upperCaseLetters)) {
		capital.classList.remove("invalid");
		capital.classList.add("valid");
	} else {
		capital.classList.remove("valid");
		capital.classList.add("invalid");
	}
		  // Validate numbers
	var numbers = /[0-9]/g;
	if(psw.value.match(numbers)) {
		number.classList.remove("invalid");
		number.classList.add("valid");
	} else {
		number.classList.remove("valid");
		number.classList.add("invalid");
	}
	  // Validate length
	if(psw.value.length >= 8) {
		length.classList.remove("invalid");
		length.classList.add("valid");
	} else {
		length.classList.remove("valid");
		length.classList.add("invalid");
	}
	}