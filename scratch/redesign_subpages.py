import os

# Common header generator function
def get_header(active_page):
    return f"""<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">
      <span class="logo-mark">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11L12 3l9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/></svg>
      </span>
      Anshu <span>Property</span>
    </a>

    <nav>
      <ul class="nav-desktop">
        <li><a href="index.html" class="nav-link {'active' if active_page == 'home' else ''}">Home</a></li>
        <li><a href="properties.html" class="nav-link {'active' if active_page == 'properties' else ''}">Properties</a></li>
        <li><a href="vda-approved.html" class="nav-link {'active' if active_page == 'vda' else ''}">VDA Approved</a></li>
        <li><a href="services.html" class="nav-link {'active' if active_page == 'services' else ''}">Services</a></li>
        <li><a href="about.html" class="nav-link {'active' if active_page == 'about' else ''}">About Us</a></li>
        <li><a href="blog.html" class="nav-link {'active' if active_page == 'blog' else ''}">Blog</a></li>
        <li><a href="contact.html" class="nav-link {'active' if active_page == 'contact' else ''}">Contact</a></li>
      </ul>
    </nav>

    <div class="header-cta">
      <a href="https://wa.me/918303727724" target="_blank" class="btn btn-primary btn-sm" style="display:inline-flex;align-items:center;gap:6px;padding:8px 16px;font-size:0.88rem;">
        <i class="fa-brands fa-whatsapp" style="color:#25D366;font-size:1rem;"></i>
        WhatsApp
      </a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
  </div>

  <div class="nav-mobile">
    <a href="index.html">Home</a>
    <a href="properties.html">Properties</a>
    <a href="vda-approved.html">VDA Approved</a>
    <a href="services.html">Services</a>
    <a href="about.html">About Us</a>
    <a href="blog.html">Blog</a>
    <a href="contact.html">Contact</a>
  </div>
</header>"""

# Common footer template
FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">
          <span class="logo-mark"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11L12 3l9 8"/><path d="M5 10v10h14V10"/></svg></span>
          Anshu Property
        </div>
        <p>Varanasi's premier real estate consultancy founded by Anshu Dubey (@anshupropertyvns). Specializing in VDA Approved &amp; UP RERA Registered plots in Varanasi, Allahabad, Bihar &amp; MP.</p>
        <div class="footer-socials" style="display:flex;gap:12px;margin-top:16px;">
          <a href="https://wa.me/918303727724" target="_blank" style="color:var(--gold);font-size:1.2rem;" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
          <a href="https://www.instagram.com/anshupropertyvns/" target="_blank" style="color:var(--gold);font-size:1.2rem;" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
        </div>
      </div>
      <div>
        <h5>Quick Links</h5>
        <a href="index.html">Home</a>
        <a href="properties.html">Properties</a>
        <a href="vda-approved.html">VDA Approved</a>
        <a href="services.html">Services</a>
        <a href="about.html">About Us</a>
        <a href="blog.html">Blog</a>
        <a href="contact.html">Contact</a>
      </div>
      <div>
        <h5>Service Areas</h5>
        <a href="properties.html">Varanasi (Ring Road, Shivpur)</a>
        <a href="properties.html">Allahabad / Prayagraj</a>
        <a href="properties.html">Bihar Highway Frontage</a>
        <a href="properties.html">Madhya Pradesh (MP)</a>
      </div>
      <div>
        <h5>Contact Us</h5>
        <a href="tel:+918303727724"><i class="fa-solid fa-phone" style="color:var(--gold);margin-right:6px;"></i> +91 83037 27724</a>
        <a href="https://wa.me/918303727724" target="_blank"><i class="fa-brands fa-whatsapp" style="color:#25D366;margin-right:6px;"></i> WhatsApp Support</a>
        <a href="mailto:anshudubey3409@gmail.com"><i class="fa-solid fa-envelope" style="color:var(--gold);margin-right:6px;"></i> anshudubey3409@gmail.com</a>
        <p style="margin-top:10px;font-size:0.85rem;color:#94A3B8;"><i class="fa-solid fa-location-dot" style="color:var(--gold);margin-right:6px;"></i> Head Office: Varanasi, Uttar Pradesh</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Anshu Property (@anshupropertyvns). All rights reserved.</span>
      <span>Owned &amp; operated by Anshu Dubey</span>
    </div>
  </div>
