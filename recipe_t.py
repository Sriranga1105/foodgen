import flet as ft

#--------------------India----------------------#
goat_t = ft.Column(
    [
        ft.Container(height=10),   
        ft.Text(value="<ஆட்டுக்கறி>", font_family="Ancient", size=30),
        ft.Container(height=5),
        ft.Image(src="/images/goat.jpg", width=300),
        ft.Container(height=10),
        ft.Text("செய்முறை",font_family="Sticky",size=50),
        ft.Container(height=5),
        ft.Container(
            ft.Text('''1) 4 முதல் 8 காய்ந்த சிவப்பு மிளகாய் (விரும்பினால் குறைந்த முதல் காரமான வகை, விருப்பப்பட்டால் டீசீட் அல்லது 1 முதல் 1.5 தேக்கரண்டி மிளகாய் தூள்)
2) 2 தேக்கரண்டி கொத்தமல்லி விதைகள்
3) 1 நட்சத்திர சோம்பு (சிறியது)
4) 1 தேக்கரண்டி சீரகம்
5) 1 தேக்கரண்டி பெருஞ்சீரகம் விதைகள்
6) 5 பச்சை ஏலக்காய் (எலைச்சி)
7) 4 முதல் 5 கிராம்பு
8) 2 இரண்டு அங்குல இலவங்கப்பட்டை
9) ½ தேக்கரண்டி மிளகு சோளம்
10) 1 முதல் 2 சிறிய பகுதிகள் கல்பசி / கல் மலர் / தகட் பூல் (விரும்பினால்)
11) கறிவேப்பிலை 3 தளிர்கள்'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=420,
        )
       ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
    )
goa_t = ft.Container(
        content=goat_t,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=('#E4EEE9', '#93A5CE')
        ),
        width=400,
        height=800,
        padding=5
    )


Dosa_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<தோசை>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/dosa.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) அரிசி - 3.5 கப்,
2) உளுத்தம் பருப்பு - 1 கப்,
3) வங்காளப் பருப்பு - 2 டீஸ்பூன் (விரும்பினால்),
4) எண்ணெய் - தோசை வறுக்க,
5) உப்பு - தேவையான அளவு.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=200,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
dos_a = ft.Container(
    content=Dosa_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

biriyani_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<பிரியாணி>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/biriyani.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
        ft.Text('''தேவையான பொருட்கள்:
1) பழுப்பு வெங்காயம் (குறிப்பு 1)
2 பெரிய வெங்காயம்
½ கப் தாவர எண்ணெய்
2) கோழி இறைச்சி:
700 கிராம் கோழி தொடைகள் மற்றும் முருங்கைக்காய் எலும்பு மற்றும் தோல் இல்லாதது (குறிப்பு 2)
¾ கப் தயிர் அல்லது தொங்கவிட்ட தயிர்
¼ கப் தக்காளி ப்யூரி
¼ கப் காய்கறி எண்ணெய்
1 தேக்கரண்டி இஞ்சி பூண்டு விழுது இஞ்சி மற்றும் பூண்டு
1 தேக்கரண்டி சிவப்பு மிளகாய் தூள் துணையுடன் 1 தேக்கரண்டி மிளகு + 1 தேக்கரண்டி கெய்ன்
1 தேக்கரண்டி மஞ்சள் தூள்
1 தேக்கரண்டி கரம் மசாலா தூள்
2 தேக்கரண்டி பழுப்பு வெங்காயம்
1 ¼ தேக்கரண்டி உப்பு
3) குங்குமப்பூ:
2 தேக்கரண்டி சூடான பால்
10-15 குங்குமப்பூ இழைகள்
வேகவைத்த அரிசி (70% சமைத்த):
2 கப் பாஸ்மதி அரிசி குறிப்பு 3
6 கப் தண்ணீர்
2 தேக்கரண்டி உப்பு
1 பேய்லீஃப்
5-6 கிராம்பு
2-3 ஏலக்காய் காய்கள்'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=750,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
biriyan_i = ft.Container(
    content=biriyani_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

chicken_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<சிக்கன்65>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/chicken 65.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) கோழி - 1 பவுண்டு (கடி அளவு துண்டுகளாக நறுக்கவும்),
2) வெங்காயம் - 2 (பொடியாக நறுக்கியது),
3) பச்சை மிளகாய் - 2,
4) இஞ்சி பூண்டு விழுது - 1 டீஸ்பூன்,
5) தக்காளி - 2 (தூள்),
6) தயிர் - 2 டீஸ்பூன் (அடித்தது),
7) மஞ்சள் தூள் - 1/2 டீஸ்பூன்,
8) சிவப்பு மிளகாய் தூள் - 3 தேக்கரண்டி,
9) கொத்தமல்லி தூள் - 2 டீஸ்பூன்,
10) சீரகப் பொடி - 1/2 டீஸ்பூன்,
11) பெருஞ்சீரகம் பொடி - 1/2 டீஸ்பூன்,
12) கரம் மசாலா தூள் - 1/2 டீஸ்பூன்,
13) சீரகம் - 1/2 டீஸ்பூன்,
14) பெருஞ்சீரகம் விதைகள் - 1/2 தேக்கரண்டி,
15) உப்பு - தேவைக்கேற்ப,
16) எண்ணெய் - 3 டீஸ்பூன்.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=450,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
chicke_n = ft.Container(
    content=chicken_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

sambhar_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<சாம்பார்>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/sambhar-masala.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
            ft.Container(
            ft.Text('''1) துவரம்பருப்பு - 3/4 கப் (நீங்கள் மசூர் பருப்பு அல்லது பச்சைப்பயறு பருப்பு அல்லது பருப்புகளின் கலவையையும் பயன்படுத்தலாம்),
2) காய்கறிகள் (ஒற்றை/கலப்பு காய்கறிகளில் ஏதேனும் விருப்பம்) - 1 கப் (காய்கறிகளின் தேர்வில் பிரிஞ்சி, உருளைக்கிழங்கு, முள்ளங்கி, முருங்கை, கீரை, வெங்காயம், தக்காளி, பச்சை மாம்பழம், கேரட், சுரைக்காய், மஞ்சள் பூசணி, எலுமிச்சை பீன்ஸ், பூசணி ஆகியவை அடங்கும். , யாம், டாரோ-ரூட், ஓக்ரா, நோல்கோல் போன்றவை),
3) சின்ன வெங்காயம் - 8- 10 (அல்லது 1 வெங்காயம் நறுக்கியது),
4) பச்சை மிளகாய் - 1 அல்லது 2,
5) தக்காளி - 1,
6) புளி சாறு - 1 1/2 டேபிள் ஸ்பூன்,
7) சாம்பார் பொடி (அங்கமைந்திருக்கும் அல்லது வீட்டில் செய்து அடையாளம் செய்யலாம்) - 1 டேபிள் ஸ்பூன் (உங்கள் சுவைக்கு அருகிலும் அதை அதிகரிக்க முடியும்),
8) கடுகு - 1/4 தேக்கரண்டி,
9) சீரகம் - 1/4 தேக்கரண்டி,
10) உகாரத் தூள் - 2,
11) கறிவேப்பிலை - 2 நாட்கள்.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=630,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
sambha_r = ft.Container(
    content=sambhar_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

cookies_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<குக்கீஸ்>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/cookies.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
            ft.Container(
            ft.Text('''1) 3 தேக்கரண்டி வெண்ணெய், மிகவும் மென்மையான அல்லது ஓரளவு உருகிய,
2) 3 தேக்கரண்டி நிரம்பிய பழுப்பு சர்க்கரை,
3) 1-1/2 தேக்கரண்டி வெள்ளை சர்க்கரை,
4) 1/4 தேக்கரண்டி வெண்ணிலா,
5) 1 முட்டையின் மஞ்சள் கரு,
6) 1/3 கப் + 2 டேபிள்ஸ்பூன் அனைத்து-பயன்பாட்டு மாவு (~60 கிராம், குறிப்பு 1 ஐப் பார்க்கவும்),
7) 1 தேக்கரண்டி சோள மாவு,
8) 1/4 தேக்கரண்டி பேக்கிங் சோடா,
9) 1/4 தேக்கரண்டி கோஷர் உப்பு,
10) 1/4 கப் சாக்லேட் சிப்ஸ்.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=380,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
cookie_s = ft.Container(
    content=cookies_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)
