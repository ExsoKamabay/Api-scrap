try:
    from .enggine_search_apk import *
    from .enggine_search_exe import *
    from .github_search_file import *
except:
    from os import name,system
    if name == "nt":
        system("pip install bs4");
        system("pip install requests");
    else:
        system("pip3 install bs4");
        system("pip3 install requests");
