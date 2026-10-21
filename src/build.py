#!/usr/bin/env python3
"""
Agri Master Cambodia - Static Site Generator
Generates the complete website from templates and content definitions.
Output: ../docs/ (for GitHub Pages)
"""
import os
from pathlib import Path

# Configuration
OUTPUT_DIR = Path(__file__).parent.parent / "docs"
TEMPLATES_DIR = Path(__file__).parent / "templates"

# Navigation
NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("products.html", "Products"),
    ("contact.html", "Contact")
]

# Product data
PRODUCTS = [
    ("swine", "Swine", "swine.jpg", 
     "Feed for all production stages — from piglet starter to finishing pig, gestation and sows.",
     ["Piglet starter", "Grower &amp; finishing pig", "Gestation", "Sows"]),
    ("poultry", "Poultry", "poultry.jpg",
     "Feed for native, layers and broilers — from chick starter to grower and finisher.",
     ["Native chicken", "Layers", "Broilers", "Chick starter → grower → finisher"]),
    ("ruminant", "Ruminant", "ruminant.jpg",
     "Feed for cattle, goats and others — from young stock to adult and fattening.",
     ["Cattle", "Goats", "Young stock → adult", "Fattening"]),
    ("aquaculture", "Aquaculture", "aquaculture.jpg",
     "Feed for freshwater fish — from fingerlings through every growth stage to harvest.",
     ["Freshwater fish", "Fingerlings", "Every growth stage", "Floating fish feed"])
]

# Brand data
BRANDS = [
    ("Master Feed", "b1"), ("Super Feed", "b2"), ("Golden Feed", "b3"),
    ("Echo Feed", "b4"), ("Vital Feed", "b5"), ("Diamond Feed", "b6")
]

# Timeline HTML
TIMELINE = '''<ol class="timeline">
<li><b>2004</b><p>Cambodia's first locally owned and operated animal feed producers.</p></li>
<li><b>2013</b><p>Opened a modern feed mill in Kandal Province near Phnom Penh.</p></li>
<li><b>2020</b><p>Cambodia's first aquafeed plant, with a capacity of 1,500 tons/month.</p></li>
<li><b>2023–2026</b><p>Expanding and modernising the facility, including new silos with 10,000 tons of storage capacity.</p></li>
</ol>'''

def load_template(name):
    """Load a template file"""
    return (TEMPLATES_DIR / name).read_text()

def render_nav(current_page):
    """Render navigation links with current page highlighted"""
    links = []
    for href, title in NAV:
        aria = ' aria-current="page"' if href == current_page else ''
        links.append(f'<li><a href="{href}"{aria}>{title}</a></li>')
    return ''.join(links)

def render_page(filename, title, description, content):
    """Render a complete page with header, footer, and content"""
    page_class = filename[:-5]  # Remove .html extension
    
    # Load templates
    base = load_template("base.html")
    header = load_template("header.html")
    footer = load_template("footer.html")
    
    # Render navigation
    nav_links = render_nav(filename)
    header = header.replace("{{nav_links}}", nav_links)
    
    # Replace placeholders in base template
    html = base.replace("{{title}}", title)
    html = html.replace("{{description}}", description)
    html = html.replace("{{page_class}}", page_class)
    html = html.replace("{{header}}", header)
    html = html.replace("{{content}}", content)
    html = html.replace("{{footer}}", footer)
    
    return html

def page_hero(eyebrow, title, lead, img):
    """Generate a page hero section"""
    return f'''<section class="page-hero wrap"><div class="ph-inner" style="background-image:url(assets/img/{img})"><div class="ph-text"><p class="eyebrow light">{eyebrow}</p><h1>{title}</h1><p>{lead}</p></div></div></section>'''

def cta(title="Looking for a <span class=\"accent\">reliable feed partner?</span>",
        text="Talk to our team about the right feed line for your farm or distribution business."):
    """Generate a call-to-action section"""
    return f'<section class="wrap"><div class="cta"><h2>{title}</h2><p>{text}</p><a class="btn btn-light" href="contact.html">Contact us</a></div></section>'

def product_cards():
    """Generate product cards for homepage"""
    cards = []
    for pid, name, img, desc, _ in PRODUCTS:
        cards.append(
            f'<article class="card"><a href="products.html#{pid}"><img src="assets/img/{img}" '
            f'alt="{name} feed" loading="lazy" width="1000" height="646"><h3>{name}</h3></a>'
            f'<p>{desc}</p></article>'
        )
    return ''.join(cards)

