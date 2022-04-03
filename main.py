from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import collections

#item type: knife or rifle
class itemType(object):    
    
    def __init__(self, itemType_dict):
          
        for key in itemType_dict:
            setattr(self, key, itemType_dict[key])
            
 
class itemVers(object): 
    
    def __init__(self, typeVariant_dict):
        
        for key in typeVariant_dict:
            setattr(self, key, typeVariant_dict[key])
            
def typeToDict(args):
    
    df_csv = pd.read_csv(args)
    dict_csv = df_csv.to_dict(orient='list')
    print(dict_csv) #testing purposes 
    return dict_csv
    
class itemGen(): 

    def __init__(self, itemType, itemSkintype, itemSkin): #e.g : knife = new knife(Knife,Karambit, Doppler)
        self.itemType = itemType #knife and rifles for now.         print(knife.itemtype)  = karambit
        self.itemSkintype = itemSkintype
        self.ItemSkin = itemSkin
        #get instance attributes from user 
    itemType = input("Enter the item type(Knife): ")
    itemSkintype = input("Enter the variation of that Item(e.g Karambit or Bayonet): ")
    inteSkin = input("Enter the skin(e.g Dopper): ")
    

if __name__ == "__main__":
      
    #Initial(super) dictionary 
     itemType_dict = {"knife":'CSGO_Knives.csv',"rifle": 'rifles_CSGO.csv'}     
     
type  = itemType(itemType_dict)
typeVariant_dict = typeToDict(type.knife) 
version = itemVers(typeVariant_dict)
print(version.Karambit) #test










