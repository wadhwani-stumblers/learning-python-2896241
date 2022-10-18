#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while(x < 5):
        print(x)
        x = x + 1

    print("---")
    # TODO: define a for loop
    for x in range(5, 10):
        print(x)

    print("---")
    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print(d)

    print("---")
    # TODO: use the break and continue statements
    for x in range(5, 10):
        if x % 2 == 0:
            continue
        print(x)

    print("---")
    # TODO: using the enumerate() function to get index 
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i,d in enumerate(days):
        print(i, d)

    print("---")    
  
if __name__ == "__main__":
    main()
