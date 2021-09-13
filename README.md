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

# Downloads 👇
```python
#👉 Windows
pip install kmy_scrap
#👉 Linux
pip3 install kmy_scrap
```

- usage example!
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


    
- classname().methodname(query) -> <a href="https://github.com/ExsoKamabay/Api-scrap/blob/master/response.json">return json</a>
- take a specific value<br>
classname().methodname(query)["key"]<br><br> Mail : lexyong66@gmail.com;
