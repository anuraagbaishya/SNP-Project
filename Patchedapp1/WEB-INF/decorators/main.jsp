<%@ page import="org.apache.struts2.result.StrutsResultSupport" %>
<!DOCTYPE html>
<%@ page
        language="java"
        contentType="text/html; charset=UTF-8"
        pageEncoding="UTF-8" %>
<%
    response.setHeader("Pragma", "no-cache");
    response.setHeader("Cache-Control", "no-cache");
    response.setDateHeader("Expires", 0);

    // Calculate the view sources url
    String sourceUrl = request.getContextPath() + "/viewSource.action";
    com.opensymphony.xwork2.ActionInvocation inv = com.opensymphony.xwork2.ActionContext.getContext().getActionInvocation();
    org.apache.struts2.dispatcher.mapper.ActionMapping mapping = org.apache.struts2.ServletActionContext.getActionMapping();
    if (inv != null) {
        try {
            com.opensymphony.xwork2.util.location.Location loc = inv.getProxy().getConfig().getLocation();
            sourceUrl += "?config=" + (loc != null ? loc.getURI() + ":" + loc.getLineNumber() : "");
        } catch (Exception e) {
            sourceUrl += "?config=";
        }
        sourceUrl += "&className=" + inv.getProxy().getConfig().getClassName();

        if (inv.getResult() != null && inv.getResult() instanceof StrutsResultSupport) {
            sourceUrl += "&page=" + mapping.getNamespace() + "/" + ((StrutsResultSupport) inv.getResult()).getLastFinalLocation();
        }
    } else {
        sourceUrl += "?page=" + request.getServletPath();
    }
%>
<%@taglib prefix="decorator" uri="http://www.opensymphony.com/sitemesh/decorator" %>
<%@taglib prefix="page" uri="http://www.opensymphony.com/sitemesh/page" %>
<%@taglib prefix="s" uri="/struts-tags" %>

<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Struts2 Showcase for Apache Struts Project">
    <meta name="author" content="The Apache Software Foundation">

    <title><decorator:title default="Struts2 Showcase"/></title>

    <link href="<s:url value='/styles/bootstrap.css' encode='false' includeParams='none'/>" rel="stylesheet" type="text/css" media="all">
    <link href="<s:url value='/styles/main.css' encode='false' includeParams='none'/>" rel="stylesheet" type="text/css" media="all"/>

    <script src="<s:url value='/js/jquery-2.1.4.min.js' encode='false' includeParams='none'/>"></script>
    <script src="<s:url value='/js/bootstrap.min.js' encode='false' includeParams='none'/>"></script>
    <script type="text/javascript">
        $(function () {
            var alerts = $('ul.alert').wrap('<div />');
            alerts.prepend('<a class="close" data-dismiss="alert" href="#">&times;</a>');
            alerts.alert();
        });
    </script>

    <!-- Prettify -->
    <link href="<s:url value='/styles/prettify.css' encode='false' includeParams='none'/>" rel="stylesheet">
    <script src="<s:url value='/js/prettify.js' encode='false' includeParams='none'/>"></script>

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
    <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <decorator:head/>
</head>

<body id="page-home" onload="prettyPrint();">
<decorator:body/>


<hr>

<footer id="footer" class="footer">

    <div class="pull-right">
        <div>
            <a href="http://struts.apache.org"/>
                Powered by Struts
            </a>
        </div>
        <!-- end search -->
    </div>

    <div class="pull-left">
        Copyright &copy; 2003-<s:property value="#dateAction.now.year + 1900"/>
        <a href="http://www.apache.org">
            The Apache Software Foundation.
        </a>
    </div>
</footer>
</body>
</html>
