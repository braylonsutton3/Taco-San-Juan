from flask import Flask, render_template_string

app = Flask(__name__)

BUSINESS = {
    "name": "Tacos San Juan",
    "phone_display": "(859) 803-7584",
    "phone_link": "+18598037584",
    "address": "610 N Broadway St",
    "city": "Georgetown, KY 40324",
    "maps_url": "https://www.google.com/maps/search/?api=1&query=610+N+Broadway+St+Georgetown+KY+40324",
}

HIGHLIGHTS = [
    {"tag": "Every Tuesday", "name": "Taco Tuesday", "price": "Discounted Tacos", "text": "Street tacos at a special Tuesday price. Choose your favorite meat, topped with onions and cilantro.", "icon": "🌮"},
    {"tag": "House Favorite", "name": "Grande Burrito", "price": "$12.50", "text": "Meat, cheese, beans, rice, lettuce, tomatoes and avocado.", "icon": "🌯"},
    {"tag": "Loaded & Crispy", "name": "Birria Fries", "price": "$13.50", "text": "Loaded fries with queso, birria, pico de gallo and jalapeños.", "icon": "🍟"},
]

MENU = [
    ("Tacos", [
        ("Street Taco — small tortilla", "$3.25 ea", "Double tortilla, meat, onions and cilantro."),
        ("Supreme Taco", "$4.75 ea", "Corn or flour tortilla, meat, cheese, lettuce, tomato, onions and cilantro."),
        ("Large Taco — flour or corn", "$4.50 ea", "Large tortilla with your choice of meat."),
        ("Lengua add-on", "$4.25", "Tender beef tongue."),
        ("Cabeza add-on", "$3.75", "Seasoned beef head."),
    ]),
    ("Appetizers", [
        ("Salsa & Chips", "$3.99", "Fresh salsa with crisp tortilla chips."),
        ("Queso & Chips", "$4.99", "Add asada or chorizo +$3.00."),
        ("Pico de Gallo", "$4.50", "Fresh tomatoes, onion, cilantro and lime."),
        ("Guacamole & Chips", "$6.50", "Fresh guacamole with tortilla chips."),
        ("Nachos", "$13.50", "Refried beans, queso, meat, lettuce, pico, avocado and sour cream."),
        ("Street Nachos", "$13.50", "Refried beans, queso, tomatillo sauce and your choice of meat."),
        ("Loaded Fries", "$13.50", "Queso, steak, chorizo or al pastor, pico de gallo and avocado."),
        ("Esquite", "$6.50", "Street corn in a cup with mayo, cotija and chili powder."),
    ]),
    ("Burritos", [
        ("Grande Burrito", "$12.50", "Meat, cheese, beans, rice, lettuce, tomatoes and avocado."),
        ("Burrito Mexicano", "$12.50", "Cheese, whole pinto beans, rice, meat, onions and cilantro."),
        ("Queso Burrito", "$13.99", "Choice of meat covered with cheese sauce, served with rice and beans."),
        ("Burrito Dorado with Queso", "$13.50", "Deep-fried burrito with cheese, beans and meat, covered in cheese sauce."),
        ("Burrito Enchilada", "$13.50", "Cheese, rice, beans and chicken or steak, smothered in sauce."),
        ("Burrito California", "$12.99", "Mozzarella, asada, fries, cheese sauce, pico and avocado."),
    ]),
    ("Quesadillas", [
        ("Cheese Quesadilla", "$4.00", "Classic grilled cheese quesadilla."),
        ("Meat & Cheese Quesadilla", "$10.99", "Choice of meat with melted cheese."),
        ("Quesadilla Suprema", "$11.50", "Meat, lettuce, tomato and avocado."),
        ("Quesadilla Mexicana", "$11.50", "Cheese, whole pinto beans, meat, onions and cilantro."),
        ("Machete Quesadilla", "$16.00", "Cheese, meat of choice, onions and cilantro."),
    ]),
    ("Birria", [
        ("Birria Quesatacos — 3", "$14.99", "Cheese and birria, onions and cilantro, with consommé."),
        ("Pizza Birria", "$22.50", "Cheese, birria, onions and cilantro, served with consommé."),
        ("Birria Ramen", "$11.00", "Rich birria broth with ramen noodles."),
        ("Birria Ramen + 2 Quesatacos", "$15.50", "Birria ramen paired with two quesatacos."),
        ("Birria Burrito", "$13.99", "Cheese, beans, rice and birria, smothered with consommé."),
        ("Birria Fries", "$13.50", "Loaded fries with queso, birria, pico de gallo and jalapeños."),
        ("Birria Nachos", "$13.50", "Loaded with queso, birria and pico de gallo."),
    ]),
    ("Tortas", [
        ("La Clasica", "$12.75", "Meat, mayo, cheese, lettuce, tomatoes, avocado and onions."),
        ("Torta del Chavo", "$12.75", "Cheese, ham, lettuce, avocado, tomato and onions."),
        ("La Cubana", "$15.50", "Ham, hot dog, chorizo, asada, eggs, mayo, cheese and vegetables."),
        ("Pambazo", "$12.75", "Guajillo-dipped telera with potatoes, chorizo, lettuce, cheese and sour cream."),
    ]),
    ("Antojitos Mexicanos", [
        ("Flautas", "$13.99", "Five chicken taquitos with lettuce, tomatoes, cheese and sour cream; rice and beans."),
        ("Flautas Ahogadas", "$12.99", "Five chicken taquitos with green tomatillo sauce and toppings."),
        ("Tacos Dorados", "$13.99", "Four potato or chicken tacos with toppings, rice and beans."),
        ("Empanadas Ahogadas", "$13.50", "Two chicken-and-cheese empanadas with tomatillo sauce."),
        ("Empanadas — 3", "$15.50", "Chicken or cheese empanadas topped with lettuce, tomatoes and cheese."),
        ("Gordita", "$6.50 ea", "Thick tortilla with beans, meat, lettuce and crumbling cheese."),
        ("Sope", "$6.99", "Thick tortilla with beans, meat, lettuce, tomato, cheese and sour cream."),
        ("Huarache", "$8.50", "Oval tortilla with beans, meat, lettuce and crumbling cheese."),
        ("Enchiladas Verdes — 4", "$13.99", "Chicken or cheese enchiladas with tomatillo sauce, toppings and rice."),
    ]),
    ("Breakfast · 9 AM–12 PM", [
        ("Chorizo Breakfast Burrito", "$8.75", "Eggs, potatoes, chorizo and cheddar."),
        ("El Mexicano Breakfast Burrito", "$8.75", "Egg, potatoes, grilled vegetables, jalapeños and cheddar."),
        ("Birria Breakfast Burrito", "$11.00", "Eggs, potatoes, birria and cheddar, served with consommé."),
        ("Bacon Breakfast Burrito", "$8.75", "Eggs, potatoes, bacon and cheddar."),
        ("Breakfast Sopes — 2", "$9.50", "Thick tortillas with beans, egg and avocado."),
        ("Los Chilaquiles", "$13.00", "Red or green chilaquiles with crema, queso, three eggs and beans. Add steak +$3."),
        ("Traditional Breakfast Platter", "$13.99", "Three eggs, potatoes, bacon and beans."),
        ("Huevos con Chorizo", "$13.99", "Served with potatoes, bacon and beans."),
        ("Huevos Rancheros", "$13.99", "Eggs on corn tortillas with mild sauce, avocado and beans."),
        ("El Breakfast Sandwich", "$7.99", "Eggs, cheddar, bacon, lettuce, avocado and mayo on white bread."),
    ]),
    ("Sides & Extras", [
        ("Rice or Beans", "$3.75", "A side of rice or refried beans."),
        ("Beans & Rice", "$4.75", "A side of both."),
        ("French Fries", "$4.00", "Crispy golden fries."),
        ("Sour Cream", "$0.50", "Side portion."),
        ("Extra Tortillas", "$1.50", "Corn or flour."),
        ("Shredded Cheese", "$0.25", "Per taco."),
        ("Side of Limes", "$1.00", "Fresh lime wedges."),
    ]),
]

