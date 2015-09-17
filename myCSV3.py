import csv

with open('C:/Python34/myPy/myData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    prices = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        price = row[4]
        dates.append(date)
        colors.append(color)
        prices.append(price)

    print(dates)
    print(colors)

    # now, remember our lists?

    whatColor = input('What color do you wish to know the date of?:')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of',whatColor,'is:',theDate)
    
#   print the price of the Yellow shirt
    whatColorPrice = input('What color do you wish to know the price of?: ')
    coldexPrice = colors.index(whatColorPrice)
    thePrice = prices[coldexPrice]
    print('The price of',whatColorPrice,'is:',thePrice)
