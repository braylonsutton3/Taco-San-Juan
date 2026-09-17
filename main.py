from flask import Flask, render_template_string

app = Flask(__name__)

MENU = [
    {
        "name": "Street Tacos",
        "description": "Three warm corn tortillas with your choice of steak, chicken, or pork, topped with onion and cilantro.",
        "price": "$10.99",
        "emoji": "🌮",
    },
    {
        "name": "Loaded Burrito",
        "description": "A large flour tortilla filled with steak, chicken, or pork, plus rice, beans, cheese, and fresh salsa.",
        "price": "$11.99",
        "emoji": "🌯",
    },
    {
        "name": "Quesadilla",
        "description": "A grilled flour tortilla loaded with melted cheese and your choice of steak, chicken, or pork.",
        "price": "$9.99",
        "emoji": "🧀",
    },
    {
        "name": "Chips & Salsa",
        "description": "Freshly prepared tortilla chips served with our house-made salsa.",
        "price": "$4.49",
        "emoji": "🥣",
    },
    {
        "name": "Rice & Beans",
        "description": "A generous serving of traditional Mexican rice and seasoned beans.",
        "price": "$4.99",
        "emoji": "🍚",
    },
    {
        "name": "Taco Combo",
        "description": "Three tacos with your choice of meat, served with rice and beans.",
        "price": "$13.99",
        "emoji": "🍽️",
    },
]

