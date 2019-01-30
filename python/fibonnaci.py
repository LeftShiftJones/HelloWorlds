def main():
    # We have to let the user do SOMETHING
    get_to = input("How many digits am I calculating to?: ")
    if get_to is '': # What to do if the user is lazy
        result = fibonacheese(0, 1, 0)
    else:
        result = fibonacheese(0, 1, 0, int(get_to))
    print(result)

"""
Fibonnaci sequence
"""
def fibonacheese(prev, next, iter, max=25):
    if iter == max:
        return next
    if prev == 0:
        prev = 1
        iter = iter + 1     # Increment
        return fibonacheese(prev, next, iter, max)
    else:
        temp = next
        next = next + prev  # Add
        prev = temp         # Increment
        iter = iter + 1     # Increment
        return fibonacheese(prev, next, iter, max)


main()
