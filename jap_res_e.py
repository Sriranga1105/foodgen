import flet as ft

fonts = {
    "Nightcore": "/fonts/Nightcore.ttf",
    "Oswald-Bold": "/fonts/Oswald-Bold.ttf",
    "Ancient": "/fonts/Ancient Ad.ttf",
    "Orange Squash": "/fonts/Orange Squash Free.ttf",
    "Sticky":"/fonts/Sticky Memos Demo Two.ttf"
}
theme = ft.Theme(font_family="Oswald-Bold")
sushi_e = ft.Column(
[
    ft.Container(height=5),   
    ft.Text(value="<GOAT CURRY>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/logo.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
        ft.Text('''4 to 8 dried red chilies (use low to spicy kind as per preference, deseed if preferred, or 1 to 1.5 tsp chili powder)
2 tablespoon coriander seeds
1 star anise (small)
1 teaspoon cumin seeds
1 teaspoon fennel seeds
5 green cardamoms (elaichi)
4 to 5 cloves
2 two inch cinnamon stick
½ teaspoon pepper corn
1 to 2 small portions kalpasi / stone flower/ dagad phool (optional)
3 sprigs of curry leaves'''),
        padding=ft.padding.only(left=10,right=10,bottom=20),
        width=400,
        height=400,
    )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
sushi = ft.Container(
    content=sushi_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)


