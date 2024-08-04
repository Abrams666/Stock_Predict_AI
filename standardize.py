def standardize(data):
    #average
    total = 0
    for i in range(len(data)):
        total = total + data[i]
    ave = total / len(data)

    #standard deviation
    total=0
    for i in range(len(data)):
        total = total + (data[i] - ave) ** 2
    std_dev = (total / len(data)) ** 0.5

    #standardized data
    for i in range(len(data)):
        data[i] = (data[i] - ave) / std_dev

    return data