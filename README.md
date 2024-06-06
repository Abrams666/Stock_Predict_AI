English
#stockorderAI
>Use the stock's closing price and trading volume on several days to predict the amount suitable for buying and selling on a certain day.

#Introduction to functions and programs
>arrangement(integer A, integer B)
-Generate all permutations and combinations that have B items in total and each item has A possible values
-Output: a two-dimensional array
-EX:
    arrangement(3,2)
    =>[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1] ,[2,2]]

>cross_multiplication(one-dimensional array A, one-dimensional array B)
-Multiply each item of the two arrays
-Output: a one-dimensional array
-EX:
    a=[1,2,3]
    b=[4,5,6]
    cross_multiplication(a,b)
    =>[4,10,18]

>array_plus(one-dimensional array A)
-Add each item of the array
-Output: a floating point number or integer (determined by the input array)
-EX:
    a=[1,2,3]
    array_plus(a)
    =>6

>transaction_val (a microarray (stock price weight) A, a microarray (stock volume weight) B, a microarray (stock daily price) C, a microarray (stock daily trading volume) D, floating point number ( Constants in functions)E, integers (Fth day)F)
-Calculate the recommended buying and selling volume on day F under this weight (positive means buying volume, negative means selling volume)
-Output: a floating point number

>transaction(a microarray (stock price weight) A, a microarray (stock volume weight) B, a microarray (stock daily price) C, a microarray (stock daily trading volume) D, floating point number ( Constants in functions)E)
-Calculate the money that can be earned during the entire transaction period under this weight (initially 1,000 dollors)
-Output: a floating point number

>differential (a microarray (daily best trading volume) F, a microarray (stock price weight) A, a microarray (stock volume weight) B, a microarray (stock daily price) C, a microarray Array (daily trading volume of stocks) D, floating point number (constant in function) E, G+1th weight G)
-Calculate the slope (multiplied by -1) of the G+1th weight direction of its cost_function (loss function) during the entire transaction period under this weight
-Output: a floating point number

>get_stock_price.py
-Use a crawler to download the monthly stock price csv file from "https://www.twse.com.tw/zh/trading/historical/stock-day.html"

>data_combine.py
-Organize and convert csv files into excel files

>best_situation.py
-Calculate the situation in which a certain stock can make the most money (buy at the low point, sell at the highest point) since its listing (with records), and record the best results in excel

>cost_function.py
-Calculate the error between a set of weights and the best solution
-Not referenced in other programs

>★train.py
-Training weights, first calculate the permutations and combinations of all weight days, and then continuously correct the weights (original weight - (cost_function slope of the weight direction * learning rate 0.0000000001)) until the error is between -0.1 and 0.1, select all combinations of days The one with the largest final income, and its weight is displayed

中文
#股票下單AI
>利用股票錢幾日的收盤價、成交量來預測某日適合買進、賣出的數量

#函式、程式介紹
>arrangement(整數A,整數B)
-生成所有在總共有B項，每項有A種可能數值的所有排列組合
-輸出:一個二維陣列
-EX:
    arrangement(3,2) 
    =>[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

>cross_multiplication(一維陣列A,一維陣列B)
-將兩陣列的每一項各自相乘
-輸出:一個一維陣列
-EX:
    a=[1,2,3] 
    b=[4,5,6]
    cross_multiplication(a,b)
    =>[4,10,18]

 >array_plus(一維陣列A)
 -將陣列的每一項相加
 -輸出:一個浮點數或整數(由輸入的陣列決定)
 -EX:
    a=[1,2,3]
    array_plus(a)
    =>6

>transaction_val(一微陣列(股票價格權重)A,一微陣列(股票成交量權重)B,一微陣列(股票每日價格)C,一微陣列(股票每日成交量)D,浮點數(函式中的常數)E,整數(第F天)F)
-計算該權重下，第F天推薦買賣量(正為買量、負為賣量)
-輸出:一個浮點數

>transaction(一微陣列(股票價格權重)A,一微陣列(股票成交量權重)B,一微陣列(股票每日價格)C,一微陣列(股票每日成交量)D,浮點數(函式中的常數)E)
-計算該權重下，整個交易期間，能賺到的錢(初始為1000元)
-輸出:一個浮點數

>differential(一微陣列(每日買賣最佳量)F,一微陣列(股票價格權重)A,一微陣列(股票成交量權重)B,一微陣列(股票每日價格)C,一微陣列(股票每日成交量)D,浮點數(函式中的常數)E,第G+1個權重G)
-計算該權重下，整個交易期間，對其cost_function(損失函數)的第G+1個權重方向的斜率(乘-1)
-輸出:一個浮點數

>get_stock_price.py
-利用爬蟲從"https://www.twse.com.tw/zh/trading/historical/stock-day.html" 下載每月股價csv檔

>data_combine.py
-將csv檔整理並轉換為excel檔

>best_situation.py
-計算出自上市(有紀錄)以來，某一股能賺到最多錢的情況(買在低點、賣在最高點)，並將最佳結果記錄在excel

>cost_function.py
-計算一組權重與最佳清況的誤差
-其他程式中未引用

>★train.py
-訓練權重，先計算所有權重天數的排列組合，後將權重不斷修正(原權重-(cost_function該權重方向的斜率*學習率0.0000000001))直到誤差在-0.1到0.1之間，選出所有天數組合中最終所得最大者，並顯示其權重

#Copyright Notice 版權聲明 
This work is licensed under Creative Commons Attribution-NonCommercial 4.0 International.
To view a copy of this license, visit https://creativecommons.org/licenses/by-nc/4.0/
Copyright © 2024 陳元謙(Abrams666) All Rights Reserved