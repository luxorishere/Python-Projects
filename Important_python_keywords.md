# Python
# Strings operations
- `len()` returns the length of the string. Example: `len("hi")` -> 2
- `title()` capitalizes the first letter of each word in the string. Example: `title("hi")` -> "Hi"
- `lower()` converts the string to lowercase.
- `upper()` converts the string to uppercase
- `count(str, start, end)` returns the number of times substring `str` occurs between `start` and `end`
- `find(str, start, end)` returns the lowest index of the substring `str` in the string `start` to `end`. If `str` is not found, it returns -1.
- `index(str, start, end)` similar to `find()` but raises a ValueError if `str` is not found
- `endswith()` tells us if the string is ending with that substring or not
- `startswith()` tells us if the string started with that substring or not
- `isalnum()` tells us if the string contains only alphabets or numbers, not symbols like !@# etc
- `isspace()` returns true if the string is non-empty and all the elements are white spaces (string = "\n \t \r" or " ") otherwise false
- `islower()` returns true if all elements are lowercase
- `isupper()` returns true if all elements are uppercase
- `istitle()` returns true if the first letter is capitalized
- `lstrip()` removes spaces from the left side
- `rstrip()` removes spaces from the right side
- `strip()` removes spaces from both sides
- `replace(oldstr, newstr)` replaces the old substring with the new substring
- `join()` returns the string in which elements are combined by hyphens '-'
- `partition(str)` divides the string based on the substring `str`
- `split()` splits the string into a list of words

# Lists in Python

Lists in Python are used to store multiple items in a single variable. They are ordered and mutable, which means you can change, add, and remove items after the list is created.

### Syntax

- To create a list in Python, you use square brackets `[]` and separate the elements with commas.
```python
my_list = [element1, element2, ..., elementn]

```
### Nested Lists and Indexing

- In Python, you can create nested lists, which are lists containing other lists or different types of elements. Here's an example of a nested list:
```python
nested_list = [[1, 2, 3], "safa", [[2131], [3242]]]
```
### List Operations
- Concatenation
  ```
  list1 = [1,2]
  list2 = [3]
  list3 = list1 + list2
  print(list3)
  ```
Output is [1,2,3]
- Repetiion
  ```
  list = [1,2,3]
  print(list * 3)
  ```
  Output
  ```
  [1, 2, 3, 1, 2, 3, 1, 2, 3]
  ```
- Memberships
  ```
  list = [1,2,3]
  print(1 in list)
  ```
  Output
  ```
  True
  ```
- Slicing
  ```
  list = [1,2,3]
  print(list[0 : 3])
  print(list[0 : ])
  print(list[: : -1])
  print(list[:])
  print(list[-1:])
  print(list[-2:])
  print(list[1::-1])
  print(list[:-3:-1])
  print(list[-3::-1])
  ```
  Output
  ```
  [1, 2, 3]
  [1, 2, 3]
  [3, 2, 1]
  [1, 2, 3]
  [3]
  [2, 3]
  [2, 1]
  [3, 2]
  [1]
  ```
### Built-in functions for list
- `len()` returns the length of the list. Example: `len([1, 2, 3])` -> 3
- `list(object)` creates a list from an object. Example: `list("hello")` -> ['h', 'e', 'l', 'l', 'o']
- `append()` adds the element at the end of the list. Example: `my_list.append(4)`
- `extend()` extends one list by appending elements from another list. Example: `my_list.extend([5, 6, 7])`
- `insert()` inserts an element at a specified position in the list. Example: `my_list.insert(1, 'a')`
- `count()` counts the number of times an element occurs in the list. Example: `my_list.count(3)` -> 1
- `index()` returns the index of the first occurrence of an element in the list. Example: `my_list.index('a')` -> 1
- `remove()` removes the first occurrence of an element from the list. Example: `my_list.remove('a')`
- `pop()` removes and returns the last element from the list. Example: `last_element = my_list.pop()`
- `reverse()` reverses the elements of the list in place. Example: `my_list.reverse()`
- `sort()` sorts the list in ascending order. Example: `my_list.sort()`
- `sorted()` returns a new sorted list without modifying the original list. Example: `sorted_list = sorted(my_list)`
- `min()` returns the minimum element in the list. Example: `min_value = min(my_list)`
- `max()` returns the maximum element in the list. Example: `max_value = max(my_list)`
- `sum()` returns the sum of all elements in the list. Example: `total_sum = sum(my_list)`

