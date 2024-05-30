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
for i in range(2,42):
    stock_price.append(float(sheetx["D"+str(i)].value))
    stock_quantity.append(float(sheetx["G"+str(i)].value))

#correct_weight
def correct_weight(weights):
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            weights[i][j]=(weights[i][j]-1)/10
    
    return weights

#train
print("start")
money=0
max_money=0
best=[0,0,0,0]
x=0

day_arr=ar.arrangement(1,4) #len(stock_price)
for i in range(len(day_arr)):
    for j in range(4):
        day_arr[i][j]=day_arr[i][j]+3
print("Days_Arrangment Done")
print(day_arr)

for i in range(len(day_arr)):
    price_weights=ar.arrangement(3,day_arr[i][0])
    print("price_weights")
    price_quantity_weights=ar.arrangement(3,day_arr[i][1])
    print("price_quantity_weights")
    keep_weights=ar.arrangement(3,day_arr[i][2])
    print("keep_weights")
    keep_quantity_weights=ar.arrangement(3,day_arr[i][3])
    print("keep_quantity_weights")

    price_weights=correct_weight(price_weights)
    price_quantity_weights=correct_weight(price_quantity_weights)
    keep_weights=correct_weight(keep_weights)
    keep_quantity_weights=correct_weight(keep_quantity_weights)

    print("Weights_Arrangment "+str(i)+" Done")

    for j in range(0,len(price_weights)):
        print("j")
        for k in range(0,len(price_quantity_weights)):
            for m in range(0,len(keep_weights)):
                for n in range(0,len(keep_quantity_weights)):
                    money=ts.transaction(price_weights[j],price_quantity_weights[k],keep_weights[m],keep_quantity_weights[n],stock_price,stock_quantity)
                    if (money>max_money):
                        max_money=money
                        best[0]=j
                        best[1]=k
                        best[2]=m
                        best[3]=n
                    x=x+1
                    print(x)

print(price_weights[best[0]])
print(price_quantity_weights[best[1]])
print(keep_weights[best[2]])
print(keep_quantity_weights[best[3]])
print(max_money)