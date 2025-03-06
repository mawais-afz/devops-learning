# Simple for loop with numbers
for ($i = 1; $i -le 5; $i++) {
    Write-Host "Number: $i"
}

# For loop with array
$fruits = @("Apple", "Banana", "Orange", "Mango")
for ($i = 0; $i -lt $fruits.Length; $i++) {
    Write-Host "Fruit at index $i is: $($fruits[$i])"
}

# ForEach loop (alternative syntax)
$colors = @("Red", "Blue", "Green")
foreach ($color in $colors) {
    Write-Host "Color: $color"
}

# For loop with break statement
for ($i = 1; $i -le 10; $i++) {
    if ($i -eq 6) {
        break
    }
    Write-Host "Counting: $i"
}

# For loop with continue statement
for ($i = 1; $i -le 5; $i++) {
    if ($i -eq 3) {
        continue
    }
    Write-Host "Current number: $i"
}
