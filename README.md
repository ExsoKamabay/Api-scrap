# kmy_scrap

# *`apikey search enggine scraping based!`*


## **`like this site!`**

- **_`Github`_** [link](https://github.com/search?q=)
- **_`Google`_** [link](https://google.com/search?q=)
- **_`HappyMod`_** [link](https://www.happymod.com/?q=)
- **_`Rexdl`_** [link](https://www.rexdl.com)

**`Example`**

```python 
#import package
from kmy_scrap import Google,Github,Search_App_Mod

google = Google(query='wolf')
google_search = google.search_query(start=1,stop=20)
google_image = google.google.search_image(start=1,related_results=True)
google_video = google.search_video(max_search=10)

search_app_mod = Search_App_Mod(query='free fire')
search_rexdl = search_app_mod.rexdl(1)
search_happymod = search_app_mod.happymod()

github = Github(query='networking')
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
# Google search result
print(loads(google_search))
print(loads(google_image))
print(loads(google_video))
```
```results``` ➡️ [google_search](response/google.search_query(start=1,stop=10).json) ➡️ [google_image](response/google.search_image(start=1,related_results=True).json)  ➡️  [google_video](response/google.search_video(max_search=10).json)

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
