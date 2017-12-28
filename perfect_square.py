from main import perfect_square

num = int(input("What is your number? "))

if num > 0:
    ans = perfect_square(num)
else:
    ans = "Sorry that's an invalid entry"

ans = perfect_square(num)

print(ans)