from flask import Flask, render_template_string

app = Flask(__name__)

BUSINESS = {
    "name": "Tacos San Juan",
    "phone_display": "(859) 803-7584",
    "phone_link": "+18598037584",
    "address": "610 N Broadway St",
    "city": "Georgetown, KY 40324",
    "maps_url": (
        "https://www.google.com/maps/search/"
        "?api=1&query=610+N+Broadway+St+Georgetown+KY+40324"
    ),
}

MENU = [
    {
        "name": "Street Tacos",
        "description": (
            "Authentic street tacos with onion and cilantro. Choose from "
            "steak, barbacoa, chicken, al pastor, chorizo, lengua, or tripe."
        ),
        "price": "From $2.00",
        "emoji": "🌮",
    },
    {
        "name": "Grande Burrito",
        "description": (
            "Your choice of meat with cheese, rice, beans, lettuce, "
            "tomatoes, and avocado."
        ),
        "price": "$8.00",
        "emoji": "🌯",
    },
    {
        "name": "Quesadilla",
        "description": (
            "Large flour tortilla with cheese and your choice of meat, "
            "served with rice and beans."
        ),
        "price": "$9.00",
        "emoji": "🧀",
    },
    {
        "name": "Taco Salad",
        "description": (
            "A fresh bed of lettuce with steak or grilled chicken, "
            "tomatoes, cheese, avocado, and sour cream."
        ),
        "price": "$8.50",
        "emoji": "🥗",
    },
    {
        "name": "Carne Asada Fries",
        "description": (
            "French fries loaded with steak, melted cheese, pico de gallo, "
            "and avocado."
        ),
        "price": "$11.00",
        "emoji": "🍟",
    },
    {
        "name": "Molcajete",
        "description": (
            "Grilled steak, chicken, shrimp, chorizo, peppers, onions, "
            "and melted cheese with rice and beans."
        ),
        "price": "House Favorite",
        "emoji": "🍽️",
    },
]

