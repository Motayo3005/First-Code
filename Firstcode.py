# Age=20
# print(Age,5,20,15)

# product1 = "Macbook"
# product2 = "Envy"
# manufacturer1 = "Apple"
# manufacturer2 = "HP"
# beginning = "I know that"
# middle = "is made by"
# next_mid = "while"

# print(beginning, product1, middle, manufacturer1, next_mid, product2, middle, manufacturer2)

product = "apples"
qty = 3
unit_cost = 300
total_cost = qty*unit_cost

statement = "Hi Customer, you bought " + str(qty) + " nos of " + product + " at NGN" + str(unit_cost) + ", which makes a total of NGN" + str(total_cost)

print(statement)

a = input ("a : ")
b = input ("b : ")
#convert variables to integer
a = int(a)
b = int(b)

c = (a**2 + b**2)**0.5

print(c)

statement = f"If a = {a} and b = {b}, then c will be {c}"
print(statement)






