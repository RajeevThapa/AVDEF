# Vulnerability Scan Report

## Nmap Scan Results
# Nmap 7.94SVN scan initiated Thu Nov 14 11:10:11 2024 as: nmap -sV --script vuln -oN ./scans/nmap/testhtml5.vulnweb.com_nmap.txt testhtml5.vulnweb.com
Nmap scan report for testhtml5.vulnweb.com (44.228.249.3)
Host is up (0.21s latency).
rDNS record for 44.228.249.3: ec2-44-228-249-3.us-west-2.compute.amazonaws.com
Not shown: 998 filtered tcp ports (no-response), 1 filtered tcp ports (admin-prohibited)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.19.0
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=testhtml5.vulnweb.com
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://testhtml5.vulnweb.com:80/
|     Form id: loginform
|_    Form action: /login
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-dombased-xss: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=testhtml5.vulnweb.com
|   Found the following indications of potential DOM based XSS: 
|     
|     Source: document.write('<div class="fb-comments" data-num-posts="4" data-width="470"  data-href="'+window.location.href+'"></div>')
|_    Pages: http://testhtml5.vulnweb.com:80/static/app/post.js
| http-enum: 
|   /admin/: Possible admin folder (401 UNAUTHORIZED)
|_  /samples/: Sample scripts

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Nov 14 11:18:03 2024 -- 1 IP address (1 host up) scanned in 472.41 seconds
## ZAP Scan Results
#
![](data:image/png;base64,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)
ZAP Scanning Report

##  Site: http://testhtml5.vulnweb.com

###  Generated on Thu, 14 Nov 2024 15:55:05

###  ZAP Version: 2.15.0

####  ZAP by [Checkmarx](https://checkmarx.com/)

### Summary of Alerts

Risk Level | Number of Alerts  
---|---  
High |  0  
Medium |  3  
Low |  3  
Informational |  2  
False Positives: |  0  
  
### Alerts

Name | Risk Level | Number of Instances  
---|---|---  
Content Security Policy (CSP) Header Not Set | Medium | 1  
Cross-Domain Misconfiguration | Medium | 1  
Missing Anti-clickjacking Header | Medium | 1  
Cross-Domain JavaScript Source File Inclusion | Low | 4  
Server Leaks Version Information via "Server" HTTP Response Header Field | Low | 1  
X-Content-Type-Options Header Missing | Low | 1  
Information Disclosure - Suspicious Comments | Informational | 1  
Modern Web Application | Informational | 1  
  
### Alert Detail

