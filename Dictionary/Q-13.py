__author__ = "ResearchInMotion"

# Write a Python program to sort a dictionary by key.

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}


for keys in sorted(color_dict):
    print(keys ,":",color_dict[keys])