<script type="text/javascript">
$(function() {
	$("#orbit01").click(function() {
		printlnMessage('messages', "forward");
		spinnerfl.spinner("value", 3);
		spinnerfr.spinner("value", 3);
		spinnerrl.spinner("value", 3);
		spinnerrr.spinner("value", 3);
		setSpeed();
	});
});

</script>


