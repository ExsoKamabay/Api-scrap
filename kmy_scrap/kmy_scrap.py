import json,requests,random
from time import sleep as timeout
from youtube_search import YoutubeSearch
from urllib.parse import quote_plus;from bs4 import BeautifulSoup

def random_user_agent():
    return {'User-Agent':random.choice((
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    ))}
    

class Github:
    def __init__(self,query='exso kamabay'):
        self.query = quote_plus(query)
        self.url = f"https://github.com/search?p=%s&q={self.query}&type=Repositories"

    @property
    def total_results(self):
        try:
            self.get = requests.get(self.url%(1),headers=random_user_agent())
            if self.get.status_code != 200:
                return 'Invalid response! %s'%(self.get.status_code)
            else:
                self.soup = BeautifulSoup(self.get.content,'html.parser')
                self.find_ = self.soup.find('div',{'class','d-flex flex-column flex-md-row flex-justify-between border-bottom pb-3 position-relative'})
                return (self.find_.h3.text.replace('   ','').replace('\n',''))
        except:return 'Check your internet connection!'

    def search(self,page:int):
        try:
            self.lst = [];
            self.get = requests.get(self.url%(page),headers=random_user_agent())
            if self.get.status_code == 200:
                self.soup = BeautifulSoup(self.get.content,'html.parser')
                for url,dec,star,lang,up in zip(
                    self.soup.find_all('a',{'class':'v-align-middle'}),
                    self.soup.find_all('p',{'class':'mb-1'}),
                    self.soup.find_all('a',{'class':'Link--muted'}),
                    self.soup.find_all('span',{'itemprop':'programmingLanguage'}),
                    self.soup.find_all('relative-time',{'class':'no-wrap'}),
                    ):
                    self.lst.append({
                        'url':f"https://github.com{url['href']}",
                        'star':star.text.replace(' ','').strip('\n').replace('\n',' '),
                        'upload':up.text,
                        'language':lang.text,
                        'decription':dec.text.replace('    ','').strip('\n').replace('\n',''),
                        })
                return json.dumps({"search":self.lst},indent=2,sort_keys=True)
            else:return "Invalid response %s"%(self.get.status_code)
        except:pass

    def searches(self,page:int):
        self.lst = []
        self.list = []
        for i in range(page):
            self.value = self.search(self.url%(i+1))
            self.list.append(self.value)
        for y in self.list:
            for x in json.loads(y)['search']:
                self.lst.append(x)
        return json.dumps({"searches":self.lst},indent=2,sort_keys=True)


class Google:
    """query string"""
    def __init__(self,query='exso kamabay'):
        self.query = quote_plus(query)
        # Templates
        self.urlp = f"https://www.picsearch.com/index.cgi?q={self.query}"
        self.urlq = f"https://www.google.com/search?q={self.query}&safe=off"#&hl=%(language)s&cr=%(country)s&num=%(stop)s"%vars()
        self.urli = f"https://www.google.com/search?q={self.query}&tbm=isch"


    def get_content(self,url) -> str:
        """Mengambil konten alamat url"""
        try:
            self.url = requests.get(url,headers=random_user_agent())
            if self.url.status_code == 200:return self.url.content
            else:return f"Response status code {self.url.status_code}"
        except:return "Check koneksi internet!"

    def search_image(self,**kwargs):
        """
        Untuk 'images'
        start : int -> index pencarian 
        related_results : boolean -> mengembalikan hasil terkait
        Filter Pencarian
        color : str -> warna 
        :red,orange,yellow,green,teal,purple,pink,brown,gray,white,black
        size : str -> ukuran
        :small,medium,large,wallpaper
        orientation : str -> orientasi
        :portrait,landscape,square
        anim : str -> yes/no -> animasi
        face : str -> yes/no -> wajah
        Untuk 'related_results'
        hl : str -> bahasa query
        cr : str -> spesifik negara untuk hasil query
        """
        def related_results():
            self.lst_rst = []
            if not kwargs:
                return "no keywords!";
            else:
                for k,v in kwargs.items():
                    if k in ('hl','cr'):
                        self.urli += f'&%s=%s'%(k,v)
                    else:pass
            self.soup = BeautifulSoup(self.get_content(self.urli),'html.parser')
            for i in self.soup.find_all('a',{'class':'VFACy kGQAp sMi44c lNHeqe WGvvNb'}):
                try:
                    self.lst_rst.append({'title':i['title'],'url':i['href']})
                except:pass
            if not self.lst_rst:return 'terjadi kesalahan,silakan coba lagi!'
            else:return self.lst_rst;
        def search_results():
            self.lst_rst = []
            if not kwargs:pass
            else:
                for k,v in kwargs.items():
                    if k in ('color','size','orientation','anim','face','start'):
                        self.urlp += '&%s=%s'%(k,v)
                    else:pass
            self.soup = BeautifulSoup(self.get_content(self.urlp),'html.parser')
            for i,d in zip(
                self.soup.find_all('span',{'class':'result'}),
                self.soup.find_all('span',{'class':'dimensions'})):
                self.lst_rst.append({'url':'http:'+i.a.img['src'],'size':d.text})
            return self.lst_rst;
        if 'related_results' in kwargs.keys():
            if kwargs['related_results'] == True:
                return json.dumps({
                    'images':search_results(),
                    'related_results':related_results()
                },indent=2)
            else:
                return json.dumps({
                        'images':search_results(),
                        'related_results':'%s tidak valid, silakan diubah ke True'%(kwargs['related_results']),
                    },indent=1)
        else:return json.dumps({'images':search_results()},indent=1)

    def search_query(self,**kwargs):
        """
        start : int -> start search
        stop : int -> stop search
        lang : str -> language query
        country : str -> country code
        """
        if not kwargs:
            return "no keywords!";
        else:
            self.results = []
            def filter_(url):
                remove = url.strip('/url?q=')
                find = remove.find('&sa=U&ved=')
                return remove[:find]
            self.dict = dict({'lang':'hl','country':'cr','start':'start','stop':'num'})
            for k,v in kwargs.items():
                if k in self.dict.keys():
                    self.urlq += "&%s=%s"%(self.dict[k],v)
                else:pass
            self.soup = BeautifulSoup(self.get_content(self.urlq),'html.parser')
            for u,d,t in zip(
                self.soup.find_all('div',{'class':'kCrYT'}),
                self.soup.find_all('div',{'class':'BNeawe s3v9rd AP7Wnd'}), 
                self.soup.find_all('div',{'class':'BNeawe vvjwJb AP7Wnd'})
                ):
                if not 'pause' in kwargs.keys():pass
                else:timeout(kwargs['pause'])
                try:
                    # result
                    self.results.append({'url':filter_(u.a['href']),'title':t.text,'decription':d.text})
                except:pass
            if not self.results:
                return "sorry an error occurred please try again!"
            else:return json.dumps(self.results,indent=1,sort_keys=True)

    def search_video(self,max_search=5):
        "maximal search"
        self.query_ = self.query.replace('+',' ')
        self.results = YoutubeSearch(self.query_,max_search)
        return json.dumps(self.results.to_dict(),indent=2)


