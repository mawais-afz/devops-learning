$age = 25

if ($age -gt 18) {
    Write-Host "You are an adult"
} elseif ($age -eq 18) {
    Write-Host "You just turned adult"
} else {
    Write-Host "You are under age"
}

# Another example with string comparison
$name = "John"

if ($name -eq "John") {
    Write-Host "Hello John!"
} else {
    Write-Host "Hello Stranger!"
}

# Example with multiple conditions using -and operator
$isStudent = $true
$hasID = $true

if ($isStudent -and $hasID) {
    Write-Host "Welcome to the school!"
} else {
    Write-Host "Please check your credentials"
}
