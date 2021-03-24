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

0(1)
a constant function with a constant time/space it will require to run. 
it's simplest component is itself.

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

0(n)
this function requires more time as the input increases.
linear progression of input vs time needed.

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

0(nˆ2)
this function requires exponentially more time to run as the input increases.
for each additional piece of data, (n) must be ran (n)(n) times 
because of the double nested looping.

---

### Written Questions

- What method would you use to look up a word in a dictionary (book, not Python)?
merge sort. merge sort is very intuitive and quick, has the fastest worst case. 
a "normal" human thought process behind finding a word in the dictionary would be 
dividing the dictionary into smaller and smaller chunks until we feel close enough
to the primary key that our chunks have become individual pages to flip through.

this method is faster more often than flipping individual pages from front or back, 
regardless of where the word is actually located.

- Imagine you have a closet full of shirts. What can you do to organize your shirts for easy retrieval?
sort them based on a unique identifier or an identifier that would allow easily recognizable groupings.

- Describe advantages and disadvantages of the most popular sorting algorithms.
advantages of most popular sorting algorithms is that we already know their worst case, their average cases, and their best cases in terms of Big O notation. We also know what specific use cases each one would be best suited for. However, this is also a disadvantage of theirs. They have specific use cases and using a sorting algorithm incorrectly can leave you spending much more time and memory than you should if you aren't careful with your selections.

---

### HackerRank Problems

- [Diagonal Difference](https://www.hackerrank.com/challenges/diagonal-difference/problem) (Algorithm, Warmup)

```javascript 
function diagonalDifference(arr) {
    // Write your code here
    let sum = 0
    let firstDiagonal = 0
    let secondDiagonal = 0
    for(let i = 0; i < arr.length; i++){
        firstDiagonal += arr[i][i]
        secondDiagonal += arr[i][arr.length - (1 + i)]
    }
    sum = firstDiagonal - secondDiagonal
    return Math.abs(sum)
}
```

```python
def diagonalDifference(arr):
  sum = 0
  first_diagonal = 0
  second_diagonal = 0
  for i in len(arr):
    first_diagonal += arr[i][i]
    second_diagonal += arr[i][len(arr) - (1 + i)]
  sum = first_diagonal - second_diagonal
  return abs(sum)
```


- [Left Rotation](https://www.hackerrank.com/challenges/array-left-rotation/problem) (Data Structures, Array)

```javascript
function rotateLeft(d, arr) {
    // Write your code here
    for(let i = 0; i < d; i++){
        let rotatedValue = arr[0]
        arr.shift()
        arr.push(rotatedValue)
    }
    return arr
}
```

- [Get Node Value](https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail) (Data Structures, Linked List)

```javascript
function getNode(head, positionFromTail) {
    let thisNode = head
    for(let i = 0; head.next !== null; i++){
        head = head.next
        if( i >= positionFromTail){
            thisNode = thisNode.next
        }
    }
    return thisNode.data
}
```
