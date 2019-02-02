package main

import "fmt"

func main() {
    fmt.Print("Enter a number: ")
    var i int
    fmt.Scanf("%d", &i) //assign inputted variable to input
    f := fibonnaci(0, 1, 0, i)
    fmt.Print("\n", f, "\n")
}

func fibonnaci(prev int, next int, iter int, max int) (int) {
    fmt.Print(prev, " ")
    if iter == max {
        return prev
    }
    // implicit else
    temp := prev
    prev = next
    next += temp
    iter++
    return fibonnaci(prev, next, iter, max)
}
