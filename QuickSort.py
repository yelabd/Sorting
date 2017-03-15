def quickSort(list,left, right):
	if left >= right: #if statement that checks if left is greater than right bound,returns if true
		return
	pivot = list[(left+right)/2] #Generate a pivot point from the list, the index of point is not really relavent as long as its within the list bounds
	split = partition(list,left,right, pivot) #Gets the split point after sorting the list with respect to the pivot point
	quickSort(list,left,split-1) #Call the quickSort method again to left side of the split point
	quickSort(list,split,right) #Call the quickSort method again to the right side of the split point

def partition(list,left,right,pivot):
	while left <= right: #Loop executes as long as the left value has not exceeded right value, 
		while list[left] < pivot: #Loops from the left point until the list element at the left index is greater than the pivot value
			left = left + 1

		while list[right] > pivot: #Loops from the right point until the list element at the right index is less than the pivot value
			right = right - 1

		if left <= right: #Checks to see if they the left and right pointers have overlapped, if not, the list elements at the right and left indices are swapped
			temp = list[right] 
			list[right] = list[left]
			list[left] = temp
			left = left + 1
			right = right - 1
	return left #Main while loop is done and returns the left value that will be used as the split point in the recursive quicksort calls

toSort = [91,49,2,8,4,3,15]
quickSort(list = toSort,left = 0,right = 6)
print(toSort)

