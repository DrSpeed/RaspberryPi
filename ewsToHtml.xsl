<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:g="http://schemas.microsoft.com/exchange/services/2006/messages"
xmlns:c="http://schemas.microsoft.com/exchange/services/2006/types"
>
<xsl:template match="/">
<html>
<body>
  <h2>Room Client Engineering</h2>
    <xsl:for-each select="/s:Envelope/s:Body/g:GetUserAvailabilityResponse/g:FreeBusyResponseArray/g:FreeBusyResponse/g:FreeBusyView/c:CalendarEventArray/c:CalendarEvent[1]">
      <xsl:variable name="rawStartDate" select="c:StartTime" />
      <xsl:variable name="startJustDate" select="substring-before($rawStartDate, 'T')" />
      <td><xsl:value-of select="$startJustDate"/></td>
    </xsl:for-each>

  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Start</th>
      <th>End</th>
      <th>Status</th>
      <th>Subject</th>
    </tr>
    <xsl:for-each select="/s:Envelope/s:Body/g:GetUserAvailabilityResponse/g:FreeBusyResponseArray/g:FreeBusyResponse/g:FreeBusyView/c:CalendarEventArray/c:CalendarEvent">
    <tr>
      <xsl:variable name="rawStart" select="c:StartTime" />
      <xsl:variable name="startJustTime" select="substring-after($rawStart, 'T')" />

      <xsl:variable name="rawEnd" select="c:EndTime" />
      <xsl:variable name="endJustTime" select="substring-after($rawEnd, 'T')" />
      <td>
      <xsl:call-template name="strip-end-characters">
        <xsl:with-param name="text" select="$startJustTime"/>
        <xsl:with-param name="strip-count" select="3"/>
      </xsl:call-template>
      </td>
      <td>
      <xsl:call-template name="strip-end-characters">
        <xsl:with-param name="text" select="$endJustTime"/>
        <xsl:with-param name="strip-count" select="3"/>
      </xsl:call-template>
      </td>
      <td><xsl:value-of select="c:BusyType"/></td>
      <td><xsl:value-of select="c:CalendarEventDetails/c:Subject"/></td>
    </tr>
    </xsl:for-each>
  </table>
</body>
</html>
</xsl:template>

<xsl:template name="strip-end-characters">
    <xsl:param name="text"/>
    <xsl:param name="strip-count"/>
    <xsl:value-of select="substring($text, 1, string-length($text) - $strip-count)"/>
  </xsl:template>

</xsl:stylesheet>
