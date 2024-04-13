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

# Syntax

- To create a list in Python, you use square brackets `[]` and separate the elements with commas.
```python
my_list = [element1, element2, ..., elementn]

```
# Nested Lists and Indexing

- In Python, you can create nested lists, which are lists containing other lists or different types of elements. Here's an example of a nested list:
```python
nested_list = [[1, 2, 3], "safa", [[2131], [3242]]]
```
# List Operations
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

  

  







