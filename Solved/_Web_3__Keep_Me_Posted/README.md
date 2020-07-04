# [Web-3] Keep Me Posted
Web

## Challenge 

DESCRIPTION
Some weird page. Looks fishy. Please help.

http://keepmeposted.chall.cddc2020.nshc.sg:1057/

## Solution

Hint: look at the response header.

	$ curl http://keepmeposted.chall.cddc2020.nshc.sg:1057/ -vvv
	*   Trying 157.230.246.85:1057...
	* TCP_NODELAY set
	* Connected to keepmeposted.chall.cddc2020.nshc.sg (157.230.246.85) port 1057 (#0)
	> GET / HTTP/1.1
	> Host: keepmeposted.chall.cddc2020.nshc.sg:1057
	> User-Agent: curl/7.68.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	< HTTP/1.1 200 OK
	< Date: Fri, 03 Jul 2020 15:51:08 GMT
	< Server: Apache/2.4.43 (Unix)
	< X-Powered-By: PHP/7.3.14
	< Authorization: Tm8=
	< Content-Length: 58
	< Content-Type: text/html; charset=UTF-8
	< 
	Who are you? Post me a letter and I might let you in heh.
	* Connection #0 to host keepmeposted.chall.cddc2020.nshc.sg left intact


We see an Authorization header.

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization

It is `Authorization: Tm8=` which is "No" in base 64. Send "Yes" instead.


	curl http://keepmeposted.chall.cddc2020.nshc.sg:1057/ --data "" -H "Authorization: $(printf 'Yes' | base64)"
	Congrats! Your flag is: CDDC20{YEs5SS_1_4m_aUTh0r1z3DDdD}

Alternatively, use this online tool.

- https://reqbin.com/req/yjok4snr

## Flag

	CDDC20{YEs5SS_1_4m_aUTh0r1z3DDdD}