# Dictionary
A dictionary in Python is a collection of key-value pairs where each key maps to a corresponding value. It allows efficient lookup and manipulation of data based on unique keys.

```
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values by keys
print(my_dict['name'])  # Output: John
print(my_dict['age'])   # Output: 30

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'

# Updating a value
my_dict['age'] = 35

# Deleting a key-value pair
del my_dict['city']

print(my_dict)  # Output: {'name': 'John', 'age': 35, 'occupation': 'Engineer'}
```
Dictionary uses hash table internally to search keys that's why they are really fast
for an example
```
(10, element1)
(12, element2)
(15, element3)
'''Searching formula is k mod 10 so Dictionary take the key which are 10, 12, 15 and perform the formula
10 mod 10 = 0
12 mod 10 = 2
15 mod 10 = 5
k mod 10 = some key value'''
#So this is how they got the key value which makes dictionary so easy to search for specific element
```
# If-else and elif condtion
```
# Taking user input
num = int(input("Enter a number: "))

# Checking conditions
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
# Output sample
''' Enter a number: 3
The number is positive.'''
```
We can use and & or operators too between if and elif conditions
```
# Taking user input
num = int(input("Enter a number: "))

# Checking conditions
if num > 0 and num % 2 == 0:
    print("The number is a positive even number.")
elif num > 0 and num % 2 != 0:
    print("The number is a positive odd number.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

```
# NUMPY

### NumPy Overview

1. **Numerical Computing:** 
   - NumPy is a Python library for numerical computations.
   - Supports large, multi-dimensional arrays and matrices.

2. **Efficient Data Structures:** 
   - Main object: `ndarray` for array-based computations.
   - Enables fast and concise mathematical operations.
   - *n in ndarray represents the dimensions of an array*

3. **Wide Range of Functions:** 
   - Provides mathematical functions like linear algebra, Fourier transforms, etc.
   - Widely used in scientific computing, data analysis, and machine learning.

```python
import numpy as np

# Create a Python list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
my_array = np.array(my_list)
print(my_array)  # Output: [1 2 3 4 5]

# Create a nested Python list
my_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(my_list)  # Output: [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Convert the nested list to a NumPy array
my_array = np.array(my_list)
print(my_array)  # Output:
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]

```
What if we put float in integer array
```python
import numpy as np

my_list = [1, 2, 3, 4, 5.5]
print("Original list:", my_list)  # Output: Original list: [1, 2, 3, 4, 5.5]

my_array = np.array(my_list)
print("NumPy array:", my_array)  # Output: NumPy array: [1.  2.  3.  4.  5.5]

print("Type of array:", type(my_array))  # Output: Type of array: <class 'numpy.ndarray'>

my_list = [1, '2', 3, 4, 5.5]
print(my_list)  # Output: [1, '2', 3, 4, 5.5]

my_array = np.array(my_list)
print(my_array)  # Output: ['1' '2' '3' '4' '5.5']

print(type(my_array))  # Output: <class 'numpy.ndarray'>

```
1. **`array = np.arange(1,10)`**: Creates a NumPy array from 1 to 9 (excluding 10).
2. **`array1 = np.arange(1,7).reshape((2,3))`**: Creates a 2x3 array with numbers from 1 to 6.
3. **`array0 = np.zeros(4)`**: Creates a NumPy array of zeros with length 4.
4. **`array11 = np.ones(5)`**: Creates a NumPy array of ones with length 5.

```python
import numpy as np

# Create an array from 1 to 9
array = np.arange(1, 10)
print(array)  # Output: [1 2 3 4 5 6 7 8 9]

# Create a 2x3 array with numbers from 1 to 6
array1 = np.arange(1, 7).reshape((2, 3))
print(array1)  # Output: [[1 2 3] [4 5 6]]

# Create an array of zeros with length 4
array0 = np.zeros(4)
print(array0)  # Output: [0. 0. 0. 0.]

# Create an array of ones with length 5
array11 = np.ones(5)
print(array11)  # Output: [1. 1. 1. 1. 1.]
```
### Types of Attributes
1. **Shape (`shape`):** Describes how many elements are in each dimension of the array. For example, a 2D array with 3 rows and 4 columns has a shape of `(3, 4)`.

