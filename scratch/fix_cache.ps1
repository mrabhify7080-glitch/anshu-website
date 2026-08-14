$files = Get-ChildItem -Path "d:\ansu\website" -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $content = [regex]::Replace($content, "style\.css(\?v=[\d\.]+)?", "style.css?v=4.0")
    Set-Content $file.FullName -Value $content -Encoding UTF8
    Write-Host "Updated cache buster v=4.0 in $($file.Name)"
}
