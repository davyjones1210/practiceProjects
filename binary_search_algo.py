#Have a function that takes a list and target parameter
#Calculate multiple variables: middle, start, end, steps
#Recursion or while loop
#Increase the steps each time a split is done
#Conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("Step", steps, ":", str(list[start: end+1]))

        steps = steps+1
        middle = (start + end)//2

        if element == list[middle]:
            print("Found target at index: ", middle)
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

my_list = [1,2,3,4,5,6,7,8,9]
target = 8
binary_search(my_list, target)
