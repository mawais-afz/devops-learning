# Get all environment variables
Write-Host "`nAll Environment Variables:"
Get-ChildItem Env: | Format-Table -AutoSize

# Get specific system environment variables
Write-Host "`nCommon System Environment Variables:"
Write-Host "OS: $env:OS"
Write-Host "Computer Name: $env:COMPUTERNAME" 
Write-Host "System Root: $env:SystemRoot"
Write-Host "Program Files: $env:ProgramFiles"
Write-Host "User Profile: $env:USERPROFILE"

# Get user-specific environment variables
Write-Host "`nUser Environment Variables:"
Write-Host "Username: $env:USERNAME"
Write-Host "User Domain: $env:USERDOMAIN"
Write-Host "Home Directory: $env:HOMEDRIVE$env:HOMEPATH"

# Search for a specific environment variable
$searchVar = "PATH"
Write-Host "`nSearching for $searchVar variable:"
$pathValue = [Environment]::GetEnvironmentVariable($searchVar, "Machine")
Write-Host "$searchVar = $pathValue"
