# In an array 1-100 numbers are stored, one number is missing how do you find it
list = [ 5, 4, 6, 1, 2, 3, 7,9]
n = 9
exp_sum = n*(n+1)/2;

real_sum = 0;

for num in list :
    real_sum = real_sum + num;
missing_no = exp_sum - real_sum;

print ("missing_number: ", missing_no);
