#search a value in a sorted list using recursive function:

def recursive_search(list_, target):
    if len(list_)== 0:
        return False
    elif len(list_) ==  1 and list_[0] != target:
        return False
    else:
        mid = len(list_)//2
        if list_[mid] == target:
            return True
        else:
            if list_[mid] > target:
                return recursive_search(list_[:mid],target)
            elif list_[mid]<target:
                return recursive_search(list_[mid:], target)
    return False



numbers = [1,6,9,10,20,22,26,78,100,456,1000]
target = 2.5
print(recursive_search(numbers,target))