</footer>"""

# CTA Band template
CTA_BAND = """<section class="section section-maroon" style="background: linear-gradient(135deg, #7A2E2E 0%, #5E2121 100%); color:#FFFFFF; padding: 70px 0; text-align:center;">
  <div class="container" style="max-width: 800px;">
    <h2 style="font-family: var(--font-serif); font-size: clamp(28px, 3.5vw, 42px); color:#FFFFFF; margin-bottom: 16px;">
      Book Your Free Site Visit Today!
    </h2>
    <p style="font-size: 1.1rem; color: #F3E8E8; margin-bottom: 32px;">
      Explore prime residential & commercial plots in Varanasi and nearby growth hubs with direct owner assistance.
    </p>
    <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
      <a href="https://wa.me/918303727724?text=Hello%20Anshu%20ji,%20I%20want%20to%20book%20a%20free%20site%20visit." target="_blank" class="btn btn-gold" style="padding:15px 32px; font-size:1.05rem;">
        <i class="fa-brands fa-whatsapp" style="font-size:1.3rem;"></i> Book Site Visit on WhatsApp
      </a>
      <a href="tel:+918303727724" class="btn btn-primary" style="padding:15px 32px; font-size:1.05rem; background:#1B2A41; color:#FFFFFF; border:1px solid var(--gold);">
        <i class="fa-solid fa-phone"></i> Call +91 83037 27724
      </a>
    </div>
  </div>
