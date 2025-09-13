Clear-Host
Write-Host "Running Password Generator..." -ForegroundColor Cyan
python .\PasswordGenerator.py
Write-Host "`Done. Press Enter to exit..." -ForegroundColor Green
$null = Read-Host