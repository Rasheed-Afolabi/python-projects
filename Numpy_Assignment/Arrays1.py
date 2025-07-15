## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
step1_array = np.full((4, 3), 2)
print(step1_array)
print()

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
step2_array = np.arange(0, 120, 10).reshape(3, 4)
print(step2_array)
print() 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
step3_array = step2_array.reshape(4, 3)
print(step3_array)
print()

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
step4_array = step3_array * 3
print(step4_array)
print()

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")
try:
    step5_array = step1_array * step2_array
    print(step5_array)
except ValueError as e:
    print(f"Error: {e}")
    print("This errored out because step1_array is 4x3 and step2_array is 3x4 - incompatible shapes for element-wise multiplication")
## This errored out... why?
print()

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")
step6_array = step1_array * step3_array
print(step6_array)
## this worked! why?
print("This worked because both step1_array and step3_array have the same shape (4x3), so element-wise multiplication is possible")
print()