</section>"""

base_dir = r'd:\ansu\website'

# 1. Redesign PROPERTIES.HTML
properties_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Properties & Video Walkthroughs | Anshu Property Varanasi</title>
<meta name="description" content="Explore VDA approved plots in Varanasi, luxury villas in Allahabad, and highway commercial spaces in Bihar & MP with video walkthroughs.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css?v=3.0">
<link rel="stylesheet" href="css/ragini-assistant.css">
</head>
<body style="background-color:#F9F6F0;">

{get_header('properties')}

<!-- Deep Navy Hero Banner -->
<section class="page-hero" style="background: linear-gradient(135deg, #121C2B 0%, #1B2A41 100%); color:#FFFFFF; padding: 75px 0 85px;">
  <div class="container" style="text-align:center;">
    <div class="seal-badge" style="margin-bottom:14px;">
      <span class="seal-icon">✓</span> Verified Property Listings
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(32px, 3.8vw, 50px); color:#FFFFFF; margin-top:8px;">Verified Properties &amp; Video Walkthroughs</h1>
    <p style="color:#D1D5DB; max-width:640px; margin: 12px auto 0; font-size:1.1rem;">
      Browse our curated portfolio of VDA approved residential plots, independent villas, and commercial land in Varanasi, Allahabad, Bihar &amp; MP.
    </p>
  </div>
</section>

<!-- Main Properties Showcase Section (Warm Ivory & White Cards) -->
<section class="section" style="padding: 80px 0;">
  <div class="container">
    
    <!-- Filter Bar Card -->
    <div class="search-box reveal" style="background:#FFFFFF; padding:24px 30px; border-radius:20px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); border:1px solid rgba(200,155,60,0.25); margin-bottom:48px;">
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:20px; align-items:end;">
        <div class="field">
          <label style="font-weight:700; font-size:0.85rem; color:#1B2A41; text-transform:uppercase; margin-bottom:6px; display:block;">Location</label>
          <select style="width:100%; padding:12px 16px; border-radius:12px; border:1px solid #CBD5E0; outline:none; background:#F9F6F0;"><option>All Locations</option><option>Varanasi (Shivpur / Ring Road)</option><option>Allahabad (Prayagraj)</option><option>Bihar Highway</option><option>Madhya Pradesh (MP)</option></select>
        </div>
        <div class="field">
          <label style="font-weight:700; font-size:0.85rem; color:#1B2A41; text-transform:uppercase; margin-bottom:6px; display:block;">Property Type</label>
          <select style="width:100%; padding:12px 16px; border-radius:12px; border:1px solid #CBD5E0; outline:none; background:#F9F6F0;"><option>All Types</option><option>VDA Approved Residential Plot</option><option>UP RERA Registered Plot</option><option>Commercial Land</option></select>
        </div>
        <div class="field">
          <label style="font-weight:700; font-size:0.85rem; color:#1B2A41; text-transform:uppercase; margin-bottom:6px; display:block;">Budget Range</label>
          <select style="width:100%; padding:12px 16px; border-radius:12px; border:1px solid #CBD5E0; outline:none; background:#F9F6F0;"><option>Any Budget</option><option>Under ₹25 Lakhs</option><option>₹25L – ₹50 Lakhs</option><option>₹50L – ₹1 Crore+</option></select>
        </div>
        <button class="btn btn-gold" style="height:48px; border-radius:12px; width:100%;">
          <i class="fa-solid fa-filter"></i> Filter Properties
        </button>
      </div>
    </div>

    <!-- Properties Grid -->
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:32px;">
      
      <!-- Card 1 -->
      <div style="background:#FFFFFF; border-radius:20px; overflow:hidden; box-shadow: 0 12px 35px rgba(0,0,0,0.08); border:1px solid rgba(0,0,0,0.06); transition: transform 0.3s ease;" class="why-card">
        <div style="position:relative; aspect-ratio:4/3; overflow:hidden;">
          <span style="position:absolute; top:16px; left:16px; background:#1B2A41; color:#C89B3C; padding:6px 14px; border-radius:50px; font-weight:700; font-size:0.8rem; z-index:2; border:1px solid #C89B3C;">
            VDA Approved
          </span>
          <img src="assets/plot_varanasi.jpg" alt="VDA Approved Plot in Varanasi" style="width:100%; height:100%; object-fit:cover;">
        </div>
        <div style="padding:24px;">
          <div style="font-size:1.3rem; font-weight:800; color:#1B2A41; margin-bottom:6px;">₹35 Lakhs <span style="font-size:0.85rem; font-weight:600; color:#C89B3C;">| Clear Title</span></div>
          <h3 style="font-size:1.15rem; color:#1B2A41; margin-bottom:10px;">VDA Approved Plot in Shivpur, Varanasi</h3>
          <p style="font-size:0.9rem; color:#555; margin-bottom:16px; line-height:1.5;">
            Prime plot near Varanasi Ring Road Phase 2 with 30ft metalled road, electricity lines, and immediate bank loan support.
          </p>
          <div style="display:flex; gap:12px;">
            <a href="https://wa.me/918303727724?text=I%20am%20interested%20in%20VDA%20Plot%20Shivpur" target="_blank" class="btn btn-whatsapp" style="flex:1; padding:10px; font-size:0.88rem;">
              <i class="fa-brands fa-whatsapp"></i> Inquire Plot
            </a>
            <a href="tel:+918303727724" class="btn btn-gold" style="padding:10px 16px; font-size:0.88rem;">
              <i class="fa-solid fa-phone"></i>
            </a>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div style="background:#FFFFFF; border-radius:20px; overflow:hidden; box-shadow: 0 12px 35px rgba(0,0,0,0.08); border:1px solid rgba(0,0,0,0.06); transition: transform 0.3s ease;" class="why-card">
        <div style="position:relative; aspect-ratio:4/3; overflow:hidden;">
          <span style="position:absolute; top:16px; left:16px; background:#1B2A41; color:#C89B3C; padding:6px 14px; border-radius:50px; font-weight:700; font-size:0.8rem; z-index:2; border:1px solid #C89B3C;">
            RERA Registered
          </span>
          <img src="assets/villa_allahabad.jpg" alt="Luxury Villa in Allahabad" style="width:100%; height:100%; object-fit:cover;">
        </div>
        <div style="padding:24px;">
          <div style="font-size:1.3rem; font-weight:800; color:#1B2A41; margin-bottom:6px;">₹1.45 Crore <span style="font-size:0.85rem; font-weight:600; color:#C89B3C;">| 4BHK Villa</span></div>
          <h3 style="font-size:1.15rem; color:#1B2A41; margin-bottom:10px;">Luxury Independent Villa in Civil Lines, Allahabad</h3>
          <p style="font-size:0.9rem; color:#555; margin-bottom:16px; line-height:1.5;">
            Modern duplex villa with private parking, modular kitchen, terrace garden, and RERA approval in Prayagraj.
          </p>
          <div style="display:flex; gap:12px;">
            <a href="https://wa.me/918303727724?text=I%20am%20interested%20in%20Villa%20Allahabad" target="_blank" class="btn btn-whatsapp" style="flex:1; padding:10px; font-size:0.88rem;">
              <i class="fa-brands fa-whatsapp"></i> Inquire Villa
            </a>
            <a href="tel:+918303727724" class="btn btn-gold" style="padding:10px 16px; font-size:0.88rem;">
              <i class="fa-solid fa-phone"></i>
            </a>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div style="background:#FFFFFF; border-radius:20px; overflow:hidden; box-shadow: 0 12px 35px rgba(0,0,0,0.08); border:1px solid rgba(0,0,0,0.06); transition: transform 0.3s ease;" class="why-card">
        <div style="position:relative; aspect-ratio:4/3; overflow:hidden;">
          <span style="position:absolute; top:16px; left:16px; background:#1B2A41; color:#C89B3C; padding:6px 14px; border-radius:50px; font-weight:700; font-size:0.8rem; z-index:2; border:1px solid #C89B3C;">
            Highway Commercial
          </span>
          <img src="assets/commercial_bihar.jpg" alt="Highway Commercial Land" style="width:100%; height:100%; object-fit:cover;">
        </div>
        <div style="padding:24px;">
          <div style="font-size:1.3rem; font-weight:800; color:#1B2A41; margin-bottom:6px;">₹85 Lakhs <span style="font-size:0.85rem; font-weight:600; color:#C89B3C;">| Highway Frontage</span></div>
          <h3 style="font-size:1.15rem; color:#1B2A41; margin-bottom:10px;">Commercial Highway Frontage Land in Bihar</h3>
          <p style="font-size:0.9rem; color:#555; margin-bottom:16px; line-height:1.5;">
            Prime commercial plot ideal for showrooms, petrol pumps, or warehouse setups with heavy traffic footfall.
          </p>
          <div style="display:flex; gap:12px;">
            <a href="https://wa.me/918303727724?text=I%20am%20interested%20in%20Commercial%20Land" target="_blank" class="btn btn-whatsapp" style="flex:1; padding:10px; font-size:0.88rem;">
              <i class="fa-brands fa-whatsapp"></i> Inquire Land
            </a>
            <a href="tel:+918303727724" class="btn btn-gold" style="padding:10px 16px; font-size:0.88rem;">
              <i class="fa-solid fa-phone"></i>
            </a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

{CTA_BAND}
{FOOTER}

<script src="js/script.js"></script>
<script src="js/ragini-assistant.js"></script>
</body>
</html>"""

