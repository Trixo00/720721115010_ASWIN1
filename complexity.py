from typing import List
def SingleOne (array: List[int]):
    for i in array:
        if array.count(i)==1: 
            return i
print("Test_Casel: ", SingleOne ([2,2,1]))
print("Test_Case2: ", SingleOne ([4,1,2,1,2]))
print("Test Case3: ", SingleOne([1]))