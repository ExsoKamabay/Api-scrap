# Api-scrap
<p>apikey search engine scraping methods.</p>
<p>results are displayed based on content</p>
<h2> liked the site </h2>
<ul>
  <li>Github</li>
  <li>Google</li>
  <li>SourceForge</li>
  <li>Oceanofgames</li>
  <li>Happymod</li>
  <li>Uptodown</li>
  <li>Dlandroid</li>
  <li>GameMod</li>
  <li>Rexdl</li>
  <li>A2zapk</li>
  <li>IpWhois</li>
  <li>picSearch</li>
</ul>

# install on pip for windows
```python
#version 1.0 has problems importing if using pip upgraded to version 2.0
pip install kmy_scrap
pip install --upgrade kmy_scrap
# OR
pip install kmy_scrap==0.2.0
```

# install on pip for Linux
```python
#version 1.0 has problems importing if using pip upgraded to version 2.0
pip3 install kmy_scrap && pip3 install --upgrade kmy_scrap
# OR
pip3 install kmy_scrap==0.2.0
```

- from kmy_scrap import className
```python
#example
from kmy_scrap import HappyMod
print(HappyMod().happymod("free fire"))
```

<strong><h3>start using</h3>
  <h4>Class : Github_search_enggine() - Method : search_github(query) - str<br>
      Class : Sourceforge() - Method : sourceforge(query) -> str <br>
      Class : OceanOfGame() - Method : oceanofgame(query) -> str <br>
      Class : HappyMod() - Method : happymod(query) -> str <br>
      Class : Uptodown() - Method : uptodown(query,lang) -> str <br>
      Class : DlanDroid() - Method : dlandroid(query) -> str <br>
      Class : Gamemod() - Method : gamemod(query) -> str <br>
      Class : A2zapk() - Method : a2zapk(query) -> str <br>
      Class : Rexdl() - Method : rexdl(query) -> str <br>
      Class : IpWhois() - Method : ipwhois(query) -> ip str <br>
      Class : Google() - Method : google_search_query(query,lang,maxSearch,kwargs) -> str -> int -> opt <br>
      Class : Warna() - Method : color[value] -> str - red,cyan,magenta,green,blue,yellow<br>
      Class : picSearch() - Method : picsearch_pages1(query),picsearch_pages2345(query),picSearch_All(query) ->  str <br>
      <p><strong>Note   :<br>"   The picsearch_pages1(); method searches only the main page section, while the picsearch_pages2345(); method searches pages 2,3,4,5 this method may be a little slower, whereas the picSearch_All () method will search these 5 pages 1,2,3,4,5 will be slower than the picsearch_pages1(); and picsearch_pages2345() methods"</strong></p><br><h4></strong>
# call the class method<br>
    
```python
from scrap import *
#displays results
wrna = Warna().color;
print(wrna["red"]+"RED"+wrna["cyan"]+"CYAN");
print(wrna["green"]+"GREEN"+wrna["magenta"]+"MAGENTA");
print(wrna["yellow"]+"YELLOW"+wrna["blue"]+"BLUE");
print(HappyMod().happymod("free fire"));
print(Github_search_enggine().search_github("free fire"));
print(Sourceforge().sourceforge("tools"));
print(OceanOfGame().oceanofgame("free fire"));
print(Uptodown().uptodown("free fire","id"));
print(DlanDroid().dlandroid("free fire"));
print(Gamemod().gamemod("free fire"));
print(A2zapk().a2zapk("free fire"));
print(Rexdl().rexdl("free fire"));
#print(IpWhois().ipwhois("2404:6800:4001:806::200e"));
print(picSearch().picsearch_pages1("bird parrot"));
print(picSearch().picsearch_pages2345("bird parrot"));
print(picSearch().picSearch_All("bird parrot"));
print(Google().google_search_query("free fire",lang="id",maxSearch=10));
```
    
- classname().methodname(query) -> <a href="https://github.com/ExsoKamabay/Api-scrap/blob/master/example-response.txt">return json</a>
- take a specific value<br>
classname().methodname(query)["key"]<br><br> Mail : lexyong66@gmail.com;
