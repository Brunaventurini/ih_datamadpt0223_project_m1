#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import pandas as pd

def get_info_by_address():
    while True:
        # Prompt the user to enter an address
        x = input("Please enter an address: ")
        
        # Load the dataset
        data = pd.read_csv('Closest_Bici_Mad.csv')

        # Find the row that matches the address
        row = data[data['Place Address'] == x]

        if row.empty:
            print('No information found for this address')
        else:
            # Get the information from a different column in the same row
            info = row['Station Location'].values[0]

            print("This is the closest BiciMad station near this Medical Center: " + info)
            
get_info_by_address()


# In[ ]:




