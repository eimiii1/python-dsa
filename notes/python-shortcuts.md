# Python Speed Coding Tricks
## Trick 1: List Comprehensions
```python
# loops < list comprehension
result = [i * 2 for i in range(10) if i % 2 == 0]
```

## Trick 2: `enumerate()` -> get index + value
```python
for i, num in enumerate(nums):
	print(i, num)
```

## Trick 3: `zip()` -> loop multiple lists
```python
for name, score n zip(names, scores):
	print(name, score)
```

## Practice Problem
Given:
```python
items = ['apple', 'banana', 'cherry', 'date']
prices = [1.2, 0.5, 3.0, 2.5]

fruits = [f"{i}: {item} costs ${price}" for i, (item, price) in enumerate(zip(items, prices))]

print('\n'.join(fruits))
```