#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""BMI 6018 Fall 2022 

Instructions: For this assignment, please return all answers as variables in your
.py file. You will quickly note that you will need to find answers outside the
class lectures. This is not an accident! You will need to become professionally
comfortable with looking things up via the python docs and google. 

Ensure that all variables are labelled according to the example. IE the answer
to problem 1 part c should be labelled one_c. While all questions are answerable
with a single line of code, you are free to use helper variables so long as they
are helpfully/informatively named. 

I should be able to open your .py file and run it without errors. I will **not** be 
debugging your code for you. If your file does not run, it will **not** be graded. 
If you are unsure if your file will run, open up a chpc terminal and test it there.

For this assignment, please only use base python files types. That is: there 
should be no import calls in your file save my use of sys at the end.

Example Problem

0.a Create a list of strings
0.b Using a str method, capitalize one of the elements in the list using a slice
0.c Coerce one character of the list to display as a hex

zero_a = ['first','second','third','fourth','fifth']
zero_b = zero_a[1].upper()
zero_c = hex(ord(zero_a[1][1]))

#Problem 1: Lists, Sets and Coersion

1.a Create a list of integers no fewer than 10 items from 0 to 9.
 .b Add 3 to the 5th indexed element
 .c Coerce all elements in the list to floats using list comprehension
 .d Coerce the list to a set
 .e Using a method, append int 10 to the set
 .f Using a method, pop an item from the set
 .g Using a length counting function, count the number of items in the set
 .h Check if the number of items in the set is the same as the 
    number of items in the list
 .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
 .j Coerce 1.i to a set
 .k Count the number of elements in the 1.j



Problem 2: Dictionary woes

2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    two_a, ensure the key names are the same as the dictionary names.
 .b Using keys, retrieve the Dango's name from 2.a
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
 .e Coerce the keys of 2.d into a list
 .f Coerce the values of 2.d into a list
 .g Use the zip function to combine 2.e and 2.f into a dictionary again


two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}



Problem 3: Set combinations

Given the predefined sets below and using set methods
3.a Is set E a subset of set A
 .b Is set E a strict subset of set A
 .c Create a set that is the intersection of set A and set B
 .d Create a set that is the union of sets C, D and E
 .e add 9 to the set
 .f Using == compare this set to the list in one_a
 .g Explain why they are not the same. What would you need to change if you
    wanted this to be True?
 

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}



Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.

4.a Create a variable of type int with the value of 8
 .b Create an empty list 
 .c Using type(), add the type of 4.a to this list
 .d Add 0.39 to 4.c
 .e append the type of 0.39 to the list
 .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    decimal places, and append to list.
 .g append the type to the list
 
 
Problem 5: More variable type changes

Continue from where you left off in Problem 4.

5.a Manually create a dictionary where the values are items in the list from where we left in 
    problem 4, and the keys should be their index in the list. Print the dictionary.
 .b Add 300 and coerce it into a string
 .c append the type to the list
 .d slice the string up to the 2nd element
 .e append the type to the list
 .f use list comprehension to convert this into a new list of integers
 .g append the type to the list
 .h append the type of three_setA to the list
