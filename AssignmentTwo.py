
idArray = [11,1,30,2,51,6,29,7,67,15,118,4,89,23]
inSelection = True

#method to print out the whole array in a styalized in the console
def PrintArray(arr):
    print("Array to be sorted: ", arr)  

#This is a recursive function that does the merge sort algorithim to the array provided
def MergeSort(arrToSort):

    #checks if the array is larger then one to sort
    if len(arrToSort) > 1:
        #Divides the original array into two sub arrays to be sorted
        leftData = arrToSort[:len(arrToSort)//2]#starts from the the start of the array to the midpoint
        rightData = arrToSort[len(arrToSort)//2:]#starts from the midpoint of the array to the end of the original array

        MergeSort(leftData)
        MergeSort(rightData)
        

        #merge
        leftArrIndex = 0
        rightArrIndex = 0
        finalArrIndex = 0

        while leftArrIndex < len(leftData) and rightArrIndex < len(rightData):
            if leftData[leftArrIndex] < rightData[rightArrIndex]:
                arrToSort[finalArrIndex] = leftData[leftArrIndex]
                leftArrIndex += 1
            else:
                arrToSort[finalArrIndex] = rightData[rightArrIndex]
                rightArrIndex += 1

            finalArrIndex += 1
        
        while leftArrIndex < len(leftData):
            arrToSort[finalArrIndex] = leftData[leftArrIndex]
            leftArrIndex += 1
            finalArrIndex += 1
        
        while rightArrIndex < len(rightData):
            arrToSort[finalArrIndex] = rightData[rightArrIndex]
            rightArrIndex += 1
            finalArrIndex += 1

#partitions the array around the pivot element making the pivot the first element
def partition(arrToSort, arrBegin, arrEnd):
    pivot = arrToSort[arrBegin]
    i = arrBegin + 1
    j = arrEnd
    
    while True:
        while i <= j and arrToSort[i] <= pivot:
            i += 1
        while i <= j and arrToSort[j] >= pivot:
            j -= 1
        if i <= j:
            arrToSort[i], arrToSort[j] = arrToSort[j], arrToSort[i]
        else:
            break
    
    arrToSort[arrBegin], arrToSort[j] = arrToSort[j], arrToSort[arrBegin]
    return j

#This is a recursive function that sorts the idArray
def QuickSort(arrToSort, arrBegin, arrEnd):
    if arrBegin < arrEnd:
        pivot_index = partition(arrToSort, arrBegin, arrEnd)
        QuickSort(arrToSort, arrBegin, pivot_index - 1)
        QuickSort(arrToSort, pivot_index + 1, arrEnd)

PrintArray(idArray)

while(inSelection):
    print("How would you like to sort the array?(Input the name of the sort ex: MergeSort)")
    print("1) Mergesort")
    print("2) Quicksort")

    userSelection = input()
    print("Player Input: " + userSelection)

    if userSelection.lower() == "mergesort" or userSelection.lower() == "quicksort":
        inSelection = False
    else:
        print("ERROR: Please input your selection again")

if userSelection.lower() == "mergesort":
    print("Performing Merge sort!!!!!!")
    MergeSort(idArray)
elif userSelection.lower() == "quicksort":
    print("Performing Quick sort!!!!")
    QuickSort(idArray, 0, len(idArray) - 1)

print("-------------------------------FINAL SORTED ARRAY --------------------------")
print("Final sorted array: ", idArray)






            











