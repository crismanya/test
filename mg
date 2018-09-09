<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

<item>
<title>[B]El Marginal Temporada 2 Capítulo 1[/B]</title>
<link>https://archive.org/download/3l.Mrg1n3l/3l.M%40rg1n3l.2x01.mp4</link>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>
 
<item>
<title>[B]El Marginal Temporada 2 Capítulo 2[/B]</title>
<link>https://archive.org/download/3l.Mrg1n3l/3l.M%40rg1n3l.2x02.mkv</link>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>


<item>
<title>[B]El Marginal Temporada 2 Capítulo 3[/B]</title>
<link>https://archive.org/download/3l.Mrg1n3l/3l.M%40rg1n3l.2x03.mkv</link>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>

<item>
<title>[B]El Marginal Temporada 2 Capítulo 4[/B]</title> 
<link>https://archive.org/download/3l.Mrg1n3l/3l.M%40rg1n3l.2x04.mkv</link>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>


<item>
<title>[B]El Marginal Temporada 2 Capítulo 5[/B]</title>
<link>https://archive.org/download/3l.Mrg1n3l/3l.M%40rg1n3l.2x05.mkv</link>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>


<item>
<title>[B]El Marginal Temporada 2 Capítulo 6[/B]</title>
<link>https://archive.org/download/3l.Mrg1n3l/3l.M%40rg1n3l.2x06.mkv</link>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>

<item>
<title>[B]El Marginal Temporada 2 Capítulo 7[/B]</title>
<link>https://archive.org/download/3l.Mrg1n3l/3l.M%40rg1n3l.2x07.mkv</link>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>

<item>
<title>[B]El Marginal Temporada 2 Capítulo 88[/B]</title>
<link>https://archive.org/download/3l.Mrg1n3l/3l.M%40rg1n3l.2x08.mkv</link>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>


<item>
<title>[B]El Marginal Temporada 2 Capítulo 8[/B]</title>
 
<link>$doregex[url]</link>
<regex>
<name>url</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
 import requests,re
 url= 'https://docs.google.com/uc?id=1PxWRUL4RgFG4FpQHve6Yq5DQUwFgpNcv&export=download'
 headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0 Iceweasel/44.0'}
 source0= requests.get(url,headers=headers)
 pageUrl = 'https://docs.google.com' + re.findall('goog-inline-block jfk-button jfk-button-action" href="(.*?)"', source0.text)[0].replace('amp;', '')
 cookies =  source0.cookies.get_dict()
 
 headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0 Iceweasel/44.0','Referer': url}
 source= requests.get(pageUrl, headers=headers, cookies=cookies, allow_redirects=False)
 
 streamUrl = re.findall('HREF="(.*?)"',source.text)[0]
 
 return streamUrl
]]></expres>
<page></page>
<cookieJar></cookieJar>
<thumbnail>https://i.imgur.com/WpfeuMH.jpg</thumbnail>
<fanart>https://conlagentenoticias.com/wp-content/uploads/2018/07/marginal.jpg</fanart>
</item>
