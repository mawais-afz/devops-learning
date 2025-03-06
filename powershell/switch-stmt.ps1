# Simple switch statement with a number
$number = 2
switch ($number) {
    1 { Write-Host "One" }
    2 { Write-Host "Two" }
    3 { Write-Host "Three" }
    default { Write-Host "Unknown number" }
}

# Switch with strings
$fruit = "Apple" 
switch ($fruit) {
    "Apple" { Write-Host "Selected fruit is Apple" }
    "Banana" { Write-Host "Selected fruit is Banana" }
    "Orange" { Write-Host "Selected fruit is Orange" }
    default { Write-Host "Unknown fruit" }
}

# Switch with multiple matches using wildcards
$text = "Hello World"
switch -Wildcard ($text) {
    "Hello*" { Write-Host "Text starts with Hello" }
    "*World" { Write-Host "Text ends with World" }
    "*World*" { Write-Host "Text contains World" }
}

# Switch with regex pattern matching
$email = "user@example.com"
switch -Regex ($email) {
    "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$" { Write-Host "Valid email format" }
    default { Write-Host "Invalid email format" }
}

# Switch with break statement
$value = 2
switch ($value) {
    1 { Write-Host "One"; break }
    2 { Write-Host "Two"; break }
    3 { Write-Host "Three"; break }
    default { Write-Host "Unknown value" }
}
