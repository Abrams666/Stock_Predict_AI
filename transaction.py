def transaction_val(buy_weight,buy_quantity_weight,stock_price,stock_quantity,day):
    #imports
    import cross_multiplication as cm
    import array_plus as ap

    price_data=[]
    for i in range(day-len(buy_weight)+1,day+1):
        price_data.append(float(stock_price[i-1]))

    quantity_data=[]
    for i in range(day-len(buy_quantity_weight)+1,day+1):
        quantity_data.append(float(stock_quantity[i-1]))
    
    #count
    value=ap.array_plus(cm.cross_multiplication(price_data,buy_weight))+ap.array_plus(cm.cross_multiplication(quantity_data,buy_quantity_weight))

    return value

def transaction(buy_weight,buy_quantity_weight,keep_weight,keep_quantity_weight,stock_price,stock_quantity):
    #ZeroMoney
    money=1000
    stock=0

    #find start day
    max_day=len(buy_weight)
    if(max_day<len(buy_quantity_weight)):
        max_day=len(buy_quantity_weight)
    if(max_day<len(keep_weight)):
        max_day=len(keep_weight)
    if(max_day<len(keep_quantity_weight)):
        max_day=len(keep_quantity_weight)

    #get three value
    for i in range(2500,len(stock_price)+1): #max_day
        buy_value=transaction_val(buy_weight,buy_quantity_weight,stock_price,stock_quantity,i)
        keep_value=transaction_val(keep_weight,keep_quantity_weight,stock_price,stock_quantity,i)

        #transact
        x=buy_value
        if(x<0):
            x=-x
        
        if(x>keep_value):
            buy_num=int(buy_value)
            if(money-buy_num*stock_price[i-1]<0):
                buy_num=money//stock_price[i-1]
            if(stock+buy_num<0):
                buy_num=-stock
            stock=stock+buy_num
            money=money-buy_num*stock_price[i-1]
        elif(keep_value>=buy_value):
            continue

    #end count
    money=money+stock*float(len(stock_price)-1)
    print(money)
    return money

#import openpyxl

# file_path = "D:/Stock AI/Stock_Price_Data/Stock_tsmc.xlsx"
# workbook = openpyxl.load_workbook(file_path)
# sheetx = workbook.active

# stock_price=[]
# stock_quantity=[]
# for i in range(2,3534):
#     stock_price.append(float(sheetx["D"+str(i)].value))
#     stock_quantity.append(float(sheetx["G"+str(i)].value))

# buy_weight=[-1,0,1]
# buy_quantity_weight=[-1,0,1]
# keep_weight=[0.5,0,-0.5]
# keep_quantity_weight=[0.5,0,-0.5]

# print(transaction(buy_weight,buy_quantity_weight,keep_weight,keep_quantity_weight,stock_price,stock_quantity))