#------------------------------INDIAN FINISHED------------------------------#
#------------------------------JAPANESE-------------------------------------#
sushi_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<சுஷி>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/sushi.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) 100 கிராம் சுஷி அரிசி
2) 1 தாள் நோரி கடற்பாசி
3) 2 டீஸ்பூன் சுஷி வினிகர்
4) சோயா சாஸ்
5) வசாபி
6) சுஷி இஞ்சி
7) வறுத்த வெள்ளை எள் (விரும்பினால்)

பரிந்துரைக்கப்பட்ட நிரப்புதல்கள்:
1) டுனா - சாஷிமி கிரேடு, பச்சை
2) சால்மன் - சாஷிமி கிரேடு, பச்சை
3) வெண்ணெய்
4) வெள்ளரி
5) நண்டு குச்சிகள்
6) பதிவு செய்யப்பட்ட சூரை மாயோவுடன் கலக்கப்படுகிறது
7) இறால்'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=450,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
sush_i = ft.Container(
    content=sushi_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

ramen_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<ராமேன்>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/ramen.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) ராமன் நூடுல்ஸ் (எங்கள் கிளாசிக் மருச்சான் பேக்கேஜ் மட்டுமே நமக்குத் தேவை, சுவையூட்டல் இல்லை!)
2) பூண்டு மற்றும் இஞ்சி
3) குழம்பு (கோழி அல்லது காய்கறி)
4) உலர்ந்த ஷிடேக் காளான்கள்
5) கேரட் அல்லது காலே போன்ற காய்கறிகள்
6) பாங்கோ, முட்டை, மிளகாய் எண்ணெய் போன்ற உங்களுக்குப் பிடித்த அனைத்து டாப்பிங்ஸ்களும்.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=320,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
rame_n = ft.Container(
    content=ramen_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

takoyagi_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<டகோயகி>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/takoyagi.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) டகோயாகி கலவை
3 பெரிய முட்டைகள் லேசாக அடிக்கப்பட்டது
4.25 கப் குளிர்ந்த நீர்
2 தேக்கரண்டி உடனடி தாஷி
2 தேக்கரண்டி சோயா சாஸ்
1/2 தேக்கரண்டி உப்பு
2.5 கப் அனைத்து நோக்கம் கொண்ட மாவு சுமார் 300 கிராம்

