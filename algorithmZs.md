Algorithm:
==
**def main:**
1. Initialize an array of integers (practically, we use 3 values) of size M x N according to the given boolean array. Each cell will contain 3 values - `0, 1, Z`
2. While there is some cell with the value 1 in the array:
    1. Find a cell `(x,y)` with the value 1 that minimizes `new_Z_count(x, y)`
    2. Set that cell value to `0`, and then for each other cell `(x1, y1)`:
        `value(x1, y1)` = new_state_given_new_circle((x, y), (x1, y1))
3. If at termination, there exists a circle that intersects only `Z` valued cells, return `?`
(I suspect this will never happen)
4. Otherwise, return the amount of iterations performed in step 2. 


**def new_Z_count(x, y):**
1. count = 0
2. for every cell `x1, y1` with the value `1`:
    3. if new_state_given_new_circle((x, y), (x1, y1)) == Z
        4. count++
5. return count



**def new_state_given_new_circle((x, y), (x1, y1)):**
1. If every circle that contains `(x, y)`, and is legal due
to the given state of the array - i.e., it does not contain any `0` valued cell -
also contains `(x1, y1)`, then return `0`
2. If all of these circles do not contain `(x1, y1)`, then return `value(x1, y1)`
3. Otherwise, return `Z`