HOURS = [
    ("Monday", "11:00 AM – 8:00 PM"),
    ("Tuesday", "11:00 AM – 8:00 PM"),
    ("Wednesday", "11:00 AM – 8:00 PM"),
    ("Thursday", "11:00 AM – 8:00 PM"),
    ("Friday", "11:00 AM – 9:00 PM"),
    ("Saturday", "11:00 AM – 9:00 PM"),
    ("Sunday", "12:00 PM – 7:00 PM"),
]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta
        name="description"
        content="Taco San Juan serves fresh tacos, burritos, quesadillas and traditional Mexican favorites in Blanchester, Ohio."
    >

    <title>Taco San Juan | Blanchester, Ohio</title>

    <style>
        :root {
            --orange: #f36b21;
            --dark-orange: #c94a0b;
            --cream: #fff8ef;
            --white: #ffffff;
            --dark: #23170f;
            --muted: #715e50;
            --green: #257a48;
            --shadow: 0 14px 36px rgba(70, 36, 13, 0.14);
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
            font-family: Arial, Helvetica, sans-serif;
            color: var(--dark);
            background: var(--cream);
            line-height: 1.6;
        }

        a {
            text-decoration: none;
        }

        .container {
            width: min(1120px, 92%);
            margin: auto;
        }

        nav {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.97);
            border-bottom: 1px solid rgba(243, 107, 33, 0.18);
            box-shadow: 0 4px 18px rgba(40, 20, 8, 0.06);
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
            font-size: 1.65rem;
            font-weight: 800;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 25px;
        }

        .nav-links a {
            color: var(--dark);
            font-weight: 700;
        }

        .nav-links a:hover {
            color: var(--orange);
        }

        .call-button,
        .primary-button {
            display: inline-block;
            padding: 13px 22px;
            border-radius: 999px;
            background: var(--orange);
            color: white !important;
            font-weight: 800;
            transition: 0.2s ease;
            box-shadow: 0 8px 20px rgba(243, 107, 33, 0.25);
        }

        .call-button:hover,
        .primary-button:hover {
            background: var(--dark-orange);
            transform: translateY(-2px);
        }

        .secondary-button {
            display: inline-block;
            padding: 12px 21px;
            border: 2px solid white;
            border-radius: 999px;
            color: white;
            font-weight: 800;
            transition: 0.2s ease;
        }

        .secondary-button:hover {
            background: white;
            color: var(--orange);
        }

        .hero {
            min-height: 650px;
            display: grid;
            place-items: center;
            text-align: center;
            color: white;
            background:
                linear-gradient(rgba(25, 12, 5, 0.58), rgba(25, 12, 5, 0.67)),
                url("https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=1800&q=85")
                center/cover no-repeat;
        }

        .hero-content {
            max-width: 830px;
            padding: 80px 0;
        }

        .eyebrow {
            display: inline-block;
            margin-bottom: 18px;
            padding: 8px 15px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.16);
            border: 1px solid rgba(255, 255, 255, 0.35);
            font-size: 0.82rem;
            font-weight: 800;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }

        h1 {
            font-family: Georgia, serif;
            font-size: clamp(3rem, 8vw, 6.5rem);
            line-height: 0.98;
            margin-bottom: 20px;
        }

        .hero p {
            max-width: 690px;
            margin: 0 auto 30px;
            font-size: clamp(1rem, 2vw, 1.25rem);
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
            max-width: 680px;
            margin: 0 auto 44px;
            text-align: center;
        }

        .section-heading span {
            color: var(--orange);
            font-weight: 900;
            letter-spacing: 1.3px;
            text-transform: uppercase;
            font-size: 0.82rem;
        }

        .section-heading h2 {
            margin: 8px 0 12px;
            font-family: Georgia, serif;
            font-size: clamp(2.2rem, 5vw, 3.6rem);
            line-height: 1.05;
        }

        .section-heading p {
            color: var(--muted);
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
        }

        .menu-card {
            position: relative;
            padding: 28px;
            background: white;
            border: 1px solid rgba(243, 107, 33, 0.15);
            border-radius: 22px;
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
            width: 56px;
            height: 56px;
            margin-bottom: 18px;
            border-radius: 16px;
            background: #fff0e4;
            font-size: 1.8rem;
        }

        .menu-card h3 {
            font-family: Georgia, serif;
            font-size: 1.45rem;
            margin-bottom: 8px;
        }

        .menu-card p {
            color: var(--muted);
            padding-right: 35px;
        }

        .price {
            display: inline-block;
            margin-top: 18px;
            color: var(--orange);
            font-size: 1.15rem;
            font-weight: 900;
        }

        .about {
            background: white;
        }

        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 55px;
            align-items: center;
        }

        .about-photo {
            min-height: 480px;
            border-radius: 28px;
            background:
                linear-gradient(rgba(243, 107, 33, 0.08), rgba(243, 107, 33, 0.08)),
                url("https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=1200&q=85")
                center/cover no-repeat;
            box-shadow: var(--shadow);
        }

        .about-copy h2 {
            margin-bottom: 20px;
            font-family: Georgia, serif;
            font-size: clamp(2.2rem, 5vw, 3.6rem);
            line-height: 1.08;
        }

        .about-copy p {
            margin-bottom: 17px;
            color: var(--muted);
        }

        .features {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 13px;
            margin-top: 28px;
        }

        .feature {
            padding: 17px 12px;
            border-radius: 14px;
            background: var(--cream);
            text-align: center;
            font-weight: 800;
        }

        .visit {
            background: var(--orange);
            color: white;
        }

        .visit-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
        }

        .visit h2 {
            margin-bottom: 15px;
            font-family: Georgia, serif;
            font-size: clamp(2.2rem, 5vw, 3.5rem);
        }

        .visit-copy p {
            margin-bottom: 13px;
            font-size: 1.06rem;
        }

        .details-box {
            padding: 28px;
            border-radius: 22px;
            background: white;
            color: var(--dark);
            box-shadow: var(--shadow);
        }

        .details-box h3 {
            margin-bottom: 16px;
            font-family: Georgia, serif;
            font-size: 1.6rem;
        }

        .hours-row {
            display: flex;
            justify-content: space-between;
            gap: 15px;
            padding: 9px 0;
            border-bottom: 1px solid #eee2d8;
        }

        footer {
            padding: 32px 0;
            color: #d9c9bd;
            background: #21150f;
            text-align: center;
        }

        footer strong {
            color: white;
        }

        @media (max-width: 850px) {
            .nav-links a:not(.call-button) {
                display: none;
            }

            .menu-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .about-grid,
            .visit-grid {
                grid-template-columns: 1fr;
            }

            .about-photo {
                min-height: 380px;
            }
        }

        @media (max-width: 560px) {
            .logo {
                font-size: 1.3rem;
            }

            .call-button {
                padding: 10px 15px;
                font-size: 0.9rem;
            }

            .hero {
                min-height: 590px;
            }

            section {
                padding: 68px 0;
            }

            .menu-grid,
            .features {
                grid-template-columns: 1fr;
            }

            .menu-card {
                padding: 24px;
            }

            .hours-row {
                font-size: 0.91rem;
            }
        }
    </style>
