number_of_books=int(input())
list_of_prices=[]
final_price=0
for i in range(number_of_books):
    book_price=int(input())
    list_of_prices.append(book_price)
list_of_prices.sort(reverse=True)
for books in list_of_prices:
    final_price+=books
for j in range(0, len(list_of_prices), 2):
    if j==0:
        continue
    elif j==2:
        final_price-=list_of_prices[j]
    else:
        final_price-=list_of_prices[j+1]
print(final_price)