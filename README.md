# kmy_scrap

# *`apikey search enggine scraping based!`*


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
                                                    
Search_App_Mod(query:str).happymod()
Search_App_Mod(query:str).rexdl(page:int)
Search_App_Mod(query:str).ocean_of_game
    (
      type:str, # value : category / search
      page:int,
             )
```
<hr>

```python
import kmy_scrap

happymod = kmy_scrap.Search_App_Mod('free fire')
print(happymod.happymod())
```

***Results***

```json
{
 "Results": [
  [
   {
    "App": "lulubox APK ",
    "app_info": [
     {
      "name": "lulubox APK Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/6/1/2/682c1728df6d012b181047ef739e76e2.jpg",
      "package": "com.lulu.lulubox",
      "detail": " Version: 4.9.9, Size: 12.39 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/lulubox-mod/com.lulu.lulubox/download.html",
      "decription": "Lulubox is all in one game plugin box for Android game players. Like parallel space, you will create new game account to play games. Please do remember to open games in Lulubox, because no magic will happen once you run the game directly with your real game account.   Sign in social account:  Not supported  Game online or offline:  Offline  Root Needed?: No   License Needed?: No Install Steps: 1) Download APK files on happymod.com. 2.) Install and Enjoy. Also read: COC MOD. Mod info: unlimted money and unlimited coins, private server.  "
     }
    ]
   }
  ],
  [
   {
    "App": "Garena Free Fire MAX ",
    "app_info": [
     {
      "name": "Garena Free Fire MAX Mod Apk:",
      "icon": "https://i.git99.com/app_img/20220323/79/79/55/1648049435.jpg",
      "package": "com.dts.freefiremax",
      "detail": " Version: 2.60.1, Size: 884.24 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/garena-free-fire-max-mod/com.dts.freefiremax/download.html",
      "decription": " Garena Free Fire MAX Mod Garena Free Fire MAX Mod APK v2.60.1 Features:  ff max free mod apk + data by MineYoussefYT  Free Fire MAX is designed exclusively to deliver premium gameplay experience in a Battle Royale! Enjoy a variety of exciting game modes with Free Fire players via exclusive Firelink technology. Experience combat like never before with Ultra HD resolutions and breathtaking effects. Ambush, snipe, and survive; There is only one goal: to survive and be the last one standing.[Firelink technology]With Firelink, you can use your account to play Free Fire MAX and Free Fire using the same account without any hassle. This means your progress and collectibles are maintained across both applications, and you can play all game modes with all Free Fire players, no matter which application they are using.[Hassle free installation]Free Fire MAX offers all additional packages straight up after booting the game for the first time. Enjoy the MAX experience right away![Same game, maximized experience]With Ultra HD resolutions, breathtaking effects, and realistic animations, MAX elevates Free Fire graphics and delivers the best survival experience you will find on mobile.[50 players, 10 minutes, 1 survivor]50 players parachute onto a graphically rich island (or desert), scavenging for weapons. Stay in the safe zone, and take down your enemies along the way. Compete for legendary airdrops to gain an extra edge against other survivors, and be the last one standing. All within 10 minutes.[4-man squad, with in-game voice chat]Create squads of up to 4 players and establish communication with your squad right from the start. Lead your friends to victory and be the last team standing victorious at the apex![Contact us]Customer Service: https://goo.gl/8f5918 "
     }
    ]
   }
  ],
  [
   {
    "App": "Cover Fire: Offline Shooting Mod Apk 1.21.28  ",
    "app_info": [
     {
      "name": "Cover Fire: Offline Shooting Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/5/1/3/556d25e4d820dec1f9a4798f649ab573.jpg",
      "package": "com.generagames.resistance",
      "detail": " Version: 1.21.28, Size: 310.43 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/cover-fire-mod/com.generagames.resistance/download.html",
      "decription": "Cover Fire: Shooting Games PRO Mod game is an action game with unlimited money. In this mod game, you can get all things for free. You will get anything in the game. In a word, you will enjoy the game better with this mod.  Root Needed?: No   License Needed?: No  Install Steps: 1) This is a game with Obb file, please download APK + Obb on HappyMod App. 2.) Install and Enjoy. Also read: COC MOD. Mod info: unlimted money and unlimited coins, private server. "
     }
    ]
   }
  ],
  [
   {
    "App": "BOOYAH! Mod Apk 1.37.1 [Unlimited money] ",
    "app_info": [
     {
      "name": "BOOYAH! Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210702/6/35/40/1625196036.jpg",
      "package": "com.mambet.tv",
      "detail": " Version: 1.37.1, Size: 16.45 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/booyah-mod/com.mambet.tv/download.html",
      "decription": " BOOYAH! Mod BOOYAH! Mod APK v1.37.1 Features:  unlimited coin tickits  BOOYAH! offers enjoyable short gaming videos generated by its' users. With our app you are able to livestream to major streaming platforms. It can also help to automatically capture your precious gaming moments, for you to share with your friends and community! Experience the games you love like never before, and connect with your friends through gaming. Top features of BOOYAH!:- Short gaming videos (clips). Swipe down to see exciting game moments shared by our community! Upload your own clip and share fun with viewers from all over the world!  - Livestream to major streaming platforms (Facebook Gaming, Youtube Gaming, Twitch). You can restream your favourite game and chat with your viewers from all platforms simultaneously, without any fee or membership!- Highlights. After your livestream ends, our app will generate highlight with key moments where you experience intense fight, adventure and emotions!Share your proudest game moments with your friends on social networks with a touch.Play and record your games at the same time, you are just moments away from becoming the next gaming star! Be a part of the latest innovation in sharing your gameplay! Be it godlike moments, epic comebacks, or funny fails, BOOYAH! helps you capture them all! For feedback and assistance, or business collaboration, please contact us at [email\u00a0protected] "
     }
    ]
   }
  ],
  [
   {
    "App": "Drone 2 - Free Fire Mod Apk 2.2.142  ",
    "app_info": [
     {
      "name": "Drone 2 - Free Fire Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210709/89/3/88/1625836442.jpg",
      "package": "com.reliancegames.ss2",
      "detail": " Version: 2.2.142, Size: 576.73 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/drone-2-air-assault-unreleased-mod/com.reliancegames.ss2/download.html",
      "decription": " Drone 2 - Free Fire Mod Drone -Air Assault v2.2.142 mod Features:  Get money, gold bars, diamonds increases  [Note] English first start the game, restart the game to change the language to Chinese.  Battle Strike Gunship Assault puts you in command of specialized aerial warfare gunships with 120 action-packed missions and campaigns for you to take on. Battle across the world, take command of Hi-Tech aerial assault vehicles and establish PVP supremacy from your strike carrier Damocles. Perform lethal strikes, defend allies and destroy targets globally to restore World Peace.DIVERSE MISSIONS Disrupt the enemy control, provide close Air Support and raid Enemy Bases worldwide before they take you out. Strategize in Annihilate, Defend, Hunt and Precision Strike missions.REALISTIC COMBAT ENVIRONMENTSEngage with 50 types of authentic attack units \u2013 gunships, snipers, armoured cars, tanks and attack helicopters. Adapt to changing terrain, sandstorms & fog using multiple vision modes - FLIR and Night Vision.BUILD YOUR ARSENAL Equip your vehicles with devastating Cannons, Guided Missiles, Rockets, Machine Guns, AMRs & Bombs to bring the rain.COMMAND FUTURISTIC VEHICLESStrategize your attacks with Light Altitude Vehicles (LAVs) for precision targeting and High Altitude Vehicles (HAVs) for greater area damage.SUPER RAPTOR or THUNDERBIRD GUNSHIPExecute preciselow level attacks with the Super Raptor, or rain heavy ordinance, using the Thunderbird gunship.ESTABLISH PVP SUPREMACY FROM YOUR STRIKE CARRIERDestroy opponent carriers to collect Intel & Steal resources. Defend yourself by building your Strike Fleet Destroyers and Shield ships with advanced weaponry.JOIN THE EXCLUSIVE CLUB OF \u2018BATTLE STRIKE GUNSHIP ASSAULT' FANSEnjoy regular news on game updates, characters, features, views, video tips and more for FreeLike us on facebook: https://www.facebook.com/Drone2AAFollow us on twitter: https://twitter.com/Drone2AA Watch us on youtube: http://www.youtube.com/reliancegamesVisit us: http://www.shadowstrike2.com/This game is completely free to download and play. However, some game items can be purchased with real money within the game. You can restrict in-app purchases in your store's settings.Note: A network connection is required to play. "
     }
    ]
   }
  ],
  [
   {
    "App": "Fire Emblem Heroes Mod Apk 1.3.0  ",
    "app_info": [
     {
      "name": "Fire Emblem Heroes Mod Apk:",
      "icon": "https://i.git99.com/app_img/20220326/95/49/8/1648252229.jpg",
      "package": "com.nintendo.zaba",
      "detail": " Version: 1.3.0, Size: 41.1 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/fire-emblem-heroes-mod/com.nintendo.zaba/download.html",
      "decription": " Fire Emblem Heroes Mod Fire Emblem Heroes MOD Android Download 1.3.0 Features:  Feather/Crystal/badge IncreasedRarity EditorSkill Point and Limit breaker editor  Android MOD APK Download Fire Emblem Heroes Unlimited Money Fire Emblem purely going on a gameplay basis is very simple and yields itself well to a mobile installment I\u2019m just surprised this didn\u2019t happen sooner. It is a strategy game where you move your own units to try to attack enemy units moving your units around in an attempt to defeat the enemy. often requires a bit of strategy and careful thinking that\u2019s really where the great fun of Fire Emblem comes in. it\u2019s fun to try to route the enemy when you\u2019re faced with a challenging situation. Fire Emblem heroes MOD on iOS or Android it works in pretty much the same way. you move your units with your finger and try not to get defeated yourself like I said the Gameplay is pretty simple and something really anybody can get into. this is an enjoyable game to play between class periods and during lunch if you don\u2019t have anybody to socialize with like me I have to give Nintendo props for making a mobile game that\u2019s accessible free and fun to play. ALSO TRY SUPER MARIO RUN WITH MOD APK This is by far the best mobile game they\u2019ve put out so far plus I actually feel like I\u2019m going to play more of Fire Emblem heroes unlike Super Mario run now. the game itself is pretty basic the maps are nothing to thought provoking or interesting and most of the time you just need to overpower the enemy rather than device tactics to outsmart them. sure you could make the argument that since this is a mobile Fire Emblem game I shouldn\u2019t be expecting the same quality standard that I would get on a console Fire Emblem game or a handheld one. Fire Emblem fans there\u2019s quite a bit of fanservice here and the way that you can see your favorite characters from the franchise in one small group collecting all of these heroes that you might have played with throughout. the whole entirety of the Fire Emblem franchise is something I imagine fans will really get a kick out of not to mention the great music. if you\u2019re someone who doesn\u2019t know anything about fire emblem this is still a game you can get into and have fun. Easiest Way to get Unlimited Feather,Money,Crystal,orbs and Badge in Fire Emblem Heroes is to install the MOD APK and Play it.you can not play Fire Emblem Heroes Offline with MOD. "
     }
    ]
   }
  ],
  [
   {
    "App": "ShellFire - MOBA FPS Mod Apk 1.16  ",
    "app_info": [
     {
      "name": "ShellFire - MOBA FPS Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210709/92/6/61/1625802637.jpg",
      "package": "id.co.duniagames.android.mobafps",
      "detail": " Version: 1.16, Size: 29.67 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/shellfire-moba-fps-mod/id.co.duniagames.android.mobafps/download.html",
      "decription": " ShellFire - MOBA FPS Mod ShellFire MOBA FPS  1.16 Fraudulent Features:  Fraudulent  With ShellFire we are entering a new generation first-person shooter and MOBA concept.  "
     }
    ]
   }
  ],
  [
   {
    "App": "Kill It With Fire Mod Apk 1.0 [Paid for free] ",
    "app_info": [
     {
      "name": "Kill It With Fire Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210709/98/92/82/1625818777.jpg",
      "package": "com.tinybuildgames.killitwithfire",
      "detail": " Version: 1.0, Size: 640.32 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/kill-it-with-fire-mod/com.tinybuildgames.killitwithfire/download.html",
      "decription": " Kill It With Fire Mod Kill It With Fire Mod APK 1.0 Features:  All paid content of this game is available  The spider - mankind's most ancient and deadly nemesis. As a licensed Kill It With Fire exterminator, it's time to fight back! Assemble your arsenal of increasingly excessive weapons, track spiders across suburbia, and burn everything in your path!To defeat spiders you must exploit their one weakness: FIRE. Or bullets. Or explosions, throwing stars, gettin' smushed by stuff...pretty much anything, really. But that doesn't mean it'll be easy - first you've gotta find the spiders. Use state-of-the-art arachnid tracking technology to pinpoint your target's location among hundreds of potential hiding spots - then, torch everything and smash the spider with a frying pan after it runs out. It's the only way to be sure.Features- Tons of unique weapons and equipment.- Eight different spider species.- \u201cRealistic\u201d fire simulation system.- Gratuitous chaos and destruction.- Dozens of optional objectives.- Loads of hidden upgrades.- Battle in the Arachno-Gauntlet!- A secret ending?!?! (...shh!) "
     }
    ]
   }
  ],
  [
   {
    "App": "Fire Hero 2 Mod Apk 1.23  ",
    "app_info": [
     {
      "name": "Fire Hero 2 Mod Apk:",
      "icon": "https://i.git99.com/app_img/20220207/23/61/65/1644230103.jpg",
      "package": "com.EveryDayGames.FireHero2",
      "detail": " Version: 1.23, Size: 29.64 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/fire-hero-2-mod/com.EveryDayGames.FireHero2/download.html",
      "decription": " Fire Hero 2 Mod Fire Hero 2 v1.23 mod Features:  Gold coins use not to reduce  New version with new challenges. Meet new opponents and new abilities! "
     }
    ]
   }
  ],
  [
   {
    "App": "Modern Ops: Gun Shooting Games Mod Apk 7.11  ",
    "app_info": [
     {
      "name": "Modern Ops: Gun Shooting Games Mod Apk:",
      "icon": "https://i.git99.com/app_img/20220131/42/85/18/1643612723.jpg",
      "package": "com.edkongames.mobs",
      "detail": " Version: 7.11, Size: 560.53 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/modern-ops-online-pvp-shooter-mod/com.edkongames.mobs/download.html",
      "decription": " Modern Ops: Gun Shooting Games Mod Modern Ops: Gun Shooting Games v7.11 mod Features:  In the game, the cheat menu is created, click the button button to enter the upper left corner button.  Mod Menu  2. No gravity // Remove gravity  3. SPEED MULTIPLIER / / Increase Mobile Speed  4. SET FOV / / Custom FOV  5. AIM assist // increase aiming assist  6. No recoil // Eliminate after sitting  7. no spread // Eliminate weapons distribution  8. No flashbang // Eliminate flash bomb effect  9. Enemies Won't shang // Only for AI  10. Red crosshair // Ten quasi lines becomes red when aiming at the enemy  [Note] The game is active for the first time to apply for a suspension, please allow it to operate normally.  Clash with other players in new mobile FPS with never-ending action. Jump into the action and enter the battle right now! It's totally free to play!Use different strategies and tactics in explosive online game on a variety of maps. MAIN FEATURES:More than 30 modern lethal guns and camos. Choose your own tactics for battle: pistols, snipers, shotgun, machine guns or riflesUp to 10 players in one game. Test your speed in killingJoin team battles against other players from all over the world on unique mapsCreate your own clan and enjoy team game 4vs4 in various locations playing in squadCompete in ranked seasons and get promoted to higher leagues among other heroesUse killstreaks such as drone strike, sentry gun and attack helicopter. Or even UAV, chopper gunner or rocket launcher to devastate opponent soldiersInteract with other players, complete contracts and military missions Intuitive control and easy interface - swipe, aim and shootPerfect optimizationRegular updates and new game elementsModern Ops: Black Squad is competitive free FPS game with easy and intuitive controls, vivid 3D graphics and exciting gameplay.Play for cops, S.W.A.T. or bandits and show your combat skills in first person shooter for Android. One team becomes Counter-Terrorists and attack other Terrorists team. Buy different ammo, guns and weapons, upgrade it, change the look of your weapon skins. Increase your killing skills against other soldiers and prove yourself in each map using combat killstreaks and extreme kill shots. Shoot to kill and make a headshot to be pro in mobile shooting game. Be the best assassin of special forces and show all players who's boss!Zombie mode is coming. Survival is critical!Follow us:Join us on Facebook: https://www.facebook.com/Modern_Ops/Watch our videos on YouTube: https://www.youtube.com/channel/UCtVNQDXXPifEsXpYilxVWcAImportant note: This application requires a persistent internet connection.Once you have any questions or concerns, please contact our customer service at [email\u00a0protected] "
     }
    ]
   }
  ],
  [
   {
    "App": "Fire Strike - Gun Shooter FPS Mod Apk 2.93  ",
    "app_info": [
     {
      "name": "Fire Strike - Gun Shooter FPS Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/4/8/4/64f6868400bcd408ee74d43106a1bfb4.jpg",
      "package": "com.edkongames.aurora",
      "detail": " Version: 2.93, Size: 384.93 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/fire-strike-online-free-shooter-fps-mod/com.edkongames.aurora/download.html",
      "decription": " Fire Strike - Gun Shooter FPS Mod Fire Strike - Gun Shooter FPS v2.93 mod Features:  No advertisement after the completion of the game  Cheat function:  No gravity // remove gravity  2. Speed \u200b\u200bX5 // increase the speed of motion  3 Jump height x20 // increase jump height  4. Set up FOVX120 // Custom FOV  5. Aiming aided X30 // increase aiming assist  6. Perspective // \u200b\u200bCan see the enemy behind the wall  7. No reverse // eliminate the rebound  8. No spread // Eliminate weapons spread  9. No explosion // remove FlashBang special effects  10. The enemy will not shoot // only for AI  11. Red Cross Quasi Line / / When the enemy will become a red  [Tips] Game networking, may be sealed, mindful players cautiously download!  Play 5v5 quick action matches for 5-7 minutes, upgrade weapons and equipment, arrange shooters, use tactical grenades and try to survive. Learn all the game maps and they will become your weapon in the world of the game engulfed in protests and critical confrontation of different fractions.[Play to Win, not Pay to Win]Join epic PvP battles and become heroes of battlefield. All shooting game items affecting gameplay, you can get just by playing the game. So go get some weapons, gears, and grenades and bang bang bang![Fight against gun games players from all over the world in Free to Play FPS game]Lead military operations in Chernobyl, Japan, USA, and other virtual war zones. Take part in action team battles, plant a bomb, or defuse it. Acquire new weapons, soldiers and armor, try new tactics and install unique attachments.[5 minutes, 10 players, fast matches and best survival tactics]-Fast and easy gameplay-Simple controls, just two fingers-Autolock and Autofire or hand controls -Great graphics and effects-Excellent performance and optimization[Clash squad with Friends up to 5 people or 10 players FFA]Get together in online games with your friends in a squad of 5 people against other FPS games players to be the one who get the apex rating. Play custom online game mode up to 10 people.[4 game modes already available, 4 in development]-Team fight-Free for All (Death Match Survival)-Bomb mode (Defuse)-Arms Race (Gun Game)[A wide variety of weapons and equipment, flexible specialist settings]Choose who to play as a fast SMG assassin, Sniper support or Tank machine gunner. Be whoever you want in one of the most dynamic 3D shooting games![15 leagues, convenient rating system]What is your final league? Become one of the legends, join the Fire Titans league in ranked games. Make your way through the rating as part of a squad or alone and get rampage in defferent shooter games and rounds.[Regular updates]In the future, Fire Strike Online players will have new modes: capture, combat arena, 2v2 tournaments. And of course new maps: SLUMS RAID, CAMPO SACRO, etc.Lots of new shooting content: skins, characters, weapons, attachments.Please note! Fire Strike Online Shooter is completely free to play and download, while some in-game content can be purchased for real money.[Contact us]For any questions or comments, write to us at [email\u00a0protected] will gladly try to help youFollow us:Instagram: https://www.instagram.com/fire.strike.official/YouTube: https://www.youtube.com/channel/UCtVNQDXXPifEsXpYilxVWcAFacebook: https://www.facebook.com/groups/firestrikeofficialVK: https://vk.com/firestrikeofficialgroup*Attention! The game requires a stable internet connectionRecommended system requirements: Android 5.1.1 or above and at least 2 GB memory "
     }
    ]
   }
  ],
  [
   {
    "App": "MaskGun: FPS Shooting Gun Game Mod Apk 3.010  ",
    "app_info": [
     {
      "name": "MaskGun: FPS Shooting Gun Game Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/3/8/2/23b4ed669df54fd21c0ec01ce588bd82.jpg",
      "package": "com.junesoftware.maskgun",
      "detail": " Version: 3.010, Size: 162.63 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/maskgun-mod/com.junesoftware.maskgun/download.html",
      "decription": "MaskGun, a punk-style competitive first-person shooter mobile game. The game has an explosive shooting scene. Choose your hero, enter the arena, defeat other players, and take the first place in the game. MaskGun is a passionate multiplayer real-time shooting battle game. Numerous players plunged into the battlefield, searching for weapons, equipment and materials. Beware of attacks by other players, download this mobile game and experience the exciting battle in the game! In this game, if you want always win in the game. You can download MaskGun Mod for free. You can open the mod menu to get unlimited ammo and one hit kill the enemy. Graphic The graphics of this game are very beautiful and support all old devices: you can enjoy beautiful visual effects on old device. Gameplay This game is a multiplayer instant shooting combat game. Many players will plunge into the battlefield, searching for weapons, equipment and materials. Try to kill the opponent as many times as possible within the specified time.  Highlights Players can use various equipment, masks, armor and equipment to customize your character.  Shortcomings The map is really small Difficulty The game is easy to play with"
     }
    ]
   }
  ],
  [
   {
    "App": "Piano Fire: Edm Music & Piano Mod Apk 1.0.77  ",
    "app_info": [
     {
      "name": "Piano Fire: Edm Music & Piano Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/2/1/1/db06ca8430ccac74cd026eced8f43e50.jpg",
      "package": "beatmaker.edm.musicgames.PianoGames",
      "detail": " Version: 1.0.77, Size: 39.31 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/piano-fire-edm-music-new-rhythm-mod/beatmaker.edm.musicgames.PianoGames/download.html",
      "decription": " Piano Fire: Edm Music & Piano Mod Piano Fire: Edm Music & Piano mod v1.0.77 (unlocked / many diamonds) Features:  Unlocked / many diamonds   Play Piano Fire on mobile anywhere today!Piano Fire is a special game in different genres of piano games and wonderful gameplay. Blends piano and EDM music perfectly, you can feel the collision of ice and fire, get addicted to hot and popular songs around the world!How to Play:It's similar to other piano games, tap the tiles continuously to follow the music melody and don't miss any tile. Prove how fast and accurate can you play!Game features:- Real music feeling when tapping the tiles.- More albums and songs of various styles.- Cool design and graphics.- Simple to play, hard to master. Tapping only the music tile in some high-speed songs can be a real challenge!Do not hesitate to try Piano Fire online! This excellent piano game has more surprises in store for you than you imagine! "
     }
    ]
   }
  ],
  [
   {
    "App": "Red Ball 4 Mod Apk 1.4.21  ",
    "app_info": [
     {
      "name": "Red Ball 4 Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210710/87/84/56/1625892329.jpg",
      "package": "com.FDGEntertainment.redball4.gp",
      "detail": " Version: 1.4.20, Size: 52.07 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/red-ball-4-mod/com.FDGEntertainment.redball4.gp/download.html",
      "decription": "Red Ball 4 Mod  game is a casual game with all levels unlock. In this mod game, you can free to play any levels as you like.  With this mod, this game will be easy for you. Enjoy the game! Sign in social account:  Not supported  Game online or offline:  Offline  Root Needed?: No   License Needed?: No  Install Steps: 1) Download APK fiel on happymod.com. 2) Install and Enjoy. Also read: COC MOD. Mod info: unlimted money and unlimited coins, private server.  HappyMod Download  "
     }
    ]
   }
  ],
  [
   {
    "App": "Firefighter: Fire Truck games Mod Apk 1.02 [Unlocked] ",
    "app_info": [
     {
      "name": "Firefighter: Fire Truck games Mod Apk:",
      "icon": "https://i.git99.com/app_img/20220325/72/71/99/1648179951.jpg",
      "package": "mytown.firestation.free",
      "detail": " Version: 1.02, Size: 51.81 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/my-town-fire-station-rescue-free-mod/mytown.firestation.free/download.html",
      "decription": " Firefighter: Fire Truck games Mod My Town : Fireman & Fire Station Story Game mod v1.02 (unlocked) Features:  Unlocked  Become the hero of My town by playing as a fireman or paramedic. Start by dressing your characters in their protective gear, then head into the control room, where you'll receive emergency calls, then drive the firetruck, helicopter or ambulance to reach your missions!  and spray the fire, extinguish the burning flames and save lives!But! There's more to My Town : Fire Station Rescue than heading out for your missions. Children can learn about the daily lives of emergency workers by exploring what they do while waiting for the next call. Your family can visit you at the fire station and you can challenge them to a ping-pong game. Perhaps they've always wanted to see My Town from the sky? You can take them out on a helicopter flight! Just don't forget to leave time for the gym, so you ensure you are fit and ready for any mission that might come your way. FEATURES*Save game mode: You can exit or log out of the game, and when you pick it back up none of your progress is lost- you can continue on your adventure.  *Multi Touch function: children can play alone, or with parents and friends on single device. *Nine locations in the fire station to explore including the mission control room, rest area, kitchen, ambulance, gym, firetruck garage and more!RECOMMENDED AGE GROUPKids 4-12: My Town games are safe to play even when parents are out of the room. ABOUT MY TOWNThe My Town Games studio designs digital dollhouse-like games that promote creativity and open ended play for your children all over the world. Loved by children and parents alike, My Town games introduce environments and experiences for hours of imaginative play. The company has offices in Israel, Spain, Romania and the Philippines. For more information, please visit www.my-town.com "
     }
    ]
   }
  ],
  [
   {
    "App": "Fire Engine Simulator Mod Apk 1.4.8  ",
    "app_info": [
     {
      "name": "Fire Engine Simulator Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/3/8/6/24ef8e75b62093ff1966ffc405c076ac.jpg",
      "package": "com.skisosoft.fes",
      "detail": " Version: 1.4.8, Size: 52.18 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/fire-engine-simulator-mod/com.skisosoft.fes/download.html",
      "decription": " Fire Engine Simulator Mod Fire Engine Simulator Mod APK 1.4.8 Features:    FES: Fire Engine SimulatorFire trucks are waiting for you. Jump in to the fully modeled fire trucks and put out some fires. Use your earnings to upgrade and customize your fire truck, or purchase one that suits you more.There are a lot of different fires to extinguish. Put out a dumpster fire or a massive office building. The joice is yours. Features:\u2022 Working beacons and sirens\u2022 High detail truck models\u2022 Fully modeled interiors for each truck\u2022 A lot of upgrades for each truck\u2022 Different control options (buttons, tilt, sliders or steering wheel)\u2022 Manual and automatic gearbox options\u2022 Realistic physics\u2022 Open world without load screens\u2022 AI traffic system\u2022 Realistic engine sounds "
     }
    ]
   }
  ],
  [
   {
    "App": "Gun Battle Royale: FPS Shooter Mod Apk 1.0.2  ",
    "app_info": [
     {
      "name": "Gun Battle Royale: FPS Shooter Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/8/1/1/4d4d8220e9f9999da2375f1834036985.jpg",
      "package": "com.battle.ganstar.fps",
      "detail": " Version: 1.0.2, Size: 44.23 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/city-battle-roayle-free-shooting-game-pixel-fps-mod/com.battle.ganstar.fps/download.html",
      "decription": " Gun Battle Royale: FPS Shooter Mod FPS Battle Royale: Free Pixel Gun Shooting Game 3D v1.0.2 mod Features:  Large grenade, health value   Enjoying shooters and cartoon-style gun games? Want to try something new in 2020 \u2753\u2757 The Best Non-Stop Action Shooting Game for FREE! Download Now! \u2757The shooting madness and third person shooter that will make you forget all other FPS combat is here! Get ready for some action with your favorite gun and join this shooting battle now. Have you already? Run, shoot, laugh, and respawn! Go on a mission as a hero in the 3D open world. Make your mark as in the city. Survive the battlegrounds, improve your shooting skills, and develop new tactics for FREE! Download the game and enjoy cartoon  graphics, competitive gameplay, and much more:KEY FEATURES Cool and long lasting more than 40 missions. You can drive any vehicle you wish - auto, cars, tanks, helicopter, jet pack. Easy and intuitive combat controls! Optimization for weak devices! Completely offline that you can play everywhere and any time. More than 20 skinned modern guns like Desert eagle,AK47,M4A1,AWP,GATLIN and so on.Download now and drive into pixel battles! Battle Royale has begun! Become the last man standing, the last hero, the king of the battlefield! Good luck, good hunt ! SUPPORTWe're grateful for any and all feedback and suggestions on the project. "
     }
    ]
   }
  ],
  [
   {
    "App": "Gun Fire: Fun Shooting Games Mod Apk 1.0.0  ",
    "app_info": [
     {
      "name": "Gun Fire: Fun Shooting Games Mod Apk:",
      "icon": "https://i.git99.com/app_img/20211004/28/99/53/1633333113.jpg",
      "package": "com.pixel.grandbattle.multiplayer.fps",
      "detail": " Version: 1.0.0, Size: 54.16 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/grand-battle-island-pixel-multiplayer-shooter-3d-mod/com.pixel.grandbattle.multiplayer.fps/download.html",
      "decription": " Gun Fire: Fun Shooting Games Mod Grand Battle Island: Pixel Multiplayer Shooter 3D v 1.0.0 Mod Features:  Enter the game to give a lot of money  One of best PvP tactical shooting games on mobiles, and now play offline. Your duty is to lead the battle and become the best shooter and sniper.Download now for free one of best offline shooting games on mobiles!Easy on-the-go shooter action where everyone can experience truly competitive combat on their mobile device. It's fun and accessible for beginners and hardcore gamers will find plenty of challenge. Anyone can compete in Team Deathmatch game modes!Team tactics will ensure victory in this free to play multiplayer shooter.===Game Features===\u2022 20 unique weapon types: combat pistols, awp rifles, cool machine guns, swat shotguns and Pubg style Weapon skins!\u2022 Awesome PvP battles: You'll need good FPS games tactics, strategic thinking and teamwork to win! Find your enemy's weak spots and win!\u2022 Free Daily rewards! Easy and intuitive combat controls!\u2022 Optimization for weak devices!Download now and drive into pixel battles! Battle Royale has begun! Become the last man standing, the last hero, the king of the battlefield! Good luck "
     }
    ]
   }
  ],
  [
   {
    "App": "Survival: Fire Battlegrounds Mod Apk 11.1  ",
    "app_info": [
     {
      "name": "Survival: Fire Battlegrounds Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/8/3/5/9ae557888a0e4a5dfb9ae1cca9bad15a.jpg",
      "package": "com.c17h21no4.freesurvival.firebattlegrounds",
      "detail": " Version: 11.1, Size: 375.23 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/free-survival-fire-battlegrounds-battle-royale-mod/com.c17h21no4.freesurvival.firebattlegrounds/download.html",
      "decription": " Survival: Fire Battlegrounds Mod Survival: Fire Battlegrounds v11.1 mod Features:  Unlimited bullet  Free survival: fire battlegrounds battle royale, the ultimate survival battle royale game for your mobile. One of the best single player games with strategic play, amazing graphics, and diverse joyful experience. Supply yourself with a huge battle arsenal. You have never seen so realistic gun games: pistols, shotguns, rifles, machine guns\u2026 feel like a real frontline commando!Experience the journey of real survival shooter on the battlefields. Explore the environments of the shooting battlegrounds. Encounter the best strategy action offline game to hit your play store this year. Build up your own rules for the best offline single player shooter. Survive in the loot island to win over all the levels and be the #1 survivor in unknown island battlegrounds. Easy to use controls and smooth graphics with which we guarantee the best survival battle royale you can play on mobile, play our game and get your name among the legends.Free survival: fire battlegrounds battle royale is an offline shooting game with survival challenges.Answer the call of duty and achieve victory to be the last one standing at the apex, play Offline. We recommend a wifi to download the game, but you don't need wifi to play the new Shooting Game and enjoy the challenging Story mode. Join the survival battle and command this battle like a pro. Take your weapon, strike the enemy army with a hail of bullet, and massive guns. Free survival: fire battlegrounds battle royale is FREE ON MOBILE \u2013 We deliver jaw-dropping HD graphics and amazing sounds. Featuring customizable mobile controls, experience the most smooth control and realistic ballistics, weapon behavior on mobile.I- GAMEPLAY WITH IMMENSE ACTION:- Splendid 3D graphics with real life animations and environment.- Perfect aiming and shot system, giving you thrilling experience of the Free survival: fire battlegrounds battle royale.- Amazing gun fire sounds, giving you intense feel of the battleground heat.- Flexible support for low end devices with low graphics capacity.II- HIGHLY LOADED WEAPONRY AND VAST ENVIRONMENTS:- Diverse options of guns from different modern weaponry category like machine guns, pistols, sniper rifles or shotguns to have a unique experience in battleground survival game.- Play on your own a great story mode and enjoy the best offline battle royale combat.- New and amusing warfare environments of gun games in free battleground shooting game.- Get loaded with 1 primary gun and 1 secondary gun to shoot your rivals at your best in intense combat experience.- Medic kits to accompany your journey of #1 survival in battleground games.III- STAGGERING CLASSIC GAME MODE:- Enjoy the real survival battle of the Free survival: fire battlegrounds battle royale  with a variety of items in the maps to loot and get equipped.- Boost your gameplay with med kits and loots in the TPS shooting game, exp booster in top free war games.- Earn exciting rewards by clicking the get reward button. "
     }
    ]
   }
  ],
  [
   {
    "App": "Fire Balls 3D Mod Apk 1.32.1  ",
    "app_info": [
     {
      "name": "Fire Balls 3D Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/5/6/2/4c428e55b4ca45bedcf71704595d8022.jpg",
      "package": "com.NikSanTech.FireDots3D",
      "detail": " Version: 1.32.1, Size: 56.83 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/fire-balls-3d-mod/com.NikSanTech.FireDots3D/download.html",
      "decription": "Fire Balls 3D Mod game is an arcade game with unlimited gems and life. You can use these money to buy all the items on the shop. Enjoy the game.  Sign in social account:  Not supported  Game online or offline:  Offline  Root Needed?: No   License Needed?: Yes Install Steps: 1) Download APK files on happymod.com. 2.) Install and Enjoy."
     }
    ]
   }
  ],
  [
   {
    "App": "Aero Smash -open fire Mod Apk 1.0.2  ",
    "app_info": [
     {
      "name": "Aero Smash -open fire Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210709/42/9/92/1625807573.jpg",
      "package": "com.zplay.aerosmash",
      "detail": " Version: 1.0.2, Size: 48.46 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/aero-smash-open-fire-mod/com.zplay.aerosmash/download.html",
      "decription": " Aero Smash -open fire Mod Aero Smash -open fire v1.0.2 mod Features:  Aircraft unconditional purchase available.  Drive you plane to guard your territory and shoot down all the enemies! Characteristics:You can collect and own more than 135 kinds of planes.An unknown and thrilling adventure will be started from a random unique map. The world will show up as a huge map.360-degree free shooting.Contact us:[email\u00a0protected] "
     }
    ]
   }
  ],
  [
   {
    "App": "Fire Flying Mod Apk 1.02  ",
    "app_info": [
     {
      "name": "Fire Flying Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210710/97/36/84/1625899176.jpg",
      "package": "com.devm.fireflying",
      "detail": " Version: 1.02, Size: 26.25 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/fire-flying-mod/com.devm.fireflying/download.html",
      "decription": " Fire Flying Mod Fire Flying 1.02 MOD Unlimited Money + NO Ads Features:  Point + NO ads   A strategic wildfire fighting game! Use your aircraft to drop water on the spreading fire. Protect buildings and towns from the blazing wildfire. Plan ahead and use chokepoints to utilise the water better and take the wind direction into account.  Features:   22 exciting and fire-filled levels 8 Achievements. Three different aircraft types, each with their own strengths. Upgrade your aircraft as you earn upgrade points. Simple touch interface, complex strategies.  "
     }
    ]
   }
  ],
  [
   {
    "App": "Fire Force: Gun Battle Royale Mod Apk 2.4.3 [Unlimited money] ",
    "app_info": [
     {
      "name": "Fire Force: Gun Battle Royale Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/8/1/3/337f5c0b2a1055ceb68087ce4a6d0679.jpg",
      "package": "com.firstanvilgames.Cyberpunk.Battleground",
      "detail": " Version: 2.4.3, Size: 84.96 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/cyber-battle-royale-2077-beta-version-mod/com.firstanvilgames.Cyberpunk.Battleground/download.html",
      "decription": " Fire Force: Gun Battle Royale Mod Fire Force Free: Shooting Games & Gun Survival War MOD APK 2.4.3 (Unlimited Money) Features:  Unlimited Money  Cyber battle royale 2077Do you like military pixel shooter survival games? Collect loot, look for rivals, BUT be afraid of the narrowing zone, it causes significant damage! Shoot from the pixel gan, Kalash and other weapons.Multiplayer survival on the island.The battlefield is constantly changing and becoming less and less, you have little time!Our game is absolutely free to download. Install and start pixel shooting right now! The battle has already begun! "
     }
    ]
   }
  ],
  [
   {
    "App": "The Glorious Resolve Army Game Mod Apk 1.9.9  ",
    "app_info": [
     {
      "name": "The Glorious Resolve Army Game Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210709/16/14/16/1625835461.jpg",
      "package": "com.rockvillegames.thegreatarmy",
      "detail": " Version: 1.9.9, Size: 147.93 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/the-glorious-resolve-journey-to-peace-mod/com.rockvillegames.thegreatarmy/download.html",
      "decription": " The Glorious Resolve Army Game Mod The Glorious Resolve: Journey To Peace - Army Game v1.9.9 mod Features:  The game has been cracked in the purchase, the purchase will not pop any payment interface, immediate success, IAP supports flight mode, flight mode recommended for purchase.  ISPR presents you with an action packed, multi role FPS shooter game. It takes the players through the epic battles Pakistan Armed Forces and Law enforcement agencies have fought.Militants are expanding their territory in Pakistan with the help of external forces. They are trying to destabilize the country but there is one thing they should be scared of, \"Patriotism of The Armed Forces\".In this darkest hour all the forces have been united to eliminate the deadliest threats the country is facing. Army, Air Force, Navy, ISPR, SSG Commandos, Aviation and other LEA's are all working together and fighting terrorism using their tactical expertise and state of the art weapon systems.In this CS Critical Strike: Counter Terrorist Online FPS Games, you will be part of an elite military force fighting at the front lines. You will use tactical military weapons to counter the hostile takeover of the region by armed militants. As you progress through this Delta IGI Force FPS action shooter critical strike army games you will get the opportunity to take part in special joint operations, Delta CS surgical strikes and special force operations. Get ready to take on the challenge and jump into an action adventure military game lite that will take you behind enemy lines into the fiercest player unknown IGI battlefield of the century.Now it is our turn to show them what we are made of. Gear-up, be a part of this glorious mission resolve army game and eliminate militant forces once and for all. Operate and traverse through realistic 3D environments consisting of treacherous mountains, underground tunnels and dry deserts. Use deadly missile systems, deploy air strikes, smoke grenades, hand grenades and much more to defeat the militants.Take on different roles on the war games IGI unknown battlefield, pilot Cobra helicopters and eliminate all hostile threats in this action packed thrilling Delta CS Critical Strike: Counter Terrorist Online FPS Games.  The Glorious Resolve: Journey To Peace - Free FPS Delta Critical Strike Game of ISPR and Pakistan Armed Forces with key features as following: \u25c9 TGR Multi role Latest and best Delta FPS Shooter game for peace.\u25c9 AAA quality modern graphics with easy controls.\u25c9 Best Android 3D game with Powerful military weapons including machine guns, sub-machine guns, shotguns, sniper rifles and pistols. \u25c9 Use of force and force multipliers like close air support, UAV drones.\u25c9 Realistic 3D Fauji game play including strict rules of engagement.\u25c9 Unique 3D maps set in a realistic 3D environment in border game.\u25c9 Use gun strikes, smoke grenades and air CS Critical Strikes against militants. \u25c9 Earn medals to unlock and upgrade powerful guns in latest and best Android Mobile FPS Home Guard game. \u25c9 A system of rewards like medals and promotions to keep the player engaged throughout the Delta army home guard game.\u25c9 Encounter a variety of threats including gunners, snipers and bazooka enemies.\u25c9 Intelligence Based Operations.\u25c9 Compete against top players and make it to the highest rankings in the online Leader board.Current Chapters: The Glorious Resolve: Journey To Peace - Free FPS Delta Army Home Guard Games \u25c9 Operation Rah-e-Rast\u25c9 Operation Sherdil\u25c9 Operation Rah-e-Nijat\u25c9 Operation Surprise Attack LoCIf you like \u201cThe Glorious Resolve: Journey To Peace\u201d Free FPS Delta IGI Army Home Guard Games, please try our other games. And don't forget to rate and review about Delta CS Critical Strike Army Mission Games. "
     }
    ]
   }
  ],
  [
   {
    "App": "Cover Strike - 3D Team Shooter Mod Apk 1.7.35  ",
    "app_info": [
     {
      "name": "Cover Strike - 3D Team Shooter Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/8/9/5/10cd49eacae6ad73a29ea77623cd0238.jpg",
      "package": "com.gun.black.ops",
      "detail": " Version: 1.7.35, Size: 67.26 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/cover-strike-3d-team-shooter-mod/com.gun.black.ops/download.html",
      "decription": "Cover Strike - 3D Team Shooter Mod  game is a action game with unlimited money. In this mod game,  you can free to buy all the items on the shop.  With this mod, this game will be easy for you. Enjoy the game! Sign in social account:  Not supported  Game online or offline:  Offline  Root Needed?: No   License Needed?: No  Install Steps: 1) Download APK fiel on happymod.com. 2) Install and Enjoy. Also read: COC MOD. Mod info: unlimted money and unlimited coins, private server.  HappyMod Download "
     }
    ]
   }
  ],
  [
   {
    "App": "Nickname Generator for Gamers Mod Apk 1.5.3 [Premium] ",
    "app_info": [
     {
      "name": "Nickname Generator for Gamers Mod Apk:",
      "icon": "https://i.git99.com/app_img/20211010/65/11/34/1633840823.jpg",
      "package": "com.rtlab.namegenerator",
      "detail": " Version: 1.5.3, Size: 7.17 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/nickname-generator-for-gamers-mod/com.rtlab.namegenerator/download.html",
      "decription": " Nickname Generator for Gamers Mod Nickname Generator for Gamers Mod APK 1.5.3 Features:  Premium  The app is easy to use and straightforward. Just hit the desired naming button or write your name and it will give you multiple choices decorated with custom fonts and ornaments.Everything is customizable with the coolest ASCII characters. Afterwards, you can just copy and paste it into your favorite game or social networks.Choose from tons of cool results when searching for a pubg name maker, ff nicks, wow names and others.What the Nicks \u26a1 Nickname Generator & Customizer has and can do:\u26a1 Can render you nicknames for male, female and also has a funny/cool category\u26a1 Generate pubg names, ff nicks, wow names, usernames, etc.\u26a1 Customize each name with special characters  \u26a1 Copy and paste the newly created nicknames anywhere \u26a1 Create an easily accessible list of all your favorite nicknamesGenerate your pro ff nicks, wow names and pubg names easily and in a fun way. Differentiate yourself from other players by personalizing your nickname to the smallest detail.If you wanna ask questions or suggest any features for Nicks \u26a1 Nickname Generator & Customizer, hit us up on the email bellow. "
     }
    ]
   }
  ],
  [
   {
    "App": "Fire Craft: 3D Pixel World Mod Apk 1.80 [Unlimited money] ",
    "app_info": [
     {
      "name": "Fire Craft: 3D Pixel World Mod Apk:",
      "icon": "https://i.git99.com/app_img/20211025/1/49/59/1635101574.jpg",
      "package": "com.abi.pixelshooter.blockcraft.zombie",
      "detail": " Version: 1.80, Size: 80.04 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/block-craft-shadow-awakens-mod/com.abi.pixelshooter.blockcraft.zombie/download.html",
      "decription": "Block Craft: Shadow Awakens Mod game is a nice simulation game with unlimited money. In this game, you can free to buy some of items for free on the shop.  Game online or offline:  Offline  Root Needed?: No   License Needed?: No  Install Steps: 1) Download APK fiel on happymod.com. 2) Install and Enjoy. Also read: COC MOD. Mod info: unlimted money and unlimited coins, private server.  HappyMod Download "
     }
    ]
   }
  ],
  [
   {
    "App": "GFX Tool - Game Booster Mod Apk 1.4.6.1  ",
    "app_info": [
     {
      "name": "GFX Tool - Game Booster Mod Apk:",
      "icon": "https://i.git99.com/upload/android/icon/5/3/7/62575083c04eb9d28a6204935587d471.jpg",
      "package": "com.bshowinc.gfxtool",
      "detail": " Version: 1.4.6.1, Size: 5.35 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/gfx-tool-free-fire-booster-mod/com.bshowinc.gfxtool/download.html",
      "decription": " GFX Tool - Game Booster Mod GFX Tool V1.4.6.1 Features:  Pro Unlocked  Free Fire is the ultimate survival shooter game available on mobile. Each 10-minute game places you on a remote island where you are pit against 49 other players, all seeking survival. Players freely choose their starting point with their parachute, and aim to stay in the safe zone for as long as possible. Drive vehicles to explore the vast map, hide in trenches, or become invisible by proning under grass. Ambush, snipe, survive, there is only one goal: to survive. "
     }
    ]
   }
  ],
  [
   {
    "App": "Real Robot Fire Battleground : Free Sci-fi Firing Mod Apk 1.3  ",
    "app_info": [
     {
      "name": "Real Robot Fire Battleground : Free Sci-fi Firing Mod Apk:",
      "icon": "https://i.git99.com/app_img/20210710/10/72/81/1625889009.jpg",
      "package": "com.fun_battle_fire_games.free.real.robot.battleground",
      "detail": " Version: 1.3, Size: 44.44 MB, Price: Free, Root needed: No Need, Offers InApp Purchase: No, Price: Free",
      "download": "https://happymod.com/real-robot-fire-battleground-free-sci-fi-firing-mod/com.fun_battle_fire_games.free.real.robot.battleground/download.html",
      "decription": " Real Robot Fire Battleground : Free Sci-fi Firing Mod Real Robot Fire Battleground : Free Sci-fi Firing Mod APK 1.3 Features:  Modify the free app purchases, click the dollar to trade successfully purchased.  Experience intense shooting legacy ops of robots war, here you are at the frontline of infinite futuristic robot battlefield. .Mankind is at sci-fi deathmatch of robots scifi games, You as legacy robot are trying to save the legacy in firing clans of futuristic station in deep space.This is the first person shooter game more than simple FPS scifi games. Fight against infinite waves of enemies. You can encounter locked doors and reply with free fire shooting, destructible environments & many types of enemies. Defeat enemies with, unique weapons, deadly grenades, rocket launchers, pistols, melee Armament, and assault rifles. Use ARMOR for free firing squad for your safety in this free to fire sci-fi game. You have modern and hi-tech weapons inside the laboratory such as laser guns, shotguns, modern grenades, and legacy shadow guns.you can upgrade and improve equipment ability to gain DAILY REWARD of sci fi games. use the best strategies for modern war combat during Free Fire of robot battle. Become the brutal fps shooter to compete opponents of robot c-ops. Follow the rules of survival in free fire during the critical ops of robot warfare. Act like legacy Robot special soldier with ninja infinity powers in this true players pro game.Time to sharp infinity blade for shooting of enemies, take serious actions, Strategize missions for domination and fight to win the battles, You have shadowguns during enemies free Fire game shooting for your help use heavy weapons to become the war legends of black battle ops in this fps shooter game.Player! You are just one step away from infinite warfare of Real Robot Fire Battleground. You have played many multiplayer games with free fire squad, sci-fi games or infinite warfare games but this is clan time game with solo game mode, Players will have realistic robot combat in free modes like classes from Recruit, Tank, Assault, and Saboteur. Enjoy modern war combat of fps game with unique martial interaction where universal gravity can affect your position and running speed and low gravity frees player to jump far and high, Use Jett packs flight in free fire battlegrouds to conduct combat operations more effectively. Relish the optimized game on all devices in a'll Game modes. Master your Team of blitz to fight at a highest furious level and become the futurista robot who wins the infinity action game. Make new  rules for legacy fps shooter, encourage clans of teams for custom game lobby and free fire battle till you fulfill your free questAll Features of Real Robot Fire Battleground: Free Sci-fi Firing:-- Fantastic 3D Graphics-- Excellent 3D characters-- HARDCORE Gameplay-- Robot Battle Free Fire Shooting-- Blitz operations-- First person shooting games-- Robot Free Games-- Legacy Combat "
     }
    ]
   }
  ]
 ]
}
```

# ```Update```

- ```17-01-2022``` 

add the ```ocean_of_game``` method to the ```Search_App_Mod``` class, a new ```SourceForge``` class with the ```search``` method to search.
