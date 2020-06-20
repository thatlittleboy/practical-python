# bounce.py
#
# Exercise 1.5
def bounce_height(initial_height, num_bounces):
    height = initial_height
    for i in range(1, num_bounces + 1):
        height = height * 0.6
        print(f"{i} {round(height, 4)}")


if __name__ == "__main__":
    bounce_height(100, num_bounces=10)
