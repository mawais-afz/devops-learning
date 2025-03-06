# Example of working with secure strings in PowerShell

# Create a secure string from plain text
$secureString = ConvertTo-SecureString "MySecretPassword" -AsPlainText -Force
Write-Host "Secure string created $secureString"

# Convert secure string to encrypted standard string that can be stored
$encrypted = ConvertFrom-SecureString $secureString
Write-Host "Encrypted string: $encrypted"

# Convert encrypted string back to secure string
$secureStringFromEncrypted = ConvertTo-SecureString $encrypted
Write-Host "Converted back to secure string $secureStringFromEncrypted"