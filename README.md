# kmy_scrap

# *`apikey search enggine scraping based!`*

***support python version 3.9.x***

## **`like this site!`**

- **_`Github`_** [link](https://github.com/search?q=)
- **_`Google`_** [link](https://google.com/search?q=)
- **_`HappyMod`_** [link](https://www.happymod.com/?q=)
- **_`Rexdl`_** [link](https://www.rexdl.com)
- **_`Ocean Of Games`_** [link](http://oceanofgames.com/)
- **_`Source Forge`_** [link](https://sourceforge.net/)


```python
# download from pip
pip install kmy-scrap
```
[https://pypi.org/project/kmy-scrap/](https://pypi.org/project/kmy-scrap/)

**`Example`**

```python 
#import package
import kmy_scrap

search_app_mod = kmy_scrap.Search_App_Mod(query='free fire')
search_rexdl = search_app_mod.rexdl(1)
search_happymod = search_app_mod.happymod()

github = kmy_scrap.Github(query='networking')
search_github = github.search(page=2)# it's looking for 1 page 
# https://github.com/search?q=networking&page=2
searches_github = github.searches(page=2) # it searches pages starting from 1 to stop at the specified page
# https://github.com/search?q=networking&page=1 and https://github.com/search?q=networking&page=2
```

## ```the result is still in string form, we need to import json to convert the result in json form```
```python
#load results
from json import loads
```
### ```display the result in json form```

```python
# Search app mod result
print(loads(search_rexdl))
print(loads(search_happymod))
```
```results``` ➡️ [rexdl](response/search_app_mod.rexdl(1).json) ➡️ [happymod](response/search_app_mod.happymod().json)

```python
#Github search results
print(loads(search_github))
print(loads(searches_github))
```
```results``` ➡️ [search_github](response/github.search(page=2).json) ➡️ [searches_github](response/github.searches(page=2).json)
<hr>

```python
# kmy_scrap
'''
random_user_agent -> (function)

list_category_OceanOfGame -> (function)

Github -> (class)
    |-> __init__(self,query:str) -> str:
    |-> total_results -> (@property)
    |-> search -> (method)
    |-> searches -> (method)

Google -> (class)
    |-> __init__(self,query:str) -> str:
    |-> get_content -> (method)
    |-> search_image -> (method)
    |-> search_query -> (method)
    |-> search_video -> (method)
    
Search_App_Mod -> (class)
    |-> __init__(self,query:str) -> str:
    |-> happymod -> (method)
    |-> rexdl -> (method)
    |-> ocean_of_game -> (method)

SourceForge -> (class)
    |-> __init__(self,query:str) -> str:
    |-> search -> (method)
'''
from kmy_scrap import *
# Parameters
Github(query:str).search(page:int)
Github(query:str).searches(page:int)

Google(query:str).get_content(url:str)
Google(query:str).search_video(max_search:int)
Google(query:str).search_image
    (
      start:int,
      related_results:bool,
      # filter result
      orientation:str, # value : portrait,landscape,square
      anim:str, # value : yes / no
      face:str, # value : yes / no
      size:str, # value : small,medium,large,wallpaper
      color:str, # value : red,orange,yellow,green,teal,purple,pink,brown,gray,white,black
      hl:str, # language
      cr:str, # country
                      )
Google(query:str).search_query
    (
      start:int, # start search
      stop:int, # end search
      lang:str, # language
      country:str, # country
                          )
                                                    
Search_App_Mod(query:str).happymod(search_mode='fast') # mode option 'fast' or 'slow'
Search_App_Mod(query:str).rexdl(page:int)
Search_App_Mod(query:str).ocean_of_game
    (
      type:str, # value : category / search
      page:int,
             )
```

# ```Update```

- ```17-01-2022``` 

add the ```ocean_of_game``` method to the ```Search_App_Mod``` class, a new ```SourceForge``` class with the ```search``` method to search.

- ```29-04-2022``` 

added search mode to happymod

results [slow](response/search_app_mod.happymod().json),  [fast](response/happymod_fast_m.json)
