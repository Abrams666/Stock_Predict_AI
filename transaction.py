def transaction_val(buy_weight,buy_quantity_weight,day):
    #imports
    import cross_multiplication as cm
    import array_plus as ap
    import openpyxl

    #read excel price and quantity
    file_path = "D:/Stock AI/Stock_Price_Data/Stock_tsmc.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    price_row_data = []
    quantity_row_data = []
    for i in range(2, 3533):
        price_row_data.append(float(sheet["D"+str(i)].value))
        quantity_row_data.append(float(sheet["G"+str(i)].value))

    price_data=[]
    for i in range(day-len(buy_weight),day):
        price_data.append(float(price_row_data[i]))

    quantity_data=[]
    for i in range(day-len(buy_quantity_weight),day):
        quantity_data.append(float(quantity_row_data[i]))
    
    #count
    value=ap.array_plus(cm.cross_multiplication(price_data,buy_weight))+ap.array_plus(cm.cross_multiplication(quantity_data,buy_quantity_weight))

    return value

def transaction(buy_weight,buy_quantity_weight,keep_weight,keep_quantity_weight,sell_weight,sell_quantity_weight):
    #imports
    import openpyxl

    #read excel price and quantity
    file_path = "D:/Stock AI/Stock_Price_Data/Stock_tsmc.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    #ZeroMoney
    money=0
    stock=0

    #find start day
    max_day=len(buy_weight)
    if(max_day<len(buy_quantity_weight)):
        max_day=len(buy_quantity_weight)
    if(max_day<len(keep_weight)):
        max_day=len(keep_weight)
    if(max_day<len(keep_quantity_weight)):
        max_day=len(keep_quantity_weight)
    if(max_day<len(sell_weight)):
        max_day=len(sell_weight)
    if(max_day<len(sell_quantity_weight)):
        max_day=len(sell_quantity_weight)

    #get three value
    for i in range(max_day,31): #2533
        buy_value=transaction_val(buy_weight,buy_quantity_weight,i)
        keep_value=transaction_val(keep_weight,keep_quantity_weight,i)
        sell_value=transaction_val(sell_weight,sell_quantity_weight,i)

        #choose
        if(buy_value>keep_value and buy_value>sell_value):
            buy_num=int(buy_value)
            stock=stock+buy_num
            money=money-(buy_num*float(sheet["D"+str(i+1)].value)*1000)
            print("Day"+str(i)+" Buy"+str(buy_num))
        
        elif(keep_value>buy_value and keep_value>sell_value):
            print("Day"+str(i)+" Keep")

        elif(sell_value>buy_value and sell_value>keep_value):
            sell_num=int(sell_value)
            if((stock-sell_num)>=0):
                stock=stock-sell_num
                money=money+(sell_num*float(sheet["D"+str(i+1)].value)*1000)
            else:
                money=money+(stock*float(sheet["D"+str(i+1)].value)*1000)
                stock=0
            print("Day"+str(i)+" Sell"+str(sell_num))
        print(" Money:"+str(money))
    #end count
    money=money+(stock*867000)
    return money/stock

buy_weight=[1,2,3]
buy_quantity_weight=[1,2,3]
keep_weight=[2,2,2]
keep_quantity_weight=[2,2,2]
sell_weight=[3,2,1]
sell_quantity_weight=[3,2,1]
print(transaction(buy_weight,buy_quantity_weight,keep_weight,keep_quantity_weight,sell_weight,sell_quantity_weight))