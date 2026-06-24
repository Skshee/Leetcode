### Sliding Window

General Template

```
function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer
```

- Number of subarrays

- Fixed window size

General Template :

```
function fn(arr, k):
    curr = some data to track the window

    // build the first window
    for (int i = 0; i < k; i++)
        Do something with curr or other variables to build first window

    ans = answer variable, probably equal to curr here depending on the problem
    for (int i = k; i < arr.length; i++)
        Add arr[i] to window
        Remove arr[i - k] from window
        Update ans

    return ans
```

## 2D Arrays

'''
If no. of rows = m and cols = n
Row = // n
Col = % n

Example :  matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
row = //n
col = % n

## Hashing
https://www.datacamp.com/tutorial/guide-to-python-hashmaps
## Sets 
https://www.datacamp.com/tutorial/sets-in-python

`Lists can't be added to sets untilllll -> we use .update instead of .add`