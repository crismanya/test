<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<SetViewMode>55</SetViewMode>





<item>
<title>[COLOR lime][B][  ][/B][/COLOR]  [COLOR lightgreen][B]LAS PELICULAS[/B] [/COLOR][COLOR skyblue] Recientes - Taquilleras - Populares [/COLOR] </title>

<link>$doregex[makelist4]</link>


<regex>
<name>makelist4</name>
<listrepeat><![CDATA[
   <title>[COLOR deepskyblue] [makelist4.param1][/COLOR]</title>
    <link>$doregex[lista]</link>
 <thumbnail>[makelist4.param2]</thumbnail>
<fanart>[makelist4.param2]</fanart>

]]></listrepeat>
<expres><![CDATA[img\salt="(.*?)"[\w\W\s]{0,20}oadlate="(.*?)"]]></expres>
<page>$doregex[select]</page>
</regex>

<regex>
<name>select</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
   import xbmcgui
   dialog = xbmcgui.Dialog()
   ret = dialog.select('Elige tu Audio preferido ', ['Recientes', 'En Taquilla', 'Populares'])
   lists = ['http://www.imdb.com/search/title?title_type=feature,tv_movie&amp;languages=en&amp;num_votes=500,&amp;production_status=released&amp;groups=top_1000&amp;sort=moviemeter,asc&amp;count=20&amp;start=1', 'http://www.imdb.com/search/title?title_type=feature,tv_movie&amp;sort=boxoffice_gross_us,desc&amp;count=20&amp;start=1', 'http://www.imdb.com/search/title?title_type=feature&amp;languages=en&amp;num_votes=200,&amp;release_date=2016-09-13,2017-09-13&amp;sort=release_date_us,desc&amp;count=20&amp;start=1']
   return lists[ret]
]]></expres>
<page></page>
</regex>






<regex>
<name>lista</name>
  <listrepeat><![CDATA[
         <SetViewMode>55</SetViewMode>
		 <title>$pyFunction:'[lista.param3]'.replace(".mp4", "  [COLOR blue][I]Cris.TV[/I][/COLOR]").replace(".avi", "  [COLOR blue][I]Cris.TV[/I][/COLOR]").replace(".mkv", "  [COLOR blue][I]Cris.TV[/I][/COLOR]")</title>
        <link>$doregex[getUrl]</link>
		 <thumbnail>[makelist4.param2]</thumbnail>
		<fanart>[makelist4.param2]</fanart>
		]]></listrepeat>
<expres><![CDATA[href=\"(.*?,(.*?)\..*?)\".*?preview">(.*?mkv|.*?mp4|.*?avi)<]]><expres>
<page>http://diskokosmiko.mx/action/SearchFiles?Phrase=adryanlist&amp;Mode=List&amp;Type=Video&amp;SizeFromMB=0&amp;SizeToMB=0&amp;pageNumber=10</page>
<rawpost>Phrase=[makelist4.param1]&__RequestVerificationToken=$doregex[tok]</rawpost>
<referer>http://diskokosmiko.mx/action/SearchFiles</referer>
<accept>*/*</accept>
<X-Req>XMLHttpRequest</X-Req>
<cookieJar>d248aa4e1e697a53b195098a52759e8d21507325199</cookieJar>
</regex>


<regex>
<name>tok</name>
<expres>DownloadFile.*RequestVerificationToken.*?value="([^"]+)<expres>
<page>http://diskokosmiko.mx/[lista.param1]</page>
<referer>http://diskokosmiko.mx/adryanlist</referer>
<cookieJar></cookieJar>
</regex>



<regex>
<name>getUrl</name>
<expres>DownloadUrl":"([^"]+)<expres>
<page>http://diskokosmiko.mx/action/DownloadFile?location=fi&amp;f=[lista.param1]</page>
<rawpost>fileId=[lista.param2]&__RequestVerificationToken=$doregex[tok2]</rawpost>
<referer>http://diskokosmiko.mx[lista.param1]</referer>
<accept>*/*</accept>
<X-Req>XMLHttpRequest</X-Req>
<cookieJar></cookieJar>
</regex>

