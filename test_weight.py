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

price_weight=[2081.6989410698675, 2088.0609506733094, 2094.188376731748, 2099.7669432687585, 2107.3502935561987, 2111.0980932766324]
quantity_weight=[121448.68696594796, 130258.02920147413, 146575.07220020893, 135287.0114978831, 125123.21140756858, 136782.2214675607]
b=-96.65041586582784

print(ts.transaction(price_weight,quantity_weight,stock_price,stock_quantity,b))