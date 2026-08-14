$files = Get-ChildItem -Path "d:\ansu\website" -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8

    # Remove floating fab-whatsapp link
    $content = [regex]::Replace($content, '(?s)<a href="https://wa\.me/[^"]*"[^>]*class="fab fab-whatsapp"[^>]*>.*?</a>', '')

    # Update Header CTA button to Direct Call button
    $headerCta = @'
<div class="header-cta">
      <a href="tel:+918303727724" class="btn btn-primary btn-sm" style="display:inline-flex;align-items:center;gap:6px;padding:8px 16px;font-size:0.88rem;background:#C89B3C;color:#121C2D;font-weight:700;">
        <i class="fa-solid fa-phone"></i> +91 83037 27724
      </a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
'@
    $content = [regex]::Replace($content, '(?s)<div class="header-cta">.*?</div>', $headerCta)

    Set-Content $file.FullName -Value $content -Encoding UTF8
    Write-Host "Removed non-form WhatsApp icons in $($file.Name)"
}
