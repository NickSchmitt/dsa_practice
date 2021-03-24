# Data Structures and Algorithms

1. Fork and clone this repo
2. Fill out the Big O and Written Questions in this README.
3. Complete the HackerRank challenges on hackerrank.com
4. You have 1 hour and 20 minutes


### Big O Analysis

---
Function 1 Time Complexity: O(1)

Explain your answer: It will do one computation and return true or false.
```
function bobIsFirst(people){
  return people[0] == 'bob'
}
```

---
Function 2 Time Complexity: O(n)

Explain your answer: The time complexity is directly proportional to the i, which is determined by the length of the 'phrase'
```
function wordOccurrence(word, phrase){
  let result = 0
  const array = phrase.split(' ')
  for(let i = 0; i < array.length; i++){
    if(word.toLowerCase() === array[i].toLowerCase()){
      result++;
    }
  }
  return result
}
```
---
Function 3 Time Complexity: O(n^2)

Explain your answer: Quadraatic because the 'i' loop runs about list.length times for each element in list
```
function sort(list){
  for(let i = 0; i < list.length - 1; i++){
    for(let j  = 0; j < list.length - 2; j++){
      if(list[j+1] < list[j]){
        const temp = list[j];
        list[j] = list[j+1];
        list[j+1] = temp;
      }
    }
  }
  return list;
}
```

---

### Written Questions

- What method would you use to look up a word in a dictionary (book, not Python)?
    I think it would be quick sort. I'm not sure. It's got a logarithmic big O though. Opening the book at a pivot point, deciding to look left or right based on the word in relation to that point, and moving in that direction to a new pivot point.

- Imagine you have a closet full of shirts. What can you do to organize your shirts for easy retrieval?
  I could organize them by category, maybe by keeping them in groups of similar color. Or I could assign each shirt a fanciness index and line them up according to how fancy they are.

- Describe advantages and disadvantages of the most popular sorting algorithms.
    Quick sort is fast unless the list is already fairly sorted or it has a lot of items that are equal. Then it can have a big big O.

---

### HackerRank Problems

- [Diagonal Difference](https://www.hackerrank.com/challenges/diagonal-difference/problem) (Algorithm, Warmup)
- [Left Rotation](https://www.hackerrank.com/challenges/array-left-rotation/problem) (Data Structures, Array)
- [Get Node Value](https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail) (Data Structures, Linked List)