"""

#Start your assignment here
print("Assignment 3")



# In[6]:


#Problem 1
print("Problem # 1")
#this is the original list
one_a = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
print(one_a)

#if I print(one_b) then it returns none, therefore I have to print(one_a) for the insert to show. This is not the case for one_c, one_d, so when this is run for grading purposes... how? 
one_b = one_a.insert(5 , 3)
print(one_a)

# coerced all elements in the list to floats using list comprehension 
one_c = [float(x) for x in one_a]
print(one_c)

# coerced the list in to a set using set()
one_d = set(one_c)
print(one_d)

# one_a.append(10) -> if we are appending the list, but the question says append the SET and there is no append in sets
#why does this give none instead of adding 10 to the set 
one_e = one_d.add(10) 
print(one_d)

# one_a.pop(1) -> if we are popping from list, but the question says pop an item from the list
one_f = one_d.pop() 
print(one_f)

# in the original set? because if I do this here, then it counts the length after the changes in one_b, one_e, and one_f have been made
one_g = len(one_a) 
print(one_g)

# Using == to check if length of the list is the same as the length of the set 
one_h = "The number of items in the set is the same as the number of items in the list" if len(one_a) == len(one_d) else "No the number of items in the set is not the same as the number of items in the list"
print(one_h)

# coerced the set to a list and added the original list using the + operator
one_i = list(one_d) + [0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9] 
print(one_i)

# when coerced to a set, the repeat values from one_i will not print, because sets do not allow duplicates
one_j = set(one_i) 
print(one_j)

# the number of elements in the list is same as the number of items since a list does not allow duplicates
one_k = len(one_j)
print(one_k)


# In[8]:


#Problem 2
print("Problem # 2")
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

#nested dictionary for the three provided dictionaries
two_a = {
    "two_patient_dictionary_kinoko" : two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango" : two_patient_dictionary_dango,
    "two_patient_dictionary_mochi" : two_patient_dictionary_mochi
}
print(two_a)

#retrieve dangos name from nested dictionary
two_b = two_patient_dictionary_dango['name']
print(two_b)

#update value of Mochis year to 2018 - two_c not used as variable as this should simply updated two_a
two_patient_dictionary_mochi['year'] = 2018
print(two_a)

#Single level dictionary where the key:value is patient:year , where Mochis year is now set to 2019
two_d = {
    "kinoko" : 2021,
    "dango" : 2019,
    "mochi" : 2019
}
print(two_d)

#coerce the keys, therefore the patients, into a list
two_e = list(two_d.keys())
print(two_e)
#Coerce the values, therefore the years, into a list
two_f = list(two_d.values())
print(two_f)
#Combine two_e and two_f back into a dictionary using the dict function and zip function
two_g = dict(zip(two_e , two_f))
print(two_g)


# In[10]:


#Problem 3
print("Problem # 3")
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

# E is a subset of A
three_a = print(three_setE.issubset(three_setA))

# E is a subset of A but does not equal A, and therefore a proper, or strict, subset of A
three_b = print(three_setE < three_setA)

# Set that is the intersection of set A and set B
three_c = print(three_setA.intersection(three_setB))

# Set that is union of sets C, D and E 
three_d = print(three_setC.union(three_setD, three_setE))

# Add 9 to the set
three_e = print(three_setC.union(three_setD, three_setE).add(9))

# Boolean - if this set equals the list in one_a
three_f = print(three_setC.union(three_setD, three_setE) == [0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9])

# three_f is false because a set cannot equal a list. This list has integer 0 at 0 index, therefore for three_f to be true, integer 0 must be removed from the list, and the list must be changed to a set.
one_a =  [0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
one_a_remove_0 = one_a.remove(0)
one_a_set = set(one_a)
three_g = print(three_setC.union(three_setD, three_setE) == one_a_set)


# In[3]:


# The variable is 8, for which the type is integer
four_a = 8

#Empty list
four_b = []

# Add the type int from four_a to the empty list in four_b
four_c = four_b.append(type(four_a))
print(four_b)

# Add .39 to four_c - print(four_c) gives none type, however print(four_b) gives expected answer, as the .append() change occurs to four_b
four_d = four_b.append(.39)
print(four_b)

# Append the type of the object .39 to this list
four_e = four_b.append(type(.39))
print(four_b)

# Exponentiate .39 to -10 power and round to no decimal places
four_f_exp = round(.39 ** (-10))
four_f = four_b.append(four_f_exp)
print(four_b)

# Append the type of the integer 12284 to the list appended in four_e
four_g = four_b.append(type(four_f_exp))
print(four_b)


# In[4]:


#Problem 5
print("Problem # 5")
# create a dictionary from four_g where key:value is index:corresponding object
five_a = {
    0 : "<class 'int'>" ,
    1 : 0.39 ,
    2 : "<class 'float'>" ,
    3 : 12284 ,
    4 : "<class 'int'>"
}
print(five_a)

# add 300 to the list from problem 4, coerced as a string
five_b = four_b.append("300")
print(four_b)

# append the type of the object "300" to the list
five_c = four_b.append(type("300"))
print(four_b)

# slice the string "300" up to the second element
five_d_str = "300"
print(five_d_str[0:2])

# append type from five_d in to list
five_e = four_b.append(type(30))
print(four_b)

# Convert string 30 in to new list of integers
five_f_list = '30'
five_f_split = [x for x in five_f_list]
five_f = [eval(x) for x in five_f_split]
print(five_f)

# append the type of five_f to the list
five_g = four_b.append(type(five_f))
print(four_b)

# append the type of three_setA to the list
three_setA = {1,2,3,4,5}
five_h = four_b.append(type(three_setA))
print(four_b)


# In[ ]:




