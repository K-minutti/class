#Code for PSET 0
import numpy 

#Ask user for input x
#Ask user for input y
#Print out X raised to the power Y
#Print out the log (base2) of x


def main():
    x = input("Enter a value for x: ")
    print(x)
    y = input("Enter a vlue for y: ") 
    print(y)
    n = int(x)**int(y)
    print("X**y =", n)
    s = numpy.log2(int(x))
    print("log(x)", int(s))

main()