HOURS = [
    ("Monday", "Call for hours"),
    ("Tuesday", "Call for hours"),
    ("Wednesday", "Call for hours"),
    ("Thursday", "Call for hours"),
    ("Friday", "Call for hours"),
    ("Saturday", "Call for hours"),
    ("Sunday", "Call for hours"),
]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <meta
        name="description"
        content="Tacos San Juan serves authentic Mexican food in Georgetown, Kentucky."
    >

    <title>Tacos San Juan | Georgetown, Kentucky</title>

    <style>
        :root {
            --orange: #ef641f;
            --orange-dark: #bd400b;
            --green: #17673d;
            --cream: #fff8ef;
            --white: #ffffff;
            --dark: #21150f;
            --muted: #6d5a4d;
            --border: rgba(239, 100, 31, 0.16);
            --shadow: 0 18px 45px rgba(71, 37, 15, 0.14);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background: var(--cream);
            color: var(--dark);
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
        }

        img {
            display: block;
            width: 100%;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        .container {
            width: min(1140px, 92%);
            margin: auto;
        }

        nav {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.96);
            border-bottom: 1px solid var(--border);
            box-shadow: 0 5px 22px rgba(50, 25, 10, 0.07);
            backdrop-filter: blur(12px);
        }

        .nav-content {
            min-height: 76px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 25px;
        }

        .logo {
            color: var(--orange);
            font-family: Georgia, serif;
            font-size: 1.7rem;
            font-weight: 900;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 24px;
        }

        .nav-links > a {
            font-weight: 800;
        }

        .nav-links > a:hover {
            color: var(--orange);
        }

        .button {
            display: inline-block;
            padding: 13px 22px;
            border-radius: 999px;
            font-weight: 900;
            transition: 0.2s ease;
        }

        .button:hover {
            transform: translateY(-2px);
        }

        .button-orange {
            color: white !important;
            background: var(--orange);
            box-shadow: 0 9px 22px rgba(239, 100, 31, 0.28);
        }

        .button-orange:hover {
            background: var(--orange-dark);
        }

        .button-outline {
            color: white;
            border: 2px solid white;
        }

        .button-outline:hover {
            color: var(--orange);
            background: white;
        }

        .hero {
            min-height: 690px;
            display: grid;
            place-items: center;
            color: white;
            text-align: center;
            background:
                linear-gradient(
                    rgba(24, 12, 5, 0.54),
                    rgba(24, 12, 5, 0.72)
                ),
                url("/static/images/storefront.jpg")
                center/cover no-repeat;
        }

        .hero-content {
            max-width: 850px;
            padding: 100px 0;
        }

        .eyebrow {
            display: inline-block;
            margin-bottom: 18px;
            padding: 8px 16px;
            border: 1px solid rgba(255, 255, 255, 0.45);
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.15);
            font-size: 0.82rem;
            font-weight: 900;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }

        h1 {
            margin-bottom: 22px;
            font-family: Georgia, serif;
            font-size: clamp(3.2rem, 8vw, 6.7rem);
            line-height: 0.96;
            text-shadow: 0 5px 20px rgba(0, 0, 0, 0.24);
        }

        .hero p {
            max-width: 700px;
            margin: 0 auto 31px;
            font-size: clamp(1.05rem, 2vw, 1.28rem);
        }

        .hero-buttons {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 13px;
        }

        section {
            padding: 90px 0;
        }

        .section-heading {
            max-width: 700px;
            margin: 0 auto 45px;
            text-align: center;
        }

        .section-label {
            color: var(--orange);
            font-size: 0.82rem;
            font-weight: 900;
            letter-spacing: 1.4px;
            text-transform: uppercase;
        }

        .section-heading h2,
        .about-copy h2,
        .visit-copy h2 {
            margin: 8px 0 14px;
            font-family: Georgia, serif;
            font-size: clamp(2.3rem, 5vw, 3.7rem);
            line-height: 1.06;
        }

        .section-heading p,
        .about-copy p {
            color: var(--muted);
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
        }

        .menu-card {
            padding: 29px;
            border: 1px solid var(--border);
            border-radius: 23px;
            background: white;
            box-shadow: var(--shadow);
            transition: 0.25s ease;
        }

        .menu-card:hover {
            transform: translateY(-7px);
            border-color: var(--orange);
        }

        .menu-icon {
            display: grid;
            place-items: center;
            width: 58px;
            height: 58px;
            margin-bottom: 18px;
            border-radius: 17px;
            background: #ffede1;
            font-size: 1.85rem;
        }

        .menu-card h3 {
            margin-bottom: 8px;
            font-family: Georgia, serif;
            font-size: 1.48rem;
        }

        .menu-card p {
            color: var(--muted);
        }

        .price {
            display: inline-block;
            margin-top: 18px;
            color: var(--orange);
            font-size: 1.12rem;
            font-weight: 900;
        }

        .about {
            background: white;
        }

        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            gap: 58px;
        }

        .about-photo img {
            height: 500px;
            object-fit: cover;
            border-radius: 28px;
            box-shadow: var(--shadow);
        }

        .about-copy p {
            margin-bottom: 17px;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-top: 29px;
        }

        .feature {
            padding: 17px 10px;
            border-radius: 15px;
            background: var(--cream);
            text-align: center;
            font-weight: 900;
        }

        .gallery-grid {
            display: grid;
            grid-template-columns: 1.25fr 1fr 1fr;
            grid-template-rows: 245px 245px;
            gap: 16px;
        }

        .gallery-card {
            position: relative;
            overflow: hidden;
            border-radius: 22px;
            background: #e8ded5;
            box-shadow: var(--shadow);
        }

        .gallery-card:first-child {
            grid-row: 1 / 3;
        }

        .gallery-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.35s ease;
        }

        .gallery-card:hover img {
            transform: scale(1.04);
        }

        .gallery-caption {
            position: absolute;
            right: 0;
            bottom: 0;
            left: 0;
            padding: 30px 17px 15px;
            color: white;
            font-weight: 900;
            background: linear-gradient(transparent, rgba(0, 0, 0, 0.75));
        }

        .visit {
            color: white;
            background: var(--orange);
        }

        .visit-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: start;
            gap: 52px;
        }

        .visit-copy p {
            margin-bottom: 16px;
            font-size: 1.07rem;
        }

        .contact-card {
            overflow: hidden;
            border-radius: 24px;
            background: white;
            color: var(--dark);
            box-shadow: var(--shadow);
        }

        .contact-image {
            height: 210px;
            object-fit: cover;
        }

        .contact-details {
            padding: 27px;
        }

        .contact-details h3 {
            margin-bottom: 14px;
            font-family: Georgia, serif;
            font-size: 1.7rem;
        }

        .contact-row {
            padding: 13px 0;
            border-bottom: 1px solid #eee1d7;
        }

        .contact-row:last-child {
            border-bottom: 0;
        }

        .contact-row span {
            display: block;
            color: var(--muted);
            font-size: 0.87rem;
            font-weight: 800;
            text-transform: uppercase;
        }

        .contact-row strong {
            display: block;
            margin-top: 3px;
            font-size: 1.04rem;
        }

        .map-button {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 19px;
            border-radius: 999px;
            color: white;
            background: var(--green);
            font-weight: 900;
        }

        footer {
            padding: 34px 0;
            background: #20140e;
            color: #d9c8bc;
            text-align: center;
        }

        footer strong {
            color: white;
        }

        @media (max-width: 900px) {
            .nav-links > a:not(.button) {
                display: none;
            }

            .menu-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .about-grid,
            .visit-grid {
                grid-template-columns: 1fr;
            }

            .gallery-grid {
                grid-template-columns: 1fr 1fr;
                grid-template-rows: repeat(3, 270px);
            }

            .gallery-card:first-child {
                grid-column: 1 / 3;
                grid-row: auto;
            }
        }

        @media (max-width: 600px) {
            .logo {
                font-size: 1.28rem;
            }

            .nav-content {
                min-height: 68px;
            }

            .nav-links {
                gap: 8px;
            }

            .nav-links .button {
                padding: 10px 14px;
                font-size: 0.86rem;
            }

            .hero {
                min-height: 620px;
            }

            section {
                padding: 68px 0;
            }

            .menu-grid,
            .features,
            .gallery-grid {
                grid-template-columns: 1fr;
            }

            .gallery-grid {
                grid-template-rows: repeat(5, 255px);
            }

            .gallery-card:first-child {
                grid-column: auto;
            }

            .about-photo img {
                height: 390px;
            }
        }
    </style>