def brand_grid():
    """Generate brand grid"""
    items = [f'<li class="{cls}">{name}</li>' for name, cls in BRANDS]
    return '<ul class="brands">' + ''.join(items) + '</ul>'

def build_home():
    """Build homepage content"""
    return f'''
<section class="hero wrap"><div class="hero-img">
  <div class="hero-content">
    <p class="eyebrow light">Agri Master Cambodia · Animal Nutrition</p>
    <h1>Feeding Cambodia's farms <span class="accent-l">since 2004</span></h1>
    <div class="hero-row">
      <div class="stats"><div class="stat"><b>30,000</b><small>Tons / month capacity</small></div><div class="stat dark"><b>360,000</b><small>Tons / year capacity</small></div></div>
      <p class="hero-copy">One of Cambodia's first locally owned feedmills, producing complete swine, poultry, ruminant and aquaculture feed.</p>
      <a class="btn btn-light" href="products.html">Explore our feeds →</a>
    </div></div></div></section>
<section class="section center wrap">
  <p class="eyebrow">About Agri Master</p>
  <h2>Cambodian-owned <span class="accent">animal nutrition</span><br>built for local farmers</h2>
  <p class="lead">Established in 2004 as part of Medivet Cambodia, Agri Master serves all major segments of Cambodia's animal feed sector — and was the first Cambodian company to commercially produce floating fish feed.</p>
  <a class="btn btn-outline" href="about.html">Our story</a>
</section>
<section class="wrap section pt0">
  <div class="sec-head row"><div><p class="eyebrow">Our products</p><h2>Complete feed in <span class="accent">pellet &amp; mash</span></h2></div><a class="link" href="products.html">All products →</a></div>
  <div class="grid4">{product_cards()}</div>
</section>
<section class="wrap"><div class="band" style="background-image:url(assets/img/feedmill-aerial.jpg)">
  <div class="band-text"><p class="eyebrow light">Production capacity</p><h2>Scalable infrastructure in Kandal Province</h2></div>
  <div class="band-stats"><div class="stat"><b>1,500</b><small>Tons / month aquafeed plant</small></div><div class="stat dark"><b>10,000</b><small>Tons new silo storage</small></div><div class="stat"><b>4</b><small>Feed categories</small></div></div>
</div></section>
<section class="section center wrap mission"><p>We prioritise <span class="hl">local raw materials — corn, cassava and rice by-products</span> — combined with quality imports, and <span class="hl">test every batch</span> in-house for nutritional value, safety and consistency.</p></section>
<section class="wrap section pt0"><div class="sec-head"><p class="eyebrow">Milestones</p><h2>Two decades of <span class="accent">growth</span></h2></div>{TIMELINE}</section>
<section class="wrap section pt0"><div class="sec-head row"><div><p class="eyebrow">Our brands</p><h2>Tailored to <span class="accent">every region</span></h2></div><a class="link" href="products.html#brands">View brands →</a></div>{brand_grid()}</section>
<section class="wrap section pt0"><div class="sec-head"><p class="eyebrow">Why Agri Master</p><h2>Why farmers <span class="accent">choose us</span></h2></div>
<div class="grid4 why">
<div><span class="dot d1"></span><h3>Locally owned</h3><p>Among Cambodia's first locally owned feedmills, serving the domestic market since 2004.</p></div>
<div><span class="dot d2"></span><h3>Aquafeed pioneers</h3><p>First Cambodian company to commercially produce floating fish feed.</p></div>
<div><span class="dot d3"></span><h3>Quality at every stage</h3><p>Raw material inspection, production monitoring, lab analysis and finished product checks.</p></div>
<div><span class="dot d4"></span><h3>Scalable capacity</h3><p>30,000 tons per month at full operation, with room to grow with demand.</p></div></div></section>
{cta()}'''

