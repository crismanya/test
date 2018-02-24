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
		 <title>$pyFunction:'[lista.param3]'.replace(".mp4", "  [COLOR blue][I]AdryanList[/I][/COLOR]").replace(".avi", "  [COLOR blue][I]AdryanList[/I][/COLOR]").replace(".mkv", "  [COLOR blue][I]CRIS.TV[/I][/COLOR]")</title>
        <link>$doregex[getUrl]</link>
		 <thumbnail>[makelist4.param2]</thumbnail>
		<fanart>[makelist4.param2]</fanart>
		]]></listrepeat>
<expres><![CDATA[href=\"(.*?,(.*?)\..*?)\".*?preview">(.*?mkv|.*?mp4|.*?avi)<]]><expres>
<page>http://diskokosmiko.mx/action/SearchFiles?Phrase=adryanlist&amp;Mode=List&amp;Type=Video&amp;SizeFromMB=0&amp;SizeToMB=0&amp;pageNumber=10</page>
<rawpost>Phrase=[makelist4.param1]&__RequestVerificationToken=$doregex[tok]</rawpost>
<referer>http://diskokosmiko.mx/action/SearchFiles</referer>
<connection>keep-alive</connection>
<accept>*/*</accept>
<X-Req>XMLHttpRequest</X-Req>
<cookieJar>d248aa4e1e697a53b195098a52759e8d21507325199</cookieJar>
</regex>


<regex>
<name>tok</name>
<expres>DownloadFile.*RequestVerificationToken.*?value="([^"]+)<expres>
<page>http://diskokosmiko.mx/[lista.param1]</page>
<referer>http://diskokosmiko.mx/adryanlist</referer>
<connection>keep-alive</connection>
<cookieJar></cookieJar>
</regex>



<regex>
<name>getUrl</name>
<expres>DownloadUrl":"([^"]+)<expres>
<page>http://diskokosmiko.mx/action/DownloadFile?location=fi&amp;f=[lista.param1]</page>
<rawpost>fileId=[lista.param2]&__RequestVerificationToken=$doregex[tok2]</rawpost>
<referer>http://diskokosmiko.mx[lista.param1]</referer>
<connection>keep-alive</connection>
<accept>*/*</accept>
<X-Req>XMLHttpRequest</X-Req>
<cookieJar></cookieJar>
</regex>

<regex>
<name>tok2</name>
<expres>DownloadFile.*RequestVerificationToken.*?value="([^"]+)<expres>
<page>http://diskokosmiko.mx[lista.param1]</page>
<referer>http://diskokosmiko.mx/adryanlist</referer>
<connection>keep-alive</connection>
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
		 <title>$pyFunction:'[lista.param3]'.replace(".mp4", "  [COLOR blue][I]AdryanList[/I][/COLOR]").replace(".avi", "  [COLOR blue][I]AdryanList[/I][/COLOR]").replace(".mkv", "  [COLOR blue][I]CRIS.TV[/I][/COLOR]")</title>
        <link>$doregex[getUrl]</link>
		<thumbnail>NA</thumbnail>
		<fanart>https://i.imgur.com/0N9p0X7.jpg</fanart>
		]]></listrepeat>
<expres><![CDATA[href=\"(.*?,(.*?)\..*?)\".*?preview">(.*?mkv|.*?mp4|.*?avi)<]]><expres>
<page>http://diskokosmiko.mx/action/SearchFiles?Phrase=adryanlist&amp;Mode=List&amp;Type=Video&amp;SizeFromMB=0&amp;SizeToMB=0&amp;pageNumber=10</page>
<rawpost>Phrase=$doregex[search]&__RequestVerificationToken=$doregex[tok]</rawpost>
<referer>http://diskokosmiko.mx/action/SearchFiles</referer>
<connection>keep-alive</connection>
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
<connection>keep-alive</connection>
<cookieJar></cookieJar>
</regex>



