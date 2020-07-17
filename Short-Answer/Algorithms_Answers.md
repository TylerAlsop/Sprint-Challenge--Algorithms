#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because the while loop will run as many times as n.


b) O(n^2) because of the nested loops.


c) O(n) because it will run as many times as there are bunnies.

## Exercise II

Real World Solution:
    Start on the middle floor and drop an egg. 
        If the egg cracks then go down half of the remaining floors below you and start this solution again until you find adjacent floors where the egg doesn't crack on one floor and then it does crack on the next.
        If the egg doesn't crack then go up half of the remaining floors and start this solution again until you find adjacent floors where the egg doesn't crack on one floor and then it does crack on the next.


Worst case runtime complexity: O(n)
