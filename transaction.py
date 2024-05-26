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

buy=[1,1,1]
buy_quantity=[1,1,1]
print(transaction_val(buy,buy_quantity,3))