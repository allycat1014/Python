# In an array 1-100 exactly one number is duplicate how do you find it?

list = [1,2,2,3,3,4,4,5,5,6,7,8,9,9,0,0]

s =set([]);
for number in list:
   if (number in s)  :
     print("found the duplicate number",number)
   s.add(number)