import os;
inSelection = True

#method to print out the whole array in a styalized in the console
def PrintArray(arr):
    print("Array to be sorted: ", arr)  

def MergeSort(arrToSort):

    #checks if the array is larger then one to sort
    if len(arrToSort) > 1:
        #Divides the original array into two sub arrays to be sorted
        leftData = arrToSort[:len(arrToSort)//2]#starts from the the start of the array to the midpoint
        rightData = arrToSort[len(arrToSort)//2:]#starts from the midpoint of the array to the end of the original array

        #prints out the itterations of the mergesort algorithim
        print("ITTERATION: ")
        print("Array Being Split is: ", arrToSort)
        print("Left Data Split: ", leftData, " Right Data Split: ", rightData)
        print(" ")

        MergeSort(leftData)
        MergeSort(rightData)


        #merge
        leftArrIndex = 0
        rightArrIndex = 0
        finalArrIndex = 0

        #these set of while loops sort the data depending and insert them into the final array to be out putted
        while leftArrIndex < len(leftData) and rightArrIndex < len(rightData):
            #checks if the leftside data is smaller then the right data at the index
            if leftData[leftArrIndex] < rightData[rightArrIndex]:
                #inputs the value to the correct position in the array
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

print("Welcome to Mergesort!!")
print("Please input the size of the array you would like to sort(ex: input 10 to get an array size of 10 values)")
arraySize = input()
arraySize = int(arraySize)
userArray = [0] * arraySize
print("This is the new array before values inputted: ", userArray)
for x in range(arraySize):
    print("Please input one of ", arraySize," integer values to the array")
    arrayVal = input()
    arrayVal = int(arrayVal)
    userArray[x] = arrayVal

print(" ")
print("This is the new array after values inputted: ", userArray)

print("-------------------------------Performing Merge Sort --------------------------")
MergeSort(userArray)


print("-------------------------------FINAL SORTED ARRAY --------------------------")
print("Final sorted array: ", userArray)