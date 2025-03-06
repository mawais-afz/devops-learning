# Create a new directory
New-Item -Path ".\TestFolder" -ItemType Directory

# Create a test file
Set-Content -Path ".\test.txt" -Value "This is a test file"

# Copy item to the new directory
Copy-Item -Path ".\test.txt" -Destination ".\TestFolder\test.txt"

# Verify the copy operation
if (Test-Path ".\TestFolder\test.txt") {
    Write-Host "File copied successfully"
} else {
    Write-Host "File copy failed"
}

# Clean up - remove test files and directory
Remove-Item -Path ".\test.txt"
Remove-Item -Path ".\TestFolder" -Recurse


# Create test directories
New-Item -Path ".\SourceDir" -ItemType Directory
New-Item -Path ".\DestDir" -ItemType Directory

# Create a test file in source directory
Set-Content -Path ".\SourceDir\movetest.txt" -Value "This file will be moved"

# Move the file from source to destination
Move-Item -Path ".\SourceDir\movetest.txt" -Destination ".\DestDir"

# Verify the move operation
if (Test-Path ".\DestDir\movetest.txt") {
    Write-Host "File moved successfully"
} else {
    Write-Host "File move failed"
}

# Clean up - remove test directories
Remove-Item -Path ".\SourceDir" -Force
Remove-Item -Path ".\DestDir" -Recurse -Force
