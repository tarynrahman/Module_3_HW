#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[ ]:




