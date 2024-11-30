import flet as ft


#********************* INDIAN ENGLISH RECIPE **************************#
goat_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<GOAT CURRY>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/goat.jpg", width=300),
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
goat = ft.Container(
    content=goat_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

Dosa_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<DOSA>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/dosa.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) Rice - 3.5 cups,
2) Urad dal - 1 cup,
3) Bengal gram dal - 2 tbsp (optional),
4) Oil - to fry dosas,
5) Salt - what amount you need.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=200,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
dosa = ft.Container(
    content=Dosa_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

biriyani_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<BIRIYANI>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/biriyani.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''Ingredients:
1) Brown Onions (Note 1)
2 Onions Large
½ cup Vegetable Oil
2) Chicken Marinade:
700 grams Chicken Thighs and Drumsticks bone-in and skinless (Note 2)
¾ cup Yogurt or hung curd
¼ cup Tomato Puree
¼ cup Vegetable Oil
1 tablespoon Ginger Garlic Paste minced ginger and garlic
1 tablespoon Red Chilli Powder sub with 1 teaspoon Paprika + 1 teaspoon Cayenne
1 teaspoon Turmeric Powder
1 teaspoon Garam Masala Powder
2 tablespoon Brown Onions
1 ¼ teaspoon Salt
3) Saffron:
2 tablespoon Hot Milk
10-15 Saffron strands
Parboiled Rice (70% cooked):
2 cups Basmati Rice Note 3
6 cups Water
2 tablespoon Salt
1 Bayleaf
5-6 Cloves
2-3 Cardamom Pods
4) Other Biryani Ingredients:
1 cup Mint Leaves fresh
1 cup Coriander Leaves Cilantro
1 ½ tablespoons Ghee or Butter
5) To Serve:
Crispy Brown Onions
Onion Raita'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=830,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
biriyani = ft.Container(
    content=biriyani_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=830,
    padding=5
)

chicken_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<CHICKEN65>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/chicken 65.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) Chicken - 1 lb (cut into bite size pieces),
2) Onion - 2 (finely chopped),
3) Green Chillies - 2,
4) Ginger Garlic Paste - 1 tbsp,
5) Tomatoes - 2 (pureed),
6) Yogurt - 2 tbsp (beaten),
7) Turmeric Powder - 1/2 tsp,
8) Red Chili Powder - 3 tsp,
9) Coriander Powder - 2 tsp,
10) Cumin Powder - 1/2 tsp,
11) Fennel Powder - 1/2 tsp,
12) Garam Masala Powder - 1/2 tsp,
13) Cumin Seeds - 1/2 tsp,
14) Fennel seeds - 1/2 tsp,
15) Salt - as needed,
16) Oil - 3 tbsp.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=400,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
chicken = ft.Container(
    content=chicken_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=750,
    padding=5
)

sambhar_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<SAMBHAR>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/sambhar-masala.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) Toor dal - 3/4 cup (You can also use masoor dal or green gram dal or a combination of dals),
2) Vegetables (any choice of a single/mixed vegetables) - 1 cup (The choice of vegetables can include brinjal, potato, radish, drumstick, spinach, shallot onions, tomato, raw mango, carrot, zucchini, yellow squash, lima beans, pumpkin, yam, taro-root, okra, knolkhol etc),
3) Shallot Onions - 8-10 (or 1 onion chopped),
4) Green Chilly - 1 or 2,
5) Tomatoes - 1,
6) Tamarind Juice - 1 1/2 tbsp,
7) Sambhar powder (store bought or home made) - 1 tbsp (you can increase to your taste),
8) Mustard seeds - 1/4 tsp,
9) Cumin seeds - 1/4 tsp,
10) Dry red Chilies - 2,
11) Curry leaves - 2 strands.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=450,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
sambhar = ft.Container(
    content=sambhar_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

cookies_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<COOKIES>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/cookies.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) 3 tablespoons butter, very soft or partially melted,
2) 3 tablespoons packed brown sugar,
3) 1-1/2 tablespoons white sugar,
4) 1/4 teaspoon vanilla,
5) 1 egg yolk,
6) 1/3 cup + 2 tablespoons all-purpose flour (~60 grams, see note 1),
7) 1 teaspoon cornstarch,
8) 1/4 teaspoon baking soda,
9) 1/4 teaspoon kosher salt,
10) 1/4 cup chocolate chips.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=330,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
cookies = ft.Container(
    content=cookies_e,
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
sushi_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<SUSHI>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/sushi.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) 100g sushi rice
2) 1 sheet nori seaweed
3) 2 tbsp sushi vinegar
4) soy sauce
5) wasabi
6) sushi ginger
7) roasted white sesame seeds (optional)