</head>

<body>
    <nav>
        <div class="container nav-content">
            <a class="logo" href="#home">Taco San Juan</a>

            <div class="nav-links">
                <a href="#menu">Menu</a>
                <a href="#about">Our Story</a>
                <a href="#visit">Visit Us</a>
                <a class="call-button" href="tel:8888888888">Call to Order</a>
            </div>
        </div>
    </nav>

    <main>
        <section class="hero" id="home">
            <div class="container hero-content">
                <div class="eyebrow">Fresh Mexican Food • Blanchester, Ohio</div>

                <h1>Bold flavor.<br>Made fresh.</h1>

                <p>
                    Fresh tacos, loaded burritos, cheesy quesadillas and
                    traditional Mexican favorites prepared with care.
                </p>

                <div class="hero-buttons">
                    <a class="primary-button" href="#menu">Explore Our Menu</a>
                    <a class="secondary-button" href="tel:8888888888">
                        Call 888-888-8888
                    </a>
                </div>
            </div>
        </section>

        <section id="menu">
            <div class="container">
                <div class="section-heading">
                    <span>Our Favorites</span>
                    <h2>Made to satisfy</h2>
                    <p>
                        Choose steak, chicken, or pork and enjoy the fresh,
                        comforting flavors of Taco San Juan.
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
                <div class="about-photo" aria-label="Fresh tacos"></div>

                <div class="about-copy">
                    <div class="eyebrow" style="color:#f36b21; background:#fff0e4;">
                        Our Story
                    </div>

                    <h2>Local food with unforgettable flavor</h2>

                    <p>
                        Taco San Juan is a local Blanchester taco shop focused
                        on serving fresh Mexican favorites in a welcoming,
                        family-friendly atmosphere.
                    </p>

                    <p>
                        Whether you choose steak, chicken, or pork, every meal
                        is prepared to order and served with the bold flavors
                        you love.
                    </p>

                    <div class="features">
                        <div class="feature">🌮 Made Fresh</div>
                        <div class="feature">🥩 Quality Meat</div>
                        <div class="feature">📍 Local Shop</div>
                    </div>
                </div>
            </div>
        </section>

        <section class="visit" id="visit">
            <div class="container visit-grid">
                <div class="visit-copy">
                    <h2>Come visit us</h2>

                    <p>
                        <strong>Location:</strong><br>
                        Blanchester, Ohio
                    </p>

                    <p>
                        <strong>Phone:</strong><br>
                        <a href="tel:8888888888" style="color:white;">
                            888-888-8888
                        </a>
                    </p>

                    <p>
                        Dine in, pick up your order, or call ahead and we’ll
                        have your food ready.
                    </p>

                    <br>

                    <a class="secondary-button" href="tel:8888888888">
                        Call to Order
                    </a>
                </div>

                <div class="details-box">
                    <h3>Hours</h3>

                    {% for day, time in hours %}
                        <div class="hours-row">
                            <strong>{{ day }}</strong>
                            <span>{{ time }}</span>
                        </div>
                    {% endfor %}
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>
                <strong>Taco San Juan</strong> • Blanchester, Ohio •
                888-888-8888
            </p>
            <p>Fresh food. Local flavor. Made for you.</p>
        </div>
    </footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE, menu=MENU, hours=HOURS)


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
