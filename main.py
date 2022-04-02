from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import collections
from collections import defaultdict
import csv


#item type: knife or rifle
class itemType(object):     #convert ItemType dictionary to class for calling items 
    
    def __init__(self, itemType_dict):
          
        for key in itemType_dict:
            setattr(self, key, itemType_dict[key])
            
#item version: if type was knife:           
class itemVers(object): #convert ItemVersion to classes for calling items
    
    def __init__(self, typeVarient_dict):
        
        for key in typeVarient_dict:
            setattr(self, key, typeVarient_dict[key])
            

def typeToDict(args):
    
    df_csv = pd.read_csv(args)
    dict_csv = df_csv.to_dict(orient='list')
    print(dict_csv)
    return dict_csv
    
class dataIn(): ## loads website resources. whhere do you want to scrap. adds these to an array. dict? (parameters) 
    
    def __init__(self,itemType='',itemSkintype ='',itemSkin = ''): #e.g : knife = new knife(knife,karambit, doppeler)
        self.itemType = itemType #knife and rifles for now. 
        self.itemSkinType = itemSkintype
        self.ItemSkin = itemSkin
        

def itemCheck(self):
    self.itemType
    self.itemSkintype 
    self.itemSkin 
       #try {} because they put something wrong in. 
        #if self.item_time == KEY.hey:
        #   find the element on the menu
        #click it 
        #exit loop
        #create another if statement 
        #catch(),continue,....
    return itemCheck(self);


if __name__ == "__main__":
      
    # Creating intial dictionary
     itemType_dict = {"knife":'CSGO_Knives.csv',"rifle": 'rifles_CSGO.csv'}     
     
     
type  = itemType(itemType_dict)
typeVarient_dict = typeToDict(type.knife) 
version = itemVers(typeVarient_dict)
print(version.Karambit) # if I print this I should get a list of all the key for karambit(Slaughter,Marble Fade, Autotronic)
#version.[index][] #would return karambit 





