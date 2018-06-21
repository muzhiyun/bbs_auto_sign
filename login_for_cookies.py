#直接用的前辈的 修改了下post的参数

import urllib
import urllib2
import cookielib
 
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
            'fastloginfield':'username',
		    	  'username':'muzhi',
		      	'cookietime':'2592000',
		      	'password':'',
			     'quickforward':'yes',
		      	'handlekey':'ls'
           })
loginUrl = 'http://www.com/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
print "cookie is OK"