<regex>
<name>getUrl</name>
<expres>DownloadUrl":"([^"]+)<expres>
<page>http://diskokosmiko.mx/action/DownloadFile?location=fi&amp;f=[lista.param1]</page>
<rawpost>fileId=[lista.param2]&__RequestVerificationToken=$doregex[tok2]</rawpost>
<referer>http://diskokosmiko.mx[lista.param1]</referer>
<connection>keep-alive</connection>
<accept>*/*</accept>
<X-Req>XMLHttpRequest</X-Req>
<cookieJar></cookieJar>
</regex>

<regex>
<name>tok2</name>
<expres>DownloadFile.*RequestVerificationToken.*?value="([^"]+)<expres>
<page>http://diskokosmiko.mx[lista.param1]</page>
<referer>http://diskokosmiko.mx/adryanlist</referer>
<connection>keep-alive</connection>
<cookieJar></cookieJar>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
</item>








<item>
<title> [COLOR lime]•[/COLOR]    [COLOR aquamarine][B]ESTRENOS LATINOS [/COLOR][COLOR lightgreen]MAS RECIENTES[/COLOR]  [/B]</title>

<link>$doregex[makelist]</link>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>$pyFunction:'[COLOR deepskyblue][makelist.param1][/COLOR]'.replace("+", " ")</title>
<link>$doregex[id3]</link>
<thumbnail>https://image.tmdb.org/t/p/original/$doregex[imagen]</thumbnail>
<fanart>https://image.tmdb.org/t/p/original/$doregex[imagen]</fanart>
]]></listrepeat>
<expres><![CDATA[Estrenos:"(.*?)" url:"(.*?)" server:"(.*?)"]]></expres>
<page>http://adryanlist.org/adryan/estrenoslatinos.txt</page>
</regex>

<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
   import urlresolver
   url = '[makelist.param2]'
   try:
     u = urlresolver.resolve(url)
   except:
     u = 'http://adryanlist.org/error.mp4'
   return u
]]></expres>
<page></page>
</regex>

<regex>
<name>imagen</name>
<expres><![CDATA[poster_path\":\"\\/(.*?)\"]]></expres>
<page>https://api.themoviedb.org/3/search/movie?api_key=3d8a2c67653e2f8fd7dd09959e835f02&amp;language=es&amp;query=[makelist.param1]</page>
</regex>
</item>



<item>
<title> [COLOR lime]•[/COLOR]    [COLOR aquamarine][B]ESTRENOS LATINOS [/COLOR][COLOR aquamarine][/COLOR]  [/B]</title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/peliculas_favoritas.xml</externallink>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
</item>






<item>
<title> [COLOR lime]•[/COLOR]    [COLOR aquamarine][B]ESTRENOS ESPAÑA [/COLOR][COLOR lightgreen]MAS RECIENTES[/COLOR]  [/B]</title>

<link>$doregex[makelist]</link>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>$pyFunction:'[COLOR deepskyblue][makelist.param1][/COLOR]'.replace("_", " ")</title>
<link>$doregex[id3]</link>
<thumbnail>https://image.tmdb.org/t/p/original/$doregex[imagen]</thumbnail>
<fanart>https://image.tmdb.org/t/p/original/$doregex[imagen]</fanart>
]]></listrepeat>
<expres><![CDATA[EstrenosESP:"(.*?)" url:"(.*?)" server:"(.*?)"]]></expres>
<page>http://adryanlist.org/adryan/estrenoslatinos.txt</page>
</regex>

<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
   import urlresolver
   url = '[makelist.param2]'
   try:
     u = urlresolver.resolve(url)
   except:
     u = 'http://adryanlist.org/error.mp4'
   return u
]]></expres>
<page></page>
</regex>

<regex>
<name>imagen</name>
<expres><![CDATA[poster_path\":\"\\/(.*?)\"]]></expres>
<page>https://api.themoviedb.org/3/search/movie?api_key=3d8a2c67653e2f8fd7dd09959e835f02&amp;language=es&amp;query=$doregex[titulo]</page>
</regex>
<regex>
<name>titulo</name>
<expres>$pyFunction:'[makelist.param1]'.replace("_", "+")</expres>
<page></page>
</regex>


</item>



<item>
<title> [COLOR lime]•[/COLOR]    [COLOR aquamarine][B]ESTRENOS ESPAÑA | CASTELLANO [/COLOR][COLOR aquamarine][/COLOR]  [/B]</title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/favoritas_esp.xml</externallink>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
</item>






 <iem>
<title> [COLOR lime]•[/COLOR]    [COLOR aquamarine][B]ESTRENOS TORRENT  [/COLOR][COLOR skyblue] [/COLOR] [COLOR deepskyblue] - QUASAR REQUERIDO[/COLOR] [/B] </title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/quasar.xml</externallink>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>


 <item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightgreen][B]MOVIES [/COLOR][COLOR skyblue]PACK[/COLOR] [/B]</title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/moviepack.xml</externallink>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>




<item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightgreen][B]TAQUILLAS [/COLOR][COLOR skyblue]+[/COLOR] [/B]</title>
<link>$doregex[makelist3]</link>

<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>[COLOR skyblue][makelist3.param2][/COLOR]</title>
        <link>$doregex[makelist]</link>
        ]]></listrepeat>
<expres>peliculas:"(.*?)" name:"(.*?)";</expres>
<page>http://adryanlist.org/adryan/kozm.txt</page>
<cookieJar></cookieJar>
</regex>




<regex>
  <name>makelist</name>
  <listrepeat><![CDATA[
        <title> [makelist.param3]</title>
        <link>$doregex[getUrl]</link>
		<thumbnail>$doregex[poster]</thumbnail>
		<info>$doregex[plot]</info>
        ]]></listrepeat>
<expres><![CDATA[href="\/.*,(.*?),list.*\n.*\n.*\n.*href="\/([^"]*)".*?>(.*?)<]]></expres>
<page>[makelist3.param1]/list,1,15</page>
<cookieJar></cookieJar>
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
<referer>http://diskokosmiko.mx[makelist2.param1]/list,1,15</referer>
<connection>keep-alive</connection>
<cookieJar></cookieJar>
</regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
</item>











































































<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]ESTRENOS FULLHD[/B] [/COLOR][COLOR skyblue]AudioLatino[/COLOR] </title>
<link>$doregex[makelist]</link>

<regex><name>makelist</name>
<listrepeat><![CDATA[
          <title>[COLOR deepskyblue][makelist.param3][/COLOR]</title>
		  <link>$$LSPlayOnlyOne$$</link>
		  <link>$doregex[resolver2]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0&Referer=http://www.cinecalidad.com/pelicula/[makelist.param1]</link>
          <link>$doregex[resolver]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0&Referer=http://www.cinecalidad.com/pelicula/[makelist.param1]</link>
		  <thumbnail>[makelist.param2]</thumbnail>
   ]]></listrepeat>
<expres><![CDATA[>.*?<a href=".*?\/pelicula\/(.*?)".*?src="(.*?)".*?title="(.*?)"]]></expres>
<page>http://www.cinecalidad.com/</page>
<agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>




<regex><name>resolver</name>
<expres><![CDATA[#$pyFunction
import re ,requests
import urlresolver
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))

def GetLSProData(page_data,Cookie_Jar,m):

  values = re.search(r'service=="TheVideoMe"\)\{h=dec\("(.*?)"\)\+dec\("(.*?)"', page_data, re.DOTALL)
  var1=values.group(1)
  var2=values.group(2)
  var1+=''.join(' ')
  var1+=''.join(var2)
  str=var1
  d = "" ; str = str.split(" ")
  i=0
  for i in range(0,len(str)):
   pp=(parseint(str[i])-7)
   d+=''.join(unichr(pp))

  streamLink = urlresolver.resolve(d)
  return streamLink
]]></expres>
  <page>http://www.cinecalidad.com/pelicula/[makelist.param1]</page>
  <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>


<regex><name>resolver2</name>
<expres><![CDATA[#$pyFunction
import re ,requests
import urlresolver
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))

def GetLSProData(page_data,Cookie_Jar,m):

  values = re.search(r'service=="OnlineYourUpload"\)\{h=dec\("(.*?)"\)\+dec\("(.*?)"', page_data, re.DOTALL)
  var1=values.group(1)
  var2=values.group(2)
  var1+=''.join(' ')
  var1+=''.join(var2)
  str=var1
  d = "" ; str = str.split(" ")
  i=0
  for i in range(0,len(str)):
   pp=(parseint(str[i])-7)
   d+=''.join(unichr(pp))

  streamLink = urlresolver.resolve(d)
  return streamLink
]]></expres>
  <page>http://www.cinecalidad.com/pelicula/[makelist.param1]</page>
  <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]ESTRENOS FULLHD[/B] [/COLOR][COLOR aquamarine]Audio Castellano[/COLOR] </title>
<link>$doregex[makelist]</link>

<regex><name>makelist</name>
<listrepeat><![CDATA[
          <title>[COLOR deepskyblue][makelist.param3][/COLOR]</title>
		  <link>$$LSPlayOnlyOne$$</link>
		  <link>$doregex[resolver2]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0&Referer=http://www.cinecalidad.com/espana/pelicula/[makelist.param1]</link>
          <link>$doregex[resolver]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0&Referer=http://www.cinecalidad.com/espana/pelicula/[makelist.param1]</link>
		  <thumbnail>[makelist.param2]</thumbnail>
   ]]></listrepeat>
<expres><![CDATA[>.*?<a href=".*?\/pelicula\/(.*?)".*?src="(.*?)".*?title="(.*?)"]]></expres>
<page>http://www.cinecalidad.to/espana</page>
<agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>




<regex><name>resolver</name>
<expres><![CDATA[#$pyFunction
import re ,requests
import urlresolver
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))

def GetLSProData(page_data,Cookie_Jar,m):

  values = re.search(r'service=="TheVideoMe"\)\{h=dec\("(.*?)"\)\+dec\("(.*?)"', page_data, re.DOTALL)
  var1=values.group(1)
  var2=values.group(2)
  var1+=''.join(' ')
  var1+=''.join(var2)
  str=var1
  d = "" ; str = str.split(" ")
  i=0
  for i in range(0,len(str)):
   pp=(parseint(str[i])-7)
   d+=''.join(unichr(pp))

  streamLink = urlresolver.resolve(d)
  return streamLink
]]></expres>
  <page>http://www.cinecalidad.to/espana/pelicula/[makelist.param1]</page>
  <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>



<regex><name>resolver2</name>
<expres><![CDATA[#$pyFunction
import re ,requests
import urlresolver
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))

def GetLSProData(page_data,Cookie_Jar,m):

  values = re.search(r'service=="OnlineYourUpload"\)\{h=dec\("(.*?)"\)\+dec\("(.*?)"', page_data, re.DOTALL)
  var1=values.group(1)
  var2=values.group(2)
  var1+=''.join(' ')
  var1+=''.join(var2)
  str=var1
  d = "" ; str = str.split(" ")
  i=0
  for i in range(0,len(str)):
   pp=(parseint(str[i])-7)
   d+=''.join(unichr(pp))

  streamLink = urlresolver.resolve(d)
  return streamLink
]]></expres>
  <page>http://www.cinecalidad.to/espana/pelicula/[makelist.param1]</page>
  <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]FULLHD[/B] [/COLOR][COLOR skyblue](GENEROS)  [Latino][/COLOR] </title>



<link>$doregex[makelist3]</link>


<regex>
   <name>makelist3</name>
   <listrepeat><![CDATA[
       <title>[makelist3.param1]</title>

    <link>$doregex[makelist2]</link>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
   ]]></listrepeat>
   <expres>genero-peliculas\/(.*?)\/</expres>
   <page>http://www.cinecalidad.to/</page>
 <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
   <cookieJar></cookieJar>
</regex>





<regex>
   <name>makelist2</name>
   <listrepeat><![CDATA[
       <title>Page [makelist2.param1]</title>

    <link>$doregex[makelist]</link>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
   ]]></listrepeat>
   <expres><![CDATA[paginado:"(.*?)";]]></expres>
   <page>http://adryanlist.org/adryan/kozm.txt</page>
   <cookieJar></cookieJar>
</regex>



<regex><name>makelist</name>
<listrepeat><![CDATA[
          <title>[COLOR deepskyblue][makelist.param3][/COLOR]</title>
		  <link>$$LSPlayOnlyOne$$</link>
		  <link>$doregex[resolver2]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0&Referer=http://www.cinecalidad.com/pelicula/[makelist.param1]</link>
          <link>$doregex[resolver]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0&Referer=http://www.cinecalidad.com/pelicula/[makelist.param1]</link>
		  <thumbnail>[makelist.param2]</thumbnail>
   ]]></listrepeat>
<expres><![CDATA[>.*?<a href=".*?\/pelicula\/(.*?)".*?src="(.*?)".*?title="(.*?)"]]></expres>
<page>http://www.cinecalidad.to/genero-peliculas/[makelist3.param1]/page/[makelist2.param1]/</page>
<agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>




<regex><name>resolver</name>
<expres><![CDATA[#$pyFunction
import re ,requests
import urlresolver
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))

def GetLSProData(page_data,Cookie_Jar,m):

  values = re.search(r'service=="TheVideoMe"\)\{h=dec\("(.*?)"\)\+dec\("(.*?)"', page_data, re.DOTALL)
  var1=values.group(1)
  var2=values.group(2)
  var1+=''.join(' ')
  var1+=''.join(var2)
  str=var1
  d = "" ; str = str.split(" ")
  i=0
  for i in range(0,len(str)):
   pp=(parseint(str[i])-7)
   d+=''.join(unichr(pp))

  streamLink = urlresolver.resolve(d)
  return streamLink
]]></expres>
  <page>http://www.cinecalidad.com/pelicula/[makelist.param1]</page>
  <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>



<regex><name>resolver2</name>
<expres><![CDATA[#$pyFunction
import re ,requests
import urlresolver
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))

def GetLSProData(page_data,Cookie_Jar,m):

  values = re.search(r'service=="OnlineYourUpload"\)\{h=dec\("(.*?)"\)\+dec\("(.*?)"', page_data, re.DOTALL)
  var1=values.group(1)
  var2=values.group(2)
  var1+=''.join(' ')
  var1+=''.join(var2)
  str=var1
  d = "" ; str = str.split(" ")
  i=0
  for i in range(0,len(str)):
   pp=(parseint(str[i])-7)
   d+=''.join(unichr(pp))

  streamLink = urlresolver.resolve(d)
  return streamLink
]]></expres>
  <page>http://www.cinecalidad.com/pelicula/[makelist.param1]</page>
  <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>












<itm>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]FULLHD[/B] [/COLOR][COLOR skyblue](GENEROS)  [Castellano][/COLOR] </title>



<link>$doregex[makelist3]</link>


<regex>
   <name>makelist3</name>
   <listrepeat><![CDATA[
       <title>[makelist3.param1]</title>

    <link>$doregex[makelist2]</link>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
   ]]></listrepeat>
   <expres>genero-peliculas\/(.*?)\/</expres>
   <page>http://www.cinecalidad.to/espana/</page>
 <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
   <cookieJar></cookieJar>
</regex>





<regex>
   <name>makelist2</name>
   <listrepeat><![CDATA[
       <title>Page [makelist2.param1]</title>

    <link>$doregex[makelist]</link>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
   ]]></listrepeat>
   <expres><![CDATA[paginado:"(.*?)";]]></expres>
   <page>http://adryanlist.org/adryan/kozm.txt</page>
   <cookieJar></cookieJar>
</regex>



<regex><name>makelist</name>
<listrepeat><![CDATA[
          <title>[COLOR deepskyblue][makelist.param3][/COLOR]</title>
		  <link>$$LSPlayOnlyOne$$</link>
		  <link>$doregex[resolver2]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0&Referer=http://www.cinecalidad.com/espana/pelicula/[makelist.param1]</link>
          <link>$doregex[resolver]|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0&Referer=http://www.cinecalidad.com/espana/pelicula/[makelist.param1]</link>
		  <thumbnail>[makelist.param2]</thumbnail>
   ]]></listrepeat>
<expres><![CDATA[>.*?<a href=".*?\/pelicula\/(.*?)".*?src="(.*?)".*?title="(.*?)"]]></expres>
<page>http://www.cinecalidad.to/espana/genero-peliculas/[makelist3.param1]/page/[makelist2.param1]/</page>
<agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>




<regex><name>resolver</name>
<expres><![CDATA[#$pyFunction
import re ,requests
import urlresolver
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))

def GetLSProData(page_data,Cookie_Jar,m):

  values = re.search(r'service=="TheVideoMe"\)\{h=dec\("(.*?)"\)\+dec\("(.*?)"', page_data, re.DOTALL)
  var1=values.group(1)
  var2=values.group(2)
  var1+=''.join(' ')
  var1+=''.join(var2)
  str=var1
  d = "" ; str = str.split(" ")
  i=0
  for i in range(0,len(str)):
   pp=(parseint(str[i])-7)
   d+=''.join(unichr(pp))

  streamLink = urlresolver.resolve(d)
  return streamLink
]]></expres>
  <page>http://www.cinecalidad.com/espana/pelicula/[makelist.param1]</page>
  <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>



<regex><name>resolver2</name>
<expres><![CDATA[#$pyFunction
import re ,requests
import urlresolver
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))

def GetLSProData(page_data,Cookie_Jar,m):

  values = re.search(r'service=="OnlineYourUpload"\)\{h=dec\("(.*?)"\)\+dec\("(.*?)"', page_data, re.DOTALL)
  var1=values.group(1)
  var2=values.group(2)
  var1+=''.join(' ')
  var1+=''.join(var2)
  str=var1
  d = "" ; str = str.split(" ")
  i=0
  for i in range(0,len(str)):
   pp=(parseint(str[i])-7)
   d+=''.join(unichr(pp))

  streamLink = urlresolver.resolve(d)
  return streamLink
]]></expres>
  <page>http://www.cinecalidad.com/espana/pelicula/[makelist.param1]</page>
  <agent>Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0</agent>
<cookieJar></cookieJar></regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>


















  <iem>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]ExaByte Movies[/B] [/COLOR][COLOR skyblue][I] Recientes[/I][/COLOR] </title>
<link>http://ignora.me</link>
<externallink>http://exabytetv.info/peliculas.m3u</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<info></info>
</item>













































<iem>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]MetaCINE[/B] [/COLOR][COLOR skyblue] [ESTRENOS - Audio Latino]  [/COLOR] -  [COLOR lime] [/COLOR] </title>
<link>$doregex[makelist5]</link>
<regex>
   <name>makelist5</name>
   <listrepeat><![CDATA[
       <title>Pagina [makelist5.param1]</title>
       <link>$doregex[makelist4]</link>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
   ]]></listrepeat>
   <expres><![CDATA[paginado:"(.*?)";]]></expres>
   <page>http://adryanlist.org/adryan/kozm.txt</page>
   <cookieJar></cookieJar>
</regex>

<regex>
<name>makelist4</name>
<listrepeat><![CDATA[
<title>[makelist4.param2]</title>
<link>$doregex[makelist]</link>
<info>[makelist4.param3]</info>
<fanart>[makelist4.param4]</fanart>
<thumbnail>[makelist4.param4]</thumbnail>
]]></listrepeat>
<expres>href="(.*?)"[\w\W\s]{0,3}title="(.*?)"[\w\W\s]{0,35}span>(.*?)[\w\W\s]{0,50}src="(.*?)"</expres>
<page>http://metacine.net/explorar/page/[makelist5.param1]/</page>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist4.param2]   -- server:[makelist.param3] - idioma: [makelist.param1]</title>
 <link>$doregex[id3]</link>
<info>[makelist4.param3]</info>
<fanart>[makelist4.param4]</fanart>
<thumbnail>[makelist4.param4]</thumbnail>
]]></listrepeat>
<expres>img\/(.*?).png[\w\W\s]{0,80}domain=(.*?)".*?nbsp;(.*?)<</expres>
<page>[makelist4.param1]</page>
</regex>


<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '[makelist.param2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>




<itm>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]MetaCINE[/B] [/COLOR][COLOR skyblue] [CATEGORIAS]  [/COLOR]  [COLOR lime] [/COLOR] </title>
<link>$doregex[makelist0]</link>

<regex>
<name>makelist0</name> categories list
<listrepeat><![CDATA[
   <title>[COLOR skyblue] [makelist0.param2][/COLOR]</title>
   <link>$doregex[makelist]</link>
]]></listrepeat>
<expres><![CDATA[value="(.*?)">(.*?)<]]></expres>
<page>http://metacine.net/explorar/</page>
<agent>Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1</agent>
<cookieJar></cookieJar>
</regex>


<regex>
    <name>makelist</name> movies  (all pages)
 <listrepeat><![CDATA[
   <title>[COLOR dodgerblue] [makelist.param2][/COLOR]</title>
   <link>$doregex[makelist2]</link>
   <thumbnail>[makelist.param4]</thumbnail>
   <info>[makelist.param3]</info>
]]></listrepeat>
<expres><![CDATA[#$pyFunction
import re, requests
def GetLSProData(page_data,Cookie_Jar,m):

################################################################## FORMULARY #################################################################
 starturl = 'http://metacine.net/category/'     ### usually, ~ 'http://website.com/category/' ###
 categorylink = '[makelist0.param2]' ### check the number of the param ###
 centerurl = '/page/'      ### something like  '/page/' ###
 firstpage = 1 ### probably  = 1 ###
 endurl = '' ### can be empty ###    ### endurl without final / (SLASH) ###
#
 dataregex = 'poster[\w\W\s]{0,8}href="(.*?)"\stitle="(.*?)"[\w\W\s]{0,32}span>(.*?)<[\w\W\s]{0,45}src="(.*?)"'      ### To adapt ###
 headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0', 'Referer': ''}      ### To adapt ###
##############################################################################################################################################

############################## GENERIC PART #####################################
 fullurl = starturl + categorylink + centerurl + str(firstpage) + endurl #
 source = requests.get(fullurl, headers= headers).text #
 data = [] #
#
 last = 10 #
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
<title>[makelist.param2] - server:[makelist2.param3] - idioma: [makelist2.param1]   </title>
 <link>$doregex[id3]</link>
]]></listrepeat>
<expres>img\/(.*?).png[\w\W\s]{0,80}domain=(.*?)".*?nbsp;(.*?)<</expres>
<page>[makelist.param1]</page>
</regex>
<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '[makelist2.param2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>

















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]MIRATODO[/B] [/COLOR][COLOR skyblue] Estrenos  [/COLOR] </title>
<link>$doregex[makelist0]</link>


<regex>
    <name>makelist0</name> movies  (all pages)
 <listrepeat><![CDATA[
   <title>[COLOR skyblue] [makelist0.param3][/COLOR]</title>
   <link>$doregex[makelist2]</link>
   <thumbnail>[makelist0.param2]</thumbnail>
<fanart>[makelist0.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[#$pyFunction
import re, requests
def GetLSProData(page_data,Cookie_Jar,m):

################################################################## FORMULARY #################################################################
 starturl = 'http://miradetodo.io/'     ### usually, ~ 'http://website.com/category/' ###
 categorylink = '?s' ### check the number of the param ###
 centerurl = 'page/'      ### something like  '/page/' ###
 firstpage = 1 ### probably  = 1 ###
 endurl = '/' ### can be empty ###    ### endurl without final / (SLASH) ###
#
 dataregex = 'href="(.*?)"[\w\W\s]{0,30}src="(.*?)".*?alt="(.*?)(?<!MiraDeTodo)"'      ### To adapt ###
 headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0', 'Referer': ''}      ### To adapt ###
##############################################################################################################################################

############################## GENERIC PART #####################################
 fullurl = starturl + centerurl + str(firstpage) + endurl + categorylink #
 source = requests.get(fullurl, headers= headers).text #
 data = [] #
#
 last = 15 #
 while firstpage <= last: #
    try: #
        fullurl = starturl + centerurl + str(firstpage) + endurl + categorylink #
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
<title>$pyFunction:'[COLOR skyblue][makelist0.param3]   idioma:[makelist2.param1][/COLOR]'.replace("div2", "Subtitulado").replace("div3", "Latino").replace("div0", "Subtitulado")</title>
<link>$doregex[makelist3]</link>
   <thumbnail>[makelist0.param2]</thumbnail>
<fanart>[makelist0.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[id="(div.*?)".*?data-lazy-src="(.*?)"]]></expres>
<page>[makelist0.param1]</page>
</regex>



<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR skyblue][makelist0.param3][/COLOR]   Server:[B][COLOR deepskyblue][makelist3.param2] - url:[makelist3.param1]  [makelist3.param3][/COLOR][/B]</title>
<link>$doregex[id3]</link>
   <thumbnail>[makelist0.param2]</thumbnail>
<fanart>[makelist0.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[api\/(streamango.*?id=(.*?)\&sub[\w\W\s]{0,190}span>(.*?)<]]></expres>
<page>[makelist2.param2]</page>

</regex>





<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[uno]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<regex>
<name>uno</name>
<expres>$pyFunction:base64.b64decode('[makelist3.param1]')</expres>
<page></page>
</regex>


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>








<iem>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]MIRATODO[/B] [/COLOR][COLOR skyblue] Categorias   [/COLOR] </title>
<link>$doregex[lista]</link>

<regex>
<name>lista</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[lista.param2]</title>
<link>$doregex[makelist0]</link>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
]]></listrepeat>
<expres><![CDATA[category\/(.*?)\/"\s>(.*?)<]]></expres>
<page>http://miradetodo.io/</page>
</regex>



comedia/page/3/

<regex>
    <name>makelist0</name> movies  (all pages)
 <listrepeat><![CDATA[
   <title>[COLOR skyblue] [makelist0.param3][/COLOR]</title>
   <link>$doregex[makelist2]</link>
   <thumbnail>[makelist0.param2]</thumbnail>
<fanart>[makelist0.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[#$pyFunction
import re, requests
def GetLSProData(page_data,Cookie_Jar,m):

################################################################## FORMULARY #################################################################
 starturl = 'http://miradetodo.io/category/'     ### usually, ~ 'http://website.com/category/' ###
 categorylink = '[lista.param1]' ### check the number of the param ###
 centerurl = '/page/'      ### something like  '/page/' ###
 firstpage = 1 ### probably  = 1 ###
 endurl = '/' ### can be empty ###    ### endurl without final / (SLASH) ###
#
 dataregex = 'item\".*?href="(.*?)"[\w\W\s]{0,30}src="(.*?)".*?alt="(.*?)"'      ### To adapt ###
 headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0', 'Referer': ''}      ### To adapt ###
##############################################################################################################################################

############################## GENERIC PART #####################################
 fullurl = starturl + categorylink + centerurl + str(firstpage) + endurl #
 source = requests.get(fullurl, headers= headers).text #
 data = [] #
#
 last = 15 #
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
<title>$pyFunction:'[COLOR skyblue][makelist0.param3]   idioma:[makelist2.param1][/COLOR]'.replace("div2", "Subtitulado").replace("div3", "Latino").replace("div0", "Subtitulado")</title>
<link>$doregex[makelist3]</link>
   <thumbnail>[makelist0.param2]</thumbnail>
<fanart>[makelist0.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[id="(div.*?)".*?data-lazy-src="(.*?)"]]></expres>
<page>[makelist0.param1]</page>
</regex>


<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR skyblue][makelist0.param3][/COLOR]   Server:[B][COLOR deepskyblue][makelist3.param2][/COLOR][/B]</title>
<link>$doregex[id3]</link>
   <thumbnail>[makelist0.param2]</thumbnail>
<fanart>[makelist0.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[.*?id=(.*?)\&[\w\W\s]{0,190}span>(.*?)<]]></expres>
<page>[makelist2.param2]</page>
</regex>



<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[uno]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<regex>
<name>uno</name>
<expres>$pyFunction:base64.b64decode('[makelist3.param1]')</expres>
<page></page>
</regex>


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>










 <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]EMULELAND[/B] [/COLOR][COLOR skyblue] | ESTRENOS | BUSCADOR | GENEROS | CALIDAD | [/COLOR]  </title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/emuleland.xml</externallink>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>








   <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]CINEVALL[/B] [/COLOR][COLOR skyblue] ESTRENOS [Audio Latino][/COLOR]  </title>

  <link>$doregex[makelist3]</link>


   <regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[makelist3.param2]</title>
 <link>$doregex[finalURL]|User-Agent=iPad</link>
 <regex>
<name>finalURL</name>
<expres>file: '(.*?)'</expres>
<page>http://cine.cinevall.club/[makelist3.param1].php</page>
</regex>
<thumbnail>http://www.cinevall.club/[makelist3.param3]</thumbnail>
 </item>
]]></listrepeat>
<expres>href="(.*?).html.*?text:\s\'(.*?)\&.*?src="(.*?)"</expres>
<page>http://www.cinevall.club</page>
</regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
 </item>









	
	
	
<iem>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Especial Fin de Año[/B] [/COLOR][COLOR skyblue][I] Karaoke [/I][/COLOR] </title>

 <link>$doregex[makelist2]</link>

 
 
<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>$pyFunction:'[COLOR skyblue][B][makelist2.param1][/B][/COLOR]'.replace("%20", " ").replace("-", " [COLOR aquamarine]").replace(".", "[/COLOR]").replace("avi", " ").replace("mp4", " ").replace("_", " ")</title>
 <link>http://www.karaokesolution.com/SongLists/Spanish/CDG/1/[makelist2.param1]</link>
 <thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
]]></listrepeat>
<expres><![CDATA[td><a href="(.*?)"]]></expres>
<page>$doregex[select]</page>
</regex>

 <regex>
<name>select</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
   import xbmcgui
   dialog = xbmcgui.Dialog()
   ret = dialog.select('Elige tu Cancion y Canta ', ['A-C', 'C-D', 'D-E', 'E-L', 'L-M', 'M-N', 'N-Z', 'Ingles'])
   lists = ['http://www.karaokesolution.com/SongLists/Spanish/CDG/1/', 'http://www.karaokesolution.com/SongLists/Spanish/CDG/2/', 'http://www.karaokesolution.com/SongLists/Spanish/CDG/3/', 'http://www.karaokesolution.com/SongLists/Spanish/CDG/4/', 'http://www.karaokesolution.com/SongLists/Spanish/CDG/5/', 'http://www.karaokesolution.com/SongLists/Spanish/CDG/6/', 'http://www.karaokesolution.com/SongLists/Spanish/CDG/7/', 'http://www.karaokesolution.com/SongLists/English/']
   return lists[ret]
]]></expres>
<page></page>
</regex>



<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
 </item>


	
	
	
	
	
	


<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]BASSFOX WEB[/B] [/COLOR][COLOR skyblue][I] Estrenos [/I][/COLOR] </title>
 <link>$doregex[makelist2]</link>
 
   <regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist2.param2] [/COLOR]  [COLOR lightslategray][/COLOR]</title>
 <link>$doregex[makelist3]</link>
 <fanart>[makelist2.param1]</fanart>
  <info>[makelist2.param4]</info>
  <thumbnail>[makelist2.param1]</thumbnail>
]]></listrepeat>
<expres><![CDATA[poster[\w\W\s]{0,15}src="(.*?)" alt="(.*?)"[\w\W\s]{0,150}href="(.*?)"[\w\W\s]{0,550}texto">(.*?)<]]></expres>
<page>http://bassfox.org/movies/</page>
</regex>
	
	
 


		
		
		
		
  <regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue][makelist2.param2][/COLOR]      Server:[makelist3.param1]</title>
 <link>$doregex[id3]</link>
 <fanart>[makelist2.param1]</fanart>
  <info>[makelist2.param4]</info>
  <thumbnail>[makelist2.param1]</thumbnail>
]]></listrepeat>
<expres><![CDATA[src=\"(https://streamango.*?|http://xvidstage.*?|http://uptobox.*?|https://openload.*?|https://userscloud.*?|https://ok.*?|https://uptostream.*?)"]]></expres>
 <page>[makelist2.param3]</page>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
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


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
 </item>



 
 
 


<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]BASSFOX WEB[/B] [/COLOR][COLOR skyblue][I] Categorias[/I][/COLOR] </title>
 <link>$doregex[makelist1]</link>

 <regex>
<name>makelist1</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist1.param2]   [COLOR lightyellow][[makelist1.param3]][/COLOR][/COLOR]</title>
 <link>$doregex[makelist2]</link>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
]]></listrepeat>
<expres><![CDATA[org\/genre\/(.*?)\"\s>(.*?)<.*?i>(.*?)<]]></expres>
 <page>http://bassfox.org/movies</page>
</regex>




   <regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist2.param4] [/COLOR]  [COLOR lightslategray][makelist2.param1][/COLOR]</title>
 <link>$doregex[makelist3]</link>
 <fanart>[makelist2.param3]</fanart>
  <info>[makelist2.param2]</info>
  <thumbnail>[makelist2.param3]</thumbnail>
]]></listrepeat>
<expres><![CDATA[metadata[\w\W\s]{0,10}span>([0-9]+)<[\w\W\s]{0,80}texto">(.*?)<[\w\W\s]{0,350}poster[\w\W\s]{0,12}src="(.*?)"[\w\W\s]{0,2}alt="(.*?)"[\w\W\s]{0,150}href="(.*?)"]]></expres>
 <page>http://bassfox.org/genre/[makelist1.param1]</page>

</regex>



<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue][makelist2.param4][/COLOR]      Server:[makelist3.param1]</title>
 <link>$doregex[id3]</link>
 <fanart>[makelist2.param3]</fanart>
 <info>[makelist2.param2]</info>
 <thumbnail>[makelist2.param3]</thumbnail>
]]></listrepeat>
<expres><![CDATA[src=\"(https://streamango.*?|http://xvidstage.*?|http://uptobox.*?|https://openload.*?|https://userscloud.*?|https://ok.*?|https://uptostream.*?)"]]></expres>
 <page>[makelist2.param5]</page>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
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


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
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


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
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


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
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

 <thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>

















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

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>

















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]LACAJITA[/B] [/COLOR][COLOR skyblue]Estrenos [COLOR skyblue]   [/COLOR] </title>
<link>$doregex[makelist0]</link>






<regex>
<name>makelist0</name>
<listrepeat><![CDATA[
<SetwatchMode>55</SetwatchMode>
<title>[makelist0.param3]</title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist0.param2]</thumbnail>
]]></listrepeat>
<expres><![CDATA[href='(.*?)'[\w\W\s]{0,60}src='(.*?)' title='(.*?)']]></expres>
<page>http://lacajita.xyz/$doregex[select]</page>
<referer>http://lacajita.xyz</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>

 <regex>
<name>select</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
   import xbmcgui
   dialog = xbmcgui.Dialog()
   ret = dialog.select('Elige un Liga ', ['Estrenos DVD Español', 'Estrenos DVD Latinos', 'Estrenos DVD Subtitulados', 'Estrenos Español', 'Estrenos Latinos', 'Estrenos Subtitulados', 'Peliculas Actualizadas'])
   lists = ['estrenos-dvd/es/', 'estrenos-dvd/la/', 'estrenos-dvd/vos/', 'estrenos/es/', 'estrenos/la/', 'estrenos/vos/', 'actualizado/']
   return lists[ret]
]]></expres>
<page></page>
</regex>
<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://www.seehd.ws',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>




<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<SetwatchMode>55</SetwatchMode>
<title>[makelist0.param3] - idioma:[makelist.param3]- [makelist.param2]</title>
<link>$doregex[id3]</link>
<thumbnail>[makelist0.param2]</thumbnail>
]]></listrepeat>
<expres><![CDATA[href="(.*?)"[\w\W\s]{0,50}servidores\/(openlo.*?|streamcl.*?|powv.*?|gamov.*?|flash.*?)\.[\w\W\s]{0,670}banderas/(.*?).png]]></expres>
<page>http://lacajita.xyz[makelist0.param1]</page>
<referer>http://lacajita.xyz</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>
<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://www.seehd.ws',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>



<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[link]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<regex>
<name>link</name>
<expres>window.open\(\"(.*?)"</expres>
<page>http://lacajita.xyz[makelist.param1]</page>
<referer>http://lacajita.xyz</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>
<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://www.seehd.ws',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>












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


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
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

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>











































  <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]BassFox Movies[/B] [/COLOR][COLOR skyblue][I] Estrenos[/I][/COLOR] </title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/estrenosbassfox.xml</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<info></info>
</item>





  <iem>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]TotalShow Movies[/B] [/COLOR][COLOR skyblue][I]  [/I][/COLOR] </title>
<link>http://ignora.me</link>
<externallink>https://pastebin.com/raw/qkdjae9e</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<info></info>
</item>


<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Peliculas Gratis[/B] [/COLOR][COLOR skyblue][I]  [/I][/COLOR] </title>
<link>http://ignora.me</link>
<externallink>https://pastebin.com/raw/TA8pPbGY</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<info></info>
</item>


  <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Peliculas Sr.Regio[/B] [/COLOR][COLOR skyblue][I]  [/I][/COLOR] </title>
<link>http://ignora.me</link>
<externallink>http://srregio.xyz/regioflix.m3u</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<info></info>
</item>

  <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Peliculas TecnoTV[/B] [/COLOR][COLOR skyblue][I]  [/I][/COLOR] </title>
<link>http://ignora.me</link>
<externallink>http://tecnotv.xyz/peliculas.m3u</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<info></info>
</item>


   <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Peliculas CeceGeek[/B] [/COLOR][COLOR skyblue][I]  [/I][/COLOR] </title>
<link>http://ignora.me</link>
<externallink>http://cecegeek.com/movies.m3u</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<info></info>
</item>











 <item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]WATCHFREE[/B]  [/COLOR][COLOR blue]New Releases VO[/COLOR] </title>
<link>$doregex[makelist2]</link>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
   <title>[COLOR deepskyblue] [makelist2.param2][/COLOR]</title>
    <link>$doregex[makelist]</link>
 <thumbnail>http:[makelist2.param4]</thumbnail>
<fanart>http:[makelist2.param4]</fanart>
]]></listrepeat>
<expres><![CDATA[href="(.*?)"[\w\W\s]{0,15}Putlocker(.*?)">(.*?)<[\w\W\s]{0,4}src="(.*?)"]]></expres>
<page>http://www.gowatchfreemovies.to/
</page>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[makelist2.param3]    [COLOR lightslategray]server:[makelist.param3] [/COLOR] </title>
<link>$doregex[id3]</link>
 <thumbnail>http:[makelist2.param4]</thumbnail>
<fanart>http:[makelist2.param4]</fanart>
]]></listrepeat>
<expres>gtfo=(.*?)&amp;t.*?title="(.*?)".*?host\',\s\'(.*?)\'</expres>
<page>http://www.gowatchfreemovies.to[makelist2.param1]</page>
</regex>


<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[id2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

   <regex>
<name>id2</name>
<expres>$pyFunction:base64.b64decode('[makelist.param1]')</expres>
<page></page>
</regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>
















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]PRIMEWIRE[/B]  [/COLOR][COLOR blue]Featured VO[/COLOR] </title>
<link>$doregex[makelist2]</link>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
   <title>[COLOR deepskyblue] [makelist2.param2][/COLOR]</title>
    <link>$doregex[makelist]</link>
 <thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[href="watch-(.*?html)"[\w\W\s]{0,9}title="(.*?)"[\w\W\s]{0,6}src="(.*?)"]]></expres>
<page>http://www.primewire.ch/?sort=featured</page>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param2]    [COLOR lightslategray]server:[makelist.param3] [/COLOR] </title>
<link>$doregex[id3]</link>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[movie_version_link.*?href="(.*?)"\stitle="(.*?)"[\w\W\s]{0,145}version_host\">(.*?)<]]></expres>
<page>http://www.primewire.ch/watch-[makelist2.param1]</page>
</regex>



<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[id2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<regex>
<name>id2</name>
<expres>$pyFunction:base64.b64decode('$doregex[id1]')</expres>
<page></page>
</regex>

<regex>
<name>id1</name>
<expres>url=(.*?)&amp;d</expres>
<page>[makelist.param1]</page>
</regex>




<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>


</item>





 <item>
 <title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]SEEHD CLUB[/B]  [/COLOR][COLOR skyblue]  VO   [/COLOR] </title>


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
   <title>[makelist2.param3] </title>
 <link>$doregex[makelist3]</link>
  <thumbnail>[makelist2.param2]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[entry-header[\w\W\s]{0,2}data-url="(.*?)"[\w\W\s]{0,50}src="(.*?jpg)\"[\w\W\s]{0,652}bookmark\"><p>(.*?)Watch]]></expres>
<page>http://www.seehd.ws/category/movies/page/[makelist0.param1]/</page>
<referer>http://www.seehd.ws/</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>
<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://www.seehd.ws',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>






 <regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR skyblue] [makelist2.param3]  - [COLOR lightyellow] server:[makelist3.param1] [/COLOR] [/COLOR]</title>
<link>$doregex[id3]</link>
 <thumbnail>[makelist2.param2]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[=\"(http://gamovideo.*?|https://vidoza.*?|https://kingvid.*?|https://openload.*?|https://streamango.*?|http://streamin.*?|http://streamcloud.*?|http://uptobox.*?|https://rapidvideo.*?)"]]></expres>
<page>[makelist2.param1]</page>
<referer>http://www.seehd.ws</referer>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>

<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://www.seehd.ws',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
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


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>

</item>




















<item>
 <title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]HEVC MOVIES[/B]  [/COLOR][COLOR skyblue]  VO   [/COLOR] </title>
<link>$doregex[makelist2]</link>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
   <title>[makelist2.param2] </title>
 <link>$doregex[makelist3]</link>
  <thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[href="(.*?)".*?title="(.*?)HEVC.*?src="(.*?)".*?alt="(.*?)"]]></expres>
<page>http://hevcbluray.info/category/$doregex[select]/</page>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>
<regex>
<name>select</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
   import xbmcgui
   dialog = xbmcgui.Dialog()
   ret = dialog.select('Elige un un Genero ', ['Hollywood Movies', 'HEVC Movies', 'Dual Audio', 'TV Shows', 'TOP 20'])
   lists = ['hollywood-movies', 'english-hevc-movies', 'english-movies-dual-audio', 'tv-shows', 'imdb-top-250-movies']
   return lists[ret]
]]></expres>
<page></page>
</regex>


 <regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://hevcbluray.info',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>



 <regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR skyblue] [makelist2.param2]  - [COLOR lightyellow] server:[makelist3.param2] [/COLOR] [/COLOR]</title>
<link>$doregex[id3]</link>
 <thumbnail>[makelist2.param2]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[href=\"(http://vidto.*?|https://openload.*?|http://www.nowvideo.*?|http://uptobox.*?)\">(.*)<]]></expres>
<page>[makelist2.param1]</page>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>


<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://hevcbluray.info',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
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


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>

</item>














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
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
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
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>







 <itm>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]UltraPeliculas HD[/B] [/COLOR][COLOR skyblue]Estrenos[/COLOR] </title>
<link>$doregex[makelist2]</link>

<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[makelist2.param3]</title>
<link>$doregex[makelist]</link>
<fanart>[makelist2.param2]</fanart>
<thumbnail>[makelist2.param2]</thumbnail>
]]></listrepeat>
<expres>poster[\w\W\s]{0,10}href="(.*?)"[\w\W\s]{0,7}src="(.*?)"[\w\W\s]{0,3}alt="(.*?)"</expres>
<page> </page>
</regex>

<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param3]   server:openload/[makelist.param1]</title>
<urlsolve>https://openload.co/embed/[makelist.param1]</urlsolve>
<fanart>[makelist2.param2]</fanart>
<thumbnail>[makelist2.param2]</thumbnail>
]]></listrepeat>
<expres>openload.co\/embed\/(.*?)"</expres>
<page>[makelist2.param1]</page>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>



 <itm>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]UltraPeliculas HD[/B] [/COLOR][COLOR skyblue]Estrenos + [/COLOR] </title>
<link>$doregex[makelist2]</link>

<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[makelist2.param3]</title>
<link>$doregex[makelist]</link>
<fanart>[makelist2.param2]</fanart>
<thumbnail>[makelist2.param2]</thumbnail>
]]></listrepeat>
<expres>poster[\w\W\s]{0,10}href="(.*?)"[\w\W\s]{0,7}src="(.*?)"[\w\W\s]{0,3}alt="(.*?)"</expres>
<page>http://www.ultrapeliculashd.com/genre/estrenos/</page>
</regex>

<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param3]   server:openload/[makelist.param1]</title>
<link>$doregex[link]</link>
<fanart>[makelist2.param2]</fanart>
<thumbnail>[makelist2.param2]</thumbnail>
]]></listrepeat>
<expres>src="(.*?stream.*?)"</expres>
<page>[makelist2.param1]</page>
</regex>


<regex>
<name>link</name>
<expres>file:'(.*?)'</expres>
<page>$doregex[link2]</page>
</regex>

<regex>
<name>link2</name>
<expres>iframe src="(.*?)"</expres>
<page>[makelist.param1]</page>
</regex>


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>





<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Pelis24[/B] [/COLOR][COLOR skyblue]Estrenos[/COLOR]</title>

 <link>$doregex[makelist3]</link>



<regex>
   <name>makelist3</name>
   <listrepeat><![CDATA[
       <title>Pagina [makelist3.param1]</title>
        <link>$doregex[makelist0]</link>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
   ]]></listrepeat>
   <expres><![CDATA[paginado:"(.*?)";]]></expres>
   <page>http://adryanlist.org/adryan/kozm.txt</page>
   <cookieJar></cookieJar>
</regex>





<regex>
<name>makelist0</name>
<listrepeat><![CDATA[
    <title>[COLOR skyblue][makelist0.param2][/COLOR]</title>
    <link>$doregex[makelist]</link>
	<fanart>[makelist0.param1]</fanart>
<thumbnail>[makelist0.param1]</thumbnail>
]]></listrepeat>
<expres><![CDATA[img-box[\w\W\s]{0,12}src="(.*?)"[\w\W\s]{0,7}Ver(.*?)online[\w\W\s]{0,60}href="(.*?)"]]></expres>
<page>http://pelis24.com/estrenos/page/[makelist3.param1]/</page>
<referer></referer>
<cookieJar></cookieJar>
</regex>

<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue][makelist0.param2]    [COLOR lightslategray] server: [makelist.param1][/COLOR][/COLOR]</title>
<urlsolve>[makelist.param1]</urlsolve>
	<fanart>[makelist0.param1]</fanart>
<thumbnail>[makelist0.param1]</thumbnail>
]]></listrepeat>
<expres><![CDATA[data-src="(https.*?)"]]></expres>
<page>[makelist0.param3]</page>
</regex>




<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>











 <iem>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Yaske[/B] [/COLOR][COLOR skyblue][I] Recientes[/I][/COLOR] </title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/yaske.xml</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
<info></info>
</item>







 <itm>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]inkaPelis[/B] [/COLOR][COLOR skyblue] Estrenos | Generos[/COLOR] </title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/inka.xml</externallink>
<fanart>http://fotonin.com/data_images/out/5/776482-cool-movie-wallpaper.jpg</fanart>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
</item>






<itm>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]PelisRey[/B] [/COLOR][COLOR skyblue]por IDIOMA[/COLOR]</title>
<link>$doregex[makelist3]</link>

<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist3.param1] [/COLOR] </title>
<link>$doregex[makelist2]</link>
]]></listrepeat>
<expres>href="http://www.peliculasrey.com/idioma/(.*?)/"</expres>
<page>http://www.peliculasrey.com/</page>
<referer></referer>
<cookieJar></cookieJar>
</regex>
</regex>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[COLOR deepskyblue] [makelist2.param2] [/COLOR] </title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param1]</thumbnail>
<fanart>[makelist2.param1]</fanart>
]]></listrepeat>
<expres>class="poster"[\w\W\s]{0,8}src="(.*?)"[\w\W\s]{0,2}alt="(.*?)"[\w\W\s]{0,2}title="(.*?)"[\w\W\s]{0,32}href="(.*?)"</expres>
<page>http://www.peliculasrey.com/idioma/[makelist3.param1]/</page>
<referer></referer>
<cookieJar></cookieJar>
</regex>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param2] - [makelist.param2]</title>
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


<thumbnail>[makelist2.param1]</thumbnail>
<fanart>[makelist2.param1]</fanart>
]]></listrepeat>

<expres>http://streamin.to/embed-(.*?)-[\w\W\s]{0,115}optxt[\w\W\s]{0,4}pan>(.*?)<</expres>
<page>[makelist2.param4]</page>
<referer></referer>
<cookieJar></cookieJar>
</regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>











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

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>






<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]PeliculasDK / Estrenos[/B]  [/COLOR][COLOR skyblue]    [/COLOR] </title>
 <link>$doregex[makelist3]</link>



<regex>
   <name>makelist3</name>
   <listrepeat><![CDATA[
       <title>Pagina [makelist3.param1]</title>

<link>$doregex[makelist2]</link>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
   ]]></listrepeat>
   <expres><![CDATA[paginado:"(.*?)";]]></expres>
   <page>http://adryanlist.org/adryan/kozm.txt</page>
   <cookieJar></cookieJar>
</regex>



<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist2.param2]  [COLOR lightblue] idioma:[makelist2.param4][/COLOR][/COLOR] </title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[href="(.*?)"[\w\W\s]{0,2}title="(.*?)"[\w\W\s]{0,7}src="(.*?)"[\w\W\s]{0,300}idioma/(.*?)"]]></expres>
<page>http://www.peliculasdk.com/ver/estrenos/page/[makelist3.param1]</page>
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
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>







































<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]CINETUX COM[/B] [/COLOR][COLOR skyblue] Estrenos [Audio Latino] [/COLOR]   </title>
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
<title>[makelist2.param3]</title>
<link>$doregex[makelist]</link>
<thumbnail>http:[makelist2.param2]</thumbnail>
]]></listrepeat>
<expres>href="(.*?)"[\w\W\s]{0,80}src="(.*?)".*?Title">(.*?)<</expres>
<page>http://www.cinetux.com/peliculas/page/[makelist3.param1]</page>
</regex>




<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param3]        openload/[makelist.param1]</title>
<urlsolve>https://openload.co/[makelist.param1]</urlsolve>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres>(https:\/\/.*?)&amp;quot</expres>
<page>[makelist2.param1]</page>
</regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
 </item>































 <item>
 <title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]CINETUX NET [/B] [/COLOR][COLOR skyblue] Estrenos [Audio Latino] [/COLOR]   </title>
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
 <title>[makelist2.param2] [makelist2.param3] </title>
 <link>$doregex[makelist]</link>
 <thumbnail>[makelist2.param1]</thumbnail>
 ]]></listrepeat>
 <expres>src="(.*?)"\salt="(.*?)".*?quality">(.*?)<.*?href="(.*?)"</expres>
 <page>http://www.cinetux.net/idioma/latino/page/[makelist3.param1]/</page>
 </regex>



 <regex>
 <name>makelist</name>
 <listrepeat><![CDATA[
 <title>[B][makelist2.param2][/B] [makelist2.param3]        SERVER:[makelist.param1]</title>
 <link>$doregex[id3]</link>
 <thumbnail>[makelist2.param3]</thumbnail>
 <fanart>[makelist2.param2]</fanart>
 ]]></listrepeat>
 <expres>data-lazy-src="(.*?)"</expres>
 <page>[makelist2.param4]</page>
 <referer></referer>
 <cookieJar></cookieJar>
 </regex>

 <regex>
 <name>id3</name>
 <expres><![CDATA[#$pyFunction
 def GetLSProData(page_data,Cookie_Jar,m):
     import urlresolver
     url = '$doregex[url]'
     try:
         u = urlresolver.resolve(url)
     except:
         u = 'http://adryantv.org/error.mp4'
     return u
 ]]></expres>
 <page></page>
 </regex>

 <regex>
 <name>url</name>
 <expres>replace\(\"(.*?)"</expres>
 <page>[makelist.param1]</page>
 </regex>


 <thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
  </item>






	 <item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]CINETUX NET [/B] [/COLOR][COLOR skyblue] Estrenos [Audio Castellano] [/COLOR]   </title>
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
<title>[makelist2.param2] [makelist2.param3] </title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param1]</thumbnail>
]]></listrepeat>
<expres>src="(.*?)"\salt="(.*?)"[\w\W\s]{0,80}quality">(.*?)<[\w\W\s]{0,12}href="(.*?)"</expres>
<page>http://www.cinetux.net/idioma/espanol/page/[makelist3.param1/]</page>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param2] [makelist2.param3]        SERVER:[makelist.param1]</title>
<urlsolve>[makelist.param1]</urlsolve>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres>data-lazy-src="(.*?)"</expres>
<page>[makelist2.param4]</page>
<referer></referer>
<cookieJar></cookieJar>
</regex>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
 </item>









<item>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]Pelis-Locura[/B] [/COLOR][COLORskyblue][Castellano][/COLOR] </title>

<link>$doregex[makelist2]</link>


  <regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist2.param2]   [/COLOR]</title>
<link>$doregex[makelist3]</link>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[href="(.*?)".*?escargar(.*?)gratis.*?src="(.*?)"]]></expres>
<page>http://torrentlocura.com/peliculas/</page>
</regex>




<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist2.param2]              server: [makelist3.param1][/COLOR]</title>
<urlsolve>[makelist3.param1]</urlsolve>
<thumbnail>[makelist2.param2]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[a\shref='(http:\/\/upto.*?|https:\/\/open.*?)'\srel]]></expres>
<page>[makelist2.param1]</page>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>








<iem>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]PelisPlus - ESTRENOS[/B]  [/COLOR][COLOR skyblue]     [/COLOR] </title>



<link>$doregex[makelist3]</link>



<regex>
   <name>makelist3</name>
   <listrepeat><![CDATA[
       <title>Pagina [makelist3.param1]</title>

<link>$doregex[makelist2]</link>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
   ]]></listrepeat>
   <expres><![CDATA[paginado:"(.*?)";]]></expres>
   <page>http://adryanlist.org/adryan/kozm.txt</page>
   <cookieJar></cookieJar>
</regex>




<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>[COLOR skyblue] [makelist2.param3]  [/COLOR] </title>
<link>$doregex[makelist]</link>
<thumbnail>[makelist2.param1]</thumbnail>
<fanart>[makelist2.param1]</fanart>
]]></listrepeat>
<expres><![CDATA[src=\"(.*?)\"\sdata-url=\"http:\/\/www.pelisplus.tv\/pelicula(.*?)"\salt="(.*?)"]]></expres>
<page>http://www.pelisplus.tv/estrenos/pag-[makelist3.param1]</page>
 </regex>




<regex>
   <name>makelist</name>
   <listrepeat><![CDATA[
          <title>[makelist2.param3]           [I]Server openload [makelist.param1][/I]</title>
          <link>$doregex[id3]</link>
		  <thumbnail>[makelist2.param1]</thumbnail>
		<fanart>[makelist2.param1]</fanart>
   ]]></listrepeat>
   <expres><![CDATA[src='https://openload.co/embed\/(.*?)\/]]></expres>
   <page>http://www.elreyxhd.com/reproductor[makelist2.param2]</page>
   <cookieJar></cookieJar>
</regex>



<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = 'https://openload.co/embed/[makelist.param1]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>

























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



<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>







































































































































<itm>
<title> [COLOR lime]•[/COLOR]    [COLOR deepskyblue][B]TRAILERS [/B] [/COLOR][COLOR skyblue] PELICULAS[/COLOR] [COLOR lightslategray]Disney[/COLOR] </title>
<link>$doregex[makelist2]</link>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<title>page [makelist2.param1]</title>
<link>$doregex[makelist3]</link>
<referer></referer>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail>
]]></listrepeat>
<expres> (.*?),</expres>
<page>$doregex[get-number]</page>
<cookieJar></cookieJar>
</regex>

<regex>
            <name>makelist3</name>
            <listrepeat><![CDATA[
		<title>[COLOR lightblue][makelist3.param2][/COLOR] </title>
		<link>plugin://plugin.video.youtube/play/?video_id=[makelist3.param1]</link>
                <thumbnail>https://i.ytimg.com/vi/[makelist3.param1]/hqdefault.jpg</thumbnail>
            ]]></listrepeat>
            <expres><![CDATA[href="\/watch\?v=(.*?)">(.*?)<.*?> -(.*?)</span></h3>]]></expres>
            <page>$doregex[get-source-page]</page>
             <cookieJar></cookieJar>
</regex>

<regex>
<name>get-number</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m,lists='[makelist.param1]'):

 real = 27 + 2

 liste = list(range(real))
 return liste
]]></expres>
<page></page>
</regex>

<regex>
<name>get-source-page</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m,url='https://www.youtube.com/user/DisneyMovieTrailers/videos',page='[makelist2.param1]'):

 import requests
 import re
 import json

 page = str(page)
 print page
 pageUrl=url
 headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:42.0) Gecko/20100101 Firefox/42.0 Iceweasel/42.0'}
 r1 = requests.get(pageUrl, headers = headers)
 source = r1.text
 source =  source.replace('&quot;', '"').replace("'", "'").replace("&amp;", "&")
 pre = 'https://www.youtube.com'
 #print pre
 #page = [makelist2.param1]
 N = int(float(page))

 if (N > 1):

   for itr in range (1,N):
    continuex = re.findall('data-uix-load-more-href="(.*?)"', source)[0]
    continuationx = pre + continuex
    r = requests.get(continuationx, headers = headers)
    source = r.text
    jdata = json.loads(source)
    source = jdata["load_more_widget_html"]
    page = jdata["content_html"]
    page =  page.replace('&quot;', '"').replace("'", "'").replace("&amp;", "&")
   return page

 else:

  return source
]]></expres>
<page></page>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>
















































































































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

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>






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



<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>
















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]ESTRENOS DEL 2017[/B]  [/COLOR][COLOR blue]2017 [VO][/COLOR] </title>
<link>$doregex[makelist4]</link>


<regex>
  <name>makelist4</name>
  <listrepeat><![CDATA[
        <title>$pyFunction:'[COLOR skyblue][makelist4.param2][/COLOR]'.replace("1", "Enero").replace("2", "Febrero").replace("3", "Marzo").replace("4", "Abril").replace("5", "Mayo").replace("6", "Junio").replace("7", "Julio").replace("8", "Agosto").replace("9", "Septiembre").replace("10", "Octubre").replace("11", "Noviembre").replace("12", "Diciembre")</title>
        <link>$doregex[makelist3]</link>
		<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
        ]]></listrepeat>
<expres>href="(.*?)">(?!\.\.)(.*?)\/</expres>
<page>http://media.bia4music.com/movie/2017/Film/</page>
<cookieJar></cookieJar>
</regex>


<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>$pyFunction:'[makelist3.param2]'.replace(".", " ").replace("_", " ")</title>
        <link>http://media.bia4music.com/movie/2017/Film/[makelist4.param1][makelist3.param1]</link>
		<thumbnail>https://image.tmdb.org/t/p/original/$doregex[imagen]</thumbnail>
        ]]></listrepeat>
<expres>href="(.*?)">(.*?).20(.*?mkv|mp4)<</expres>
<page>http://media.bia4music.com/movie/2017/Film/[makelist4.param1]</page>
<cookieJar></cookieJar>
</regex>

<regex>
<name>imagen</name>
<expres><![CDATA[poster_path\":\"\\/(.*?)\"]]></expres>
<page>https://api.themoviedb.org/3/search/movie?api_key=3d8a2c67653e2f8fd7dd09959e835f02&amp;language=es&amp;query=$doregex[nombre2]</page>
</regex>
<regex>
<name>nombre2</name>
<expres>$pyFunction:'[makelist3.param2]'.replace(".", "+").replace("_", "+")</expres>
<page></page>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>




 <item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]WATCHFREE[/B]  [/COLOR][COLOR blue]SEARCH[/COLOR] </title>
<link>$doregex[makelist2]</link>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
   <title>[COLOR deepskyblue] [makelist2.param2][/COLOR]</title>
    <link>$doregex[makelist]</link>
 <thumbnail>http:[makelist2.param4]</thumbnail>
<fanart>http:[makelist2.param4]</fanart>
]]></listrepeat>
<expres><![CDATA[href="(.*?)"[\w\W\s]{0,15}Putlocker(.*?)">(.*?)<[\w\W\s]{0,4}src="(.*?)"]]></expres>
<page>https://www.watchfree.to/?keyword=$doregex[search]&amp;search_section=1</page>
</regex>

<regex>
<name>search</name>
<expres><![CDATA[#$pyFunction
import xbmc
import xbmcaddon
import xbmcgui
def GetLSProData(page_data,Cookie_Jar,m):
    dialog = xbmcgui.Dialog()
    d = dialog.input('Buscar Pelicula: ejemplo: Batman', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    return d
]]></expres>
<page></page>
<cookieJar></cookieJar>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[makelist2.param3]    [COLOR lightslategray]server:[makelist.param3] [/COLOR] </title>
<link>$doregex[id3]</link>
 <thumbnail>http:[makelist2.param4]</thumbnail>
<fanart>http:[makelist2.param4]</fanart>
]]></listrepeat>
<expres>gtfo=(.*?)&amp;t.*?title="(.*?)".*?host\',\s\'(.*?)\'</expres>
<page>http://www.watchfree.to/[makelist2.param1]</page>
</regex>


<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[id2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

   <regex>
<name>id2</name>
<expres>$pyFunction:base64.b64decode('[makelist.param1]')</expres>
<page></page>
</regex>



<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>



















<item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]PRIMEWIRE[/B]  [/COLOR][COLOR blue]SEARCH[/COLOR] </title>
<link>$doregex[makelist2]</link>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
   <title>[COLOR deepskyblue] [makelist2.param2][/COLOR]</title>
    <link>$doregex[makelist]</link>
 <thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[href="watch-(.*?html)"[\w\W\s]{0,9}title="(.*?)"[\w\W\s]{0,6}src="(.*?)"]]></expres>
<page>http://www.primewire.ch/?keywords=$doregex[search]&amp;type=movie</page>
</regex>

<regex>
<name>search</name>
<expres><![CDATA[#$pyFunction
import xbmc
import xbmcaddon
import xbmcgui
def GetLSProData(page_data,Cookie_Jar,m):
    dialog = xbmcgui.Dialog()
    d = dialog.input('Buscar Pelicula: ejemplo: Batman', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    return d
]]></expres>
<page></page>
<cookieJar></cookieJar>
</regex>


<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param2]    [COLOR lightslategray]server:[makelist.param3] [/COLOR] </title>
<link>$doregex[id3]</link>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[movie_version_link.*?href="(.*?)"\stitle="(.*?)"[\w\W\s]{0,145}version_host\">(.*?)<]]></expres>
<page>http://www.primewire.ch/watch-[makelist2.param1]</page>
</regex>



<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[id2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<regex>
<name>id2</name>
<expres>$pyFunction:base64.b64decode('$doregex[id1]')</expres>
<page></page>
</regex>

<regex>
<name>id1</name>
<expres>url=(.*?)&amp;d</expres>
<page>[makelist.param1]</page>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>






<item>
 <title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]HEVC MOVIES[/B]  [/COLOR][COLOR skyblue]SEARCH   [/COLOR] </title>
<link>$doregex[makelist2]</link>


<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
   <title>[makelist2.param2] </title>
 <link>$doregex[makelist3]</link>
  <thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[href="(.*?)".*?title="(.*?)HEVC.*?src="(.*?)".*?alt="(.*?)"]]></expres>
<page>http://hevcbluray.info/?s=$doregex[search]</page>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>

<regex>
<name>search</name>
<expres><![CDATA[#$pyFunction
import xbmc
import xbmcaddon
import xbmcgui
def GetLSProData(page_data,Cookie_Jar,m):
    dialog = xbmcgui.Dialog()
    d = dialog.input('Search Movie ej: Batman', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    return d
]]></expres>
<page></page>
<cookieJar></cookieJar>
</regex>
<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://hevcbluray.info',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
</regex>



 <regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<SetViewMode>55</SetViewMode>
<title>[COLOR skyblue] [makelist2.param2]  - [COLOR lightyellow] server:[makelist3.param2] [/COLOR] [/COLOR]</title>
<link>$doregex[id3]</link>
 <thumbnail>[makelist2.param2]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[href=\"(http://vidto.*?|https://openload.*?|http://www.nowvideo.*?|http://uptobox.*?)\">(.*)<]]></expres>
<page>[makelist2.param1]</page>
<agent>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36</agent>
<cookieJar>$doregex[createCFCookie]</cookieJar>
</regex>


<regex>
        <name>createCFCookie</name>
        <expres></expres>
        <page>$pyFunction:cloudflare.createCookie('http://hevcbluray.info',Cookie_Jar,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')</page>
        <cookieJar></cookieJar>
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


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>

</item>























<item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]IMDB[/B]  [/COLOR][COLOR blue]Beta  primewire[/COLOR] </title>
<link>$doregex[makelist3]</link>



<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
   <title>[COLOR deepskyblue] [makelist3.param1][/COLOR]</title>
    <link>$doregex[makelist2]</link>
 <thumbnail>[makelist3.param2]</thumbnail>
<fanart>[makelist3.param2]</fanart>

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
   ret = dialog.select('Elige tu Audio preferido ', ['Recientes', 'Box Offce', 'Populares'])
   lists = ['http://www.imdb.com/search/title?title_type=feature,tv_movie&amp;languages=en&amp;num_votes=500,&amp;production_status=released&amp;groups=top_1000&amp;sort=moviemeter,asc&amp;count=20&amp;start=1', 'http://www.imdb.com/search/title?title_type=feature,tv_movie&amp;sort=boxoffice_gross_us,desc&amp;count=20&amp;start=1', 'http://www.imdb.com/search/title?title_type=feature&amp;languages=en&amp;num_votes=200,&amp;release_date=2016-09-13,2017-09-13&amp;sort=release_date_us,desc&amp;count=20&amp;start=1']
   return lists[ret]
]]></expres>
<page></page>
</regex>



<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
   <title>[COLOR deepskyblue] [makelist2.param2][/COLOR]</title>
    <link>$doregex[makelist]</link>
 <thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[href="watch-(.*?html)"[\w\W\s]{0,9}title="(.*?)"[\w\W\s]{0,6}src="(.*?)"]]></expres>
<page>http://www.primewire.ch/?keywords=$doregex[titulo]&amp;type=movie</page>
</regex>


<regex>
<name>titulo</name>
<expres>$pyFunction:'[makelist3.param1]'.replace(" ", "+")</expres>
<page></page>
</regex>




<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param2]    [COLOR lightslategray]server:[makelist.param3] [/COLOR] </title>
<link>$doregex[id3]</link>
<thumbnail>[makelist2.param3]</thumbnail>
<fanart>[makelist2.param3]</fanart>
]]></listrepeat>
<expres><![CDATA[movie_version_link.*?href="(.*?)"\stitle="(.*?)"[\w\W\s]{0,145}version_host\">(.*?)<]]></expres>
<page>http://www.primewire.ch/watch-[makelist2.param1]</page>
</regex>



<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[id2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<regex>
<name>id2</name>
<expres>$pyFunction:base64.b64decode('$doregex[id1]')</expres>
<page></page>
</regex>

<regex>
<name>id1</name>
<expres>url=(.*?)&amp;d</expres>
<page>[makelist.param1]</page>
</regex>

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>























<item>
<title> [COLOR lime]•[/COLOR]    [COLOR lightyellow][B]IMDB[/B]  [/COLOR][COLOR blue]Beta  gnula[/COLOR] </title>
<link>$doregex[makelist4]</link>



<regex>
<name>makelist4</name>
<listrepeat><![CDATA[
   <title>[COLOR deepskyblue] [makelist4.param1][/COLOR]</title>
    <link>$doregex[makelist]</link>
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
   ret = dialog.select('Elige tu Audio preferido ', ['Recientes', 'Box Offce', 'Populares'])
   lists = ['http://www.imdb.com/search/title?title_type=feature,tv_movie&amp;languages=en&amp;num_votes=500,&amp;production_status=released&amp;groups=top_1000&amp;sort=moviemeter,asc&amp;count=20&amp;start=1', 'http://www.imdb.com/search/title?title_type=feature,tv_movie&amp;sort=boxoffice_gross_us,desc&amp;count=20&amp;start=1', 'http://www.imdb.com/search/title?title_type=feature&amp;languages=en&amp;num_votes=200,&amp;release_date=2016-09-13,2017-09-13&amp;sort=release_date_us,desc&amp;count=20&amp;start=1']
   return lists[ret]
]]></expres>
<page></page>
</regex>


<regex>
   <name>makelist</name>
   <listrepeat><![CDATA[
          <title>[UPPERCASE][COLOR skyblue][makelist.param2][/COLOR][/UPPERCASE]</title>
          <link>$doregex[makelist3]</link>
		  <thumbnail>http://adryanlist.org/adryan/img/peliculas.jpg</thumbnail>
   ]]></listrepeat>
   <expres>a\shref="(.*?)".*?\">Ver(.*?)online</expres>
   <page>https://www.google.com.mx/search?q=$doregex[titulo]+site:gnula.nu</page>
   <cookieJar></cookieJar>
</regex>



<regex>
<name>titulo</name>
<expres>$pyFunction:'[makelist4.param1]'.replace(" ", "+")</expres>
<page></page>
</regex>




<regex>
<name>makelist3</name>
<listrepeat><![CDATA[
<title>[B][COLOR skyblue][makelist4.param1][/COLOR] [COLOR aquamarine][makelist3.param1][/COLOR] [/B][COLOR deepskyblue][makelist3.param3][/COLOR]</title>
<link>$doregex[id3]</link>
 <thumbnail>[makelist4.param2]</thumbnail>
<fanart>[makelist4.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[em>(opc.*?)<\/em|href="(http://gamovideo.*?|https://vidoza.*?|https://kingvid.*?|https://openload.*?|https://streamango.*?|http://streamin.*?|http://streamcloud.*?|http://uptobox.*?|https://rapidvideo.*?)".*?class="(.*?)"]]></expres>
<page>[makelist.param1]</page>
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

<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart></item>













<item>
<title> miradetodo </title>
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
   <title>[COLOR deepskyblue] [makelist2.param3][/COLOR]</title>
    <link>$doregex[makelist]</link>
 <thumbnail>[makelist2.param2]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[item[\w\W\s]{0,7}href="(.*?)"[\w\W\s]{0,30}src="(.*?)"\salt="(.*?)"]]></expres>
<page>http://miradetodo.io/page/[makelist3.param1]/?s=</page>
</regex>





<regex>
<name>makelist</name>
<listrepeat><![CDATA[
<title>[makelist2.param3]    [COLOR lightslategray]server:[makelist.param1]    [/COLOR] </title>
<link>$doregex[id3]</link>
<thumbnail>[makelist2.param2]</thumbnail>
<fanart>[makelist2.param2]</fanart>
]]></listrepeat>
<expres><![CDATA[player.miradetodo.io\/api\/(.*?).[\w\W\s]{0,4}id=(.*?)\&]]></expres>
<page>$doregex[peliculas]</page>
</regex>

<regex>
<name>peliculas</name>
<expres><![CDATA[data-lazy-src=\"(http://player.*?)\"]]></expres>
<page>[makelist2.param1]</page>
</regex>



<regex>
<name>id3</name>
<expres><![CDATA[#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
    import urlresolver
    url = '$doregex[id2]'
    try:
        u = urlresolver.resolve(url)
    except:
        u = 'http://adryantv.org/error.mp4'
    return u
]]></expres>
<page></page>
</regex>

<regex>
<name>id2</name>
<expres>$pyFunction:base64.b64decode('[makelist.param2]')</expres>
<page></page>
</regex>


<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>












        <title>[makelist.param1]   ----  [makelist.param2] </title>


<itm>
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

<thumbnail> </thumbnail>
</item>




































































<item>
<title> RePelis Buscar</title>
<link>$doregex[makelist3]</link>



<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>[makelist3.param5]</title>
        <link>$doregex[makelist2]</link>
		<thumbnail>[makelist3.param3]</thumbnail>
		<info>[makelist3.param6]</info>
		]]></listrepeat>
<expres><![CDATA[href="(.*?)"[\w\W\s]{0,2}title="(.*?)".*?src="(.*?)".*?href="(.*?)"\stitle="(.*?)".*text-list">(.*?)<]]></expres>
<page>https://repelis.tv/buscar/?s=don+jon</page>
<cookieJar></cookieJar>
</regex>


<regex>
  <name>makelist2</name>
  <listrepeat><![CDATA[
        <title>[makelist3.param3]  server:[makelist2.param2] idioma:[makelist2.param3]</title>
        <link>$doregex[makelist]</link>
		<thumbnail>[makelist3.param1]</thumbnail>
		]]></listrepeat>
<expres><![CDATA[href="(.*?)".*?0\s0\">(.*?)<.*?>(La.*?|Sub.*?)<]]></expres>
<page>[makelist3.param1]</page>
<cookieJar></cookieJar>
</regex>


<regex>
  <name>makelist</name>
  <listrepeat><![CDATA[
        <title>Reproducir  [makelist3.param3]    -  [AdryanList] </title>
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
<expres>$pyFunction:base64.b64decode('[makelist.param1]')</expres>
<page></page>
</regex>
<regex>
<name>get-m3u82</name>
<expres>$pyFunction:base64.b64decode('[makelist.param2]')</expres>
<page></page>
</regex>


<thumbnail> </thumbnail>
</item>




<item>
<title>2600 Movies VO </title>
<link>$doregex[makelist3]</link>
<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>$pyFunction:'[COLOR skyblue][makelist3.param2][/COLOR]'.replace(".", " ")</title>
        <link>http://dlst18.in/dl/vip/film/3/[makelist3.param1]</link>

        ]]></listrepeat>
<expres>href="(.*?)">(.*?).20(.*?mkv|mp4)<</expres>
<page>http://dlst18.in/dl/vip/film/3/?MA</page>
<cookieJar></cookieJar>
</regex>

<thumbnail> </thumbnail>
</item>





<item>
<title>series vo </title>
<link>$doregex[makelist3]</link>
<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>$pyFunction:'[COLOR skyblue][makelist3.param2][/COLOR]'.replace(".", " ").replace("mp4", "[COLOR aquamarine]Adryanlist[/COLOR]").replace("mkv", "[COLOR aquamarine]Adryanlist[/COLOR]")</title>
        <link>http://dl.dlfile.pro/1/[makelist3.param1]</link>

        ]]></listrepeat>
<expres>href="(.*?)">(.*?mkv|mp4)<</expres>
<page>http://dl.dlfile.pro/1/</page>
<cookieJar></cookieJar>
</regex>

<thumbnail> </thumbnail>
</item>


<item>
<title>6000 peliculas VO [720p|1080p]</title>
<link>$doregex[makelist3]</link>
<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>$pyFunction:'[COLOR skyblue][makelist3.param2][/COLOR] [makelist3.param3][makelist3.param4]'.replace(".", " ").replace("mp4", "[COLOR aquamarine]Adryanlist[/COLOR]").replace("mkv", "[COLOR aquamarine]Adryanlist[/COLOR]")</title>
        <link>http://dl.dlfile.pro/2/[makelist3.param1]</link>

        ]]></listrepeat>
<expres>href="(.*?)">(.*?).(20.*?)(.*?mkv|mp4)<</expres>
<page>http://dl.dlfile.pro/2/</page>
<cookieJar></cookieJar>
</regex>

<thumbnail> </thumbnail>
</item>





<item>
<title>series vo 2</title>
<link>$doregex[makelist3]</link>
<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>$pyFunction:'[COLOR skyblue][makelist3.param2][/COLOR]'.replace("%20", " ")</title>
        <link>http://dl.dlfile.pro/2/[makelist3.param1]/</link>

        ]]></listrepeat>
<expres>href="(.*?)\/">(.*?)\/</expres>
<page>http://dl.dlfile.pro/2/</page>
<cookieJar></cookieJar>
</regex>
<thumbnail> </thumbnail>
</item>





<item>
<title>Peliculas</title>
<link>$doregex[makelist3]</link>
<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>$pyFunction:'[COLOR skyblue][makelist3.param2][/COLOR] [makelist3.param3][makelist3.param4]'.replace(".", " ").replace("mp4", "[COLOR aquamarine]Adryanlist[/COLOR]").replace("mkv", "[COLOR aquamarine]Adryanlist[/COLOR]")</title>
        <link>http://condor1726.dedicatedpanel.com/PELICULAS/[makelist3.param1]</link>

        ]]></listrepeat>
<expres>href="(.*?)">(.*?).(20.*?)(.*?mkv|mp4)<</expres>
<page>http://condor1726.dedicatedpanel.com/PELICULAS/?C=M;O=D</page>
<cookieJar></cookieJar>
</regex>

<thumbnail> </thumbnail>
</item>

<item>
<title>Peliculas CAM</title>
<link>$doregex[makelist3]</link>
<regex>
  <name>makelist3</name>
  <listrepeat><![CDATA[
        <title>$pyFunction:'[COLOR skyblue][makelist3.param2][/COLOR] [makelist3.param3][makelist3.param4]'.replace(".", " ").replace("mp4", "[COLOR aquamarine]Adryanlist[/COLOR]").replace("mkv", "[COLOR aquamarine]Adryanlist[/COLOR]")</title>
        <link>http://condor1726.dedicatedpanel.com/CAM-PELIS/[makelist3.param1]</link>

        ]]></listrepeat>
<expres>href="(.*?)">(.*?).(20.*?)(.*?mkv|mp4)<</expres>
<page>http://condor1726.dedicatedpanel.com/CAM-PELIS/</page>
<cookieJar></cookieJar>
</regex>

<thumbnail> </thumbnail>
</item>



 













 <item>
<title>Wiseplay listas </title>
<link>http://ignora.me</link>
<externallink>http://adryanlist.org/adryan/wise.xml</externallink>
<thumbnail>http://adryanlist.org/adryan/img/adryflix.png</thumbnail><fanart>http://adryanlist.org/adryan/img/fanart.jpg</fanart>
</item>





<item>
<title>some movies</title>
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

<thumbnail> </thumbnail>
</item>





<item>
<title> netai torrents</title>
<link>$doregex[makelist2]</link>

<regex>
<name>makelist2</name>
<listrepeat><![CDATA[
   <SetViewMode>55</SetViewMode>
   <title>[COLOR lightblue][B]Genero [makelist2.param1][/COLOR][/B]   </title>
<link>$doregex[makelist]</link>
]]></listrepeat>
<expres><![CDATA[option\sclass="level-0.*?">(.*?)<]]></expres>
<page>http://gruponetai.com/portal/</page>
</regex>





<regex>
<name>makelist</name>
<listrepeat><![CDATA[
   <SetViewMode>55</SetViewMode>
   <title>[COLOR lightblue][B][makelist.param3][/COLOR][/B]   </title>
   <link>plugin://plugin.video.quasar/play?uri=$doregex[torrent]</link>
 <thumbnail>[makelist.param1]</thumbnail>
]]></listrepeat>
<expres><![CDATA[171.*?src="(.*?jpg)"[\w\W\s]{0,390}href="(.*?)".*?trong>(.*?)<\/]]></expres>
<page>http://gruponetai.com/portal/Genero/[makelist2.param1]/</page>
</regex>

<regex>
<name>torrent</name>
<expres><![CDATA[href="(.*?\.torrent)"]]></expres>
<page>[makelist.param2]</page>
</regex>

<thumbnail>http://adryantv.org/adryan/img/torrent.png</thumbnail>
<info>[B][COLOR skyblue]»»»   A  D  R  Y  A  N  L  I  S  T  «««[/COLOR]
[COLOR aquamarine]Donaciones paypal.me/adryanlist[/COLOR][/B]</info>
</item>


http://gruponetai.com/portal/?s=ben&x=0&y=0




 



<item>
<title> netai test buscador torrents</title>
<link>$doregex[makelist]</link>

<regex>
<name>makelist</name>
<listrepeat><![CDATA[
   <SetViewMode>55</SetViewMode>
   <title>[COLOR lightblue][B][makelist.param3][/COLOR][/B]   </title>
   <link>plugin://plugin.video.quasar/play?uri=$doregex[torrent]</link>
 <thumbnail>[makelist.param1]</thumbnail>
]]></listrepeat>
<expres><![CDATA[171.*?src="(.*?jpg)"[\w\W\s]{0,390}href="(.*?)".*?trong>(.*?)<\/]]></expres>
<page>http://gruponetai.com/portal/?s=$doregex[search]</page>
</regex>

<regex>
<name>search</name>
<expres><![CDATA[#$pyFunction
import xbmc
import xbmcaddon
import xbmcgui
def GetLSProData(page_data,Cookie_Jar,m):
    dialog = xbmcgui.Dialog()
    d = dialog.input('Buscar por Titulo, Actor, director', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    return d
]]></expres>
<page></page>
<cookieJar></cookieJar>
</regex>

<regex>
<name>torrent</name>
<expres><![CDATA[href="(.*?\.torrent)"]]></expres>
<page>[makelist.param2]</page>
</regex>

<thumbnail>http://adryantv.org/adryan/img/torrent.png</thumbnail>
<info>[B][COLOR skyblue]»»»   A  D  R  Y  A  N  L  I  S  T  «««[/COLOR]
[COLOR aquamarine]Donaciones paypal.me/adryanlist[/COLOR][/B]</info>
</item>










