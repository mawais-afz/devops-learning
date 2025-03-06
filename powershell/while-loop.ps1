# Simple while loop with counter
$counter = 1
while ($counter -le 5) {
    Write-Host "Count: $counter"
    $counter++
}

# While loop with break statement
$number = 1
while ($number -le 10) {
    if ($number -eq 6) {
        break
    }
    Write-Host "Current number: $number" 
    $number++
}

# While loop with continue statement
$i = 0
while ($i -lt 5) {
    $i++
    if ($i -eq 3) {
        continue
    }
    Write-Host "Value of i: $i"
}

# While loop with array
$fruits = @("Apple", "Banana", "Orange", "Mango")
$index = 0
while ($index -lt $fruits.Length) {
    Write-Host "Fruit at position $index is: $($fruits[$index])"
    $index++
}

# Do-While loop example
$count = 1
do {
    Write-Host "Do-While iteration: $count"
    $count++
} while ($count -le 3)
