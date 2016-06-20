<xsl:stylesheet version="1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
		xmlns:g="http://schemas.microsoft.com/exchange/services/2006/messages"
		xmlns:c="http://schemas.microsoft.com/exchange/services/2006/types"
		>
  <xsl:output method="text" indent="yes"/>
  <xsl:template match="/">
#!/bin/sh
<xsl:text>&#xa;</xsl:text>

<xsl:for-each select="/s:Envelope/s:Body/g:GetUserAvailabilityResponse/g:FreeBusyResponseArray/g:FreeBusyResponse/g:FreeBusyView/c:CalendarEventArray/c:CalendarEvent[1]">
      <xsl:variable name="rawStartDate" select="c:StartTime" />
      <xsl:variable name="startJustDate" select="substring-before($rawStartDate, 'T')" />
      <xsl:variable name="shortDate" select="$startJustDate"/>

      <xsl:for-each select="/s:Envelope/s:Body/g:GetUserAvailabilityResponse/g:FreeBusyResponseArray/g:FreeBusyResponse/g:FreeBusyView/c:CalendarEventArray/c:CalendarEvent">
	<xsl:variable name="rawStart" select="c:StartTime" />
	<xsl:variable name="startJustTime" select="substring-after($rawStart, 'T')" />
	<xsl:variable name="shortStart">
	  <xsl:call-template name="strip-end-characters">
            <xsl:with-param name="text" select="$startJustTime"/>
            <xsl:with-param name="strip-count" select="3"/>
	  </xsl:call-template>
	</xsl:variable>
	<xsl:variable name="rawEnd" select="c:EndTime" />
	<xsl:variable name="endJustTime" select="substring-after($rawEnd, 'T')" />
	<xsl:variable name="shortEnd">
	  <xsl:call-template name="strip-end-characters">
            <xsl:with-param name="text" select="$endJustTime"/>
            <xsl:with-param name="strip-count" select="3"/>
	  </xsl:call-template>
	</xsl:variable>
curl -XPOST -s "http://auto2-report-dev-1.globix-sc.gracenote.com:9200/iot_reserved" \
  -d "{\"room\":  \"client_engg\", \
       \"date\":  \"<xsl:value-of select="$shortDate"/>\", \
       \"start\": \"<xsl:value-of select="$shortStart"/>\", \
       \"end\":   \"<xsl:value-of select="$shortEnd"/>\" }"
	<xsl:text>&#xa;</xsl:text>
      </xsl:for-each>
    </xsl:for-each>
  </xsl:template>
  <xsl:template name="strip-end-characters">
    <xsl:param name="text"/>
    <xsl:param name="strip-count"/>
    <xsl:value-of select="substring($text, 1, string-length($text) - $strip-count)"/>
  </xsl:template>
</xsl:stylesheet>
