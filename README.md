# Api-scrap

**Mesin pencarian berbasis scraping**

update kali ini benar-benar melakukan perubahan pada semua kode dari versi sebelumnya hasil yang dikembalikan pun berbeda dari versi sebelumnya,



**Daftar mesin pencarian**

- **_`Github`_** [link](https://github.com/search?q=)
- **_`Google`_** [link](https://google.com/search?q=)
- **_`HappyMod`_** [link](https://www.happymod.com/?q=)
- **_`Rexdl`_** [link](https://www.rexdl.com)

**`Menampilkan hasil`**

```python 
from kmy_scrap import Google,Github,Search_App_Mod

# parameter query ada pada class
obj = Google(query='dayaks')
result = obj.search_image(start=1)
results = obj.search_image(start=1,related_results=True)
# parameter dalam obj.search_image(**kwargs)
# ini untuk menentukan hasil yang dicari
#parameter & nilai typedata
'untuk hasil terkait'
# hl = str -> bahasa query untuk hasil terkait
# cr = str -> spesifik negara untuk hasil terkait
'untuk hasil gambar'
# start = int -> index pencarian gambar
# FILTER QUERY
# color = str -> red,orange,yellow,green,teal,purple,pink
# brown,gray,white,black -> warna gambar
# size = str -> small,medium,large,wallpaper -> ukuran gambar
# orientation = str -> portrait,landscape,square -> posisi gambar
# anim = str -> yes/no -> animasi
# face = str -> yes/no -> wajah
'hasil kembalian'
# related_results : boolean -> jika True maka hasil terkait dikembalikan
# error nilai dikembalikan,jika nilai != True
print(result,'\n\n',results)
```

***```result berhasil```*** [contoh response](response/Google('dayaks').search_image(start=1).json)

***```results berhasil```*** [contoh response](response/Google('dayaks')search_image(start=1,related_results=True)'response%20200'.json)

***```results masalah server```*** [contoh response](response/Google('dayaks')search_image(start=1,related_results=True)'error%20server'.json)

***```results masalah nilai```*** [contoh response](response/Google('dayaks')search_image(start=1,related_results='ok')'error%20value'.json)


## *Catatan!* ```dalam pypi masih versi lama belum di update,ini masih tahap pengembangan.```



[Pypi Kmy_scrap]( https://github.com/ExsoKamabay/Api-scrap)
