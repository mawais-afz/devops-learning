#!/bin/bash  
  

echo -e "Enter value of x: \c"
read x
echo -e "Enter value of y: \c" 
read y

echo "Addition of x & y is $(( $x + $y ))"  
echo "Subtraction of x & y is $(( $x - $y ))"  
echo "Multiplication of x & y is $(( $x * $y ))"  
echo "Division of x by y is $(( $x / $y ))"  
echo "Exponentiation of x,y is $(( $x ** $y ))"  
echo "Modular Division of x,y is $(( $x % $y ))"  
echo "Incrementing x by 5, then x= " $(( x += 5 ))   
echo "Decrementing x by 5, then x= " $(( x -= 5 ))  
echo "Multiply of x by 5, then x=" $(( x *= 5 ))  
echo "Dividing x by 5, x= " $(( x /= 5 ))  
echo "Remainder of Dividing x by 5, x=" $(( x %= 5 ))  
