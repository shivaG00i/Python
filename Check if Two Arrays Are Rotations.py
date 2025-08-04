# 21. Check if Two Arrays Are Rotations Input: [1,2,3,4], [3,4,1,2]
# → Output: True



'''


What is a Rotation?
Rotation means moving elements to the front or back while preserving their order, like turning a wheel.

Example:
Original:
[1, 2, 3, 4]

Possible rotations:

Rotate 1 step → [2, 3, 4, 1]

Rotate 2 steps → [3, 4, 1, 2]

Rotate 3 steps → [4, 1, 2, 3]

Rotate 4 steps → back to [1, 2, 3, 4]

So:
[3, 4, 1, 2] is a rotation of [1, 2, 3, 4].


'''




arr1=[1,2,3,4]
arr2=[3,4,1,2]

def are_rotations(arr1, arr2):
    # Step 1: Check if both arrays are the same length
    if len(arr1) != len(arr2):
        return False  # If not, they can't be rotations

    # Step 2: Try all possible rotations of arr1
    for i in range(len(arr1)):
        # Rotate arr1 by slicing at index i
        rotated = arr1[i:] + arr1[:i]

        # Check if this rotation matches arr2
        if rotated == arr2:
            return True  # Found a match

    # If none of the rotations match
    return False

print(are_rotations(arr1, arr2))  