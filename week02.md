# Week 2
`#problems` `#Heap` `#Sort`\
`#algorithms` `#Brute-Force` `#Greedy`

##

### Problems
- [Heap](https://programmers.co.kr/learn/courses/30/parts/12117)
- [Sort](https://programmers.co.kr/learn/courses/30/parts/12198)


[Solutions](./week02)

##

### Algorithms
- Brute-Force
- Greedy

##

### Takeaways
- <code>**list.sort(self, key=None, reverse=False)**</code>

  **key** = key to be compared\
  **reverse** = reverse order of sort to max-min\
  **return** = None, mutates the list
  
  
  ```
  >>> a = [5, 2, 3, 1, 4]
  >>> a.sort()
  >>> a
  [1, 2, 3, 4, 5]
  ```
  
- <code>**sorted(iterable, *, key=None, reverse=False)**</code>

  Return a new sorted list from the items in iterable
  
  **key** = key to be compared\
  **reverse** = reverse order of sort to max-min\
  **return** = sorted list
 
  ```
  >>> sorted([5, 2, 3, 1, 4])
  [1, 2, 3, 4, 5]
  >>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
  [1, 2, 3, 4, 5]
  ```
  
- <code>**zip(*iterable)**</code>
  
  Creates an iterator that will aggregate elements from two or more iterables
  
  
  ```
  >>> list(zip([1, 2, 3], [4, 5, 6]))
  [(1, 4), (2, 5), (3, 6)]
  >>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
  [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
  >>> list(zip("abc", "def"))
  [('a', 'd'), ('b', 'e'), ('c', 'f')]
  ```