<regex>
<name>tok2</name>
<expres>DownloadFile.*RequestVerificationToken.*?value="([^"]+)<expres>
<page>http://diskokosmiko.mx[lista.param1]</page>
<referer>http://diskokosmiko.mx/adryanlist</referer>
<cookieJar></cookieJar>
</regex>

<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
</item>














<item>
<title>[COLOR lime][B][  ][/B][/COLOR]  [COLOR lightgreen][B]BUSCAR PELICULA[/B] [/COLOR][COLOR skyblue] [/COLOR] </title>
<link>$doregex[lista]</link>

<regex>
<name>lista</name>
  <listrepeat><![CDATA[
         <SetViewMode>55</SetViewMode>
		 <title>$pyFunction:'[lista.param3]'.replace(".mp4", "  [COLOR blue][I]Cris.TV[/I][/COLOR]").replace(".avi", "  [COLOR blue][I]Cris.TV[/I][/COLOR]").replace(".mkv", "  [COLOR blue][I]CRIS.TV[/I][/COLOR]")</title>
        <link>$doregex[getUrl]</link>
		<thumbnail>NA</thumbnail>
		<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
		]]></listrepeat>
<expres><![CDATA[href=\"(.*?,(.*?)\..*?)\".*?preview">(.*?mkv|.*?mp4|.*?avi)<]]><expres>
<page>http://diskokosmiko.mx/action/SearchFiles?Phrase=adryanlist&amp;Mode=List&amp;Type=Video&amp;SizeFromMB=0&amp;SizeToMB=0&amp;pageNumber=10</page>
<rawpost>Phrase=$doregex[search]&__RequestVerificationToken=$doregex[tok]</rawpost>
<referer>http://diskokosmiko.mx/action/SearchFiles</referer>
<accept>*/*</accept>
<X-Req>XMLHttpRequest</X-Req>
<cookieJar>d248aa4e1e697a53b195098a52759e8d21507325199</cookieJar>
</regex>



<regex>
<name>search</name>
<expres><![CDATA[#$pyFunction
import xbmc
import xbmcaddon
import xbmcgui
def GetLSProData(page_data,Cookie_Jar,m):
    dialog = xbmcgui.Dialog()
    d = dialog.input('Buscar  Pelicula: ejemplo: Minions', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    return d
]]></expres>
<page></page>
<cookieJar></cookieJar>
</regex>

<regex>
<name>tok</name>
<expres>DownloadFile.*RequestVerificationToken.*?value="([^"]+)<expres>
<page>http://diskokosmiko.mx/[lista.param1]</page>
<referer>http://diskokosmiko.mx/adryanlist</referer>
<cookieJar></cookieJar>
</regex>



<regex>
<name>getUrl</name>
<expres>DownloadUrl":"([^"]+)<expres>
<page>http://diskokosmiko.mx/action/DownloadFile?location=fi&amp;f=[lista.param1]</page>
<rawpost>fileId=[lista.param2]&__RequestVerificationToken=$doregex[tok2]</rawpost>
<referer>http://diskokosmiko.mx[lista.param1]</referer>
<accept>*/*</accept>
<X-Req>XMLHttpRequest</X-Req>
<cookieJar></cookieJar>
</regex>

<regex>
<name>tok2</name>
<expres>DownloadFile.*RequestVerificationToken.*?value="([^"]+)<expres>
<page>http://diskokosmiko.mx[lista.param1]</page>
<referer>http://diskokosmiko.mx/adryanlist</referer>
<cookieJar></cookieJar>
</regex>

<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
</item>

































































































 






























































	 <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]AQUIPELIS[/B] [/COLOR][COLOR skyblue] RECIENTES [Audio Latino] [/COLOR]   </title>
<link>$doregex[makelist2]</link>

  <regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<SetwatchMode>55</SetwatchMode><title>[makelist2.param2]</title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param3]</thumbnail>
]]></listrepeat>
<expres>class="capa[\w\W\s]{0,18}href="(.*?)"[\w\W\s]{0,22}no-text">(.*?)Esp[\w\W\s]{0,65}src="(.*?)"[\w\W\s]{0,2}alt="(.*?)"</expres>
<page>http://aquipelis.net/</page>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<SetwatchMode>55</SetwatchMode><title>[makelist2.param2]        [makelist.param1]</title>
 <link>$doregex[id3]</link>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres>"(https://openload.*?|https://powvideo.*?|https://userscloud.*?|http://uptobox.*?)"</expres>
