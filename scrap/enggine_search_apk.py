import json,requests;from bs4 import BeautifulSoup;
from googlesearch import search,get_random_user_agent;
class HappyMod:#happymod search mod apps
    def happymod(self,query):
        setattr(self,"query",query);
        dt = {
            "happymod_search_apps":{
                "urls":[],
                "title":[],
                "ratting":[],
                "img":[]
            },
        };
        setattr(self,"url","https://www.happymod.com/search.html?q=%s"%(getattr(self,"query".replace(" ","+"))))
        for title in BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser").findAll("h3",{"class":"pdt-app-h3"}):
            dt["happymod_search_apps"]["urls"].append("https://happymod.com"+title.a["href"])
            dt["happymod_search_apps"]["title"].append(title.text)
        for ratting in BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser").findAll("span",{"class":"a-search-num"}):
            dt["happymod_search_apps"]["ratting"].append(ratting.text)
        for img in BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser").findAll("a",{"class":"pdt-app-img"}):
            dt["happymod_search_apps"]["img"].append(img.img["data-original"])
        hpym = json.dumps(dt,indent=4,sort_keys=True);return json.loads(hpym);
class Uptodown:#uptodown search apps
    def uptodown(self,query=None,lang="id"):
        setattr(self,"query",query);setattr(self,"lang",lang)
        dt = {
            "uptodown_search_apps":{
                "urls":[],
                "title":[],
                "ratting":[],
                "img":[],
                "decsription":[],
                "version":[],
                "download":[],
                "name_package":[],
            },
        };
        setattr(self,"url","https://%s.uptodown.com/android/search/%s"%(getattr(self,"lang"),getattr(self,"query".replace(" ","+"))));
        try:
            for lnk in BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser").findAll("p"):
                dt["uptodown_search_apps"]["urls"].append(lnk.a["href"]);
        except:
            for title in BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser").findAll("div",{"class":"app_card_tit"}):
                dt["uptodown_search_apps"]["title"].append(title.text.strip());
            try:
                for img in BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser").findAll("img",{"class":"app_card_img"}):
                    dt["uptodown_search_apps"]["img"].append(img["src"]);
            except:
                for decsription in BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser").findAll("div",{"class":"search-text"}):
                    dt["uptodown_search_apps"]["decsription"].append(decsription.text.strip());
            for i in dt["uptodown_search_apps"]["urls"]:
                for ratting in BeautifulSoup(requests.get(i).content,"html.parser").findAll("p",{"class":"star"}):
                    dt["uptodown_search_apps"]["ratting"].append(ratting.text.strip())
                for version in BeautifulSoup(requests.get(i).content,"html.parser").findAll("p",{"class":"version"}):
                    dt["uptodown_search_apps"]["version"].append(version.text.strip())
                for download in BeautifulSoup(requests.get(i).content,"html.parser").findAll("div",id="descargas_abreviadas"):
                    dt["uptodown_search_apps"]["download"].append(download.text.strip())
                for package in BeautifulSoup(requests.get(i).content,"html.parser").findAll("li",{"class":"top_li packagename double"}):
                    for pkc in package.findAll("dd",{"class":"right"}):
                        dt["uptodown_search_apps"]["name_package"].append(pkc.text.strip());
        utdwn = json.dumps(dt,indent=8,sort_keys=True);return json.loads(utdwn);
