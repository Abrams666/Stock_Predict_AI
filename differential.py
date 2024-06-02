#imports
import cross_multiplication as cm
import array_plus as ap

#differential
def differential(best_situation,price_weight,quantity_weight,stock_price,stock_quantity,b,i):
    if(i<len(price_weight)):
        m=-2*price_weight[i]*(ap.array_plus(cm.cross_multiplication(price_weight,stock_price))+ap.array_plus(cm.cross_multiplication(quantity_weight,stock_quantity))+b-best_situation[i])
    else:
        m=-2*quantity_weight[i-len(price_weight)]*(ap.array_plus(cm.cross_multiplication(price_weight,stock_price))+ap.array_plus(cm.cross_multiplication(quantity_weight,stock_quantity))+b-best_situation[i])

    return m