Medium | Content Security Policy (CSP) Header Not Set  
---|---  
Description |  Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.  
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter |   
Attack |   
Evidence |   
Other Info |   
Instances | 1  
Solution |  Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.  
Reference |  <https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy>   
<https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html>  
<https://www.w3.org/TR/CSP/>  
<https://w3c.github.io/webappsec-csp/>  
<https://web.dev/articles/csp>  
<https://caniuse.com/#feat=contentsecuritypolicy>  
<https://content-security-policy.com/>  
CWE Id | [693](https://cwe.mitre.org/data/definitions/693.html)  
WASC Id | 15  
Plugin Id | [10038](https://www.zaproxy.org/docs/alerts/10038/)  
  
Medium | Cross-Domain Misconfiguration  
---|---  
Description |  Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.  
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter |   
Attack |   
Evidence | Access-Control-Allow-Origin: *  
Other Info | The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.  
Instances | 1  
Solution |  Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).   
Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive
set of domains, or remove all CORS headers entirely, to allow the web browser
to enforce the Same Origin Policy (SOP) in a more restrictive manner.  
Reference |  <https://vulncat.fortify.com/en/detail?id=desc.config.dotnet.html5_overly_permissive_cors_policy>  
CWE Id | [264](https://cwe.mitre.org/data/definitions/264.html)  
WASC Id | 14  
Plugin Id | [10098](https://www.zaproxy.org/docs/alerts/10098/)  
  
Medium | Missing Anti-clickjacking Header  
---|---  
Description |  The response does not protect against 'ClickJacking' attacks. It should include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options.  
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter | x-frame-options  
Attack |   
Evidence |   
Other Info |   
Instances | 1  
Solution |  Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.   
If you expect the page to be framed only by pages on your server (e.g. it's
part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never
expect the page to be framed, you should use DENY. Alternatively consider
implementing Content Security Policy's "frame-ancestors" directive.  
Reference |  <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options>  
CWE Id | [1021](https://cwe.mitre.org/data/definitions/1021.html)  
WASC Id | 15  
Plugin Id | [10020](https://www.zaproxy.org/docs/alerts/10020/)  
  
Low | Cross-Domain JavaScript Source File Inclusion  
---|---  
Description |  The page includes one or more script files from a third-party domain.  
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter | http://bxss.s3.amazonaws.com/ad.js  
Attack |   
Evidence | <script src="http://bxss.s3.amazonaws.com/ad.js"></script>  
Other Info |   
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter | http://code.jquery.com/jquery-1.9.1.min.js  
Attack |   
Evidence | <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>  
Other Info |   
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter | http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js  
Attack |   
Evidence | <script src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>  
Other Info |   
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter | https://ajax.googleapis.com/ajax/libs/angularjs/1.0.6/angular.min.js  
Attack |   
Evidence | <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.0.6/angular.min.js"></script>  
Other Info |   
Instances | 4  
Solution |  Ensure JavaScript source files are loaded from only trusted sources, and the sources can't be controlled by end users of the application.  
Reference |   
CWE Id | [829](https://cwe.mitre.org/data/definitions/829.html)  
WASC Id | 15  
Plugin Id | [10017](https://www.zaproxy.org/docs/alerts/10017/)  
  
Low | Server Leaks Version Information via "Server" HTTP Response Header Field  
---|---  
Description |  The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.  
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter |   
Attack |   
Evidence | nginx/1.19.0  
Other Info |   
Instances | 1  
Solution |  Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.  
Reference |  <https://httpd.apache.org/docs/current/mod/core.html#servertokens>   
<https://learn.microsoft.com/en-us/previous-versions/msp-
n-p/ff648552(v=pandp.10)>  
<https://www.troyhunt.com/shhh-dont-let-your-response-headers/>  
CWE Id | [200](https://cwe.mitre.org/data/definitions/200.html)  
WASC Id | 13  
Plugin Id | [10036](https://www.zaproxy.org/docs/alerts/10036/)  
  
Low | X-Content-Type-Options Header Missing  
---|---  
Description |  The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.  
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter | x-content-type-options  
Attack |   
Evidence |   
Other Info | This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type. At "High" threshold this scan rule will not alert on client or server error responses.  
Instances | 1  
Solution |  Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.   
If possible, ensure that the end user uses a standards-compliant and modern
web browser that does not perform MIME-sniffing at all, or that can be
directed by the web application/web server to not perform MIME-sniffing.  
Reference |  <https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85)>   
<https://owasp.org/www-community/Security_Headers>  
CWE Id | [693](https://cwe.mitre.org/data/definitions/693.html)  
WASC Id | 15  
Plugin Id | [10021](https://www.zaproxy.org/docs/alerts/10021/)  
  
Informational | Information Disclosure - Suspicious Comments  
---|---  
Description |  The response appears to contain suspicious comments which may help an attacker. Note: Matches made within script blocks or files are against the entire content not only comments.  
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter |   
Attack |   
Evidence | Username  
Other Info | The following pattern was used: \bUSERNAME\b and was detected in the element starting with: "<!-- Username -->", see evidence field for the suspicious comment/snippet.  
Instances | 1  
Solution |  Remove all comments that return information that may help an attacker and fix any underlying problems they refer to.  
Reference |   
CWE Id | [200](https://cwe.mitre.org/data/definitions/200.html)  
WASC Id | 13  
Plugin Id | [10027](https://www.zaproxy.org/docs/alerts/10027/)  
  
Informational | Modern Web Application  
---|---  
Description |  The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.  
URL | <http://testhtml5.vulnweb.com/>  
Method | GET  
Parameter |   
Attack |   
Evidence | <a href="#" class="btn" id="loginFormForgot">Forgot Pwd?</a>  
Other Info | Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.  
Instances | 1  
Solution |  This is an informational alert and so no changes are required.  
Reference |   
CWE Id |   
WASC Id |   
Plugin Id | [10109](https://www.zaproxy.org/docs/alerts/10109/)

## Nikto Scan Results
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ -3092: GET /samples/: /samples/: This might be interesting...
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ -3092: GET /samples/: /samples/: This might be interesting...
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ -3092: GET /samples/: /samples/: This might be interesting...
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ -3092: GET /samples/: /samples/: This might be interesting...
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ -3092: GET /samples/: /samples/: This might be interesting...