recommended fillings:
1) tuna – sashimi grade, raw
2) salmon – sashimi grade, raw
3) avocado
4) cucumber
5) crab sticks
6) canned tuna mixed with mayo
7) prawns'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=430,
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

ramen_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<RAMEN>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/ramen.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) Ramen noodles (our classic Maruchan package is all we need, sans the seasoning!)
2) Garlic and ginger
3) Broth (chicken or veg)
4) Dried shiitake mushrooms
5) Veggies like carrots or kale
6) All your favorite toppings like some panko, egg, chili oil, etc.'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=220,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
ramen = ft.Container(
    content=ramen_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

takoyagi_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<TAKOYAGI>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/takoyagi.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) Takoyaki Mix
3 large eggs lightly beaten
4.25 cups cold water
2 tsp instant dashi
2 tsp soy sauce
1/2 tsp salt
2.5 cups all purpose flour about 300g

2) Takoyaki Filling
1/2 lb boiled octopus 0.5" cubed
1 bunch green onions sliced
1 cup tempura bits or rice krispies
beni shoga/pickled ginger if desired
shredded or cubed cheese if desired'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=370,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
takoyagi = ft.Container(
    content=takoyagi_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

omurice_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<OMURICE>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/omurice.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) 2 cups Cooked white rice Preferably day-old rice
2) 1 small Carrot
3) 1/2 White onion
4) 1/4 Green bell pepper
5) 1/4 lb Ground beef
6) 3 tbsp Vegetable oil Divided
7) 8 Eggs Divided
8) 2 tbsp Milk Divided
9) 1/2 tsp Salt Divided'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=290,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
omurice = ft.Container(
    content=omurice_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

udon_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<UDON>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/udon.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
        ft.Text('''1) 3 packs Frozen udon
2) 3-4 strips Bacon Depending on thickness
3) 3/4 cup Parmesan Grated
4) 1/4 cup Pecorino Romano Grated
5) 1 stalk Green onion
6) 4 Room temperature eggs 3 egg yolks, 1 whole egg
7) 2 tbsp Shiro miso paste
8) 2 cloves Garlic Minced
9) Shichimi togarashi Optional'''),
        padding=ft.padding.only(left=10,right=10,bottom=20),
        width=400,
        height=290,
    )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
udon = ft.Container(
    content=udon_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)

curryrice_e = ft.Column(
[
    ft.Container(height=10),   
    ft.Text(value="<CURRYRICE>", font_family="Ancient", size=30),
    ft.Container(height=5),
    ft.Image(src="/images/curryrice.png", width=300),
    ft.Container(height=10),
    ft.Text("Recipe",font_family="Sticky",size=50),
    ft.Container(height=5),
    ft.Container(
            ft.Text('''1) 2 cubes Japanese curry block I used Golden Curry
2) 1/2 Potato
3) 1/2 Onion
4) 1/2 Large carrot
5) 1/2 Chicken breast
6) 1 and 1/2 cup Chicken broth
7) 1 cup Rice
8) 1 sheet Nori
9) 1 tsp Olive oil'''),
            padding=ft.padding.only(left=10,right=10,bottom=20),
            width=400,
            height=280,
        )
   ], horizontal_alignment='center',scroll=ft.ScrollMode.HIDDEN 
)
curryrice = ft.Container(
    content=curryrice_e,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=('#E4EEE9', '#93A5CE')
    ),
    width=400,
    height=800,
    padding=5
)