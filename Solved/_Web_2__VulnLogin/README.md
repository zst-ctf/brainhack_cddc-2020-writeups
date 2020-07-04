# [Web-2] VulnLogin
Web

## Challenge 
DESCRIPTION
This is not how you log someone in!

http://vulnlogin.chall.cddc2020.nshc.sg:8090/

Note:
Flag format is CDDC20{username_password}

## Solution

Source code, look at login.js
		
	function login() {
		var username = document.forms[0].username.value;
		username = CryptoJS.MD5(username).toString();
		var password = document.forms[0].password.value;
		password = CryptoJS.MD5(password).toString();
		if (username == "200ceb26807d6bf99fd6f4f0d1ca54d4" && password == "bbb0ddff1b944b3cc68eaaeb7ac20099") {
			alert("CONGRATS! Go ahead and submit your well-earned flag ;)");
		}
		else {
			alert("Login failed! :(");
		}
	}

    if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {

Serach online for hashes

	Algorithm	Hash	Decrypted
	md5	200ceb26807d6bf99fd6f4f0d1ca54d4	administrator
	md5	bbb0ddff1b944b3cc68eaaeb7ac20099	password12345678

## Flag

	CDDC20{administrator_password12345678}
