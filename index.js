function onload_function() {
	// printlnMessage('messages', 'index.js: onload_function()');

	root_path = window.location.pathname;
	// printlnMessage('messages', 'index.js: root path ' + root_path);

	// load most recent page
	page = getCookie('page');
	title = getCookie('title');
	// printlnMessage('messages', 'index.js: from cookies: ' + page + ' ' +
	// title);
	if (page == null) {
		page = 'home.html';
		title = 'JAT';
	}

	$('#iframe_a').attr('src', page);
	document.title = title;

}

(function($) {
	$(document).ready(function() {

		$('#iframe_a').load(function() {
			printlnMessage('messages', 'index.js: iframe_a loaded');

			// printlnMessage('messages', 'index.js: ' +
			// this.contentWindow.location);

			full_path = this.contentWindow.location.href;
			// printlnMessage('messages', 'index.js: full path ' + full_path);

			var pathArrayStr = this.contentWindow.location + '';
			pathArray = pathArrayStr.split('/');
			page = pathArray[pathArray.length - 1];
			// printlnMessage('messages', 'index.js: ' + pathArrayStr);
			// printlnMessage('messages', 'index.js: ' + pathArrayStr + 'test');
			// printlnMessage('messages', 'index.js: ' + pathArray);
			// printlnMessage('messages', 'index.js: ' + page);

			setCookie('page', full_path, 100);
			// setCookie('page', page, 100);
			// setCookie('title', title, 100);

			page = getCookie('page');
			// printlnMessage('messages', 'index.js: saved to cookies: ' +
			// page);

			autoResize('iframe_a');

		});

	});
}(jQuery));


function autoResize(id) {
	var newheight = 0;
	var newwidth = 0;

	// if(document.getElementById){
	newheight = document.getElementById(id).contentWindow.document.body.scrollHeight;
	newwidth = document.getElementById(id).contentWindow.document.body.scrollWidth;
	// }
	// printlnMessage('messages', 'index.js: newheight='+newheight);

	document.getElementById(id).height = (newheight) + "px";
	document.getElementById(id).width = (newwidth) + "px";
	document.location.href = "#top";
}

function linkClick(page, title) {

	$('#container').load(page);
	document.title = title;
	setCookie('page', page, 100);
	setCookie('title', title, 100);

}

function redirect() {
	printlnMessage('messages', 'index.js: redirect()');
	$('#iframe_a').attr('src', 'Applications.html');
	// document.getElementById('iframe_a').src = 'Applications.html';
}
