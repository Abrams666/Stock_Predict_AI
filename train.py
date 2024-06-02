#imports
import arrangement as ar
import differential as df
import transaction as ts
import openpyxl

#load stock data
file_path = "D:/Stock AI/Stock_Price_Data/Stock_tsmc.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheetx = workbook.active

stock_price=[]
stock_quantity=[]
for i in range(2,len(sheetx["A"])+1):
    stock_price.append(float(sheetx["D"+str(i)].value))
    stock_quantity.append(float(sheetx["G"+str(i)].value))

#load best_situation data
file_path = "D:/Stock AI/Stock_Price_Data/best_tsmc_situation.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheetx = workbook.active

best_situation=[]
for i in range(2,len(sheetx["A"])+1):
    best_situation.append(float(sheetx["B"+str(i)].value))

#day arrangement
day_arr=ar.arrangement(len(stock_price),2)
for i in range(len(day_arr)):
    for j in range(4):
        day_arr[i][j]=day_arr[i][j]+1

#gradient decent
learn_rate=0.000001
max_money=0
best_price_weight=[]
best_quantity_weight=[]

for i in range(len(day_arr)):
    #init weight
    price_weight=[]
    quantity_weight=[]
    b=-100

    for j in range(day_arr[i][0]):
        price_weight.append(-0.01)

    for j in range(day_arr[i][1]):
        price_weight.append(-0.01)

    while(1):
        m_is_0=1
        for j in range(len(day_arr[i][0])+len(day_arr[i][1])):
            if(j<len(price_weight)):
                if (df.differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,j)<0.1 or df.differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,j)>0.1):
                    continue
                else:
                    price_weight[j]=price_weight[j]-learn_rate*(df.differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,j))
                    m_is_0=0
            else:
                if (df.differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,j)<0.1 or df.differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,j)>0.1):
                    continue
                else:
                    quantity_weight[j-len(day_arr[i][0])]=quantity_weight[j-len(day_arr[i][0])]-learn_rate*(df.differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,j))
                    m_is_0=0
        
        if(m_is_0==1):
            break

    money=ts.transaction(price_weight,quantity_weight,stock_price,stock_quantity)

    if(money>max_money):
        max_money=money
        best_price_weight=price_weight
        best_quantity_weight=quantity_weight

#result
print(best_price_weight)
print(best_quantity_weight)