import numpy as np

def quicksort(table, first, last, shift):
        if first < last:
                z = partition(table, first, last,shift)
                quicksort(table, first, z - 1,shift)
                quicksort(table, z + 1, last,shift)
        return table

def partition(table, first, last, shift):
        pivot = table[first][shift]
        i     = first + 1
        j     = last
        done  = False
        while not done:
                while i <= j and table[i][shift] <= pivot:
                        i += 1
                while j >= i  and table[j][shift] >= pivot:
                        j -= 1
                if j < i:
                        done = True
                else:
                        tmp      = table[j]
                        table[j] = table[i]
                        table[i] = tmp
        tmp          = table[first]
        table[first] = table[j]
        table[j]     = tmp
        return j