</head>

<body>
    <nav>
        <div class="container nav-content">
            <a class="logo" href="#home">{{ business.name }}</a>

            <div class="nav-links">
                <a href="#menu">Menu</a>
                <a href="#about">Our Story</a>
                <a href="#gallery">Photos</a>
                <a href="#visit">Visit</a>

                <a
                    class="button button-orange"
                    href="tel:{{ business.phone_link }}"
                >
                    Call to Order
                </a>
            </div>
        </div>
    </nav>

    <main>
        <section class="hero" id="home">
            <div class="container hero-content">
                <div class="eyebrow">
                    Authentic Mexican Food • Georgetown, Kentucky
                </div>

                <h1>Real flavor.<br>Made fresh.</h1>

                <p>
                    Authentic street tacos, loaded burritos, quesadillas,
                    seafood, and traditional Mexican favorites served locally
                    in Georgetown.
                </p>

                <div class="hero-buttons">
                    <a class="button button-orange" href="#menu">
                        Explore Our Menu
                    </a>

                    <a
                        class="button button-outline"
                        href="tel:{{ business.phone_link }}"
                    >
                        Call {{ business.phone_display }}
                    </a>
                </div>
            </div>
        </section>

        <section id="menu">
            <div class="container">
                <div class="section-heading">
                    <span class="section-label">Customer Favorites</span>
                    <h2>Authentic food made to satisfy</h2>
                    <p>
                        From street tacos and burritos to loaded fries and
                        house specialties, there is something for everyone.
                    </p>
                </div>

                <div class="menu-grid">
                    {% for item in menu %}
                        <article class="menu-card">
                            <div class="menu-icon">{{ item.emoji }}</div>
                            <h3>{{ item.name }}</h3>
                            <p>{{ item.description }}</p>
                            <div class="price">{{ item.price }}</div>
                        </article>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section class="about" id="about">
            <div class="container about-grid">
                <div class="about-photo">
                    <img
                        src="/static/images/dining-room.jpg"
                        alt="Colorful dining room inside Tacos San Juan"
                    >
                </div>

                <div class="about-copy">
                    <span class="section-label">Welcome to Tacos San Juan</span>

                    <h2>Local food with unforgettable flavor</h2>

                    <p>
                        Tacos San Juan is a local Georgetown restaurant serving
                        authentic Mexican dishes in a colorful and welcoming
                        atmosphere.
                    </p>

                    <p>
                        Stop in for street tacos, burritos, quesadillas,
                        seafood, traditional platillos, and other freshly
                        prepared favorites.
                    </p>

                    <div class="features">
                        <div class="feature">🌮 Authentic</div>
                        <div class="feature">🔥 Made Fresh</div>
                        <div class="feature">📍 Local</div>
                    </div>
                </div>
            </div>
        </section>

        <section id="gallery">
            <div class="container">
                <div class="section-heading">
                    <span class="section-label">Inside Tacos San Juan</span>
                    <h2>See our restaurant and menu</h2>
                    <p>
                        Take a look at our Georgetown location, dining room,
                        and authentic Mexican menu.
                    </p>
                </div>

                <div class="gallery-grid">
                    <figure class="gallery-card">
                        <img
                            src="/static/images/dining-room.jpg"
                            alt="Dining room at Tacos San Juan"
                        >
                        <figcaption class="gallery-caption">
                            Colorful, welcoming dining room
                        </figcaption>
                    </figure>

                    <figure class="gallery-card">
                        <img
                            src="/static/images/storefront.jpg"
                            alt="Tacos San Juan storefront"
                        >
                        <figcaption class="gallery-caption">
                            Georgetown location
                        </figcaption>
                    </figure>

                    <figure class="gallery-card">
                        <img
                            src="/static/images/menu-one.jpg"
                            alt="Tacos San Juan menu"
                        >
                        <figcaption class="gallery-caption">
                            Street tacos and favorites
                        </figcaption>
                    </figure>

                    <figure class="gallery-card">
                        <img
                            src="/static/images/menu-two.jpg"
                            alt="Tacos San Juan specialty menu"
                        >
                        <figcaption class="gallery-caption">
                            Platillos and specialties
                        </figcaption>
                    </figure>

                    <figure class="gallery-card">
                        <img
                            src="/static/images/digital-menu.jpg"
                            alt="Digital menu inside Tacos San Juan"
                        >
                        <figcaption class="gallery-caption">
                            More authentic choices
                        </figcaption>
                    </figure>
                </div>
            </div>
        </section>

        <section class="visit" id="visit">
            <div class="container visit-grid">
                <div class="visit-copy">
                    <span class="eyebrow">Visit Us</span>

                    <h2>Come enjoy Tacos San Juan</h2>

                    <p>
                        Visit us on North Broadway Street in Georgetown,
                        Kentucky, or call ahead to place your order.
                    </p>

                    <p>
                        <strong>{{ business.address }}</strong><br>
                        <strong>{{ business.city }}</strong>
                    </p>

                    <p>
                        <strong>
                            <a href="tel:{{ business.phone_link }}">
                                {{ business.phone_display }}
                            </a>
                        </strong>
                    </p>

                    <div class="hero-buttons" style="justify-content:flex-start;">
                        <a
                            class="button button-outline"
                            href="tel:{{ business.phone_link }}"
                        >
                            Call to Order
                        </a>

                        <a
                            class="button button-outline"
                            href="{{ business.maps_url }}"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Get Directions
                        </a>
                    </div>
                </div>

                <div class="contact-card">
                    <img
                        class="contact-image"
                        src="/static/images/storefront.jpg"
                        alt="Tacos San Juan at 610 North Broadway Street"
                    >

                    <div class="contact-details">
                        <h3>Restaurant Information</h3>

                        <div class="contact-row">
                            <span>Address</span>
                            <strong>
                                {{ business.address }}<br>
                                {{ business.city }}
                            </strong>
                        </div>

                        <div class="contact-row">
                            <span>Phone</span>
                            <strong>
                                <a href="tel:{{ business.phone_link }}">
                                    {{ business.phone_display }}
                                </a>
                            </strong>
                        </div>

                        <div class="contact-row">
                            <span>Hours</span>
                            <strong>
                                Call the restaurant for today's hours
                            </strong>
                        </div>

                        <a
                            class="map-button"
                            href="{{ business.maps_url }}"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Open in Google Maps
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>
                <strong>{{ business.name }}</strong> •
                {{ business.address }}, {{ business.city }} •
                {{ business.phone_display }}
            </p>

            <p>Authentic Mexican food served fresh in Georgetown.</p>
        </div>
    </footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        PAGE,
        business=BUSINESS,
        menu=MENU,
        hours=HOURS,
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
