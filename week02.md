# Week 1
`#problems` `#Hash` `#Stack` `#Queue`\
`#algorithms` `#Heap` `#Sort`

##

### Problems
- [Hash](https://programmers.co.kr/learn/courses/30/parts/12077])
- [Stack / Queue](https://programmers.co.kr/learn/courses/30/parts/12081)


[Solutions](./week01)

##

### Algorithms
- [Sort](./sort)
- Heap

##

### Takeaways
- <code>**dict.get(key, default = None)**</code>

  **key** = key to be searched in the dictionary\
  **default** = value to be returned in case key does not exist
  
  ```
  >>> dict = {}
  >>> dict['key1'] = 1
  >>> dict.get(key1, 0)
  1
  >>> dict.get(key2, 0)
  0
  ```
  
- <code>**hash(object)**</code>

  Return the hash value of the object.\
  Hash values are integers.
 
  ```
  >>> hash('example string')
  7369253315943211870
  ```
  
- <code>**max(iterable, *[, key, default])**</code>\
  <code>**max(arg1, arg2, *args[, key])**</code>
  
  Return the largest item in an iterable or the largest of two or more arguments.
  
  ```
  >>> nums = [3, 4, 5, 6]
  >>> max(nums)
  6
  ```
  
- **Time complexity of list slicing is O(n)**

  **ex)** `for item in list_[int:]` - **not recommended**
