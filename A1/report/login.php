<?php
$username = htmlspecialchars($_POST['u_name']);
$password = htmlspecialchars($_POST['password']);
?>
<html>
	<head>
	<title>login</title>
	</head>
	<body>
	<p><?php echo ( !isset($_REQUEST["u_name"])?"": $username ); ?></p>
	<p><?php echo ( !isset($_REQUEST["password"])?"":md5($password)); ?></p>
	</body>
</html>

