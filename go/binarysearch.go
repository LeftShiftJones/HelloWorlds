package main

import "fmt"

func main() {
    lst := []int{3, 1, 2, 19, 6, 2, 3, 5, 8 ,9 ,24 ,23, 12, 54 ,76, 4}
    sort(lst)
    ok, place := binary_search(lst, 5)
    if ok {
        fmt.Println("Found 5 at index", place)
    } else {
        fmt.Println("5 not found in the list")
    }
}

func binary_search(lst []int, to_find int) (bool, int) {
    lo := 0
    hi := len(lst)
    med := lo + ((hi-lo) / 2)

    for lo < hi {
        if lst[med] == to_find {
            return true, med
        } else if lst[med] < to_find {
            lo = med+1
            med = lo + ((hi-lo) / 2)
        } else {
            hi = med-1
            med = lo + ((hi-lo) / 2)
        }
    }
    return false, -1
}

//basic insertion sort
func sort(lst []int) {
    for i := 0; i < len(lst); i++ {
        for j := i+1; j < len(lst); j++ {
            if lst[i] > lst[j] {
                temp := lst[i]
                lst[i] = lst[j]
                lst[j] = temp
            }
        }
    }
}
