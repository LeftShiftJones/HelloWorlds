def main():
    num_one = int(input("Please enter a number: "))
    print()
    num_two = int(input("Please enter another number: "))
    print()
    one_factors = find_factors(num_one)
    two_factors = find_factors(num_two)
    print(one_factors)
    print(two_factors)

def find_factors(num):
    factors = [] #Num is a factor of itself, could be a factor of another number?
    while(num > 1):
        if num % 2 == 0: #Check even case
            factors.append(2)
            num = num / 2
        else:
            f = 3
            while(True):
                if num % f == 0:
                    factors.append(f)
                    num = num / f
                    break
    #implicit add of 1?
    return factors

main()
