$headerIndex = @"
<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">
      <span class="logo-mark"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11L12 3l9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/></svg></span>
      Anshu <span>Property</span>
    </a>

    <nav>
      <ul class="nav-desktop">
        <li><a href="index.html" class="nav-link {INDEX}">Home</a></li>
        <li><a href="properties.html" class="nav-link {PROPERTIES}">Properties</a></li>
        <li><a href="vda-approved.html" class="nav-link {VDA}">VDA Approved</a></li>
        <li><a href="services.html" class="nav-link {SERVICES}">Services</a></li>
        <li><a href="about.html" class="nav-link {ABOUT}">About Us</a></li>
        <li><a href="blog.html" class="nav-link {BLOG}">Blog</a></li>
        <li><a href="contact.html" class="nav-link {CONTACT}">Contact</a></li>
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
</header>
"@

$footer = @"
<footer class="site-footer">
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
</footer>
"@

$pageMap = @{
    "index.html" = "INDEX"
    "AnshuProperties.com.html" = "INDEX"
    "properties.html" = "PROPERTIES"
    "vda-approved.html" = "VDA"
    "services.html" = "SERVICES"
    "about.html" = "ABOUT"
    "blog.html" = "BLOG"
    "contact.html" = "CONTACT"
}

foreach ($item in $pageMap.GetEnumerator()) {
    $file = join-path "d:\ansu\website" $item.Key
    if (Test-Path $file) {
        $content = Get-Content $file -Raw -Encoding UTF8

        # Build specific header with active link
        $hdr = $headerIndex
        $keys = @("INDEX", "PROPERTIES", "VDA", "SERVICES", "ABOUT", "BLOG", "CONTACT")
        foreach ($k in $keys) {
            if ($k -eq $item.Value) {
                $hdr = $hdr.Replace("{$k}", "active")
            } else {
                $hdr = $hdr.Replace("{$k}", "")
            }
        }

        # Replace header regex
        $content = [regex]::Replace($content, "(?s)<header class=""site-header"">.*?</header>", $hdr)
        # Replace footer regex
        $content = [regex]::Replace($content, "(?s)<footer class=""site-footer"">.*?</footer>", $footer)

        Set-Content $file -Value $content -Encoding UTF8
        Write-Host "Harmonized $($item.Key) with active $($item.Value)"
    }
}