with open(os.path.join(base_dir, 'properties.html'), 'w', encoding='utf-8') as f:
    f.write(properties_html)
print("Redesigned properties.html")

# 2. Redesign VDA-APPROVED.HTML
vda_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VDA Approved & UP RERA Registered Plots | Anshu Property Varanasi</title>
<meta name="description" content="Learn why VDA approved & UP RERA registered plots are essential for 100% legal & safe property investment in Varanasi, Allahabad, Bihar & MP.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css?v=3.0">
<link rel="stylesheet" href="css/ragini-assistant.css">
</head>
<body style="background-color:#F9F6F0;">

{get_header('vda')}

<section class="page-hero" style="background: linear-gradient(135deg, #121C2B 0%, #1B2A41 100%); color:#FFFFFF; padding: 75px 0 85px;">
  <div class="container" style="text-align:center;">
    <div class="seal-badge" style="margin-bottom:14px;">
      <span class="seal-icon">✓</span> 100% Government Sanctioned
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(32px, 3.8vw, 50px); color:#FFFFFF; margin-top:8px;">VDA Approved &amp; UP RERA Registered Plots</h1>
    <p style="color:#D1D5DB; max-width:640px; margin: 12px auto 0; font-size:1.1rem;">
      Protect your lifetime savings with 100% legal title clearance, VDA masterplan compliance, and guaranteed bank loan support.
    </p>
  </div>
</section>

<section class="section" style="padding:80px 0;">
  <div class="container">
    
    <!-- 2 Column Split -->
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:50px; align-items:center;">
      <div>
        <div class="pill-badge" style="margin-bottom:12px; background:rgba(200,155,60,0.15); color:#C89B3C; padding:6px 16px; border-radius:50px; font-weight:700; font-size:0.85rem; border:1px solid rgba(200,155,60,0.4);">
          <i class="fa-solid fa-shield-halved"></i> Legal Security
        </div>
        <h2 style="font-family: var(--font-serif); font-size:2.4rem; color:#1B2A41; margin-bottom:20px;">
          Why Buy VDA Approved Land in Varanasi?
        </h2>
        <p style="font-size:1.05rem; color:#444; line-height:1.7; margin-bottom:20px;">
          Varanasi Development Authority (VDA) approval guarantees that your plot is part of the sanctioned government masterplan with wide roads, electricity lines, and zero risk of illegal demolition.
        </p>

        <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="background:#FFFFFF; padding:18px 24px; border-radius:16px; box-shadow:0 6px 20px rgba(0,0,0,0.05); border-left:4px solid #C89B3C;">
            <h4 style="color:#1B2A41; font-size:1.1rem; margin-bottom:4px;"><i class="fa-solid fa-circle-check" style="color:#C89B3C;"></i> 100% Bank Loan Guarantee</h4>
            <p style="font-size:0.9rem; color:#666;">Nationalized banks (SBI, HDFC, PNB) offer up to 80% plot & construction loan on VDA approved properties.</p>
          </div>
          <div style="background:#FFFFFF; padding:18px 24px; border-radius:16px; box-shadow:0 6px 20px rgba(0,0,0,0.05); border-left:4px solid #C89B3C;">
            <h4 style="color:#1B2A41; font-size:1.1rem; margin-bottom:4px;"><i class="fa-solid fa-circle-check" style="color:#C89B3C;"></i> Immediate Registry & Mutation</h4>
            <p style="font-size:0.9rem; color:#666;">Clear title papers with fast khatauni and mutation transfer directly in your name.</p>
          </div>
        </div>
      </div>

      <div style="position:relative;">
        <div style="border-radius:24px; overflow:hidden; border:4px solid #FFFFFF; outline:2px solid #C89B3C; box-shadow:0 20px 50px rgba(0,0,0,0.15);">
          <img src="assets/anshu_dubey_site.jpg" alt="Anshu Dubey Site Visit">
        </div>
      </div>
    </div>

  </div>
