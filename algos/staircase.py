# stair case 👀

def staircase(n):
    # Write your code here
    for i in range(n):
        spaceAmt = (n-(i+1))
        hashAmt = (i+1)
        print((" " * spaceAmt) + ("#" * hashAmt))


staircase(9)
