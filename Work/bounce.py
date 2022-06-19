# bounce.py

height = 100
bounce = 1

print("Bouncing the ball from a height of", height, "metres.")

while bounce <= 10:
    height = height * (3/5)
    print("Bounce number", bounce, round(height, ndigits=4), "metres.")
    bounce = bounce + 1