# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:29:58 2021

@author: Arianna
"""
contents = []   
myfile = open('data.txt')
contents = myfile.read().splitlines() 


def partition(contents, i, k):
    pivot = contents[k]
    index = i - 1
    for j in range(i,k):
        if contents[j] <= pivot:
            index += 1
            contents[index], contents[j] = contents[j], contents[index]
    contents[index + 1], contents[k] = contents[k], contents[index + 1]
    return index + 1
    
def quicksort(contents, i, k):
    if i < k:
        piv = partition(contents, i, k)
        quicksort(contents, i, piv - 1)
        quicksort(contents, piv + 1, k)
        

    
quicksort(contents, 0, len(contents) - 1)


with open('sorted_data.txt', 'w+') as output_file:
    for thingy in contents:
        output_file.write(thingy + '\n')
output_file.close()