class DlanDroid:
    def dlandroid(self,query):
        setattr(self,"query",query);
        dt = {
            "dlandroid_search_apps":{
                "urls":[],
                "decsription":[],
                "title":[],
                "img":[],
            },
        };
        setattr(self,"url","https://dlandroid.com/?s=%s"%(getattr(self,"query".replace(" ","+"))));
        setattr(self,"soup",BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser"));
        for url in getattr(self,"soup").findAll("a",{"class":"more"}):
            dt["dlandroid_search_apps"]["urls"].append(url["href"]);
        for dec in getattr(self,"soup").findAll("div",{"class":"matn-post"}):
            dt["dlandroid_search_apps"]["decsription"].append(dec.p.text.strip());
        for title in getattr(self,"soup").findAll("div",{"class":"col-lg-10 visible-lg visible-md"}):
            dt["dlandroid_search_apps"]["title"].append(title.a.text.strip());
        for img in getattr(self,"soup").findAll("a",{"class":"thumbnail icon-post"}):
            dt["dlandroid_search_apps"]["img"].append(img.img["data-src"]);
        dln =  json.dumps(dt,indent=4,sort_keys=True);return json.loads(dln);
class Gamemod:
    def gamemod(self,query):
        setattr(self,"query",query);
        dt = {
            "gamemod_search_apps":{
                "urls":[],
                "img":[],
                "title":[],
                "update":[],
            },
        };
        setattr(self,"url","https://gamemod.io/?s=%s"%(getattr(self,"query".replace(" ","+"))));
        setattr(self,"soup",BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser"));
        for url in getattr(self,"soup").findAll("h3",{"class":"entry-title td-module-title"}):
            dt["gamemod_search_apps"]["urls"].append(url.a["href"])
            dt["gamemod_search_apps"]["title"].append(url.a["title"])
        for img in getattr(self,"soup").findAll("a",{"class":"td-image-wrap"}):
            dt["gamemod_search_apps"]["img"].append(img.img["src"]);
        for update in getattr(self,"soup").findAll("span",{"class":"td-post-date"}):
            dt["gamemod_search_apps"]["update"].append(update.time["datetime"]);
        gmd = json.dumps(dt,indent=4,sort_keys=True);return json.loads(gmd);
class Rexdl:
    def rexdl(self,query):
        setattr(self,"query",query);
        dt = {
            "rexdl_search_apps":{
                "urls":[],
                "img":[],
                "title":[],
                "update":[],
                "decsription":[],
            },
        };
        setattr(self,"url","https://rexdl.com/?s=%s"%(getattr(self,"query".replace(" ","+"))));
        setattr(self,"soup",BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser"));
        for url in getattr(self,"soup").findAll("h2",{"class":"post-title"}):
            dt["rexdl_search_apps"]["urls"].append(url.a["href"]);
            dt["rexdl_search_apps"]["title"].append(url.a["title"]);
        for img in getattr(self,"soup").findAll("div",{"class":"post-thumbnail"}):
            dt["rexdl_search_apps"]["img"].append(img.img["data-src"]);
        for update in getattr(self,"soup").findAll("p",{"class":"post-date"}):
            dt["rexdl_search_apps"]["update"].append(update.text.strip());
        for dec in getattr(self,"soup").findAll("div",{"class":"entry excerpt"}):
            dt["rexdl_search_apps"]["decsription"].append(dec.p.text.strip());
        rxdl =  json.dumps(dt,indent=5,sort_keys=True);return json.loads(rxdl);
class A2zapk:
    def a2zapk(self,query):
        setattr(self,"query",query);
        dt = {
            "a2zapk_search_apps":{
                "urls":[],
                "img":[],
                "title":[],
                "update":[],
                "version":[]
            },
        };
        setattr(self,"url","https://a2zapk.com/Search/Mods/%s"%(getattr(self,"query".replace(" ","+"))));
        setattr(self,"soup",BeautifulSoup(requests.get(getattr(self,"url")).content,"html.parser"));
        for url in getattr(self,"soup").findAll("div",{"class":"AppCont"}):
            dt["a2zapk_search_apps"]["urls"].append("https://a2zapk.com"+url.a["href"]);
            dt["a2zapk_search_apps"]["title"].append(url.a["title"]);
            dt["a2zapk_search_apps"]["version"].append(url.h3.text.strip());
            dt["a2zapk_search_apps"]["update"].append(url.p.text.strip());
        try:
            for img in getattr(self,"soup").findAll("div",{"class":"ImgDiv"}):
                dt["a2zapk_search_apps"]["img"].append(img.img["data-original"])
        except:
            dt["a2zapk_search_apps"]["img"].append("None : keyError : "+query);
        apk =  json.dumps(dt,indent=5,sort_keys=True);return json.loads(apk);
class Google:
    def google_search_query(self,query,lang="id",maxSearch=10,**kwargs):
        dt = {
            "google_search_query":{
                "urls":[],
                "title":[]
            },
        };
        for i in search(query,lang=lang,start=0,stop=maxSearch,
        tld="com",safe="off",tbs="0",num=10,country=None,pause=1.5,
        domains=None,tpe="",user_agent=get_random_user_agent()):
            dt["google_search_query"]["urls"].append(i);
            tl=BeautifulSoup(requests.get(i).content,"html.parser");
            for title in tl.findAll("title"):
                dq=title.text.strip().replace("\n","");
                dt["google_search_query"]["title"].append(dq);
        ggle = json.dumps(dt,indent=2,sort_keys=True);return json.loads(ggle);
class Warna:
    @property
    def color(self):
        return {
            "red":"\033[1;31;40m",
            "blue":"\033[1;34;40m",
            "cyan":"\033[1;36;40m",
            "green":"\033[1;32;40m",
            "magenta":"\033[1;35;40m",
            "yellow":"\033[1;33;40m",
            };