<page>[makelist2.param1]</page>
<referer></referer>
<cookieJar></cookieJar>
</regex>

<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '[makelist.param1]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>


<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
 </item>
















 	 <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]AQUIPELIS[/B] [/COLOR][COLOR skyblue] ESTRENOS [Audio Latino] [/COLOR]   </title>
<link>$doregex[makelist2]</link>

  <regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<SetwatchMode>55</SetwatchMode><title>[makelist2.param2]</title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param1]</thumbnail>
]]></listrepeat>
<expres>mostrar_video.*?src='(.*?)'.*?alt="(.*?)online[\w\W\s]{0,240}href="(.*?)"</expres>
<page>http://aquipelis.net/peliculas-estrenos/</page>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<SetwatchMode>55</SetwatchMode><title>[makelist2.param2]     server/[makelist.param1]</title>
 <link>$doregex[id3]</link>
<thumbnail>[makelist2.param1]</thumbnail>
<fanart>[makelist2.param1]</fanart>
]]></listrepeat>
<expres>"(https://openload.*?|https://powvideo.*?|https://userscloud.*?|http://uptobox.*?)"</expres>
<page>[makelist2.param3]</page>
<referer></referer>
<cookieJar></cookieJar>
</regex>

<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '[makelist.param1]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>


<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
 </item>










 <item>
 <title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]NEWPCT[/B] [/COLOR][COLORskyblue][Latino + Castellano][/COLOR] </title>

 <link>$doregex[makelist2]</link>


  <regex>
 <name>makelist2</name>
 <listrepeat><![CDATA[
 <title>[COLOR skyblue] [makelist2.param2]   [/COLOR]</title>
 <link>$doregex[makelist3]</link>
 <thumbnail>[makelist2.param3]</thumbnail>
 <fanart>[makelist2.param3]</fanart>
]]></listrepeat>
 <expres>href="(.*?)".*?Descargar(.*?)gratis.*?src="(.*?)</expres>
 <page>$doregex[select]</page>
 </regex>

<regex>
<name>select</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
  import xbmcgui
  dialog = xbmcgui.Dialog()
  ret = dialog.select('Elige una Seccion ', ['Peliculas Castellano', 'Peliculas Latino', 'Estrenos de Cine Castellano', 'Peliculas Alta Definicion HD', 'Peliculas en 3D HD', 'Otras Peliculas', 'Peliculas x264 MKV', 'Peliculas V.O.Subtituladas'])
  lists = ['http://www.newpct.com/peliculas/', 'http://www.newpct.com/peliculas-latino/', 'http://www.newpct.com/estrenos-de-cine/', 'http://www.newpct.com/peliculas-hd/', 'http://www.newpct.com/peliculas-3d/', 'http://www.newpct.com/otras-peliculas/', 'http://www.newpct.com/peliculas-x264-mkv/']
  return lists[ret]
]]></expres>
 <page></page>
 </regex>







  <regex>
 <name>makelist3</name>
 <listrepeat><![CDATA[
 <title>[COLOR skyblue] [makelist2.param2]              server: [makelist3.param1][/COLOR]</title>
  <link>$doregex[id3]</link>
 <thumbnail>[makelist2.param3]</thumbnail>
 <fanart>[makelist2.param3]</fanart>
 ]]></listrepeat>
 <expres><![CDATA[href='(https://openload.co/f/.*?|https://powvideo.*?|http://uptobox.*?|https://vidabc.*?)']]></expres>
 <page>[makelist2.param1]</page>
 </regex>

 <regex>
 <name>id3</name>
 <expres><![CDATA[#$pyFunction
 def GetLSProData(page_data,Cookie_Jar,m):
     import urlresolver
     url = '[makelist3.param1]'
     try:
         u = urlresolver.resolve(url)
     except:
         u = 'http://adryantv.org/error.mp4'
     return u
 ]]></expres>
 <page></page>
 </regex>

 <thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart></item>

















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]GNULA[/B] [/COLOR][COLOR skyblue][Latino + Castellano] [COLOR aquamarine][/COLOR][/COLOR]  </title>
<link>$doregex[makelist2]</link>



