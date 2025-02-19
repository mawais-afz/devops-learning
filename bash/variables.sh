# Local variables
local_first_name="Local Devops"
local_last_name=Learning
echo $local_first_name $local_last_name

# Globle variable
export globle_first_name="Globle Devops"
export local_last_name=Learning

echo $globle_first_name $local_last_name


# Accessing variable using $ sign
pi=3.1417
echo "The value of the PI is ${pi}"

# Assigning value to a variable using backtick sign
date=`date`
echo $date