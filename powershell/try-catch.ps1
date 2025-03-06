# Simple try-catch example
try {
    # Attempt to divide by zero
    $number = 10
    $result = $number / 0
    Write-Host "This line won't execute"
} catch {
    Write-Host "An error occurred: $($_.Exception.Message)"
}

# Try-catch with specific error type
try {
    # Attempt to access non-existent file
    $content = Get-Content "nonexistent.txt"
} catch [System.IO.FileNotFoundException] {
    Write-Host "The specified file was not found"
} catch {
    Write-Host "An unexpected error occurred: $($_.Exception.Message)"
}

# Try-catch-finally example
try {
    # Attempt some risky operation
    $array = @(1, 2, 3)
    $element = $array[10]  # This will cause an index out of range error
} catch {
    Write-Host "Error accessing array: $($_.Exception.Message)"
} finally {
    Write-Host "This block always executes, regardless of errors"
}

# Try-catch with multiple operations
try {
    # Create a test file
    New-Item -Path "test.txt" -ItemType File -Force
    # Write some content
    Set-Content -Path "test.txt" -Value "Test content"
    # Read the content
    $content = Get-Content "test.txt"
    Write-Host "File content: $content"
} catch {
    Write-Host "Error handling file: $($_.Exception.Message)"
} finally {
    # Clean up - remove the test file if it exists
    if (Test-Path "test.txt") {
        Remove-Item "test.txt"
    }
}