<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR lightblue] [makelist2.param2]  [/COLOR]</title>
<link>$doregex[makelist3]</link>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<fanart>[makelist2.param3]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0</fanart>
]]></listrepeat>
<expres><![CDATA[Ntooltip\"\shref="(.*?)">(.*?)<[\w\W\s]{0,20}src="(.*?)"]]></expres>
<page>http://gnula.nu/peliculas-de-estreno/lista-de-peliculas-online-parte-1/</page>
<referer>http://gnula.nu</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>
<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://gnula.nu',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>

<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[B][COLOR skyblue][makelist2.param2][/COLOR] [COLOR aquamarine][makelist3.param1][/COLOR] [/B][COLOR deepskyblue][makelist3.param3][/COLOR]</title>
<link>$doregex[id3]</link>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<fanart>[makelist2.param3]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0&amp;Referer=http://gnula.nu</fanart>
]]></listrepeat>
<expres><![CDATA[em>(opc.*?)<\/em|href="(http://gamovideo.*?|https://vidoza.*?|https://kingvid.*?|https://openload.*?|https://streamango.*?|http://streamin.*?|http://streamcloud.*?|http://uptobox.*?|https://rapidvideo.*?)".*?class="(.*?)"]]></expres>
<page>[makelist2.param1]</page>
<referer>http://gnula.nu</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>

<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://gnula.nu',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>


<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '[makelist3.param2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart></item>



















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]REPELIS [/B] [/COLOR][COLOR skyblue]Generos [COLOR aquamarine]  [/COLOR] [/COLOR]  </title>

<link>$doregex[makelist0]</link>

