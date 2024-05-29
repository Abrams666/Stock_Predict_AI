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

#correct_weight
def correct_weight(weights):
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            weights[i][j]=(weights[i][j]-100)/100
    
    return weights

#train
print("start")
money=0
max_money=0
best=[]

day_arr=ar.arrangement(len(stock_price),4)
for i in range(len(day_arr)):
    for j in range(4):
        day_arr[i][j]=day_arr[i][j]+1
print("Days_Arrangment Done")

for i in range(len(day_arr)):
    price_weights=ar.arrangement(201,day_arr[i][0])
    price_quantity_weights=ar.arrangement(201,day_arr[i][1])
    keep_weights=ar.arrangement(201,day_arr[i][2])
    keep_quantity_weights=ar.arrangement(201,day_arr[i][3])

    price_weights=correct_weight(price_weights)
    price_quantity_weights=correct_weight(price_quantity_weights)
    keep_weights=correct_weight(keep_weights)
    keep_quantity_weights=correct_weight(keep_quantity_weights)

    print("Weights_Arrangment "+str(i)+" Done")

    for j in range(0,len(price_weights)):
        for k in range(0,len(price_quantity_weights)):
            for m in range(0,len(keep_weights)):
                for n in range(0,len(keep_quantity_weights)):
                    money=ts.transaction(price_weights[j],price_quantity_weights[k],keep_weights[m],keep_quantity_weights[n],stock_price,stock_quantity)
                    if (money>max_money):
                        max_money=money
                        best.append(i)
                        best.append(j)
                        best.append(k)
                        best.append(m)
                        best.append(n)

print(best)