# Function to generate Fibonacci sequence up to n terms
function Get-FibonacciSequence {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory=$true)]
        [int]$Terms
    )

    $fibonacci = @()
    
    if ($Terms -le 0) {
        return $fibonacci
    }
    
    # First two numbers of Fibonacci sequence
    $fibonacci += 0
    if ($Terms -eq 1) {
        return $fibonacci
    }
    
    $fibonacci += 1
    if ($Terms -eq 2) {
        return $fibonacci
    }
    
    # Generate remaining numbers
    for ($i = 2; $i -lt $Terms; $i++) {
        $fibonacci += $fibonacci[$i-1] + $fibonacci[$i-2]
    }
    
    return $fibonacci
}

$sequence = Get-FibonacciSequence
Write-Host $sequence
