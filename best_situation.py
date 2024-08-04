#imports
import openpyxl

#read excel
file_path = "D:/Stock AI/Stock_Price_Data/Stock_bitcoin.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active
prices=[]
for i in range(2,len(sheet["A"])+1):
    prices.append(float(sheet["D"+str(i)].value))

#start new excel
workbook = openpyxl.Workbook()
sheetx = workbook.worksheets[0]
sheetx["A1"]="編號"
sheetx["B1"]="買賣量"
sheetx["C1"]="價格"
sheetx["D1"]="目前餘額"
sheetx["E1"]="買或賣"

#zero money
money=1000
stock=0
buy=0
situation=-1

#transaction
sheetx["A2"]=1
sheetx["B2"]=stock
sheetx["C2"]=prices[0]
sheetx["D2"]=money
sheetx["E2"]=0

for i in range(1,len(prices)-1):
    buy=0
    bs=0
    if(situation==1):
        #sell
        if(((prices[i-1]<=prices[i])and(prices[i]>prices[i+1]))):
            buy=-(stock)
            situation=-1
            bs=-1
    elif(situation==-1):
        #buy
        if(((prices[i-1]>=prices[i])and(prices[i]<prices[i+1]))):
            buy=(money//prices[i])
            situation=1
            bs=1

    stock=stock+buy
    money=money-(buy*prices[i])
    sheetx["A"+str(i+2)]=i+1
    sheetx["B"+str(i+2)]=buy
    sheetx["C"+str(i+2)]=prices[i]
    sheetx["D"+str(i+2)]=money
    sheetx["E"+str(i+2)]=bs

sheetx["A"+str(len(prices)+1)]=len(prices)
sheetx["B"+str(len(prices)+1)]=stock
sheetx["C"+str(len(prices)+1)]=prices[len(prices)-2]
sheetx["D"+str(len(prices)+1)]=money+(stock*prices[len(prices)-2])
sheetx["E"+str(len(prices)+1)]=0

#save excel
workbook.save('best_bitcoin_situation.xlsx')