PAGE = r'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Tacos San Juan — authentic Mexican food in Georgetown, Kentucky.">
<title>Tacos San Juan | Georgetown, KY</title>
<style>
:root{--orange:#ff6a00;--orange2:#ff8b22;--black:#080808;--ink:#161616;--cream:#fff7ed;--white:#fff;--muted:#6d625b;--line:#ead9c8}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{font-family:Arial,Helvetica,sans-serif;color:var(--ink);background:var(--cream);line-height:1.55}a{text-decoration:none;color:inherit}.wrap{width:min(1180px,92%);margin:auto}
nav{position:sticky;top:0;z-index:20;background:rgba(8,8,8,.95);color:#fff;border-bottom:3px solid var(--orange);backdrop-filter:blur(10px)}.nav{min-height:72px;display:flex;align-items:center;justify-content:space-between;gap:24px}.logo{font:900 1.6rem Georgia,serif;color:var(--orange)}.links{display:flex;align-items:center;gap:22px;font-weight:800}.links a:hover{color:var(--orange)}
.btn{display:inline-flex;align-items:center;justify-content:center;padding:13px 22px;border-radius:6px;background:var(--orange);color:#fff;font-weight:900;transition:.2s}.btn:hover{background:var(--orange2);transform:translateY(-2px)}.btn.ghost{background:transparent;border:2px solid #fff}.btn.ghost:hover{background:#fff;color:#000}
.hero{min-height:700px;display:grid;place-items:center;text-align:center;color:#fff;background:linear-gradient(90deg,rgba(0,0,0,.9),rgba(0,0,0,.52),rgba(0,0,0,.88)),url('/static/images/storefront.jpg') center/cover}.hero-inner{max-width:850px;padding:100px 0}.kicker{display:inline-block;color:var(--orange);font-weight:900;letter-spacing:2px;text-transform:uppercase}.hero h1{font:900 clamp(3.5rem,9vw,7rem)/.9 Georgia,serif;margin:18px 0 24px}.hero h1 span{color:var(--orange)}.hero p{font-size:1.2rem;max-width:700px;margin:0 auto 30px}.actions{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
section{padding:90px 0}.dark{background:var(--black);color:#fff}.heading{max-width:760px;margin:0 auto 44px;text-align:center}.heading h2{font:900 clamp(2.4rem,5vw,4rem)/1 Georgia,serif;margin:10px 0 14px}.heading p{color:var(--muted)}.dark .heading p{color:#bbb}
.highlights{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.highlight{position:relative;overflow:hidden;min-height:330px;padding:30px;border:1px solid #30271f;border-radius:18px;background:linear-gradient(145deg,#21160e,#080808);box-shadow:0 20px 50px rgba(0,0,0,.3)}.highlight:before{content:"";position:absolute;width:160px;height:160px;border-radius:50%;right:-55px;top:-55px;background:var(--orange);opacity:.13}.hi-icon{font-size:3rem}.tag{display:inline-block;margin:18px 0 10px;padding:5px 10px;border-radius:4px;background:var(--orange);font-size:.72rem;font-weight:900;letter-spacing:1px;text-transform:uppercase}.highlight h3{font:900 2rem Georgia,serif}.highlight p{color:#cfc6bd;margin:12px 0 20px}.price{color:var(--orange);font-size:1.35rem;font-weight:900}
.menu-tools{display:flex;flex-wrap:wrap;justify-content:center;gap:9px;margin-bottom:34px}.menu-tools a{padding:8px 13px;border:1px solid var(--line);border-radius:999px;background:#fff;font-size:.85rem;font-weight:800}.menu-tools a:hover{border-color:var(--orange);color:var(--orange)}.category{scroll-margin-top:100px;margin:28px 0 44px}.category h3{display:flex;align-items:center;gap:15px;font:900 2rem Georgia,serif;margin-bottom:14px}.category h3:after{content:"";height:3px;flex:1;background:linear-gradient(90deg,var(--orange),transparent)}.menu-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px 28px}.item{padding:18px 0;border-bottom:1px dashed #d9c2ad}.item-top{display:flex;justify-content:space-between;gap:18px;align-items:baseline}.item h4{font-size:1.05rem}.item strong{white-space:nowrap;color:var(--orange)}.item p{color:var(--muted);font-size:.92rem;margin-top:4px}
.story{background:#fff}.story-grid,.visit-grid{display:grid;grid-template-columns:1fr 1fr;gap:55px;align-items:center}.photo{height:520px;width:100%;object-fit:cover;border-radius:18px;box-shadow:18px 18px 0 var(--orange)}.copy h2{font:900 clamp(2.5rem,5vw,4rem)/1 Georgia,serif;margin:12px 0 20px}.copy p{color:var(--muted);margin-bottom:16px}.visit{background:var(--orange);color:#fff}.visit-card{background:#0b0b0b;border-radius:18px;padding:32px}.visit-card h3{font:900 2rem Georgia,serif}.visit-card p{margin:15px 0;color:#ddd}.visit-card .btn{margin-top:8px}
footer{padding:30px;background:#000;color:#aaa;text-align:center}footer strong{color:var(--orange)}
@media(max-width:850px){.links>a:not(.btn){display:none}.highlights,.story-grid,.visit-grid{grid-template-columns:1fr}.menu-grid{grid-template-columns:1fr}.photo{height:390px}.hero{min-height:620px}}
@media(max-width:520px){section{padding:68px 0}.logo{font-size:1.25rem}.links .btn{padding:10px 13px;font-size:.82rem}.highlight{min-height:auto}.hero h1{font-size:3.6rem}.category h3{font-size:1.6rem}}
</style></head><body>
<nav><div class="wrap nav"><a class="logo" href="#home">TACOS SAN JUAN</a><div class="links"><a href="#highlights">Highlights</a><a href="#menu">Menu</a><a href="#story">Our Story</a><a href="#visit">Visit</a><a class="btn" href="tel:{{business.phone_link}}">Call to Order</a></div></div></nav>
<main>
<section class="hero" id="home"><div class="wrap hero-inner"><span class="kicker">Authentic Mexican Food · Georgetown, Kentucky</span><h1>BIG FLAVOR.<br><span>ZERO SHORTCUTS.</span></h1><p>Street tacos, loaded burritos, birria favorites and traditional Mexican plates—made fresh and served with heart.</p><div class="actions"><a class="btn" href="#menu">Explore the Menu</a><a class="btn ghost" href="#visit">Visit Us</a></div></div></section>
<section class="dark" id="highlights"><div class="wrap"><div class="heading"><span class="kicker">Menu Highlights</span><h2>Start with the favorites</h2><p>Three crave-worthy reasons to stop by Tacos San Juan.</p></div><div class="highlights">{% for h in highlights %}<article class="highlight"><div class="hi-icon">{{h.icon}}</div><span class="tag">{{h.tag}}</span><h3>{{h.name}}</h3><p>{{h.text}}</p><div class="price">{{h.price}}</div></article>{% endfor %}</div></div></section>
<section id="menu"><div class="wrap"><div class="heading"><span class="kicker">Full Menu</span><h2>Fresh, filling & full of flavor</h2><p>Current restaurant menu and updated prices. Breakfast is served from 9 AM–12 PM.</p></div><div class="menu-tools">{% for category,items in menu %}<a href="#cat-{{loop.index}}">{{category}}</a>{% endfor %}</div>{% for category,items in menu %}<section class="category" id="cat-{{loop.index}}"><h3>{{category}}</h3><div class="menu-grid">{% for name,price,description in items %}<article class="item"><div class="item-top"><h4>{{name}}</h4><strong>{{price}}</strong></div><p>{{description}}</p></article>{% endfor %}</div></section>{% endfor %}<p style="color:var(--muted);font-size:.85rem;text-align:center">Meat choices include asada, pollo, al pastor, barbacoa, chorizo, lengua and cabeza. Prices are subject to change; call to confirm specials.</p></div></section>
<section class="story" id="story"><div class="wrap story-grid"><img class="photo" src="/static/images/dining-room.jpg" alt="Colorful dining room at Tacos San Juan"><div class="copy"><span class="kicker">Our Restaurant</span><h2>Georgetown’s local stop for authentic flavor</h2><p>Tacos San Juan serves Mexican favorites in a colorful, welcoming setting. From breakfast burritos and street tacos to birria and loaded fries, every visit has something worth craving.</p><p>Bring the family, grab a quick lunch or call ahead for pickup.</p><a class="btn" href="tel:{{business.phone_link}}">Call {{business.phone_display}}</a></div></div></section>
<section class="visit" id="visit"><div class="wrap visit-grid"><div class="copy"><span class="kicker" style="color:#000">Visit Us</span><h2>Come hungry.</h2><p style="color:#fff">Find us on North Broadway in Georgetown, Kentucky. Call ahead to place your order or open directions below.</p></div><div class="visit-card"><h3>{{business.name}}</h3><p><strong>{{business.address}}<br>{{business.city}}</strong></p><p><a href="tel:{{business.phone_link}}">{{business.phone_display}}</a></p><div class="actions" style="justify-content:flex-start"><a class="btn" href="tel:{{business.phone_link}}">Call to Order</a><a class="btn ghost" href="{{business.maps_url}}" target="_blank" rel="noopener">Directions</a></div></div></div></section>
</main><footer><div class="wrap"><strong>{{business.name}}</strong> · {{business.address}}, {{business.city}} · {{business.phone_display}}</div></footer>
</body></html>'''

@app.route("/")
def home():
    return render_template_string(PAGE, business=BUSINESS, highlights=HIGHLIGHTS, menu=MENU)

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