def build_about():
    """Build about page content"""
    hero = page_hero("About us", "Our story", 
                     "Agri Master was established in 2004 as part of Medivet Cambodia, as one of Cambodia's first locally owned feedmills.",
                     "feedmill.jpg")
    
    quality_section = '''
<section id="quality" class="wrap section pt0"><div class="sec-head"><p class="eyebrow">Quality &amp; capacity</p><h2>Built for <span class="accent">quality and scale</span></h2>
<p class="muted">Quality control is integrated into every stage of our production process to support animal health, growth performance, farm productivity and food safety.</p></div>
<div class="bigstats"><div><b>30,000</b><span>tons per month at 100% full operation</span></div><div><b>360,000</b><span>tons annual production capacity</span></div><div><b>1,500</b><span>tons/month aquafeed plant (2020)</span></div><div><b>10,000</b><span>tons storage in new silos (2023–2026)</span></div></div>
<div class="grid4 why mt2">
<div><span class="dot d1"></span><h3>Raw material inspection</h3><p>Raw materials are inspected and tested before they are accepted and stored.</p></div>
<div><span class="dot d2"></span><h3>Production monitoring</h3><p>Modern PLC and SCADA technology monitors and controls manufacturing.</p></div>
<div><span class="dot d3"></span><h3>Laboratory analysis</h3><p>Moisture, crude protein, crude fat, crude fibre and ash analysed before packing.</p></div>
<div><span class="dot d4"></span><h3>Finished product checks</h3><p>Physical quality and particle size inspected against established standards.</p></div></div>
<div class="split mt2"><img class="rimg short" src="assets/img/raw-materials-corn.jpg" alt="Corn being unloaded for feed production" loading="lazy">
<div><h3 class="h3l">Raw materials: local first</h3><p class="muted">We prioritise local corn, cassava and rice by-products where available, in line with our agreement with the Ministry of Commerce.</p>
<div class="mats"><div><h3>Local</h3><ul class="ticks"><li>Corn</li><li>Cassava</li><li>Broken rice</li><li>Rice bran</li></ul></div>
<div><h3>Imported</h3><ul class="ticks"><li>Soybean (100% USA)</li><li>Soybean meal (USA/S. America)</li><li>Meat and bone meal</li><li>Blood meal</li><li>Palm kernel meal</li><li>DDGS (100% USA)</li><li>Sunflower meal (100% USA)</li></ul></div></div></div></div>
</section>'''
    
    return hero + f'''
<section class="wrap section split">
  <div><p class="eyebrow">Who we are</p><h2>Proudly <span class="accent">Cambodian</span></h2>
  <p class="lead l">We were established to serve the growing domestic feed market. Today Agri Master produces a full range of animal feed — swine, poultry, ruminant and aquaculture — and we were the first Cambodian company to commercially produce floating fish feed.</p>
  <p class="muted">Since our founding, Agri Master has steadily grown to serve all major segments of Cambodia's animal feed sector.</p></div>
  <img class="rimg" src="assets/img/feedmill-aerial.jpg" alt="Aerial view of the Agri Master feed mill in Kandal Province" loading="lazy">
</section>
<section class="wrap section pt0"><div class="sec-head"><p class="eyebrow">Milestones</p><h2>Two decades of <span class="accent">growth</span></h2></div>{TIMELINE}</section>
<section class="wrap section pt0"><div class="sec-head"><p class="eyebrow">Mission &amp; values</p><h2>What <span class="accent">guides us</span></h2>
<p class="muted">Values summarised from our company profile. <span class="todo">Formal mission statement to be provided.</span></p></div>
<div class="grid4 why">
<div><span class="dot d1"></span><h3>Serve local farmers</h3><p>Brand lines tailored to the needs of farmers in different regional markets across Cambodia.</p></div>
<div><span class="dot d2"></span><h3>Support local sourcing</h3><p>Prioritising local corn, cassava and rice by-products, in line with our agreement with the Ministry of Commerce.</p></div>
<div><span class="dot d3"></span><h3>Quality &amp; safety</h3><p>Quality control integrated into every stage to support animal health, growth performance, farm productivity and food safety.</p></div>
<div><span class="dot d4"></span><h3>Grow with Cambodia</h3><p>Continuing to expand and modernise to meet growing demand.</p></div></div></section>
{quality_section}
{cta()}'''

