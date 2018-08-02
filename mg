<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

<item>
<title>[I]El Marginal Temporada 2 Capítulo 1[/I]</title>
 
<link>$doregex[url]</link>
<regex>
<name>url</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
 import requests,re
 url= 'https://docs.google.com/uc?id=1CbWkSQZf_mBDie30eBOku9oKposdG8KM&export=download'
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
 
<item>
<title>[I]El Marginal Temporada 2 Capítulo 2[/I]</title>
 
<link>$doregex[url]</link>
<regex>
<name>url</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
 import requests,re
 url= 'https://docs.google.com/uc?id=1tbSf1aQUlop0ctcL0hZSDLDd0PGyfA6y&export=download'
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


<item>
<title>[I]El Marginal Temporada 2 Capítulo 3[/I]</title>
 
<link>$doregex[url]</link>
<regex>
<name>url</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
 import requests,re
 url= 'https://docs.google.com/uc?id=1PLALQb4QcXfNLyx8R_jAQ7MF_TOW_nfn&export=download'
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
