import os
import re

base_dir = r'd:\ansu\website'

html_files = [
    'index.html',
    'AnshuProperties.com.html',
    'landing-page.html',
    'properties.html',
    'vda-approved.html',
    'services.html',
    'about.html',
    'blog.html',
    'contact.html'
]

# Clean Header without WhatsApp button (replaced with Direct Call button)
HEADER_REPLACEMENT = """<div class="header-cta">
      <a href="tel:+918303727724" class="btn btn-primary btn-sm" style="display:inline-flex;align-items:center;gap:6px;padding:8px 16px;font-size:0.88rem;background:#C89B3C;color:#121C2D;font-weight:700;">
        <i class="fa-solid fa-phone"></i> +91 83037 27724
      </a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>"""

# Clean Footer without standalone WhatsApp link/icon
CLEAN_FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">
          <span class="logo-mark"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11L12 3l9 8"/><path d="M5 10v10h14V10"/></svg></span>
          Anshu Property
        </div>
        <p>Varanasi's premier real estate consultancy founded by Anshu Dubey (@anshupropertyvns). Specializing in VDA Approved &amp; UP RERA Registered plots in Varanasi, Allahabad, Bihar &amp; MP.</p>
        <div class="footer-socials" style="display:flex;gap:12px;margin-top:16px;">
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

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        continue

    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Remove floating fab-whatsapp link
    content = re.sub(r'<a href="https://wa\.me/[^"]*"[^>]*class="fab fab-whatsapp"[^>]*>.*?</a>', '', content, flags=re.DOTALL)

    # 2. Update Header CTA to call button instead of WhatsApp button
    content = re.sub(r'<div class="header-cta">.*?</div>', HEADER_REPLACEMENT, content, flags=re.DOTALL)

    # 3. Update Footer to clean footer without standalone WhatsApp icons
    content = re.sub(r'<footer class="site-footer">.*?</footer>', CLEAN_FOOTER, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Cleaned non-form WhatsApp icons in {fname}")
