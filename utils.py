import pickle 
import json 
import numpy as np 
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import config 

class ItemOutletSales():
    
    def __init__(self,Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
                 Item_MRP,Outlet_Identifier,Outlet_Establishment_Year,
                 Outlet_Size,Outlet_Location_Type,Outlet_Type):
        
        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_MRP = Item_MRP
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        
        self.Item_Type_col = 'Item_Type_' + Item_Type
        
        self.Outlet_Type_col = 'Outlet_Type_' + Outlet_Type
        
        self.Outlet_Identifier_col = 'Outlet_Identifier_' + Outlet_Identifier
         
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f:
            self.save_data = json.load(f)
            
            self.column_names = np.array(self.save_data['column_names'])
            
    def get_predicted_sales(self):
        
        self.load_models()
        
        Item_Type_col_index = np.where(self.column_names==self.Item_Type_col)[0]
        
        Outlet_Type_col_index = np.where(self.column_names==self.Outlet_Type_col)[0]
        
        Outlet_Identifier_col_index = np.where(self.column_names==self.Outlet_Identifier_col)[0]
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.Item_Weight
        array[1] = self.save_data['Item_Fat_Content'][Item_Fat_Content]
        array[2] = self.Item_Visibility
        array[3] = self.Item_MRP
        array[4] = self.Outlet_Establishment_Year
        array[5] = self.save_data['Outlet_Size'][Outlet_Size]
        array[6] = self.save_data['Outlet_Location_Type'][Outlet_Location_Type]

        array[Item_Type_col_index] == 1
        array[Outlet_Identifier_col_index] == 1
        array[Outlet_Type_col_index] == 1

        print('Array is :',array)
        
        sales = self.model.predict([array])[0]
        
        return sales            
        
if __name__ == '__main__':
    
    Item_Weight = 9.300000
    Item_Fat_Content = 'low fat'
    Item_Visibility = 0.016047
    Item_MRP = 249.809200
    Outlet_Establishment_Year = 1999.000000
    Outlet_Size = 'Medium'
    Outlet_Location_Type = 'Tier 1'

    Item_Type = 'Baking Goods'
  
    Outlet_Identifier = 'OUT010'

    Outlet_Type = 'Grocery Store'

    Items = ItemOutletSales(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
                 Item_MRP,Outlet_Identifier,Outlet_Establishment_Year,
                 Outlet_Size,Outlet_Location_Type,Outlet_Type)
    
    sales = Items.get_predicted_sales()
    
    print('Item Outlet Sales : $',round(sales,2))
                
        
        