
def count_item_prices(items, prices):
    price_count = {}
    cnt=0
    for item in items:
        if item in price_count:
            cnt=cnt+1
            price_count[item]=[cnt,prices[items.index(item)]]
        else:
            price_count[item]=[1,prices[items.index(item)]]
    for key in price_count:
        price_count[key][1]= price_count[key][0]*price_count[key][1]
    return price_count



items = ["apple", "banana", "apple", "orange", "banana", "apple"]
prices = [5, 3, 5, 4, 3, 5]
print(count_item_prices(items, prices))