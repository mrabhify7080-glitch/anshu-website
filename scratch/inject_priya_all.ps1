$htmlFiles = Get-ChildItem -Path "d:\ansu\website" -Filter "*.html"

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8

    $modified = $false

    if ($content -notmatch "priya-assistant.js") {
        if ($content -match "</body>") {
            $content = $content -replace "</body>", "<script src=""js/priya-assistant.js""></script>`n</body>"
            $modified = $true
        }
    }

    if ($content -notmatch "priya-assistant.css") {
        if ($content -match "</head>") {
            $content = $content -replace "</head>", "<link rel=""stylesheet"" href=""css/priya-assistant.css"">`n</head>"
            $modified = $true
        }
    }

    if ($modified) {
        Set-Content $file.FullName -Value $content -Encoding UTF8
        Write-Host "Injected Priya Assistant into $($file.Name)"
    }
}
