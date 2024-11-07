from flask import Flask,render_template,request

from utils import ItemOutletSales

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Sales Prediction....')
    return render_template('index.html')

@app.route('/predict_sales',methods=['GET','POST'])
def get_info():
    
    if request.method == 'GET':
        
        print('In GET Method')
        
        data = request.form 
        
        Item_Weight = eval(data['Item_Weight'])
        Item_Fat_Content = data['Item_Fat_Content']
        Item_Visibility = eval(data['Item_Visibility'])
        Item_Type = data['Item_Type']
        Item_MRP = eval(data['Item_MRP'])
        Outlet_Identifier = data['Outlet_Identifier']
        Outlet_Establishment_Year = eval(data['Outlet_Establishment_Year'])
        Outlet_Size = data[Outlet_Size]
        Outlet_Location_Type = data[Outlet_Location_Type]
        Outlet_Type = data[Outlet_Type]
        
        Items = ItemOutletSales(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
                 Item_MRP,Outlet_Identifier,Outlet_Establishment_Year,
                 Outlet_Size,Outlet_Location_Type,Outlet_Type)
        
        sales = Items.get_predicted_sales()
        
        return f'Item Outlet Sales $ {round(sales,2)} /-'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    app.run()