2) டகோயாகி நிரப்புதல்
1/2 பவுண்டு வேகவைத்த ஆக்டோபஸ் 0.5" கன சதுரம்
1 கொத்து பச்சை வெங்காயம் வெட்டப்பட்டது
1 கப் டெம்புரா பிட்ஸ் அல்லது அரிசி கிறிஸ்பீஸ்
விரும்பினால் பெனி ஷோகா/ஊறுகாய் இஞ்சி
விரும்பினால் துண்டாக்கப்பட்ட அல்லது க்யூப் செய்யப்பட்ட சீஸ்'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=460,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
takoyag_i = ft.Container(
    content=takoyagi_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

omurice_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<ஓமுரைஸ்>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/omurice.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) 2 கப் சமைத்த வெள்ளை அரிசி முன்னுரிமை ஒரு நாள் பழமையான அரிசி
2) 1 சிறிய கேரட்
3) 1/2 வெள்ளை வெங்காயம்
4) 1/4 பச்சை மிளகாய்
5) 1/4 பவுண்டு மாட்டிறைச்சி
6) 3 டீஸ்பூன் தாவர எண்ணெய் பிரிக்கப்பட்டது
7) 8 முட்டைகள் பிரிக்கப்பட்டது
8) 2 டீஸ்பூன் பால் பிரிக்கப்பட்டது
9) 1/2 டீஸ்பூன் உப்பு பிரிக்கப்பட்டது'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=330,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
omuric_e = ft.Container(
    content=omurice_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

udon_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<உடான்>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/udon.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) 3 பொதிகள் உறைந்த உடான்
2) 3-4 கீற்றுகள் பேக்கன் தடிமன் பொறுத்து
3) 3/4 கப் பார்மேசன் துருவியது
4) 1/4 கப் Pecorino Romano துருவல்
5) 1 தண்டு பச்சை வெங்காயம்
6) 4 அறை வெப்பநிலை முட்டைகள் 3 முட்டை மஞ்சள் கருக்கள், 1 முழு முட்டை
7) 2 டீஸ்பூன் ஷிரோ மிசோ பேஸ்ட்
8) 2 பல் பூண்டு நறுக்கியது
9) Shichimi togarashi விருப்பத்தேர்வு'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=300,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
udo_n = ft.Container(
    content=udon_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

curryrice_t = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<கறிசாதம்>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/curryrice.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) 2 க்யூப்ஸ் ஜப்பானிய கறி தொகுதி நான் கோல்டன் கறியைப் பயன்படுத்தினேன்
2) 1/2 உருளைக்கிழங்கு
3) 1/2 வெங்காயம்
4) 1/2 பெரிய கேரட்
5) 1/2 கோழி மார்பகம்
6) 1 மற்றும் 1/2 கப் சிக்கன் குழம்பு
7) 1 கப் அரிசி
8) 1 தாள் நோரி
9) 1 தேக்கரண்டி ஆலிவ் எண்ணெய்'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=300,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
curryric_e = ft.Container(
    content=curryrice_t,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)