</section>

{CTA_BAND}
{FOOTER}

<script src="js/script.js"></script>
<script src="js/ragini-assistant.js"></script>
</body>
</html>"""

with open(os.path.join(base_dir, 'vda-approved.html'), 'w', encoding='utf-8') as f:
    f.write(vda_html)
print("Redesigned vda-approved.html")

# 3. Redesign SERVICES.HTML
services_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Our Real Estate Services | Anshu Property Varanasi</title>
<meta name="description" content="Explore real estate services by Anshu Property: VDA plot sales, legal paper verification, free site visits, and bank loan support.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css?v=3.0">
<link rel="stylesheet" href="css/ragini-assistant.css">
</head>
<body style="background-color:#F9F6F0;">

{get_header('services')}

<section class="page-hero" style="background: linear-gradient(135deg, #121C2B 0%, #1B2A41 100%); color:#FFFFFF; padding: 75px 0 85px;">
  <div class="container" style="text-align:center;">
    <div class="seal-badge" style="margin-bottom:14px;">
      <span class="seal-icon">✓</span> End-to-End Property Solutions
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(32px, 3.8vw, 50px); color:#FFFFFF; margin-top:8px;">Our Professional Real Estate Services</h1>
    <p style="color:#D1D5DB; max-width:640px; margin: 12px auto 0; font-size:1.1rem;">
      From verified plot selection to legal title verification and bank loan approval — we handle everything.
    </p>
  </div>
</section>

<section class="section" style="padding:80px 0;">
  <div class="container">
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:30px;">
      
      <div style="background:#FFFFFF; padding:32px; border-radius:20px; box-shadow:0 8px 24px rgba(0,0,0,0.06); border:1px solid rgba(0,0,0,0.05);" class="why-card">
        <div style="width:56px; height:56px; background:rgba(200,155,60,0.12); color:#C89B3C; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:1.5rem; margin-bottom:20px;">
          <i class="fa-solid fa-map-location-dot"></i>
        </div>
        <h3 style="font-size:1.25rem; color:#1B2A41; margin-bottom:10px;">VDA Approved Plot Sales</h3>
        <p style="font-size:0.95rem; color:#555; line-height:1.6;">Direct owner pricing on residential & commercial plots along Varanasi Ring Road, Shivpur, and Babatpur.</p>
      </div>

      <div style="background:#FFFFFF; padding:32px; border-radius:20px; box-shadow:0 8px 24px rgba(0,0,0,0.06); border:1px solid rgba(0,0,0,0.05);" class="why-card">
        <div style="width:56px; height:56px; background:rgba(200,155,60,0.12); color:#C89B3C; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:1.5rem; margin-bottom:20px;">
          <i class="fa-solid fa-car-side"></i>
        </div>
        <h3 style="font-size:1.25rem; color:#1B2A41; margin-bottom:10px;">Free Car Site Visits</h3>
        <p style="font-size:0.95rem; color:#555; line-height:1.6;">Complimentary car transportation to inspect plot layouts at your preferred day and time without any obligation.</p>
      </div>

      <div style="background:#FFFFFF; padding:32px; border-radius:20px; box-shadow:0 8px 24px rgba(0,0,0,0.06); border:1px solid rgba(0,0,0,0.05);" class="why-card">
        <div style="width:56px; height:56px; background:rgba(200,155,60,0.12); color:#C89B3C; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:1.5rem; margin-bottom:20px;">
          <i class="fa-solid fa-building-columns"></i>
        </div>
        <h3 style="font-size:1.25rem; color:#1B2A41; margin-bottom:10px;">Bank Loan Assistance</h3>
        <p style="font-size:0.95rem; color:#555; line-height:1.6;">End-to-end loan approval support from SBI, HDFC, ICICI, and PNB with fast paperwork sanction.</p>
      </div>

      <div style="background:#FFFFFF; padding:32px; border-radius:20px; box-shadow:0 8px 24px rgba(0,0,0,0.06); border:1px solid rgba(0,0,0,0.05);" class="why-card">
        <div style="width:56px; height:56px; background:rgba(200,155,60,0.12); color:#C89B3C; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:1.5rem; margin-bottom:20px;">
          <i class="fa-solid fa-file-contract"></i>
        </div>
        <h3 style="font-size:1.25rem; color:#1B2A41; margin-bottom:10px;">Legal Title Verification</h3>
        <p style="font-size:0.95rem; color:#555; line-height:1.6;">100% legal verification of registry papers, khatauni records, mutation, and 7/12 land titles.</p>
      </div>

    </div>
  </div>
</section>

{CTA_BAND}
{FOOTER}

<script src="js/script.js"></script>
<script src="js/ragini-assistant.js"></script>
</body>
</html>"""

