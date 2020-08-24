from bs4 import BeautifulSoup;import requests,json
class Sourceforge:
    def sourceforge(self,query):
        dt = {
            "sourceforge_search_exe":{
                "page_1":{
                    "url":[],
                    "title":[],
                    "subtitle":[],
                    "last_update":[],
                    "decsription":[],
                },
                "page_2":{
                    "url":[],
                    "title":[],
                    "subtitle":[],
                    "last_update":[],
                    "decsription":[],
                },
            },
        };
        setattr(self,"query",query);setattr(self,"os",["windows","linux","android"]);#query berdasarkan OS
        setattr(self,"url_page1","https://sourceforge.net/directory/os:%s/?q=%s"%(getattr(self,"os")[0],getattr(self,"query".replace(" ","+"))));
        setattr(self,"url_page2","https://sourceforge.net/directory/os:%s/?q=%s&page=2"%(getattr(self,"os")[0],getattr(self,"query".replace(" ","+"))));
        setattr(self,"soup_1",BeautifulSoup(requests.get(getattr(self,"url_page1")).content,"html.parser"));
        setattr(self,"soup_2",BeautifulSoup(requests.get(getattr(self,"url_page2")).content,"html.parser"));
        for url_1,url_2 in zip(getattr(self,"soup_1").findAll("div",{"class":"result-heading-texts"}),getattr(self,"soup_2").findAll("div",{"class":"result-heading-texts"})):
            dt["sourceforge_search_exe"]["page_1"]["url"].append("https://sourceforge.net"+url_1.a["href"]);
            dt["sourceforge_search_exe"]["page_2"]["url"].append("https://sourceforge.net"+url_2.a["href"]);
            dt["sourceforge_search_exe"]["page_1"]["title"].append(url_1.h3.text.strip());
            dt["sourceforge_search_exe"]["page_2"]["title"].append(url_2.h3.text.strip());
        for lst1,lst2 in zip(getattr(self,"soup_1").findAll("time",{"class":"dateUpdated"}),getattr(self,"soup_2").findAll("time",{"class":"dateUpdated"})):
            dt["sourceforge_search_exe"]["page_1"]["last_update"].append(lst1.text.strip());
            dt["sourceforge_search_exe"]["page_2"]["last_update"].append(lst2.text.strip());
        for sbt1,sbt2 in zip(getattr(self,"soup_1").findAll("p",{"class":"subtitle"}),getattr(self,"soup_2").findAll("p",{"class":"subtitle"})):
            dt["sourceforge_search_exe"]["page_1"]["subtitle"].append(sbt1.text.strip());
            dt["sourceforge_search_exe"]["page_2"]["subtitle"].append(sbt2.text.strip());
        for dec1,dec2 in zip(getattr(self,"soup_1").findAll("div",{"class":"description-inner"}),getattr(self,"soup_2").findAll("div",{"class":"description-inner"})):
            dt["sourceforge_search_exe"]["page_1"]["decsription"].append(dec1.text.strip().replace("\n",""));
            dt["sourceforge_search_exe"]["page_2"]["decsription"].append(dec2.text.strip().replace("\n",""));
        srcf = json.dumps(dt,indent=3,sort_keys=True);return json.loads(srcf);
