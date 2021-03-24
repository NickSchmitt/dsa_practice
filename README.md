# Data Structures and Algorithms

1. Fork and clone this repo
2. Fill out the Big O and Written questions in this read me.
3. Complete the HackerRank challenges on hackerrank.com
4. You have 1 hour and 20 minutes


### Big O Analysis

---
Function 1 Time Complexity:

Explain your answer:
```
function bobIsFirst(people){
  return people[0] == 'bob'
}
```
---
Function 2 Time Complexity:

Explain your answer:
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
Function 3 Time Complexity:

Explain your answer:
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

- What method would you use to look up a word in a [dictionary](https://en.wikipedia.org/wiki/Dictionary) (book of words, not a Python dict)?

- Imagine you have a closet full of shirts. What can you do to organize your shirts for easy retrieval?

- Describe advantages and disadvantages of the most popular sorting algorithms.

---

### HackerRank Problems

- [Diagonal Difference](https://www.hackerrank.com/challenges/diagonal-difference/problem) (Algorithm, Warmup)
- [Left Rotation](https://www.hackerrank.com/challenges/array-left-rotation/problem) (Data Structures, Array)
- [Get Node Value](ckerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/) (Data Structures, Linked List)