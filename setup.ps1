# StockFlow Project Setup Script
Write-Host "=== Creating StockFlow Inventory System ===" -ForegroundColor Green

# Create main directories
$folders = @("backend", "frontend", "docs", "k8s", "scripts", "docker", ".github", ".vscode")
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Name $folder -Force | Out-Null
    Write-Host "✓ Created: $folder" -ForegroundColor Cyan
}

Write-Host "`n✅ Basic folders created!" -ForegroundColor Green
Write-Host "`nNext: Run docker-compose up to start development" -ForegroundColor Yellow
