# bounce.py
height = 100
bounces = 10
attempt = 1

for i in range(bounces):
    height = (height / 5) * 3
    print(attempt, round(height, ndigits=4))
    attempt = attempt + 1