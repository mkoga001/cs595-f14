<html>
	<head>
	<title>Sample</title>
	</head>
	<body>
	<form method="post" action="login.php" id="login_form">
		<label class="hidden-label" for="Email">Username</label>
		<input id="Email" name="u_name" type="text" placeholder="Username" value="" spellcheck="false" required />
		<br><br>
		<label class="hidden-label" for="Passwd">Password</label>
		<input id="Passwd" name="password" type="password" placeholder="Password" required />
		<input type="hidden" name="hidden" value="login"/>
		<div class="modal-footer">
			<button type="submit" class="btn btn-primary" name="submit">Sign In</button>
		</div>
	</form>
	</body>
</html>