<regex>
<name>makelist0</name> categories list
<listrepeat><![CDATA[
   <SetViewMode>55</SetViewMode>
   <title>[COLOR skyblue] [makelist0.param2][/COLOR]</title>
   <link>$doregex[makelist]</link>
   <thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
]]></listrepeat>
<expres><![CDATA[repelis.tv/genero/(.*?)"\stitle="(.*?)"]]></expres>
<page>https://repelis.tv/</page>
<agent>Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1</agent>
<cookieJar></cookieJar>
</regex>



<regex>
    <name>makelist</name> movies  (all pages)
 <listrepeat><![CDATA[
   <title>[COLOR skyblue] [makelist.param3][/COLOR]</title>
   <link>$doregex[makelist2]</link>
   <thumbnail>[makelist.param1]</thumbnail>
   <info>[makelist.param1]</info>
]]></listrepeat>
<expres><![CDATA[#$pyFunction
import re, requests
def GetLSProData(page_data,Cookie_Jar,m):

################################################################## FORMULARY #################################################################
 starturl = 'https://repelis.tv/genero/'     ### usually, ~ 'http://website.com/category/' ###
 categorylink = '[makelist0.param2]' ### check the number of the param ###
 centerurl = '/pag/'      ### something like  '/page/' ###
 firstpage = 1 ### probably  = 1 ###
 endurl = '' ### can be empty ###    ### endurl without final / (SLASH) ###
#
 dataregex = 'src="(.*?)".*?href="(.*?)"\stitle="(?!Ver)(.*?)"'      ### To adapt ###
 headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0', 'Referer': ''}      ### To adapt ###
##############################################################################################################################################

############################## GENERIC PART #####################################
 fullurl = starturl + categorylink + centerurl + str(firstpage) + endurl #
 source = requests.get(fullurl, headers= headers).text #
 data = [] #
#
 last = 5 #
 while firstpage <= last: #
    try: #
        fullurl = starturl + categorylink + centerurl + str(firstpage) + endurl #
        source = requests.get(fullurl, headers=headers).text #
        data += re.findall(dataregex, source) #
        firstpage += 1 #
    except: #
        pass #
 return data #
##########################################################by#twogun#and#jujuuj###
]]></expres><page></page>
</regex>





<regex>
  <name>makelist2</name>
  <listrepeat><![CDATA[
        <SetViewMode>55</SetViewMode>
		<title>[B][makelist.param3][/B]  [COLOR skyblue]server:[B][makelist2.param2][/B] [COLOR lightblue]idioma:[B][makelist2.param3][/B][/COLOR][/COLOR]</title>
        <link>$doregex[makelist4]</link>
		<thumbnail>[makelist3.param1]</thumbnail>
		]]></listrepeat>
<expres><![CDATA[href="(.*?)".*?0\s0\">(.*?)<.*?>(La.*?|Sub.*?)<]]></expres>
<page>[makelist.param2]</page>
<cookieJar></cookieJar>
</regex>


<regex>
  <name>makelist4</name>
  <listrepeat><![CDATA[
        <SetViewMode>55</SetViewMode>
		<title>Reproducir [makelist.param3]-[AdryanList] [COLOR skyblue]server:[B][makelist2.param2][/B] [COLOR lightblue]idioma:[B][makelist2.param3][/B][/COLOR][/COLOR]</title>
        <link>$doregex[id3]</link>
		<thumbnail>[makelist3.param1]</thumbnail>
		]]></listrepeat>
<expres><![CDATA[Player.decode.*?Player.decode\(\'(.*?)\'.*?Player.decode\(\'(.*?)\']]></expres>
<page>[makelist2.param1]</page>
<cookieJar></cookieJar>
</regex>





<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[get-m3u8]$doregex[get-m3u82]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<regex>
<name>get-m3u8</name>
<expres>$pyFunction:base64.b64decode('[makelist4.param1]')</expres>
<page></page>
</regex>
<regex>
<name>get-m3u82</name>
<expres>$pyFunction:base64.b64decode('[makelist4.param2]')</expres>
<page></page>
</regex>


<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
</item>














 <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]SHURWEB [/B] [/COLOR][COLOR skyblue]  [COLOR aquamarine]  [Audio Castellano][/COLOR] [/COLOR]  </title>
<link>$doregex[makelist3]</link>


   <regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<SetwatchMode>55</SetwatchMode><title>[makelist3.param2]</title>
<link>$doregex[makelist2]</link>
]]></listrepeat>
<expres><![CDATA[href="http://www.locopelis.com/pelicula/(.*?)">(.*?)<]]></expres>
<page>http://www.locopelis.com/</page>
</regex>



  <regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<SetwatchMode>55</SetwatchMode>
<title>[makelist2.param2] - [makelist2.param5]</title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param3]</thumbnail>
]]></listrepeat>
<expres><![CDATA[href="(.*?)"[\w\W\s]{0,2}title="(.*?)"[\w\W\s]{0,7}src="(.*?)"[\w\W\s]{0,2}alt="(.*?)"[\w\W\s]{0,1002}default\/img\/(idioma/.*?).png]]></expres>
<page>http://www.locopelis.com/pelicula/[makelist3.param1]</page>
</regex>


 <regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param2]</title>
<link>$doregex[id3]</link>
<thumbnail>[makelist2.param3]</thumbnail>
]]></listrepeat>
<expres><![CDATA[iframe\ssrc="(.*?)"]]></expres>
<page>[makelist2.param1]</page>
</regex>


<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '[makelist.param1]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart></item>











































 





  


  















































<iem>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Gnula[/B] [/COLOR][COLOR skyblue]Estrenos Audio Latino y [COLOR aquamarine]Castellano[/COLOR][/COLOR] </title>
<link>$doregex[makelist2]</link>

<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
   <title>[makelist2.param2]  </title>
 <link>$doregex[makelist3]</link>
 <thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres>class="Ntooltip" href="(.*?)">(.*?)<[\w\W\s]{0,19}src="(.*?)"</expres>
<page>http://gnula.nu/peliculas-online/lista-de-peliculas-online-parte-1/</page>
<referer>http://gnula.nu</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>

<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://gnula.nu',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>




 <regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist2.param2]           - [COLOR lightslategray] server  [makelist3.param1] [/COLOR] [/COLOR]</title>
<link>http://$doregex[url]|User-Agent=Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Mobile Safari/537.36/</link>
 <thumbnail>[makelist2.param3]|Referer:http://gnula.nu</thumbnail>