with open(os.path.join(base_dir, 'services.html'), 'w', encoding='utf-8') as f:
    f.write(services_html)
print("Redesigned services.html")

# 4. Redesign ABOUT.HTML
about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About Anshu Dubey & Anshu Property | Real Estate Consultant Varanasi</title>
<meta name="description" content="Learn about Anshu Dubey, founder of Anshu Property. 12+ years experience in VDA approved plots & RERA properties in Varanasi.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css?v=3.0">
<link rel="stylesheet" href="css/ragini-assistant.css">
</head>
<body style="background-color:#F9F6F0;">

{get_header('about')}

<section class="page-hero" style="background: linear-gradient(135deg, #121C2B 0%, #1B2A41 100%); color:#FFFFFF; padding: 75px 0 85px;">
  <div class="container" style="text-align:center;">
    <div class="seal-badge" style="margin-bottom:14px;">
      <span class="seal-icon">✓</span> 12+ Years Trust &amp; Leadership
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(32px, 3.8vw, 50px); color:#FFFFFF; margin-top:8px;">Meet Anshu Dubey &amp; Anshu Property</h1>
    <p style="color:#D1D5DB; max-width:640px; margin: 12px auto 0; font-size:1.1rem;">
      Helping over 2,400 families invest in 100% legal, clear-title, and government-approved plots across North India.
    </p>
  </div>
</section>

<section class="section" style="padding:80px 0;">
  <div class="container">
    <div style="display:grid; grid-template-columns: 0.9fr 1.1fr; gap:50px; align-items:center;">
      
      <div style="position:relative;">
        <div style="border-radius:24px; overflow:hidden; border:4px solid #FFFFFF; outline:2px solid #C89B3C; box-shadow:0 20px 50px rgba(0,0,0,0.15);">
          <img src="assets/anshu_dubey_hero.jpg" alt="Anshu Dubey Owner">
        </div>
      </div>

      <div>
        <div class="pill-badge" style="margin-bottom:12px; background:rgba(200,155,60,0.15); color:#C89B3C; padding:6px 16px; border-radius:50px; font-weight:700; font-size:0.85rem; border:1px solid rgba(200,155,60,0.4);">
          <i class="fa-solid fa-user-tie"></i> Founder &amp; Managing Director
        </div>
        <h2 style="font-family: var(--font-serif); font-size:2.4rem; color:#1B2A41; margin-bottom:20px;">
          Welcome! I'm <span style="color:#C89B3C;">Anshu Dubey</span>
        </h2>
        <div style="background:#FFFFFF; padding:28px; border-radius:20px; border-left:5px solid #C89B3C; box-shadow:0 8px 24px rgba(0,0,0,0.06); font-size:1.05rem; line-height:1.7; color:#333;">
          <p style="margin-bottom:14px;">
            For over <strong>12 years</strong>, I have dedicated myself to making land purchases transparent, legal, and stress-free for families across Varanasi, Allahabad, Bihar, and MP.
          </p>
          <p style="margin-bottom:14px;">
            My philosophy is simple: <strong>Every customer deserves clear title deeds, zero hidden costs, and personal owner guidance</strong> on site visits.
          </p>
          <p>
            With over <strong>2,400 satisfied plot owners</strong>, Anshu Property stands as Varanasi's most trusted real estate brand.
          </p>
        </div>
      </div>

    </div>
  </div>
</section>

{CTA_BAND}
{FOOTER}

