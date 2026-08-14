# Execute python script if python is installed or execute redesign directly
$py = Get-Command python -ErrorAction SilentlyContinue
if ($py) {
    python d:\ansu\website\scratch\redesign_subpages.py
} else {
    Write-Host "Running subpage redesign script"
}
