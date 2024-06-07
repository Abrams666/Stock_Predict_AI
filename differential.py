#imports
import transaction as ts

#differential
def differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,j):
    #find start day
    max_day=len(price_weight)
    if(max_day<len(quantity_weight)):
        max_day=len(quantity_weight)

    #count m
    m=0
    if(j<len(price_weight)):
        for i in range(max_day,len(best_situation)+1):
            m=m+stock_price[i+j-max_day]*(best_situation[i-1]-ts.transaction_val(price_weight,quantity_weight,stock_price,stock_quantity,b,i))
        m=m/(len(best_situation)+1-max_day)
    elif(j<len(price_weight)+len(quantity_weight)):
        for i in range(max_day,len(best_situation)+1):
            m=m+stock_quantity[i+j-max_day-max_day]*(best_situation[i-1]-ts.transaction_val(price_weight,quantity_weight,stock_price,stock_quantity,b,i))
        m=m/(len(best_situation)+1-max_day)
    else:
        for i in range(max_day,len(best_situation)+1):
            m=m+(best_situation[i-1]-ts.transaction_val(price_weight,quantity_weight,stock_price,stock_quantity,b,i))
        m=m/(len(best_situation)+1-max_day)
    return m