def build_products():
    """Build products page content"""
    hero = page_hero("Our products", "Complete feed for every stage",
                     "Agri Master Cambodia produces complete feed in both pellet and mash form for a wide range of livestock and aquaculture.",
                     "poultry.jpg")
    
    product_sections = []
    for k, (pid, name, img, desc, features) in enumerate(PRODUCTS):
        rev = ' rev' if k % 2 else ''
        feature_items = ''.join(f'<li>{x}</li>' for x in features)
        product_sections.append(
            f'''<article id="{pid}" class="prod{rev}"><img src="assets/img/{img}" alt="{name} – Agri Master feed" loading="lazy"><div><p class="eyebrow">Feed line 0{k+1}</p><h2>{name} <span class="accent">feed</span></h2><p class="lead l">{desc}</p><ul class="ticks">{feature_items}</ul><p class="muted small">Available as complete feed in pellet and mash form across all six Agri Master brands.</p></div></article>'''
        )
    
    return hero + f'''
<section class="wrap section">{''.join(product_sections)}</section>
<section id="brands" class="wrap section pt0"><div class="sec-head center"><p class="eyebrow">Agri Master brands</p><h2>A portfolio of <span class="accent">high-quality</span> feed brands</h2>
<p class="lead">Each brand line is tailored to the specific needs of farmers in different regional markets across Cambodia. All brands offer complete feed lines for swine, poultry, ruminants and aquaculture.</p></div>{brand_grid()}
<p class="muted small center mt">Brand logos / packaging shots: <span class="todo">to be provided</span></p></section>
{cta("Need help choosing a <span class=\"accent\">feed line?</span>", "Our team can recommend the right brand and formulation for your animals and region.")}'''

def build_contact():
    """Build contact page content"""
    hero = page_hero("Contact", "Let's talk feed",
                     "Get in touch with our team about products, brands and distribution across Cambodia.",
                     "feedmill.jpg")
    
    return hero + '''
<section class="wrap section split top">
<form class="form" onsubmit="event.preventDefault();this.querySelector('.ok').hidden=false">
 <h2>Send us a <span class="accent">message</span></h2>
 <div class="frow"><label>Full name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" autocomplete="tel"></label></div>
 <div class="frow"><label>Email<input name="email" type="email" required autocomplete="email"></label>
 <label>I'm interested in<select name="topic"><option>Swine feed</option><option>Poultry feed</option><option>Ruminant feed</option><option>Aquaculture feed</option><option>Becoming a distributor</option><option>Other</option></select></label></div>
 <label>Message<textarea name="msg" rows="5" required></textarea></label>
 <button class="btn btn-primary" type="submit">Send message</button>
 <p class="ok muted" hidden role="status">Thank you — this is a demo form (not yet connected).</p>
</form>
<aside class="cinfo"><h2>Contact <span class="accent">details</span></h2>
<dl><dt>Feed mill</dt><dd>Kandal Province, near Phnom Penh, Cambodia<br><span class="todo">Full street address to be provided</span></dd>
<dt>Phone</dt><dd><span class="todo">To be provided</span></dd><dt>Email</dt><dd><span class="todo">To be provided</span></dd>
<dt>Website</dt><dd><a href="https://agrimaster.com.kh">agrimaster.com.kh</a></dd><dt>Opening hours</dt><dd><span class="todo">To be provided</span></dd></dl></aside>
</section>
<section class="wrap section pt0"><div class="map"><iframe title="Map of Kandal Province, Cambodia" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=104.70%2C11.30%2C105.20%2C11.70&amp;layer=mapnik"></iframe><p class="muted small"><a href="https://www.openstreetmap.org/#map=11/11.48/104.95">Open larger map</a> · Map shows Kandal Province. <span class="todo">Exact mill location pin to be provided.</span></p></div></section>'''

def main():
    """Generate all pages"""
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Pages to generate
    pages = [
        ("index.html", "Animal Nutrition",
         "Agri Master Cambodia – locally owned feedmill producing swine, poultry, ruminant and aquaculture feed since 2004.",
         build_home()),
        ("about.html", "About",
         "Our story, milestones, values, quality control and capacity.",
         build_about()),
        ("products.html", "Products",
         "Swine, poultry, ruminant and aquaculture feed and our six brands.",
         build_products()),
        ("contact.html", "Contact",
         "Contact Agri Master Cambodia.",
         build_contact())
    ]
    
    # Generate each page
    for filename, title, description, content in pages:
        html = render_page(filename, title, description, content)
        output_path = OUTPUT_DIR / filename
        output_path.write_text(html)
        print(f"Generated {filename}")
    
    print(f"\n✓ Build complete. Output in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