2. **Data Type (`dtype`):** Specifies what type of data the array holds, like numbers (integers or decimals), True/False values, etc.

3. **Size (`size`):** Indicates the total number of elements in the array. For instance, a 2D array with a shape of `(3, 4)` has a size of 12 (3 * 4 = 12).

4. **Number of Dimensions (`ndim`):** Shows how many axes or dimensions the array has. A 1D array (like a list) has one dimension, while a 2D array (like a table) has two dimensions.

5. **Strides (`strides`):** Specifies how many bytes to move to get to the next element along each dimension. It's used for memory optimization and efficient access.

6. **Item Size (`itemsize`):** Represents the size of each element in bytes. For example, an integer typically takes up 4 bytes of memory.
Here's a Markdown (`.md`) file that explains the given Python code:

### NumPy Array Operations

```python
import numpy as np

# Create a 1D NumPy array
array = np.array([1, 2, 3, 4, 5])

# Accessing elements by index
print(array[2])    # Output: 3
print(array[-1])   # Output: 5
```

In the code above:
- We create a 1D NumPy array `array` with values `[1, 2, 3, 4, 5]`.
- We use array indexing to access elements by their index, where `array[2]` gives the third element (index starts from 0) and `array[-1]` gives the last element.

```python
# Create a 2D NumPy array using arange and reshape
array = np.arange(1, 11).reshape((5, 2))

# Display the 2D array and perform various indexing operations
print(array)
print(array[2, 1])   # Output: 7 (value at row 2, column 1)
print(array[0, :])   # Output: [1 2] (entire first row)
print(array[:, 1])   # Output: [2 4 6 8 10] (entire second column)
```

In the second part of the code:
- We create a 2D NumPy array `array` using `np.arange(1, 11).reshape((5, 2))`, which generates numbers from 1 to 10 and reshapes it into a 5x2 array.
- We demonstrate different indexing operations:
  - `array[2, 1]` accesses the element at row 2, column 1, which is 7.
  - `array[0, :]` accesses the entire first row `[1 2]`.
  - `array[:, 1]` accesses the entire second column `[2 4 6 8 10]`.

### NumPy Array Slicing

Let's explore various slicing operations on a NumPy array.

```python
import numpy as np

# Create a NumPy array from 1 to 9 (exclusive)
array = np.arange(1, 10)

# Original array
print("Original Array:", array)  # Output: [1 2 3 4 5 6 7 8 9]

# Slice from index 1 to index 2 (exclusive)
print("Slice [1:3]:", array[1:3])  # Output: [2 3]

# Slice from index -1 to index -3 (backwards slicing)
print("Slice [-1:-3]:", array[-1:-3])  # Output: [] (empty because -1 > -3)

# Slice with step 2 from index 1 to index 10 (exclusive)
print("Slice [1:10:2]:", array[1:10:2])  # Output: [2 4 6 8]

# Reverse slice with step 2 from index -1 to index -7 (exclusive)
print("Slice [-1:-7:-2]:", array[-1:-7:-2])  # Output: [9 7 5]

# Reverse slice from index -5 to index -1 (exclusive)
print("Reverse Slice [-5:-1:-1]:", array[-5:-1:-1])  # Output: [] (empty because -1 > -5)

# Slice with step 2 (every other element) from start to end
print("Every Other Element [::2]:", array[::2])  # Output: [1 3 5 7 9]

# Reverse the array
print("Reversed Array:", array[::-1])  # Output: [9 8 7 6 5 4 3 2 1]



```
### NumPy Array Operations

Let's perform various operations on NumPy arrays.

```python
import numpy as np

# Create two NumPy arrays
array1 = np.arange(1, 6)
array2 = np.arange(6, 11)

# Print the arrays
print("Array 1:", array1)  # Output: [1 2 3 4 5]
print("Array 2:", array2)  # Output: [ 6  7  8  9 10]

# Addition
array3 = array1 + array2
print("Array Addition:", array3)  # Output: [ 7  9 11 13 15]

# Subtraction
array0 = array1 - array2
print("Array Subtraction:", array0)  # Output: [-5 -5 -5 -5 -5]

# Element-wise multiplication (Hadamard product)
array_mult = array1 * array2
print("Element-wise Multiplication:", array_mult)  # Output: [ 6 14 24 36 50]

# Element-wise division
array_div = array1 / array2
print("Element-wise Division:", array_div)  # Output: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]

# Element-wise floor division (integer division)
array_floor_div = array1 // array2
print("Element-wise Floor Division:", array_floor_div)  # Output: [0 0 0 0 0]

# Element-wise exponentiation
array_power = array1 ** array2
print("Element-wise Exponentiation:", array_power)  # Output: [        1       128     6561   262144 9765625]

# Element-wise modulo
array_mod = array1 % array2
print("Element-wise Modulo:", array_mod)  # Output: [1 2 3 4 5]

# Matrix multiplication (dot product)
array_dot_product = array1 @ array2
print("Matrix Multiplication (Dot Product):", array_dot_product)  # Output: 130
```

