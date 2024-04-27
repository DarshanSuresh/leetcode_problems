"""
514. Freedom Trail

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.
Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.
Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.
At the stage of rotating the ring to spell the key character key[i]:
You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
 
Example 1:
Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.

Example 2:
Input: ring = "godding", key = "godding"
Output: 13
 

Constraints:
1 <= ring.length, key.length <= 100
ring and key consist of only lower case English letters.
It is guaranteed that key could always be spelled by rotating ring.
"""
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict

        def min_steps(start_idx, target_idx):
            # Calculate the minimum steps to rotate from start_idx to target_idx
            return min(abs(start_idx - target_idx), len(ring) - abs(start_idx - target_idx))

        # Create a dictionary to store the indices of each character in the ring
        char_indices = defaultdict(list)
        for idx, char in enumerate(ring):
            char_indices[char].append(idx)

        # Initialize the DP table with default values
        dp = [[float('inf')] * len(ring) for _ in range(len(key))]
        
        # Initialize the first row of DP table based on the first character in key
        for idx in char_indices[key[0]]:
            dp[0][idx] = min_steps(0, idx) + 1  # 1 step to spell the first character
        
        # Iterate through the rest of the characters in key
        for i in range(1, len(key)):
            for cur_idx in char_indices[key[i]]:
                for prev_idx in char_indices[key[i - 1]]:
                    dp[i][cur_idx] = min(dp[i][cur_idx], dp[i - 1][prev_idx] + min_steps(prev_idx, cur_idx) + 1)

        # Return the minimum steps needed to spell all characters in key
        return min(dp[-1])
