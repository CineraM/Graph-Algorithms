import pandas as pd
import numpy as np
import sys
import csv
import json

class TitleDictionary:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.title_dict = self._create_title_dict()
        self.profession_dict = self._create_profession_dict()

    def _create_title_dict(self):
        title_dict = {}
        data = self.df.values.tolist()

        for entry in data:
            title = entry[2]
            if entry[1] in title_dict:
                title_dict[entry[1]].append(title)
            else:
                title_dict[entry[1]] = [title]

        # print(title_dict['nm6081065']) # debug
        return title_dict 

    def _create_profession_dict(self):
        profession_dict = {}
        data = self.df.values.tolist()

        for entry in data:
            if entry[1] not in profession_dict:
                profession = entry[3]
                if entry[4] == 'actor':
                    profession+='_a'
                else:
                    profession+='_d'

                profession_dict[entry[1]] = profession

        # print(profession_dict['nm6446679']) # debug
        return profession_dict

# td = TitleDictionary('imdb_network.csv')
# nconst_title = td.title_dict
# nconst_ar_dr = td.profession_dict

# print(nconst_title["nm8991003"])

with open("Graph_Output.json", "r") as file:
    data = json.load(file)

td = TitleDictionary('imdb_network.csv')
nconst_title = td.title_dict
nconst_ar_dr = td.profession_dict

total=0
f=0

def dictionary_test():
    global total
    global f

    test = data["dictionary_test"]
    for key in test:
        if nconst_title[key] != test[key]:
            print(key)
            print(nconst_title[key])
            print()
            print(test[key])
            
        
    if(data["dictionary_test"] == nconst_title):
        print("\n{nconst_title} Dictionary Test Passed")
    else:
        print("{nconst : title} mapping is Mismatched")
        f+=1
    total+=1

    return nconst_title

dictionary_test()
