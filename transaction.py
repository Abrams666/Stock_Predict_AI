def transaction_val(buy_weight,buy_quantity_weight,stock_price,stock_quantity,b,day):
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
    value=ap.array_plus(cm.cross_multiplication(price_data,buy_weight))+ap.array_plus(cm.cross_multiplication(quantity_data,buy_quantity_weight))+b

    return value

def transaction(buy_weight,buy_quantity_weight,stock_price,stock_quantity,b):
    #ZeroMoney
    money=1000
    stock=0

    #find start day
    max_day=len(buy_weight)
    if(max_day<len(buy_quantity_weight)):
        max_day=len(buy_quantity_weight)

    #get three value
    for i in range(max_day,len(stock_price)+1): #max_day
        buy_value=transaction_val(buy_weight,buy_quantity_weight,stock_price,stock_quantity,b,i)

        #transact
        x=buy_value
        if(x<0):
            x=-x
        
        buy_num=int(buy_value)
        if(money-buy_num*stock_price[i-1]<0):
            buy_num=money//stock_price[i-1]
        if(stock+buy_num<0):
            buy_num=-stock
        stock=stock+buy_num
        money=money-buy_num*stock_price[i-1]

    #end count
    money=money+stock*float(len(stock_price)-1)
    return money