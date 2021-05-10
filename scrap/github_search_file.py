import json,requests;from bs4 import BeautifulSoup;
class Github_search_enggine:
    def search_github(self,query_usr=None):
        dt={
            "total_results":[],
            "page1":{
                "urls_h":[],
                "urls_d":[],
                "like":[],
                "update":[],
                "languange":[],
            },
            "page2":{
                "urls_h":[],
                "urls_d":[],
                "like":[],
                "update":[],
                "languange":[],
            },
            "page3":{
                "urls_h":[],
                "urls_d":[],
                "like":[],
                "update":[],
                "languange":[],
            },
            "page4":{
                "urls_h":[],
                "urls_d":[],
                "like":[],
                "update":[],
                "languange":[],
            },
            "page5":{
                "urls_h":[],
                "urls_d":[],
                "like":[],
                "update":[],
                "languange":[],
            },
        };
        setattr(self,"setq",query_usr.replace(" ","+"))
        setattr(self,"urlq",["https://github.com/search?q=%s",
        "https://github.com/search?p=2&q=%s&type=Repositories",
        "https://github.com/search?p=3&q=%s&type=Repositories",
        "https://github.com/search?p=3&q=%s&type=Repositories",
        "https://github.com/search?p=4&q=%s&type=Repositories"]);
        setattr(self,"req1",requests.get(getattr(self,"urlq")[0]%(getattr(self,"setq"))).content);
        setattr(self,"req2",requests.get(getattr(self,"urlq")[1]%(getattr(self,"setq"))).content);
        setattr(self,"req3",requests.get(getattr(self,"urlq")[2]%(getattr(self,"setq"))).content);
        setattr(self,"req4",requests.get(getattr(self,"urlq")[3]%(getattr(self,"setq"))).content);
        setattr(self,"req5",requests.get(getattr(self,"urlq")[4]%(getattr(self,"setq"))).content);
        setattr(self,"soup1",BeautifulSoup(getattr(self,"req1"),"html.parser"));
        setattr(self,"soup2",BeautifulSoup(getattr(self,"req2"),"html.parser"));
        setattr(self,"soup3",BeautifulSoup(getattr(self,"req3"),"html.parser"));
        setattr(self,"soup4",BeautifulSoup(getattr(self,"req4"),"html.parser"));
        setattr(self,"soup5",BeautifulSoup(getattr(self,"req5"),"html.parser"));
        for total_results in getattr(self,"soup1").findAll("div",{"class":"d-flex flex-column flex-md-row flex-justify-between border-bottom pb-3 position-relative"}):
            dt["total_results"].append(total_results.h3.text.strip());
        for con_url1 in getattr(self,"soup1").findAll("div",{"class":"mt-n1"}):
            for url1 in con_url1.findAll("a",{"class":"v-align-middle"}):
                dt["page1"]["urls_d"].append("https://github.com"+url1["href"]+"/archive/master.zip");
                dt["page1"]["urls_h"].append("https://github.com"+url1["href"]);
            for lang1 in con_url1.findAll("span",{"itemprop":"programmingLanguage"}):
                dt["page1"]["languange"].append(lang1.text);
            for like1 in con_url1.findAll("a",{"class":"muted-link"}):
                dt["page1"]["like"].append(like1.text.strip().replace("\n",""));
            for update1 in con_url1.findAll("relative-time",{"class":"no-wrap"}):
                dt["page1"]["update"].append(update1["datetime"]);
        for url2,url3,url4,url5 in zip(getattr(self,"soup2").findAll("a",{"class":"v-align-middle"}),
        getattr(self,"soup3").findAll("a",{"class":"v-align-middle"}),
        getattr(self,"soup4").findAll("a",{"class":"v-align-middle"}),
        getattr(self,"soup5").findAll("a",{"class":"v-align-middle"})):
            dt["page2"]["urls_d"].append("https://github.com"+url2["href"]+"/archive/master.zip");
            dt["page3"]["urls_d"].append("https://github.com"+url3["href"]+"/archive/master.zip");
            dt["page4"]["urls_d"].append("https://github.com"+url4["href"]+"/archive/master.zip");
            dt["page5"]["urls_d"].append("https://github.com"+url5["href"]+"/archive/master.zip");
            dt["page2"]["urls_h"].append("https://github.com"+url2["href"]);
            dt["page3"]["urls_h"].append("https://github.com"+url3["href"]);
            dt["page4"]["urls_h"].append("https://github.com"+url4["href"]);
            dt["page5"]["urls_h"].append("https://github.com"+url5["href"]);
        for lang2,lang3,lang4,lang5 in zip(getattr(self,"soup2").findAll("span",{"itemprop":"programmingLanguage"}),
        getattr(self,"soup3").findAll("span",{"itemprop":"programmingLanguage"}),
        getattr(self,"soup4").findAll("span",{"itemprop":"programmingLanguage"}),
        getattr(self,"soup5").findAll("span",{"itemprop":"programmingLanguage"})):
            dt["page2"]["languange"].append(lang2.text);
            dt["page3"]["languange"].append(lang3.text);
            dt["page4"]["languange"].append(lang4.text);
            dt["page5"]["languange"].append(lang4.text);
        for like2,like3,like4,like5 in zip(getattr(self,"soup2").findAll("a",{"class":"muted-link"}),
        getattr(self,"soup3").findAll("a",{"class":"muted-link"}),
        getattr(self,"soup4").findAll("a",{"class":"muted-link"}),
        getattr(self,"soup5").findAll("a",{"class":"muted-link"})):
            dt["page2"]["like"].append(like2.text.strip().replace("\n",""));
            dt["page3"]["like"].append(like3.text.strip().replace("\n",""));
            dt["page4"]["like"].append(like4.text.strip().replace("\n",""));
            dt["page5"]["like"].append(like4.text.strip().replace("\n",""));
        for update2,update3,update4,update5 in zip(getattr(self,"soup2").findAll("relative-time",{"class":"no-wrap"}),
        getattr(self,"soup3").findAll("relative-time",{"class":"no-wrap"}),
        getattr(self,"soup4").findAll("relative-time",{"class":"no-wrap"}),
        getattr(self,"soup5").findAll("relative-time",{"class":"no-wrap"})):
            dt["page2"]["update"].append(update2["datetime"]);
            dt["page3"]["update"].append(update3["datetime"]);
            dt["page4"]["update"].append(update4["datetime"]);
            dt["page5"]["update"].append(update4["datetime"]);
        gthb = json.dumps(dt,indent=5,sort_keys=True);return json.loads(gthb);
    
