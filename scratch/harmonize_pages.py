import os
import re

HEADER_TEMPLATE = """<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">
      <span class="logo-mark">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11L12 3l9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/></svg>
      </span>
      Anshu <span>Property</span>
    </a>

    <nav>
      <ul class="nav-desktop">
        <li><a href="index.html" class="nav-link {INDEX_ACTIVE}">Home</a></li>
        <li><a href="properties.html" class="nav-link {PROPERTIES_ACTIVE}">Properties</a></li>
        <li><a href="vda-approved.html" class="nav-link {VDA_ACTIVE}">VDA Approved</a></li>
        <li><a href="services.html" class="nav-link {SERVICES_ACTIVE}">Services</a></li>
        <li><a href="about.html" class="nav-link {ABOUT_ACTIVE}">About Us</a></li>
        <li><a href="blog.html" class="nav-link {BLOG_ACTIVE}">Blog</a></li>
        <li><a href="contact.html" class="nav-link {CONTACT_ACTIVE}">Contact</a></li>
      </ul>
    </nav>

    <div class="header-cta">
      <a href="https://wa.me/918303727724" target="_blank" class="btn btn-primary btn-sm" style="display:inline-flex;align-items:center;gap:6px;padding:8px 16px;font-size:0.88rem;">
        <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 18.2a8.2 8.2 0 01-4.2-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1120.2 12 8.2 8.2 0 0112 20.2z"/></svg>
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

FOOTER_TEMPLATE = """<footer class="site-footer">
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
        <a href="tel:+918303727724">📞 +91 83037 27724</a>
        <a href="https://wa.me/918303727724" target="_blank">💬 WhatsApp Support</a>
        <a href="mailto:anshudubey3409@gmail.com">✉️ anshudubey3409@gmail.com</a>
        <p style="margin-top:10px;font-size:0.85rem;color:#94A3B8;">📍 Head Office: Varanasi, Uttar Pradesh</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Anshu Property (@anshupropertyvns). All rights reserved.</span>
      <span>Owned &amp; operated by Anshu Dubey</span>
    </div>
  </div>
</footer>"""

def get_header(active_page):
    header = HEADER_TEMPLATE
    header = header.replace('{INDEX_ACTIVE}', 'active' if active_page == 'index' else '')
    header = header.replace('{PROPERTIES_ACTIVE}', 'active' if active_page == 'properties' else '')
    header = header.replace('{VDA_ACTIVE}', 'active' if active_page == 'vda' else '')
    header = header.replace('{SERVICES_ACTIVE}', 'active' if active_page == 'services' else '')
    header = header.replace('{ABOUT_ACTIVE}', 'active' if active_page == 'about' else '')
    header = header.replace('{BLOG_ACTIVE}', 'active' if active_page == 'blog' else '')
    header = header.replace('{CONTACT_ACTIVE}', 'active' if active_page == 'contact' else '')
    return header

pages = {
    'index.html': 'index',
    'AnshuProperties.com.html': 'index',
    'properties.html': 'properties',
    'vda-approved.html': 'vda',
    'services.html': 'services',
    'about.html': 'about',
    'blog.html': 'blog',
    'contact.html': 'contact'
}

base_dir = r'd:\ansu\website'

for filename, active_key in pages.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure fontawesome and google fonts links are present in head
    if 'font-awesome' not in content:
        fonts_tag = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n'
        content = content.replace('</head>', f'{fonts_tag}</head>', 1)

    # Ensure css/style.css is linked
    if 'css/style.css' not in content:
        content = content.replace('</head>', '<link rel="stylesheet" href="css/style.css?v=3.0">\n</head>', 1)

    # Replace header section
    content = re.sub(r'<header class="site-header">.*?</header>', get_header(active_key), content, flags=re.DOTALL)

    # Replace footer section
    content = re.sub(r'<footer class="site-footer">.*?</footer>', FOOTER_TEMPLATE, content, flags=re.DOTALL)

    # Ensure body has Warm Ivory background style
    content = re.sub(r'<body[^>]*>', '<body style="background-color:#F9F6F0;">', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Harmonized {filename} (Active link: {active_key})")
