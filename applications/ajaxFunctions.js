function ajax_callPython01(myParams) {
	// printlnMessage('messages', "ajax_callPython01() called");
	try {
		// Opera 8.0+, Firefox, Safari
		ajaxcallPython01 = new XMLHttpRequest();
	} catch (e) {
		// Internet Explorer Browsers
		try {
			ajaxcallPython01 = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajaxcallPython01 = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				// Something went wrong
				alert("Your browser broke!");
				return false;
			}
		}
	}

	ajaxcallPython01.onreadystatechange = ajaxCalled_callPython01;
	// printlnMessage('messages', JSON.stringify(myParams));
	var requeststring;
	requeststring = "applications/orbit01.php?json=" + JSON.stringify(myParams);
	printlnMessage('messages', "ajax: " + requeststring);
	ajaxcallPython01.open("GET", encodeURI(requeststring), true);
	ajaxcallPython01.send(null);

}

// Create a function that will receive data sent from the server
function ajaxCalled_callPython01() {
	if (ajaxcallPython01.readyState == 4) {
		// printlnMessage('messages', "ajaxCalled_callPython01()");
		callPython01message = ajaxcallPython01.responseText;
		printlnMessage('messages', "response from PHP and python:");
		printlnMessage('messages', callPython01message);
		callPython01JSON = JSON.parse(callPython01message);
		printlnMessage('messages', callPython01JSON.py);

		if (callPython01JSON.py == "sinePlot.py") {
			printlnMessage('messages', "reload image");
			rnd = Math.random();
			document.getElementById("sinePlotImage").src = "applications/writeFiles/sinePlot.png?rnd="
					+ rnd;
		}
		if (callPython01JSON.py == "orbitTest01.py") {
			printlnMessage('messages', "reload image");
			rnd = Math.random();
			document.getElementById("orbitTest01Image").src = "applications/writeFiles/orbitTest01.png?rnd="
					+ rnd;
		}
	}
}
