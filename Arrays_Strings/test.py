
def productArray(arr, n):
 
    # Base case
    if(n == 1):
        print(0)
        return

    left = [0]*n
    right = [0]*n

    prod = [0]*n

    left[0] = 1
 
    right[n - 1] = 1

    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]

    print(left)
    for j in range(n-2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]
    print(right)

    for i in range(n):
        prod[i] = left[i] * right[i]
 
    # print the constructed prod array
    for i in range(n):
        print(prod[i], end=' ')


# Driver Code
arr = [1, 2, 3, 4, 5]
n = len(arr)
print("The product array is: ", n)
productArray(arr, n)

# This code is contributed by mohit kumar
