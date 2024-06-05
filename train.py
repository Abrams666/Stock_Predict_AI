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
# day_arr=ar.arrangement(len(stock_price),2)
# for i in range(len(day_arr)):
#     for j in range(2):
#         day_arr[i][j]=day_arr[i][j]+1

day_arr=[[6,6]]

#gradient decent
learn_rate=0.000000002
max_money=0
money=0
best_price_weight=[]
best_quantity_weight=[]

for i in range(len(day_arr)):
    #init weight
    price_weight=[]
    quantity_weight=[]
    b=-100
    new_price_weight=[]
    new_quantity_weight=[]
    new_b=-100

    for j in range(day_arr[i][0]):
        price_weight.append(-0.01)
        new_price_weight.append(-0.01)

    for j in range(day_arr[i][1]):
        quantity_weight.append(-0.01)
        new_quantity_weight.append(-0.01)

    x=0
    ms=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    while(x<200):
        x=x+1
        m_is_0=1
        print(str(x)+"\/")
        print(ms)
        print(price_weight)
        print(quantity_weight)
        print(b)
        print(money)
        for j in range(day_arr[i][0]+day_arr[i][1]+1):
            m=df.differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,j)
            ms[j]=m
            if(j<len(price_weight)):
                if (m<0.1 and m>-0.1):
                    print("countinue")
                    continue
                else:
                    new_price_weight[j]=price_weight[j]-learn_rate*(m)
                    m_is_0=0
            elif(j<len(price_weight)+len(quantity_weight)):
                if (m<0.1 and m>-0.1):
                    continue
                else:
                    new_quantity_weight[j-day_arr[i][0]]=quantity_weight[j-day_arr[i][0]]-learn_rate*(m)
                    m_is_0=0
            else:
                if (m<0.1 and m>-0.1):
                    continue
                else:
                    new_b=b-learn_rate*(m)
                    m_is_0=0

        price_weight=new_price_weight
        quantity_weight=new_quantity_weight
        b=new_b

        if(m_is_0==1):
            break

        money=ts.transaction(price_weight,quantity_weight,stock_price,stock_quantity,b)

        if(money>max_money and x>5):
            max_money=money
            best_price_weight=price_weight
            best_quantity_weight=quantity_weight
            best_x=x+1

#result
print("*****************")
print(best_price_weight)
print(best_quantity_weight)
print(max_money)
print(best_x)