In the code above:
- We create two NumPy arrays `array1` and `array2` containing elements from 1 to 5 and 6 to 10, respectively.
- Various operations such as addition, subtraction, multiplication, division, floor division, exponentiation, modulo, and matrix multiplication (dot product) are performed.
- Each operation is explained with its respective output.


# Pandas: Data Analysis Made Easy

## Introduction to Pandas

Pandas is a Python library for data manipulation and analysis.

### Installing Pandas

```bash
pip install pandas
```

## Basics of Pandas

### Importing Pandas

```python
import pandas as pd
```

### Pandas Data Structures

1. **Series**: One-dimensional labeled array.
2. **DataFrame**: Two-dimensional labeled data structure.

### Creating a Series

```python
data = [1, 2, 3, 4, 5]
s = pd.Series(data)
print(s)
# Output:
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64
```

### Creating a DataFrame

```python
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
# Output:
#      Name  Age
# 0  Alice   25
# 1    Bob   30
# 2 Charlie  35
```

### Loading Data into DataFrame

```python
# Load CSV data
df = pd.read_csv('data.csv')
```

## Data Manipulation with Pandas

### Selecting Data

```python
# Selecting a column
ages = df['Age']

# Selecting rows based on conditions
young_people = df[df['Age'] < 30]
```

### Adding and Deleting Columns

```python
# Adding a new column
df['Gender'] = ['Female', 'Male', 'Male']

# Deleting a column
df.drop('Gender', axis=1, inplace=True)
```

### Handling Missing Data

```python
# Drop rows with missing values
df.dropna()

# Fill missing values with a specific value
df.fillna(0)
```

## Advanced Pandas Operations

### Grouping Data

```python
# Group by 'Category' and calculate mean of 'Value' column
grouped_data = df.groupby('Category')['Value'].mean()
```

### Merging DataFrames

```python
# Merge two DataFrames based on a common column
merged_df = pd.merge(df1, df2, on='common_column')
```

### Time Series Analysis

```python
# Convert column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Resample time series data
daily_data = df.resample('D').mean()
```

## Conclusion

Pandas simplifies data analysis tasks in Python by providing powerful data structures and functions. With pandas, you can efficiently work with structured data, perform data manipulations, and conduct advanced analyses.


# Handling Missing Data

#### 1. Dropping Missing Values

```python
# Drop rows with missing values
df.dropna()
```

When you use `dropna()` without any parameters, it drops rows containing any missing values (`NaN`). This can be useful when you want to remove incomplete records from your dataset.

#### 2. Filling Missing Values

```python
# Fill missing values with a specific value
df.fillna(0)
```

The `fillna()` method allows you to fill missing values with a specific value, such as 0. This is helpful when you want to replace missing values with a default value to maintain data integrity.

#### 3. Filling with Forward or Backward Values

```python
# Forward fill missing values
df.fillna(method='ffill')

# Backward fill missing values
df.fillna(method='bfill')
```

You can use forward fill (`ffill`) or backward fill (`bfill`) to propagate non-null values forward or backward along a Series or DataFrame. This is especially useful for time series data where missing values can be filled based on nearby existing values.

#### 4. Interpolation

```python
# Linear interpolation of missing values
df.interpolate()
```

Interpolation is a method to estimate missing values based on existing values. Pandas provides various interpolation methods like linear interpolation (`method='linear'`), polynomial interpolation, and more.

#### 5. Filling with Mean/Median/Mode

```python
# Fill missing values with mean of the column
df.fillna(df.mean())

# Fill missing values with median of the column
df.fillna(df.median())

# Fill missing values with mode of the column
df.fillna(df.mode().iloc[0])
```
just checking






