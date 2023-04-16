#Setting a list as the keys of the 2 dictionares below, will allow us to iterate through the dictionaries

menu = ["coffee", "tea", "croissant", "sandwich"]
stock = {"coffee": 150, "tea": 200, "croissant": 60, "sandwich": 40}
price = {"coffee": 2, "tea": 1.5, "croissant": 1.5, "sandwich": 3}

#The for loop takes the items in menu and uses them as keys to pull out the values, multiplying the matching values
#and summing them to get the total stock value.

stock_value = 0
for item in menu:
    item_value = stock.get(item)*price.get(item)
    stock_value += item_value

print(stock_value)