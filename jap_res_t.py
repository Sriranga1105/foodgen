import flet as ft

fonts = {
    "Nightcore": "/fonts/Nightcore.ttf",
    "Oswald-Bold": "/fonts/Oswald-Bold.ttf",
    "Ancient": "/fonts/Ancient Ad.ttf",
    "Orange Squash": "/fonts/Orange Squash Free.ttf",
    "Sticky":"/fonts/Sticky Memos Demo Two.ttf"
}
theme = ft.Theme(font_family="Oswald-Bold")
sushi_t = ft.Column(
[
    ft.Container(height=5),   
    ft.Text(value="<ஆட்டு கறி>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/logo.png", width=300),
    ft.Container(height=10),
    ft.Text("செய்முறை",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
        ft.Text('''1) ஆட்டு கறி செய்ய:
4 முதல் 8 காய்ந்த சிவப்பு மிளகாய் (விரும்பினால் குறைந்த முதல் காரமான வகை, விருப்பப்பட்டால் விதை, அல்லது 1 முதல் 1.5 தேக்கரண்டி மிளகாய் தூள்)
2 தேக்கரண்டி கொத்தமல்லி விதைகள்
1 நட்சத்திர சோம்பு (சிறியது)
1 தேக்கரண்டி சீரகம்
1 தேக்கரண்டி பெருஞ்சீரகம் விதைகள்
5 பச்சை ஏலக்காய் (எலைச்சி)
4 முதல் 5 கிராம்பு
2 இரண்டு அங்குல இலவங்கப்பட்டை
½ தேக்கரண்டி மிளகு சோளம்
1 முதல் 2 சிறிய பகுதிகள் கல்பசி / கல் மலர் / தகட் பூல் (விரும்பினால்)
கறிவேப்பிலை 3 துளிகள்
600 கிராம் (1.1 பவுண்டு) எலும்பில் உள்ள ஆடு (அதிகப்படியான கொழுப்பு வெட்டப்பட்டது, ± 100 கிராம்/ 4 அவுன்ஸ் பரவாயில்லை)
1 கப் (105 கிராம்) வெங்காயம் வெட்டப்பட்டது
¼ கப் வெங்காயம் (வெங்காயத்திற்கு மாற்றாக)
2 பெரிய பூண்டு கிராம்பு வெட்டப்பட்டது
1½ தேக்கரண்டி (28 கிராம்) இஞ்சி பூண்டு விழுது (அறை வெப்பநிலையில்)
1 கப் (125 கிராம்) தக்காளி விதை மற்றும் நன்றாக நறுக்கியது (2 நடுத்தர)
1 வளைகுடா இலை
1 அங்குல இலவங்கப்பட்டை துண்டு
2 பச்சை ஏலக்காய்
½ தேக்கரண்டி பெருஞ்சீரகம் விதைகள்
½ தேக்கரண்டி மஞ்சள்
1 தேக்கரண்டி உப்பு (பின்னர் சரிசெய்யலாம்)'''),
        padding=ft.padding.only(left=10,right=10,bottom=20),
        width=400,
        height=400,
    )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
sushi = ft.Container(
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