<fanart>[makelist2.param3]|Referer:http://gnula.nu</fanart>
<fanart></fanart>
]]></listrepeat>
<expres><![CDATA["(https://streamango.*?)"]]></expres>
<page>[makelist2.param1]</page>
<referer>http://gnula.nu</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>

<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://gnula.nu',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>


<regex>
<name>url</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m,url = '[makelist3.param1]'):
 import requests, re
 ua = 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Mobile Safari/537.36/'
 headers = {'User-Agent': ua, 'Accept': 'application/vnd.apple.mpegurl, text/javascript, */*; q=0.01', 'Connection': 'keep-alive'}
 source = requests.get(url, headers = headers).text
 return re.findall('src:"\/\/(.*?)"', source)[0].replace('\/','/')
]]></expres>
<page></page>
<cookieJar></cookieJar>
</regex>
<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
</item>



















<itm>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Gnula.nu[/B] [/COLOR][COLOR skyblue]Generos[/COLOR] </title>
<link>$doregex[makelist3]</link>

<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
   <title>[makelist3.param1]</title>
    <link>$doregex[makelist2]</link>

]]></listrepeat>
<expres>strong>(.*?)<[\w\W\s]{0,13}href="(.*?)"</expres>
<page>http://gnula.nu/generos/lista-de-generos/</page>
<referer>http://gnula.nu</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>

</regex>

<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://gnula.nu',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>

<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
   <title>[makelist2.param2]</title>
    <link>$doregex[makelist]</link>
 <thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres>class="Ntooltip" href="(.*?)">(.*?)<[\w\W\s]{0,29}src="(.*?)"</expres>
<page>[makelist3.param2]</page>
<referer>http://gnula.nu</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>

</regex>

<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://gnula.nu',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>

<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[COLOR lightblue][makelist2.param2][/COLOR]</title>
<link>$doregex[url]/$doregex[id2]/v.flv</link>
<regex>
<name>url</name>
<expres>vplayer[\w\W\s]{0,8}src="(.*?)\/i</expres>
<page>http://streamin.to/embed-[makelist.param1]-740x360.html</page>
<referer>http://streamin.to</referer>
</regex>
<regex>
<name>id2</name>
<expres>image\|[\w\W\s]{0,3}\|(.*?)\|file</expres>
<page>http://streamin.to/embed-[makelist.param1]-740x360.html</page>
<referer>http://streamin.to</referer>
</regex>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres>http://streamin.to/(.*?)"</expres>
<page>[makelist2.param1]</page>
<referer>http://gnula.nu</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>

</regex>

<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://gnula.nu',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>
<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
</item>








































<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]PeliculasDK / Categorias[/B]  [/COLOR][COLOR skyblue]     [/COLOR] </title>
<link>$doregex[makelist3]</link>



 <regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist3.param2][/COLOR] </title>
<link>$doregex[makelist2]</link>
]]></listrepeat>
<expres><![CDATA[href='(.*?)'>(.*?)<]]></expres>
<page>http://www.peliculasdk.com/</page>
<referer></referer>
<cookieJar></cookieJar>
</regex>



