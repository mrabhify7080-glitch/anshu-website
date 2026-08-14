$files = Get-ChildItem -Path "d:\ansu\website" -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8

    # Replace Priya file references with Ragini
    $content = $content -replace "css/priya-assistant.css", "css/ragini-assistant.css"
    $content = $content -replace "js/priya-assistant.js", "js/ragini-assistant.js"
    $content = $content -replace "Priya", "Ragini"

    Set-Content $file.FullName -Value $content -Encoding UTF8
    Write-Host "Updated Ragini Assistant in $($file.Name)"
}
