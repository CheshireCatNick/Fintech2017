import pandas

def calcPrice(r, lr):
	return r['Open'] + lr['Adj Close'] - lr['Close']

def myStrategy(pastData):
	# 1 for buy, -1 for sell, 0 for no action
	consecPriceNum = 5
	print(pastData.shape[0])
	if (pastData.shape[0] < consecPriceNum + 1):
		return 0

	rows = []
	pastData = pastData.tail(consecPriceNum + 1)
	for index, row in pastData.iterrows():
		rows.append(row)

	prices = []
	for i in range(1, len(rows)):
		prices.append(calcPrice(rows[i], rows[i - 1]))
	
	# check if the last consecPriceNum is falling or growing
	isGrowing = True
	for i in range(consecPriceNum - 1):
		if (prices[i] > prices[i + 1]):
			isGrowing = False
			break

	isFalling = True
	for i in range(consecPriceNum - 1):
		if (prices[i] < prices[i + 1]):
			isFalling = False
			break

	if (isGrowing):
		return 1
	elif (isFalling):
		return -1
	else: 
		return 0

# main
pastData = pandas.read_csv('SPY.csv')
dayNum = pastData.shape[0]
print(pastData)

state = 'allOut'
assets = 1000
stock = 0

for day in range(2, dayNum):
	#print(pastData.head(day))
	data = pastData.head(day)
	priceD = data.tail(2)
	rows = []
	for index, row in priceD.iterrows():
		rows.append(row)
	price = calcPrice(rows[1], rows[0])

	action = myStrategy(data)
	
	if (action == 1 and state == 'allOut'):
		# all in
		state = 'allIn'
		stock += assets / price
		assets = 0
	elif (action == -1 and state == 'allIn'):
		# all out
		state = 'allOut'
		assets += stock * price
		stock = 0
	print(day, stock, assets, price, stock * price + assets)


