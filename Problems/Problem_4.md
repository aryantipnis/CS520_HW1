## Problem 4 - From HumanEval/74

Write a function that accepts two lists of strings and returns the list that has the total number of characters in all strings of the list **less than** the other list.  
If the two lists have the same total number of characters, return the **first list**.

### Examples

```python
total_match([], []) ➞ []

total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']

total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']

total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']

total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
