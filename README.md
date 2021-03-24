# Data Structures and Algorithms

1. Fork and clone this repo
2. Fill out the Big O and Written Questions in this README.
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
O(1)
Accessing an element from an array means that it is given the location to read the data from and does not need to iterate through to find the data, hence it will be a constant O regardless of how big the array is
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
worst case: 0(N)?
 From the looks of it, it's a for loop that iterates through a split phrase that becomes an array of the separate values of that string, and determines if the lowercase version of the word argument is the same as that within the array.  If it is, it adds to the result value by 1.  I would think this is O(N) because it only iterates once through until the end of the array and then stops.  The output is dependent on each iterative step.
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
worst case: O(N^2)
Nested for loops create iterations within iterations, which take up both time and memory.

---

### Written Questions

- What method would you use to look up a word in a dictionary (book, not Python)?
If your knowledge of a word is just a vague idea of how to spell it and the first letter, I'd go , to the section for that letter, basically using recursion and going by sequential letter alphabetically until i've reached my word.

- Imagine you have a closet full of shirts. What can you do to organize your shirts for easy retrieval?
It depends on how you prefer to retrieve them.  If you don't mind what color, but like to reach for something based on weather, then organizing by sleeve length and fabric type are helpful.  If you care what color and what type, then organizing by weather first and within those weather-organized sections creating the same color gradient for each section might be best.  In general, I imagine it's easier to organize in multiple ways in case the data is used for a different purpose or by a different person/programmer in the future.   Mine personally vacillate between the dryer and an amorphous pile near the dresser that almost gives the impression that they're going to be folded any day now.

- Describe advantages and disadvantages of the most popular sorting algorithms.
Some of the most popular sorting algorithms include quick sort and merge sort.

---

### HackerRank Problems

- [Diagonal Difference](https://www.hackerrank.com/challenges/diagonal-difference/problem) (Algorithm, Warmup)
- [Left Rotation](https://www.hackerrank.com/challenges/array-left-rotation/problem) (Data Structures, Array)
- [Get Node Value](https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail) (Data Structures, Linked List)
