#imports
import transaction as ts

#cost function
def cost_function(best_situation,buy_weight,buy_quantity_weight,keep_weight,keep_quantity_weight,stock_price,stock_quantity):
    #zero
    cost = 0

    #find first day
    max_day=len(buy_weight)
    if(max_day<len(buy_quantity_weight)):
        max_day=len(buy_quantity_weight)
    if(max_day<len(keep_weight)):
        max_day=len(keep_weight)
    if(max_day<len(keep_quantity_weight)):
        max_day=len(keep_quantity_weight)

    #count cost
    for i in range(max_day,len(stock_price)+1):
        cost=cost+(int(ts.transaction_val(buy_weight,buy_quantity_weight,stock_price,stock_quantity,i))-best_situation[i-1])**2

    return int(cost)