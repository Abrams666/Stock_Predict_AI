#imports
import openpyxl
import transaction as ts

#load stock data
file_path = "D:/Stock AI/Stock_Price_Data/Stock_tsmc.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheetx = workbook.active

stock_price=[]
stock_quantity=[]
for i in range(2,len(sheetx["A"])+1):
    stock_price.append(float(sheetx["D"+str(i)].value))
    stock_quantity.append(float(sheetx["G"+str(i)].value))

price_weight=[-16.85990091388484, -16.415299665696725, -23.685951836955052, -20.7329435499406, -33.186925446937714, -159.8679782781999]
quantity_weight=[0.5879707547731239, 0.4051787829459283, 0.38460316746423057, 0.3892579119618806, 0.4056297342908596, 0.6042782777697913]
b=-99.99739596677014

print(ts.transaction(price_weight,quantity_weight,stock_price,stock_quantity,b))