<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist2.param2]   [COLOR lightblue] idioma:[makelist2.param4][/COLOR][/COLOR] </title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[href="(.*?)"[\w\W\s]{0,2}title="(.*?)"[\w\W\s]{0,7}src="(.*?)"[\w\W\s]{0,300}idioma/(.*?)"]]></expres>
<page>http://www.peliculasdk.com[makelist3.param1]</page>

 </regex>




<regex>
   <name>makelist</name>
   <listrepeat><![CDATA[
          <title>[makelist2.param2]</title>
          <link>$doregex[id3]</link>
		  <thumbnail>[makelist2.param3]</thumbnail>
		<fanart>[makelist2.param3]</fanart>
   ]]></listrepeat>
   <expres><![CDATA[open\("(.*?)"]]></expres>
   <page>[makelist2.param1]</page>
   <cookieJar></cookieJar>
</regex>



<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = 'https://openload.co/embed/[makelist.param1]/'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart></item>




























































<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]PELISPLANET[/B]  [/COLOR][COLOR skyblue]     [/COLOR] </title>

<link>$doregex[makelist3]</link>

<regex>
   <name>makelist3</name>
<listrepeat><![CDATA[
<title>Pagina [makelist3.param1]</title>
<link>$doregex[makelist2]</link>
]]></listrepeat>
<expres>'(.*?)'</expres>
<page>'1''2''3''4''5''6''7''8''9''10''11''12''13''14''15''16''17''18''19''20''21''22''23''24''25'</page>
</regex>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue]  [makelist2.param2]     [COLOR deepskyblue][I]Idioma: [makelist2.param4]  [/I][/COLOR] [/COLOR] </title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param5]</thumbnail>
<fanart>[makelist2.param5]</fanart>
]]></listrepeat>
<expres><![CDATA[href="(.*?)"[\w\W\s]{0,510}one-line">(.*?)<[\w\W\s]{0,350}flags/(.*?).png.*?title="(.*?)"[\w\W\s]{0,240}src="(.*?)"]]></expres>
<page>http://www.pelisplanet.com/genero/estrenos/page/[makelist3.param1]/</page>

 </regex>

<regex>
   <name>makelist</name>
   <listrepeat><![CDATA[
          <title>[makelist2.param2]    - Server:[makelist.param1]</title>
          <urlsolve>[makelist.param1]</urlsolve>
		  <thumbnail>[makelist2.param5]</thumbnail>
		<fanart>[makelist2.param5]</fanart>
   ]]></listrepeat>
   <expres><![CDATA[rel="(https://drive.*?|https://openload.*?|https://streamango.*?|http://fastplay.*?|https://www.rapidvideo.*?)"]]></expres>
   <page>[makelist2.param1]</page>
   <cookieJar></cookieJar>
</regex>



<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart></item>













































































































































































































<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]PELICULASREY[/B] [/COLOR][COLORskyblue][-][/COLOR] </title>
<link>$doregex[makelist0]</link>

<regex>
<name>makelist0</name>
<listrepeat><![CDATA[
<title>Pagina [makelist0.param1]</title>
<link>$doregex[makelist2]</link>
]]></listrepeat>
<expres>'(.*?)'</expres>
<page>'1''2''3''4''5''6''7''8''9''10''11''12''13''14''15''16''17''18''19''20''21''22''23''24''25'</page>
</regex>

<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR lightblue] [makelist2.param2]   [/COLOR]</title>
<link>$doregex[makelist3]</link>
<thumbnail>[makelist2.param1]</thumbnail>
<fanart>[makelist2.param1]</fanart>
]]></listrepeat>
<expres><![CDATA[poster[\w\W\s\n]{0,10}src="(.*?)"\salt="(.*?)"\stitle="(.*?)".*?href="(.*?)"]]></expres>
<page>http://www.peliculasrey.com/page/[makelist0.param1]/</page>
</regex>



<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR lightblue] [makelist2.param2] | [COLOR lightgreen]Idioma:[B][makelist3.param3][/B][/COLOR]  [COLOR aquamarine]Server:[B][makelist3.param2][/B][/COLOR]        [/COLOR]</title>
<link>$doregex[id3]</link>
<thumbnail>[makelist2.param1]</thumbnail>
<fanart>[makelist2.param1]</fanart>
]]></listrepeat>
<expres><![CDATA[hand\"\srel=\"(http://gamovideo.*?|https://vidoza.*?|https://kingvid.*?|https://openload.*?|https://streamango.*?|http://streamin.*?|http://powvideo.*?|https://drive.*?)\".*?title=\"(.*?)\"[\w\W\s\n]{0,50}optxt[\w\W\s\n]{0,6}pan>(.*?)<]]></expres>
<page>[makelist2.param4]</page>
</regex>

<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '[makelist3.param1]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart></item>






<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]PELICULASREY[/B] [/COLOR][COLORskyblue][Buscar][/COLOR] WIP </title>
<link>$doregex[makelist2]</link>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR lightblue] [makelist2.param2]   [/COLOR]</title>
<link>$doregex[makelist3]</link>
<thumbnail>[makelist2.param1]</thumbnail>
<fanart>[makelist2.param1]</fanart>
]]></listrepeat>
<expres><![CDATA[img\ssrc="(.*?)"\salt="(.*?)"\stitle="(.*?)".*?href="(.*?)"]]></expres>
<page>http://www.peliculasrey.com/?s=$doregex[search]</page>
</regex>


