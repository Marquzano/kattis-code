# takes the number of periods
# receives two numbers per period score and number of years 
# outputs the sum of those pairs products

# holds the amount of periods
periods = int(input())

# will hold the total
total = 0.0

products = []

for n in range(periods):
    score , years = input().split(' ')
    score = float(score)
    years = float(years)
    qaly = score * years
    products.append(qaly)

print(sum(products))