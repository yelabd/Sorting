def bubbleSort1(list):
	for i in range(len(list)-1,0,-1): #Outer for loop that starts at the end of the list and decrements
		for j in range(i): #Inner for loop goes from 0 to i
			if list[j] > list[j+1]: #Checks if the jth element in the list is greater than the j+1 element
				temp = list[j] #Stores jth element in temp variable
				list[j] = list[j+1] #Sets jth element to the j+1 element
				list[j+1] = temp #Sets the j+1 element to temp

toSort = [10,3,7,4,91,71]
bubbleSort1(toSort)
print(toSort)