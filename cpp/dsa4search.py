def binarySearch(sortedList : list, target: int) -> bool:
    if sortedList == []: return False
    current = sortedList[__import__("math").ceil((len(sortedList) -1)/2)]
    if current == target: return True
    return  binarySearch(sortedList[sortedList.index(current) + 1: len(sortedList)], target) if target>current else binarySearch(sortedList[:sortedList.index(current)], target)
    


print(binarySearch(list(range(4500)), 5000))