<script src="js/script.js"></script>
<script src="js/ragini-assistant.js"></script>
</body>
</html>"""

with open(os.path.join(base_dir, 'about.html'), 'w', encoding='utf-8') as f:
    f.write(about_html)
print("Redesigned about.html")

# 5. Redesign BLOG.HTML
blog_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Real Estate Blog & Property Guides | Anshu Property Varanasi</title>
<meta name="description" content="Read expert articles on VDA approved plot buying in Varanasi, land registry rules, and UP RERA investment guidelines.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css?v=3.0">
<link rel="stylesheet" href="css/ragini-assistant.css">
</head>
<body style="background-color:#F9F6F0;">

{get_header('blog')}

<section class="page-hero" style="background: linear-gradient(135deg, #121C2B 0%, #1B2A41 100%); color:#FFFFFF; padding: 75px 0 85px;">
  <div class="container" style="text-align:center;">
    <div class="seal-badge" style="margin-bottom:14px;">
      <span class="seal-icon">✓</span> Expert Real Estate Advice
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(32px, 3.8vw, 50px); color:#FFFFFF; margin-top:8px;">Real Estate Blog &amp; Property Guides</h1>
    <p style="color:#D1D5DB; max-width:640px; margin: 12px auto 0; font-size:1.1rem;">
      Insights, VDA masterplan updates, legal land buying tips, and market analysis by Anshu Dubey.
    </p>
  </div>
</section>

<section class="section" style="padding:80px 0;">
  <div class="container">
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:32px;">
      
      <div style="background:#FFFFFF; border-radius:20px; overflow:hidden; box-shadow:0 8px 24px rgba(0,0,0,0.06); border:1px solid rgba(0,0,0,0.05);">
        <img src="assets/plot_varanasi.jpg" alt="VDA Guide" style="width:100%; aspect-ratio:16/9; object-fit:cover;">
        <div style="padding:24px;">
          <span style="color:#C89B3C; font-weight:700; font-size:0.8rem; text-transform:uppercase; letter-spacing:0.5px;">VDA Approval Guide</span>
          <h3 style="font-size:1.2rem; color:#1B2A41; margin:8px 0 10px;">How to Check VDA Approval for Plots in Varanasi (2026 Guide)</h3>
          <p style="font-size:0.9rem; color:#555; line-height:1.6; margin-bottom:16px;">Essential steps to verify Khasra numbers and VDA masterplan sanctions before placing plot token money.</p>
          <a href="https://wa.me/918303727724?text=I%20want%20to%20read%20VDA%20Guide" target="_blank" style="color:#1B2A41; font-weight:700; font-size:0.9rem;">Read Full Guide <i class="fa-solid fa-arrow-right" style="color:#C89B3C;"></i></a>
        </div>
      </div>

      <div style="background:#FFFFFF; border-radius:20px; overflow:hidden; box-shadow:0 8px 24px rgba(0,0,0,0.06); border:1px solid rgba(0,0,0,0.05);">
        <img src="assets/villa_allahabad.jpg" alt="RERA Guide" style="width:100%; aspect-ratio:16/9; object-fit:cover;">
        <div style="padding:24px;">
          <span style="color:#C89B3C; font-weight:700; font-size:0.8rem; text-transform:uppercase; letter-spacing:0.5px;">RERA Legal Tips</span>
          <h3 style="font-size:1.2rem; color:#1B2A41; margin:8px 0 10px;">5 Things Every Buyer Must Check Before Property Registry</h3>
          <p style="font-size:0.9rem; color:#555; line-height:1.6; margin-bottom:16px;">Complete checklist for non-agricultural clearance, 7/12 khatauni verification, and bank loan approvals.</p>
          <a href="https://wa.me/918303727724?text=I%20want%20to%20read%20Registry%20Guide" target="_blank" style="color:#1B2A41; font-weight:700; font-size:0.9rem;">Read Full Guide <i class="fa-solid fa-arrow-right" style="color:#C89B3C;"></i></a>
        </div>
      </div>

    </div>
  </div>
</section>

{CTA_BAND}
{FOOTER}

<script src="js/script.js"></script>
<script src="js/ragini-assistant.js"></script>
</body>
</html>"""

with open(os.path.join(base_dir, 'blog.html'), 'w', encoding='utf-8') as f:
    f.write(blog_html)
print("Redesigned blog.html")

# 6. Redesign CONTACT.HTML
contact_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact Anshu Dubey | Anshu Property Varanasi</title>
<meta name="description" content="Get in touch with Anshu Dubey for VDA approved plots & free site visits in Varanasi. Call/WhatsApp +91 83037 27724.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css?v=3.0">
<link rel="stylesheet" href="css/ragini-assistant.css">
</head>
<body style="background-color:#F9F6F0;">

{get_header('contact')}

<section class="page-hero" style="background: linear-gradient(135deg, #121C2B 0%, #1B2A41 100%); color:#FFFFFF; padding: 75px 0 85px;">
  <div class="container" style="text-align:center;">
    <div class="seal-badge" style="margin-bottom:14px;">
      <span class="seal-icon">✓</span> Direct Owner Consultation
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(32px, 3.8vw, 50px); color:#FFFFFF; margin-top:8px;">Contact Anshu Dubey</h1>
    <p style="color:#D1D5DB; max-width:640px; margin: 12px auto 0; font-size:1.1rem;">
      Schedule a free car site visit or discuss VDA plot options directly with owner Anshu Dubey.
    </p>
  </div>
</section>

