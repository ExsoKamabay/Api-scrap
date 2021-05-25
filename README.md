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

# Class & Method

``` python
Rexdl().rexdl(query:str)
A2zapk().a2zapk(query:str)
Gamemod().gamemod(query:str)
HappyMod().happymod(query:str)
DlanDroid().dlandroid(query:str)
Sourceforge().sourceforge(query:str) 
OceanOfGame().oceanofgame(query:str) 
Uptodown().uptodown(query:str,lang:str)
IpWhois().ipwhois(query:str) -> ip4
Github_search_enggine().search_github(query:str) 
Google().google_search_query(query:str,lang:str,maxSearch:int)
Warna().color[value] -> str - red,cyan,magenta,green,blue,yellow
picSearch().picSearch_All(query:str)
picSearch().picsearch_pages1(query:str)
picSearch().picsearch_pages2345(query:str)

```


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
