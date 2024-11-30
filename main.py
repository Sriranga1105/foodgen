import flet as ft
from recipe_e import *
from recipe_t import *

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 800
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "Nightcore": "/fonts/Nightcore.ttf",
        "Oswald-Bold": "/fonts/Oswald-Bold.ttf",
        "Ancient": "/fonts/Ancient Ad.ttf",
        "Orange Squash": "/fonts/Orange Squash Free.ttf",
        "Sticky":"/fonts/Sticky Memos Demo Two.ttf",
        "Tamilbold":"/fonts/NotoSansTamil-Bold.ttf",
        "Tamil":"/fonts/NotoSansTamil-Medium.ttf",
        "Poppinsbold":"/fonts/Poppins-Bold.ttf",
        "Poppins":"/fonts/Poppins-Medium.ttf"
    }
    page.theme = ft.Theme(font_family="Poppins")
    page.update()
    
    #appbar 
    appbar = ft.CupertinoAppBar(
        leading=ft.IconButton(ft.icons.KEYBOARD_BACKSPACE,on_click=lambda _: page.go("/lan")),
        bgcolor=ft.colors.SURFACE_VARIANT,
        trailing=ft.Icon(ft.icons.FASTFOOD_OUTLINED),
      middle=ft.Text("FoodGen",font_family="Poppinsbold",size=28),
    )

    appbar_e = ft.CupertinoAppBar(
        leading=ft.IconButton(ft.icons.KEYBOARD_BACKSPACE,on_click=lambda _: page.go("/eng")),
        bgcolor=ft.colors.SURFACE_VARIANT,
        trailing=ft.Icon(ft.icons.FASTFOOD_OUTLINED),
      middle=ft.Text("FoodGen",font_family="Poppinsbold",size=28),
    )

    appbar_t = ft.CupertinoAppBar(
        leading=ft.IconButton(ft.icons.KEYBOARD_BACKSPACE,on_click=lambda _: page.go("/tam")),
        bgcolor=ft.colors.SURFACE_VARIANT,
        trailing=ft.Icon(ft.icons.FASTFOOD_OUTLINED),
      middle=ft.Text("FoodGen",font_family="Poppinsbold",size=28),
    )


    # Page Routing start
    def route_change(route):
        page.views.clear()
        page.theme_mode = ft.ThemeMode.LIGHT
        page.theme = ft.theme.Theme(color_scheme_seed='#A233A2')
        page.views.append(
            ft.View(
                "/",
                [
                    splash_screen
                ],padding=0
            )
        )
        #--------------------------ENGLISH---------------------------#
        if page.route == "/lan":
            page.views.append(
            ft.View(
                "/lan",
                [
                    langlogo
                ],
                padding=0,
                vertical_alignment="center",
                horizontal_alignment="center",
            )
        )
        if page.route == "/eng":
            page.views.append(
                ft.View(
                    "/eng",
                    [
                        appbar,
                        sectioncard,
                        tabs_menu
                    ],
                    padding=0,
                )
            )
        #-----------------------INDIAN ENGLISH RECIPE-------------------------#
        if page.route == "/recipee/goat":
            page.views.append(
                ft.View(
                    "/recipee/goat",
                    [
                        appbar_e,
                        goat
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipee/dosa":
            page.views.append(
                ft.View(
                    "/recipee/dosa",
                    [
                        appbar_e,
                        dosa
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipee/biriyani":
            page.views.append(
                ft.View(
                    "/recipee/biriyani",
                    [
                        appbar_e,
                        biriyani
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipee/chicken":
            page.views.append(
                ft.View(
                    "/recipee/chicken",
                    [
                        appbar_e,
                        chicken
                    ],
                    padding=0,
                )
            )        
        if page.route == "/recipee/sambhar":
            page.views.append(
                ft.View(
                    "/recipee/sambhar",
                    [
                        appbar_e,
                        sambhar
                    ],
                    padding=0,
                )
            )        
        if page.route == "/recipee/cookies":
            page.views.append(
                ft.View(
                    "/recipee/cookies",
                    [
                        appbar_e,
                        cookies
                    ],
                    padding=0,
                )
            )
        #-----------------------JAPANESE ENGLISH RECIPE--------------------------#
        if page.route == "/recipee/sushi":
            page.views.append(
                ft.View(
                    "/recipee/sushi",
                    [
                        appbar_e,
                        sushi
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipee/ramen":
            page.views.append(
                ft.View(
                    "/recipee/ramen",
                    [
                        appbar_e,
                        ramen
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipee/takoyagi":
            page.views.append(
                ft.View(
                    "/recipee/takoyagi",
                    [
                        appbar_e,
                        takoyagi
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipee/omurice":
            page.views.append(
                ft.View(
                    "/recipee/omurice",
                    [
                        appbar_e,
                        omurice
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipee/udon":
            page.views.append(
                ft.View(
                    "/recipee/udon",
                    [
                        appbar_e,
                        udon
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipee/curryrice":
            page.views.append(
                ft.View(
                    "/recipee/curryrice",
                    [
                        appbar_e,
                        curryrice
                    ],
                    padding=0,
                )
            )
        #----------------------------TAMIL-------------------------------#
        if page.route == "/tam":
            page.views.append(
                ft.View(
                    "/tam",
                    [
                        appbar,
                        sectioncard_t,
                        tabs_menu_t,
                    ],
                    padding=0,
                )
            )       
        #-----------------------INDIAN TAMIL RECIPE-------------------------#
        if page.route == "/recipet/goat":
            page.views.append(
                ft.View(
                    "/recipet/goat",
                    [
                        appbar_t,
                        goa_t
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipet/dosa":
            page.views.append(
                ft.View(
                    "/recipet/dosa",
                    [
                        appbar_t,
                        dos_a
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipet/biriyani":
            page.views.append(
                ft.View(
                    "/recipet/biriyani",
                    [
                        appbar_t,
                        biriyan_i
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipet/chicken":
            page.views.append(
                ft.View(
                    "/recipet/chicken",
                    [
                        appbar_t,
                        chicke_n
                    ],
                    padding=0,
                )
            )        
        if page.route == "/recipet/sambhar":
            page.views.append(
                ft.View(
                    "/recipee/sambhar",
                    [
                        appbar_t,
                        sambha_r
                    ],
                    padding=0,
                )
            )        
        if page.route == "/recipet/cookies":
            page.views.append(
                ft.View(
                    "/recipet/cookies",
                    [
                        appbar_t,
                        cookie_s
                    ],
                    padding=0,
                )
            )
        #-----------------------JAPANESE TAMIL RECIPE--------------------------#
        if page.route == "/recipet/sushi":
            page.views.append(
                ft.View(
                    "/recipet/sushi",
                    [
                        appbar_t,
                        sush_i
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipet/ramen":
            page.views.append(
                ft.View(
                    "/recipet/ramen",
                    [
                        appbar_t,
                        rame_n
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipet/takoyagi":
            page.views.append(
                ft.View(
                    "/recipet/takoyagi",
                    [
                        appbar_t,
                        takoyag_i
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipet/omurice":
            page.views.append(
                ft.View(
                    "/recipet/omurice",
                    [
                        appbar_t,
                        omuric_e
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipet/udon":
            page.views.append(
                ft.View(
                    "/recipet/udon",
                    [
                        appbar_t,
                        udo_n
                    ],
                    padding=0,
                )
            )
        if page.route == "/recipet/curryrice":
            page.views.append(
                ft.View(
                    "/recipet/curryrice",
                    [
                        appbar_t,
                        curryric_e
                    ],
                    padding=0,
                )
            )
        page.update()

    #Logo Page => 1
    splash_screen_data = ft.Column(
    [
        ft.Container(height=50),   
        ft.Text(value="FoodGen", font_family="Orange Squash", size=30),
        ft.Image(src="/images/logo.png", width=300),
        ft.Container(height=30),
        ft.ElevatedButton("START",on_click=lambda _: page.go("/lan"))
       ], horizontal_alignment='center'
    )
    splash_screen = ft.Container(
        content=splash_screen_data,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=('#E4EEE9', '#93A5CE')
        ),
        width=400,
        height=800,
        padding=25
    )

    #Language Page => 2
    langlogo_data = ft.Column(
        [   
            ft.Container(height=120),
            ft.Container(ft.Image(src="/images/lang.png",scale=2),width=250,height=100),
            ft.Container(height=30),
            ft.Text(value="Select Your Language.", font_family="Poppinsbold", size=25),
            ft.Container(height=30),
            ft.ElevatedButton("தமிழ்",on_click=lambda _: page.go("/tam")),
            ft.ElevatedButton("English",on_click=lambda _: page.go("/eng")),
            ft.ElevatedButton("Blog", url="http://localhost/my-food-recipe")
           ],horizontal_alignment='center'
        )
    
    langlogo = ft.Container(
        content=langlogo_data,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=('#E4EEE9', '#93A5CE')
        ),
        width=400,
        height=800,
        padding=25
    )

    #English Page => 3 CardMenu
    cardmenu = ft.Row(
        [
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/cookies.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='Cookies', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='Rating: 5', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipee/cookies"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            ),
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/dosa.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='Dosa', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='Rating: 4.9', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipee/dosa"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            ),
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/biriyani.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='Biriyani', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='Rating: 4.9', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipee/biriyani"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            ),
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/chicken 65.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='Chicken 65', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='Rating: 5', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipee/chicken"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            ),
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/sambhar-masala.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='Sambhar', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='Rating: 4.8', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipee/sambhar"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            )
        ]
    )

    sectioncard = ft.Container(
    padding=ft.padding.only(top=20,bottom=10,left=10,right=10),
    bgcolor="black",
    content=ft.Column([
        ft.Container(
            margin=ft.margin.only(left=10),
            content=ft.Text("Today's Best Recipes!",
                            color="white",
                            size=24, weight="bold", font_family='Oswald-Bold'
                            )
        ),
        ft.Row([
            cardmenu  
        ], scroll="ALWAYS")
    ])
    )

    #English Page 3 => Tab Menus
    #Indian Reicpe
    india = ft.Column(scroll="auto")
    india.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/goat.jpg"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Goat Curry",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/goat"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    )
    )
    # Add additional content to the "Indian" tab
    india.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/dosa.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Dosa",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/dosa"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    india.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/biriyani.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Biriyani",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/biriyani"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    india.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/chicken 65.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Chicken 65",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/chicken"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    india.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/sambhar-masala.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Sambhar",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/sambhar"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    india.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/cookies.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Cookies",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/cookies"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    
    #Japanese recipe Tab menu
    japan = ft.Column(scroll="auto")
    japan.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/sushi.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Sushi",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/sushi"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    )
    )

    japan.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/ramen.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Ramen",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/ramen"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    japan.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/takoyagi.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Takoyagi",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/takoyagi"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    japan.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/omurice.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Omurice",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/omurice"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    japan.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/udon.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Udon",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/udon"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    japan.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/curryrice.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("Curryrice",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"Rating: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("Recipe",on_click = lambda _e: page.go("/recipee/curryrice"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))

    #tab Menu Structrue:
    tabs_menu = ft.Tabs(
        selected_index=0,
        animation_duration = 300,
        tabs=[
            ft.Tab(
                text="Indian",
                content=india,
            ),
            ft.Tab(
                text="Japan",
                content=japan,
            ),
        ],expand=5,
    )
    #---------------------TAMIL----------------------------#
    cardmenu_t = ft.Row(
        [
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/cookies.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='குக்கீஸ்', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='ரேட்டிங்: 5', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipet/cookies"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            ),
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/dosa.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='தோசை', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='ரேட்டிங்: 4.9', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipet/dosa"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            ),
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/biriyani.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='பிரியாணி', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='ரேட்டிங்: 4.9', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipet/biriyani"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            ),
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/chicken 65.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='சிக்கன் 65', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='ரேட்டிங்: 5', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipet/chicken"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            ),
            ft.Card(
                elevation=10,
                content=ft.Container(
                    bgcolor="white",
                    width=220,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column([
                        ft.Image(
                            src='/images/sambhar-masala.png',
                            width=220,
                            height=150,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column([
                                ft.Text(value='சாம்பார்', size=18, weight="bold"),
                                ft.Row([
                                    ft.Text(value='ரேட்டிங்: 4.8', size=24, weight="bold"),
                                    ft.IconButton(ft.icons.FASTFOOD_OUTLINED,on_click = lambda _e: page.go("/recipet/sambhar"))
                                ], alignment="spaceBetween")
                            ])
                        )
                    ]), ink=True
                )
            )
        ]
    )

    sectioncard_t = ft.Container(
    padding=ft.padding.only(top=20,bottom=10,left=10,right=10),
    bgcolor="black",
    content=ft.Column([
        ft.Container(
            margin=ft.margin.only(left=10),
            content=ft.Text("இன்றைய சிறந்த ரெசிபிகள்!",
                            color="white",
                            size=24, weight="bold", font_family='Oswald-Bold'
                            )
        ),
        ft.Row([
            cardmenu_t  
        ], scroll="ALWAYS")
    ])
    )

    #English Page 3 => Tab Menus
    #india_tn Reicpef
    india_t = ft.Column(scroll="auto")
    india_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/goat.jpg"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("ஆட்டுக்கறி",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/goat"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    )
    )
    # Add additional content to the "india_tn" tab
    india_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/dosa.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("தோசை",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/dosa"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    india_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/biriyani.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("பிரியாணி",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/biriyani"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    india_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/chicken 65.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("சிக்கன் 65",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/chicken"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    india_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/sambhar-masala.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("சாம்பார்",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/sambhar"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    india_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/cookies.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("குக்கீஸ்",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/cookies"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    
    #japan_tese recipe Tab menu
    japan_t = ft.Column(scroll="auto")
    japan_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/sushi.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("சுஷி",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/sushi"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    )
    )
    # Add additional content to the "india_tn" tab
    japan_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/ramen.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("ராமேன்",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/ramen"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    japan_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/takoyagi.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("டகோயகி",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/takoyagi"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    japan_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/omurice.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("ஓமுரைஸ்",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/omurice"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    japan_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/udon.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("உடான்",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/udon"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))
    japan_t.controls.append(ft.Container(
        ft.Row([
            ft.Image(
                width=110,
                height=80,
                src="/images/curryrice.png"
            ),
            ft.Container(
                content = ft.Column(
                    [
                        ft.Text("கறிசாதம்",size=16,weight="bold"),
                        ft.Row(
                            [
                                ft.Container(
                                    padding=ft.padding.all(5),
                                    content=ft.Text(f"ரேட்டிங்: 4.9")
                                ),
                                ft.Column(
                                    [
                                        ft.ElevatedButton("செய்முறை",on_click = lambda _e: page.go("/recipet/curryrice"),bgcolor="#A233A2",color="white")
                                    ]
                                )
                            ],
                        )
                    ]
                )
            )
        ]
    )
    ))

    #tab Menu Structrue:
    tabs_menu_t = ft.Tabs(
        selected_index=0,
        animation_duration = 300,
        tabs=[
            ft.Tab(
                text="India",
                content=india_t,
            ),
            ft.Tab(
                text="Japanese",
                content=japan_t,
            ),
        ],expand=5,
    )

    #-----------------------------------------------------------------------------#
    def view_pop(view):
        page.views.pop()
        top_view=page.views[-1]
        page.go(top_view.route)

    page.on_route_change=route_change
    page.on_view_pop=view_pop
    page.go(page.route) 
ft.app(target=main,assets_dir="assets")