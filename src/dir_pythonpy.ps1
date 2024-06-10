# this script is in charge of adding to the directory the actual PYTHONPATH
$env:PYTHONPATH += ";$(Get-Location)"