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

price_weight=[-395.24860000082083, -389.3612499671293, -408.149514771276, -413.47552850685827, -425.492398092109, -585.439176341749]
quantity_weight=[4.498565980283323, 997.3138441261373, -937.6146582540888, -857.2151538645369, 351.05007088425305, 596.029181862752]
b=-100.90429650002667

print(ts.transaction(price_weight,quantity_weight,stock_price,stock_quantity,b))