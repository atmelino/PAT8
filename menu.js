function onload_status() {
	// printlnMessage('messages', 'onload_status() in menu.js');

}

//function pageClick(page, title) {
//	printlnMessage('messages', 'pageClick called: ' + page + ' ' + title);
//
//	setCookie('page', page, 100);
//	setCookie('title', title, 100);
//
//	document.title = title;
//	id = 'menu' + title;
//
//	resetMenuButtons();
//	document.getElementById(id).src = "images/button_gray.svg";
//
//}

function resetMenuButtons() {
	document.getElementById("menuJAT").src = "images/button_onload.svg";
	document.getElementById("menuDocumentation").src = "images/button_onload.svg";
}
