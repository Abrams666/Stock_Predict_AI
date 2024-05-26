#imports
import csv
import openpyxl

#build excel file
workbook = openpyxl.Workbook()
sheet = workbook.worksheets[0]
sheet["A1"]="編號"
sheet["B1"]="日期"
sheet["C1"]="開盤價"
sheet["D1"]="收盤價"
sheet["E1"]="最高價"
sheet["F1"]="最低價"
sheet["G1"]="成交量"
sheet["H1"]="價差"

#read csv file
counter=1

for yy in range(2010,2025):
    for mm in range(1,13):
        if((yy==2024) & (mm==6)):
            break
        if (len(str(mm))==1):
            m=str("0"+str(mm))
        else:
            m=str(mm)

        #read csv
        data_array = []

        csvfile=open('D:/Stock AI/Stock_Price_Data/scv/STOCK_DAY_2330_'+str(yy)+str(m)+'.csv')
        data = csv.reader(csvfile)
        next(data)

        for row in data:
            if len(row) < 2 or row[0] == "說明:":
                continue
            date = row[0].strip()
            values = [v.strip().replace(',', '') for v in row[1:]]
            data_array.append([date] + values)

        #write into excel
        for i in range(len(data_array)-1):
            sheet["A"+str(counter+1)]=str(counter)
            sheet["B"+str(counter+1)]=data_array[i+1][0]
            sheet["C"+str(counter+1)]=data_array[i+1][3]
            sheet["D"+str(counter+1)]=data_array[i+1][6]
            sheet["E"+str(counter+1)]=data_array[i+1][4]
            sheet["F"+str(counter+1)]=data_array[i+1][5]
            sheet["G"+str(counter+1)]=data_array[i+1][8]
            sheet["H"+str(counter+1)]=data_array[i+1][7]
            counter=counter+1

#save excel
workbook.save('Stock_tsmc.xlsx')
    