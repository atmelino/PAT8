<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>JAT</title>

<link rel="stylesheet" type="text/css" href="PAT8style.css">


<script type="text/JavaScript" src="lib/jquery-2.1.1.js"></script>
<script type="text/JavaScript" src="index.js"></script>
<script type="text/JavaScript" src="functions.js"></script>
<script type="text/JavaScript" src="menu.js"></script>
<script type="text/JavaScript" src="globals.js"></script>

<script type="text/javascript">
</script>

</head>
<body onload="onload_function()">

	<div id="menuheader">
		<ul>
			<li><a href="home.html" id=home target="iframe_a">Home</a></li>
			<li><a href='Applications.php' id='Applications' target="iframe_a">Applications</a>
			</li>
			<li><a href='Support.html' id='Support' target="iframe_a">Support</a>
			</li>
			<li><a href='Screenshots.html' id='Screenshots' target="iframe_a">Screenshots</a>
			</li>
			<li><a href='Testing.html' id='Testing' target="iframe_a">Testing</a>
			</li>
			<li><a href='Licenses.html' id='Licenses' target="iframe_a">Licenses</a>
			</li>
		</ul>
	</div>

	<!-- 	<div id="status"> -->
	<!--<?php include("status.html"); ?>-->
	<!-- 	</div> -->

	<div id='mainarea'>
		<div id='messagesDiv'>
			<!--<textarea id="messages" style="width: 90%;"></textarea>-->
			<textarea id="messages" cols=80; rows=3></textarea>
			<!-- cols=60 rows=10 -->
		</div>
		<iframe width="100%" height=400px scrolling=no name="iframe_a" id="iframe_a" seamless="seamless"></iframe>
	</div>
	<!-- end of mainarea -->




	<!-- 	<iframe width="100%" height="600px%" src="home.html" name="iframe_a" id="iframe_a"></iframe> -->


</body>
</html>