class picSearch:
    def __init__(self):
        setattr(self,"Upage",["http://www.picsearch.com/index.cgi?q=%s",
        "http://www.picsearch.com/index.cgi?start=31&q=%s",
        "http://www.picsearch.com/index.cgi?start=61&q=%s",
        "http://www.picsearch.com/index.cgi?start=90&q=%s",
        "http://www.picsearch.com/index.cgi?start=117&q=%s"]);
    def picsearch_pages1(self,query):
        dt={
            "searchImage":{
                "page1":{
                    "sites":[],
                    "images":[],
                },
            },
        };
        setattr(self,"query",query.replace(" ","+"));
        setattr(self,"set_query1",getattr(self,"Upage")[0]%(getattr(self,"query")));
        setattr(self,"setReques1",requests.get(getattr(self,"set_query1")).content);
        setattr(self,"soup1",BeautifulSoup(getattr(self,"setReques1"),"html.parser"));
        for u1_img in getattr(self,"soup1").findAll("span",{"class","result"}):
            dt["searchImage"]["page1"]["images"].append("https:"+u1_img.img["src"]);
            site = requests.get(u1_img.a["href"]).content;
            soup = BeautifulSoup(site,"html.parser");
            for sites in soup.findAll("div",{"class":"detail-links"}):
                dt["searchImage"]["page1"]["sites"].append(sites.a["href"]);
        dmp = json.dumps(dt,indent=2,sort_keys=True);return json.loads(dmp);
    def picSearch_pages2345(self,query):
        dt = {
            "searchImage":{
                "page2":{
                    "sites":[],
                    "images":[],
                },
                "page3":{
                    "sites":[],
                    "images":[],
                },
                "page4":{
                    "sites":[],
                    "images":[],
                },
                "page5":{
                    "sites":[],
                    "images":[],
                },
            },
        };
        setattr(self,"query",query.replace(" ","+"));
        setattr(self,"set_query2",getattr(self,"Upage")[1]%(getattr(self,"query")));
        setattr(self,"set_query3",getattr(self,"Upage")[2]%(getattr(self,"query")));
        setattr(self,"set_query4",getattr(self,"Upage")[3]%(getattr(self,"query")));
        setattr(self,"set_query5",getattr(self,"Upage")[4]%(getattr(self,"query")));
        setattr(self,"setReques2",requests.get(getattr(self,"set_query2")).content);
        setattr(self,"setReques3",requests.get(getattr(self,"set_query3")).content);
        setattr(self,"setReques4",requests.get(getattr(self,"set_query4")).content);
        setattr(self,"setReques5",requests.get(getattr(self,"set_query5")).content);
        setattr(self,"soup2",BeautifulSoup(getattr(self,"setReques2"),"html.parser"));
        setattr(self,"soup3",BeautifulSoup(getattr(self,"setReques3"),"html.parser"));
        setattr(self,"soup4",BeautifulSoup(getattr(self,"setReques4"),"html.parser"));
        setattr(self,"soup5",BeautifulSoup(getattr(self,"setReques5"),"html.parser"));
        for u2_img,u3_img,u4_img,u5_img in zip(getattr(self,"soup2").findAll("span",{"class","result"}),
        getattr(self,"soup3").findAll("span",{"class","result"}),
        getattr(self,"soup4").findAll("span",{"class","result"}),
        getattr(self,"soup5").findAll("span",{"class","result"})):
            dt["searchImage"]["page2"]["images"].append("https:"+u2_img.img["src"]);
            dt["searchImage"]["page3"]["images"].append("https:"+u3_img.img["src"]);
            dt["searchImage"]["page4"]["images"].append("https:"+u4_img.img["src"]);
            dt["searchImage"]["page5"]["images"].append("https:"+u5_img.img["src"]);
            site2 = requests.get(u2_img.a["href"]).content;
            site3 = requests.get(u3_img.a["href"]).content;
            site4 = requests.get(u4_img.a["href"]).content;
            site5 = requests.get(u5_img.a["href"]).content;
            soup2 = BeautifulSoup(site2,"html.parser");
            soup3 = BeautifulSoup(site3,"html.parser");
            soup4 = BeautifulSoup(site4,"html.parser");
            soup5 = BeautifulSoup(site5,"html.parser");
            for sites2,sites3,sites4,sites5 in zip(soup2.findAll("div",{"class":"detail-links"}),
            soup3.findAll("div",{"class":"detail-links"}),
            soup4.findAll("div",{"class":"detail-links"}),
            soup5.findAll("div",{"class":"detail-links"})):
                dt["searchImage"]["page2"]["sites"].append(sites2.a["href"]);
                dt["searchImage"]["page3"]["sites"].append(sites3.a["href"]);
                dt["searchImage"]["page4"]["sites"].append(sites4.a["href"]);
                dt["searchImage"]["page5"]["sites"].append(sites5.a["href"]);
        dmp = json.dumps(dt,indent=2,sort_keys=True);return json.loads(dmp);
    def picSearch_All(self,query):
        self.results = {
            'page1':self.picsearch_pages1(query),
            'page2345':self.picSearch_pages2345(query)
        }
        return json.loads(json.dumps(self.results,indent=1,sort_keys=True));
