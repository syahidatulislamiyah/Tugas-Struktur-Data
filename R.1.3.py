def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return (smallest, largest)


print(minmax([0,12,34,6,14,72,86,82,-4,50,5,-5,29,1,-1,-10]))