class OceanOfGame:
    def oceanofgame(self,query):
        dt = {
            "oceanofgame_search_game":{
                "results":[],
                "page1":{
                    "urls":[],
                    "title":[],
                    "img":[],
                    "update":[],
                    "sysi":[],
                },
                "page2":{
                    "urls":[],
                    "title":[],
                    "img":[],
                    "update":[],
                    "sysi":[],
                },
                "page3":{
                    "urls":[],
                    "title":[],
                    "img":[],
                    "update":[],
                    "sysi":[],
                },
                "page4":{
                    "urls":[],
                    "title":[],
                    "img":[],
                    "update":[],
                    "sysi":[],
                },
                "page5":{
                    "urls":[],
                    "title":[],
                    "img":[],
                    "update":[],
                    "sysi":[],
                },
            },
        };
        setattr(self,"query",query.replace(" ","+"));
        setattr(self,"urlq",["http://oceanofgames.com/?s=%s","http://oceanofgames.com/page/2/?s=%s",
        "http://oceanofgames.com/page/3/?s=%s","http://oceanofgames.com/page/4/?s=%s","http://oceanofgames.com/page/5/?s=%s"]);
        setattr(self,"url1",getattr(self,"urlq")[0]%(getattr(self,"query")));
        setattr(self,"url2",getattr(self,"urlq")[1]%(getattr(self,"query")));
        setattr(self,"url3",getattr(self,"urlq")[2]%(getattr(self,"query")));
        setattr(self,"url4",getattr(self,"urlq")[3]%(getattr(self,"query")));
        setattr(self,"url5",getattr(self,"urlq")[4]%(getattr(self,"query")));
        setattr(self,"req1",requests.get(getattr(self,"url1")).content);
        setattr(self,"req2",requests.get(getattr(self,"url2")).content);
        setattr(self,"req3",requests.get(getattr(self,"url3")).content);
        setattr(self,"req4",requests.get(getattr(self,"url4")).content);
        setattr(self,"req5",requests.get(getattr(self,"url5")).content);
        setattr(self,"soup1",BeautifulSoup(getattr(self,"req1"),"html.parser"));
        setattr(self,"soup2",BeautifulSoup(getattr(self,"req2"),"html.parser"));
        setattr(self,"soup3",BeautifulSoup(getattr(self,"req3"),"html.parser"));
        setattr(self,"soup4",BeautifulSoup(getattr(self,"req4"),"html.parser"));
        setattr(self,"soup5",BeautifulSoup(getattr(self,"req5"),"html.parser"));
        setattr(self,"total",getattr(self,"soup1").find("h1",{"class":"title"}));
        dt["oceanofgame_search_game"]["results"].append(getattr(self,"total").text);
        for con_page1 in getattr(self,"soup1").findAll("div",{"class":"post-details"}):
            for url1 in con_page1.findAll("a",{"class":"post-thumb"}):
                dt["oceanofgame_search_game"]["page1"]["urls"].append(url1["href"]);
                dt["oceanofgame_search_game"]["page1"]["title"].append(url1["title"]);
                dt["oceanofgame_search_game"]["page1"]["img"].append(url1.img["src"]);
            for date1 in con_page1.findAll("span",{"class":"ext"}):
                dt["oceanofgame_search_game"]["page1"]["update"].append(date1.text)
            for sysi in BeautifulSoup(requests.get(url1["href"]).content,"html.parser").findAll("div",{"class":"post-content clear-block"}):
                for sys in sysi.findAll("li"):
                    dt["oceanofgame_search_game"]["page1"]["sysi"].append(sys.text);
        for url2,url3,url4,url5 in zip(getattr(self,"soup2").findAll("h2",{"class":"title"}),
        getattr(self,"soup3").findAll("h2",{"class":"title"}),
        getattr(self,"soup4").findAll("h2",{"class":"title"}),
        getattr(self,"soup5").findAll("h2",{"class":"title"})):
            dt["oceanofgame_search_game"]["page2"]["urls"].append(url2.a["href"]);
            dt["oceanofgame_search_game"]["page3"]["urls"].append(url3.a["href"]);
            dt["oceanofgame_search_game"]["page4"]["urls"].append(url4.a["href"]);
            dt["oceanofgame_search_game"]["page5"]["urls"].append(url5.a["href"]);
            dt["oceanofgame_search_game"]["page2"]["title"].append(url2.a["title"].strip("Permanent Link: "));
            dt["oceanofgame_search_game"]["page3"]["title"].append(url3.a["title"].strip("Permanent Link: "));
            dt["oceanofgame_search_game"]["page4"]["title"].append(url4.a["title"].strip("Permanent Link: "));
            dt["oceanofgame_search_game"]["page5"]["title"].append(url5.a["title"].strip("Permanent Link: "));
            for sysi2,sysi3,sysi4,sysi5 in zip(BeautifulSoup(requests.get(url2.a["href"]).content,"html.parser").findAll("div",{"class":"post-content clear-block"}),
            BeautifulSoup(requests.get(url3.a["href"]).content,"html.parser").findAll("div",{"class":"post-content clear-block"}),
            BeautifulSoup(requests.get(url4.a["href"]).content,"html.parser").findAll("div",{"class":"post-content clear-block"}),
            BeautifulSoup(requests.get(url5.a["href"]).content,"html.parser").findAll("div",{"class":"post-content clear-block"})):
                for sy2,sy3,sy4,sy5 in zip(sysi2.findAll("li"),sysi3.findAll("li"),sysi4.findAll("li"),sysi5.findAll("li")):
                    dt["oceanofgame_search_game"]["page2"]["sysi"].append(sy2.text.strip());
                    dt["oceanofgame_search_game"]["page3"]["sysi"].append(sy2.text.strip());
                    dt["oceanofgame_search_game"]["page4"]["sysi"].append(sy2.text.strip());
                    dt["oceanofgame_search_game"]["page5"]["sysi"].append(sy2.text.strip());
        for img2,img3,img4,img5 in zip(getattr(self,"soup2").findAll("div",{"class":"post-details"}),
        getattr(self,"soup3").findAll("div",{"class":"post-details"}),
        getattr(self,"soup4").findAll("div",{"class":"post-details"}),
        getattr(self,"soup5").findAll("div",{"class":"post-details"})):
            dt["oceanofgame_search_game"]["page2"]["img"].append(img2.img["src"]);
            dt["oceanofgame_search_game"]["page3"]["img"].append(img3.img["src"]);
            dt["oceanofgame_search_game"]["page4"]["img"].append(img4.img["src"]);
            dt["oceanofgame_search_game"]["page5"]["img"].append(img5.img["src"]);
        for update2,update3,update4,update5 in zip(getattr(self,"soup2").findAll("span",{"class":"ext"}),
        getattr(self,"soup3").findAll("span",{"class":"ext"}),
        getattr(self,"soup4").findAll("span",{"class":"ext"}),
        getattr(self,"soup5").findAll("span",{"class":"ext"})):
            dt["oceanofgame_search_game"]["page2"]["update"].append(update2.text.strip());
            dt["oceanofgame_search_game"]["page3"]["update"].append(update3.text.strip());
            dt["oceanofgame_search_game"]["page4"]["update"].append(update4.text.strip());
            dt["oceanofgame_search_game"]["page5"]["update"].append(update5.text.strip());
        ocfg = json.dumps(dt,indent=3,sort_keys=True);return json.loads(ocfg);
class IpWhois:
    def ipwhois(self,query):
        setattr(self,"url","https://ipwhois.app/json/%s");
        setattr(self,"req",requests.get(getattr(self,"url")%(query)));
        setattr(self,"res",getattr(self,"req").json());
        return getattr(self,"res");
