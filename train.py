#imports
import transaction as ts
import arrangement as ar
import openpyxl

#load excel data
file_path = "D:/Stock AI/Stock_Price_Data/Stock_tsmc.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheetx = workbook.active

stock_price=[]
stock_quantity=[]
for i in range(2,3534):
    stock_price.append(float(sheetx["D"+str(i)].value))
    stock_quantity.append(float(sheetx["G"+str(i)].value))

#train
max_money=0
best=[]
for i in range(1,3533):
    arr=ar.arrangement(201,i)
    for j in range(1,201**i+1):
        for k in range(1,201**i+1):
            for n in range(1,201**i+1):
                for m in range(1,201**i+1):
                    money=ts.transaction(arr[j],arr[k],arr[n],arr[m],stock_price,stock_quantity)
                    if (money>max_money):
                        max_money=money
                        best.append(arr[j])
                        best.append(arr[k])
                        best.append(arr[n])
                        best.append(arr[m])
                    