from flask import Flask, render_template

app = Flask(__name__)

HOURS = [
    ("Monday", "9:00 AM – 3:00 PM"),
    ("Tuesday", "9:00 AM – 7:00 PM"),
    ("Wednesday", "9:00 AM – 7:00 PM"),
    ("Thursday", "9:00 AM – 7:00 PM"),
    ("Friday", "9:00 AM – 7:00 PM"),
    ("Saturday", "9:00 AM – 4:00 PM"),
    ("Sunday", "Closed"),
]

MENU = [
    (
        "Street Favorites",
        [
            (
                "Street Tacos",
                "$2.99",
                "Double corn tortilla with asada, al pastor, chicken, "
                "chorizo or barbacoa; onions, cilantro, lime and salsa.",
            ),
            (
                "Birria Quesatacos",
                "$14.50",
                "Three cheese-filled birria tacos with onions, cilantro "
                "and a side of rich consommé.",
            ),
            (
                "Tacos Dorados",
                "$13.00",
                "Four fried potato or chicken tacos with lettuce, pico de "
                "gallo, queso fresco and sour cream; served with rice and beans.",
            ),
            (
                "Gorditas",
                "$5.50",
                "Thick handmade tortilla with your choice of filling, "
                "beans, lettuce and queso fresco.",
            ),
        ],
    ),
    (
        "Burritos & Quesadillas",
        [
            (
                "Grande Burrito",
                "$11.99",
                "Choice of meat, cheese, rice, beans, lettuce, tomato "
                "and avocado.",
            ),
            (
                "Burrito Dorado with Cheese",
                "$12.50",
                "Deep-fried burrito with cheese, refried beans and chicken, "
                "steak or al pastor, finished with cheese sauce.",
            ),
            (
                "Quesadilla",
                "$10.99",
                "Large flour tortilla, melted cheese and choice of meat; "
                "served with lettuce, tomato and avocado.",
            ),
            (
                "Birria Burrito",
                "$13.99",
                "Tender shredded birria beef, cheese and house fillings "
                "with consommé for dipping.",
            ),
        ],
    ),
    (
        "House Specialties",
        [
            (
                "Carne Asada Fries",
                "$13.50",
                "Crispy fries loaded with steak, melted cheese, pico de "
                "gallo and avocado.",
            ),
            (
                "Nachos Mexicanos",
                "$11.99",
                "Nachos with meat, melted cheese, beans, lettuce, pico de "
                "gallo, avocado and sour cream.",
            ),
            (
                "Torta Regular",
                "$10.99",
                "Toasted telera roll with meat, mayo, cheese, lettuce, "
                "tomato, avocado and onion.",
            ),
            (
                "Enchiladas Verdes",
                "$12.50",
                "Chicken or cheese enchiladas in green sauce with lettuce, "
                "tomato, sour cream, queso fresco and rice.",
            ),
        ],
    ),
    (
        "Sides",
        [
            (
                "Chips & Salsa",
                "$4.99",
                "Crisp tortilla chips with fresh house salsa.",
            ),
            (
                "Cheese Dip",
                "$5.99",
                "Warm, creamy queso dip.",
            ),
            (
                "Guacamole",
                "$5.99",
                "Avocado, lime and fresh seasoning.",
            ),
            (
                "Rice or Beans",
                "$3.99",
                "A classic side, prepared in house.",
            ),
        ],
    ),
]


@app.context_processor
def shared_information():
    """Make the business hours available on every page."""
    return {"hours": HOURS}


@app.route("/")
def home():
    """Display the homepage."""
    return render_template("home.html")


@app.route("/menu")
def menu():
    """Display the restaurant menu."""
    return render_template(
        "menu.html",
        menu_sections=MENU,
    )


@app.route("/visit")
def visit():
    """Display the location, hours and About section."""
    return render_template("visit.html")


@app.errorhandler(404)
def page_not_found(error):
    """Send visitors back to the homepage if a page does not exist."""
    return render_template("home.html"), 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
    )