class Search_App_Mod:
    'query string'
    def __init__(self,query:str) -> str:
        self.query = quote_plus(query);

    def happymod(self) -> None:
        self.results = []
        try:self.gets = requests.get(f'https://happymod.com/search.html?q={self.query}',params=random_user_agent())
        except:return "Check Your Internet Connection!"
        self.urls = BeautifulSoup(self.gets.content,'html.parser').find_all('a',{'class':'pdt-app-img'})
        for i in self.urls:
            self.ipk = i['href'].strip('/')
            self.rpk = self.ipk.find('/')
            self.url = BeautifulSoup(
                requests.get(f"https://happymod.com{i['href']}",
                headers=random_user_agent()).content,'html.parser');
            for name,info,ftur,img,link in zip(
                self.url.find_all('div',{'class':'new-div-box new-pdt-bg-box'}),
                self.url.find_all('ul',{'class':'new-pdt-ul clearfix'}),
                self.url.find_all('div',{'class':'new-pdt-msg-box'}),
                self.url.find_all('img',{'class':'lazy'}),
                self.url.find_all('a',{'class':'download-btn'})
                ):
                self.results.append([{
                    "App":i['title'],
                    'app_info':[{
                        'name':name.h3.text,
                        'icon':img['data-original'],
                        'package':self.ipk[self.rpk:].strip('/'),
                        'detail':info.text.replace('-','').strip('\n').replace('\n',','),
                        'download':'https://happymod.com'+link['href'],
                        'decription':ftur.p.text.replace('\t','').replace('\n',' ').replace('\u221a','').replace('\r','')
                    }]
                    }])
        return json.dumps({"Results":self.results},indent=1)
    
    def rexdl(self,page:int) -> int:
        self.ls_results = []
        def search_url():
            results = [];
            for i in range(page):
                for u in BeautifulSoup(requests.get(f"https://rexdl.com/page/{i+1}/?s={self.query}",
                    params=random_user_agent()).content,'html.parser').find_all('h2',{'class':'post-title'}):
                    results.append({'url':u.a['href'],'title':u.a['title']})
            return results;
        for i in search_url():
            self.soup = BeautifulSoup(requests.get(i['url'],params=random_user_agent()).content,'html.parser')
            for dec,nw,ld in zip(
                self.soup.find_all('div',{'class':'entry-inner'}),
                self.soup.find_all('div',{'class':'DWPxHb'}),
                self.soup.find_all('span',{'class':'readdownload a'})):
                self.link_i = BeautifulSoup(requests.get(ld.a['href'],params=random_user_agent()).content,'html.parser')
                for up,vr,fs,pw in zip(
                    self.link_i.find_all('li',{'class':'dl-update'}),
                    self.link_i.find_all('li',{'class':'dl-version'}),
                    self.link_i.find_all('li',{'class':'dl-size'}),
                    self.link_i.find_all('a',{'title':'www.rexdl.com'})):
                    self.ls_results.append({
                        'Home':[{
                            'url':i['url'],
                            'title':i['title'],
                            'wts new':nw.text,
                            'decription':dec.text}],
                        'Download':[{
                            'url':ld.a['href'],
                            'update':up.text.strip('Update:'),
                            'version':vr.text.strip('Current Version:'),
                            'size':fs.text.strip('File Size:'),
                            'password':pw['title']}]})
        return json.dumps(self.ls_results,indent=1)