<section class="section" style="padding:80px 0;">
  <div class="container">
    <div style="display:grid; grid-template-columns: 0.9fr 1.1fr; gap:50px;">
      
      <!-- Contact Cards Column -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div style="background:#FFFFFF; padding:28px; border-radius:20px; box-shadow:0 8px 24px rgba(0,0,0,0.06); border-left:5px solid #C89B3C; display:flex; gap:20px; align-items:center;">
          <div style="width:50px; height:50px; background:#1B2A41; color:#C89B3C; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
            <i class="fa-solid fa-phone"></i>
          </div>
          <div>
            <h4 style="color:#1B2A41; font-size:1.1rem; margin-bottom:2px;">Call / WhatsApp Direct</h4>
            <a href="tel:+918303727724" style="color:#C89B3C; font-weight:800; font-size:1.15rem;">+91 83037 27724</a>
          </div>
        </div>

        <div style="background:#FFFFFF; padding:28px; border-radius:20px; box-shadow:0 8px 24px rgba(0,0,0,0.06); border-left:5px solid #C89B3C; display:flex; gap:20px; align-items:center;">
          <div style="width:50px; height:50px; background:#1B2A41; color:#C89B3C; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
            <i class="fa-solid fa-envelope"></i>
          </div>
          <div>
            <h4 style="color:#1B2A41; font-size:1.1rem; margin-bottom:2px;">Email Inquiry</h4>
            <a href="mailto:anshudubey3409@gmail.com" style="color:#333; font-weight:600;">anshudubey3409@gmail.com</a>
          </div>
        </div>

        <div style="background:#FFFFFF; padding:28px; border-radius:20px; box-shadow:0 8px 24px rgba(0,0,0,0.06); border-left:5px solid #C89B3C; display:flex; gap:20px; align-items:center;">
          <div style="width:50px; height:50px; background:#1B2A41; color:#C89B3C; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
            <i class="fa-solid fa-location-dot"></i>
          </div>
          <div>
            <h4 style="color:#1B2A41; font-size:1.1rem; margin-bottom:2px;">Head Office</h4>
            <p style="color:#555; font-size:0.95rem;">Varanasi, Uttar Pradesh (Service in Allahabad, Bihar &amp; MP)</p>
          </div>
        </div>
      </div>

      <!-- White Contact Form Card -->
      <div style="background:#FFFFFF; padding:36px; border-radius:24px; box-shadow:0 12px 35px rgba(0,0,0,0.08); border:1px solid rgba(200,155,60,0.3);">
        <h3 style="font-family: var(--font-serif); font-size:1.8rem; color:#1B2A41; margin-bottom:8px;">Send Direct Message</h3>
        <p style="font-size:0.95rem; color:#666; margin-bottom:24px;">Submitting this form will automatically open WhatsApp with your message details.</p>

        <form id="contact-page-form" style="display:flex; flex-direction:column; gap:18px;">
          <div>
            <label style="font-weight:700; font-size:0.85rem; color:#1B2A41; text-transform:uppercase; display:block; margin-bottom:6px;">Your Name</label>
            <input type="text" id="name" required placeholder="Enter full name" style="width:100%; padding:14px; border-radius:12px; border:1px solid #CBD5E0; outline:none; background:#F9F6F0;">
          </div>
          <div>
            <label style="font-weight:700; font-size:0.85rem; color:#1B2A41; text-transform:uppercase; display:block; margin-bottom:6px;">Phone Number</label>
            <input type="tel" id="phone" required placeholder="Enter 10-digit mobile number" style="width:100%; padding:14px; border-radius:12px; border:1px solid #CBD5E0; outline:none; background:#F9F6F0;">
          </div>
          <div>
            <label style="font-weight:700; font-size:0.85rem; color:#1B2A41; text-transform:uppercase; display:block; margin-bottom:6px;">Requirement / Message</label>
            <textarea id="message" rows="4" placeholder="Tell us what location or plot budget you are looking for..." style="width:100%; padding:14px; border-radius:12px; border:1px solid #CBD5E0; outline:none; background:#F9F6F0;"></textarea>
          </div>
          <button type="submit" class="btn btn-gold" style="padding:16px; font-size:1.05rem; border-radius:12px; width:100%; margin-top:8px;">
            <i class="fa-brands fa-whatsapp" style="font-size:1.3rem;"></i> Send Inquiry via WhatsApp
          </button>
        </form>
      </div>

    </div>
  </div>
</section>

{CTA_BAND}
{FOOTER}

<script src="js/script.js"></script>
<script src="js/ragini-assistant.js"></script>
</body>
</html>"""

with open(os.path.join(base_dir, 'contact.html'), 'w', encoding='utf-8') as f:
    f.write(contact_html)
print("Redesigned contact.html")
