import math
numbers=input().split(" ")
p=int(numbers[0])
a=int(numbers[1])
b=int(numbers[2])
c=int(numbers[3])
d=int(numbers[4])
n=int(numbers[5])

price_high=-1
price_low=-1
price_diff=0
price_high_diff=0
pre_price=1000000
for i in range(n):
    price=p*(math.sin(a*i+b)+math.cos(c*i+d)+2)
    if pre_price<price:
        continue
    else:
        pre_price=price
        if price>price_high:
            price_high=price
        else:
            price_low=price
        
        if price_high>=0 and price_low>=0:
            price_diff=float(price_high-price_low)
            if price_diff>price_high_diff:
                price_high_diff=price_diff
        print(f"price={price}, price_low={price_low}, price_high={price_high}, price_diff={price_diff}, price_high_diff={price_high_diff}.")
print('{:.9f}'.format(float(price_high_diff)))
        
    