<regex>
<name>search</name>
<expres><![CDATA[#$pyFunction
import xbmc
import xbmcaddon
import xbmcgui
def GetLSProData(page_data,Cookie_Jar,m):
    dialog = xbmcgui.Dialog()
    d = dialog.input('Buscar Serie: ejemplo: Minions', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    return d
]]></expres>
<page></page>
<cookieJar></cookieJar>
</regex>



<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR lightblue] [makelist2.param2] | [COLOR lightgreen]Idioma:[B][makelist3.param3][/B][/COLOR]  [COLOR aquamarine]Server:[B][makelist3.param2][/B][/COLOR]        [/COLOR]</title>
<link>$doregex[id3]</link>

<thumbnail>[makelist2.param1]</thumbnail>
<fanart>[makelist2.param1]</fanart>
]]></listrepeat>
<expres><![CDATA[hand\"\srel=\"(http://gamovideo.*?|https://vidoza.*?|https://kingvid.*?|https://openload.*?|https://streamango.*?|http://streamin.*?|http://powvideo.*?|https://drive.*?)\".*?title=\"(.*?)\"[\w\W\s\n]{0,50}optxt[\w\W\s\n]{0,6}pan>(.*?)<]]></expres>
<page>[makelist2.param4]</page>
</regex>

<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '[makelist3.param1]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>



<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart></item>


















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightgreen][B]MEXFLIX [/COLOR][COLOR skyblue]+[/COLOR] [/B]</title>
<link>$doregex[makelist]</link>


<regex>
  <name>makelist</name>
  <listrepeat><![CDATA[
 <title>$pyFunction:'[makelist.param3]'.replace(".mp4", " [COLOR blue][I]by MexFlix[/I][/COLOR]")</title>
        <link>$doregex[getUrl]</link>
		<thumbnail>https://image.tmdb.org/t/p/original/$doregex[imagen]</thumbnail>
		]]></listrepeat>
<expres><![CDATA[href="\/.*,(.*?),list.*\n.*\n.*\n.*href="\/([^"]*)".*?>(.*?)<]]></expres>
<page>http://diskokosmiko.mx/mexflix17/03peliculas-de-drama30-77318/list,1,1</page>
<cookieJar></cookieJar>
</regex>
<regex>
<name>imagen</name>
<expres><![CDATA[poster_path\":\"\\/(.*?)\"]]></expres>
<page>https://api.themoviedb.org/3/search/movie?api_key=3d8a2c67653e2f8fd7dd09959e835f02&amp;language=es&amp;query=$doregex[nombre2]</page>
</regex>

<regex>
<name>nombre2</name>
<expres>$pyFunction:'[makelist.param3]'.replace(".mp4", "").replace(" ", "+")</expres>
<page></page>
</regex>

<regex>
<name>getUrl</name>
<expres>DownloadUrl":"([^"]+)<expres>
<page>http://diskokosmiko.mx/action/DownloadFile?location=fi&amp;f=[makelist.param1]</page>
<rawpost>fileId=[makelist.param1]&__RequestVerificationToken=$doregex[tok]</rawpost>
<referer>http://diskokosmiko.mx/[makelist.param2]</referer>
<connection>keep-alive</connection>
<accept>*/*</accept>
<X-Req>XMLHttpRequest</X-Req>
<cookieJar></cookieJar>
</regex>
<regex>
<name>tok</name>
<expres>DownloadFile.*RequestVerificationToken.*?value="([^"]+)<expres>
<page>http://diskokosmiko.mx/[makelist.param2]</page>
<referer>http://diskokosmiko.mx/mexflix17/03peliculas-de-drama30-77318/list,1,15</referer>
<connection>keep-alive</connection>
<cookieJar></cookieJar>
</regex>

<thumbnail>NA</thumbnail>
<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
</item>





































































