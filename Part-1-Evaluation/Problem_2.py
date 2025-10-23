"""
Problem 2 - From HumanEval/89: 
Create a function encrypt that takes a string as an argument and returns a string encrypted with the alphabet being rotated.  
The alphabet should be rotated in a manner such that the letters  shift down by two multiplied to two places. 

For example: 
encrypt('hi') returns 'lm' 

encrypt('asdfghjkl') returns 'ewhjklnop' 

encrypt('gf') returns 'kj' 

encrypt('et') returns 'ix'
"""

#Prompting Strategy: Chain of Thought, LLM: OpenAI GPT 4.0
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output: 
Let's reason step-by-step, then show the Python implementation and tests.

Step-by-step reasoning: 
The prompt's phrase "shift down by two multiplied to two places" means shift by 2x2=4.
So this is a Caesar-like rotation where every alphabetic character is moved forward 4 letters in the alphabet.

Example: 'a' -> 'e', 'x' -> 'b' (wrap-around).
Preserve case: uppercase letters map to uppercase, lowercase to lowercase.
Leave non-letter characters (spaces, punctuation, digits) unchanged.
If input is empty, return an empty string.

[Generated code is given below]
"""
def solution1(s):
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            offset = ord('a')
            result.append(chr((ord(ch) - offset + 4) % 26 + offset))
        elif 'A' <= ch <= 'Z':
            offset = ord('A')
            result.append(chr((ord(ch) - offset + 4) % 26 + offset))
        else:
            result.append(ch)
    return ''.join(result)


#Prompting Strategy: Self Planning, LLM: GPT: 4.0
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
🧠 Step 1: Understand the Problem
We need to encrypt a lowercase string by rotating the alphabet.

Rule:
Each letter in the string should be shifted down the alphabet by 2 x 2 = 4 positions.
So:
'a' → 'e'
'b' → 'f'
'c' → 'g'
…
'w' → 'a'
'x' → 'b'
'y' → 'c'
'z' → 'd'
We must handle wrap-around (when we go past 'z').
Example:
encrypt('hi') → 'lm'
because 'h' → 'l', 'i' → 'm'.

🧩 Step 2: Plan / Function Design
Function 1: encrypt(text)
Purpose:
Takes a string and returns an encrypted string where each lowercase letter is shifted 4 places forward.
Steps:
Initialize an empty string encrypted_text.
Loop through each character ch in text:
If it's a lowercase letter ('a' to 'z'):
Convert to ASCII value using ord(ch).
Subtract 'a' to normalize: (ord(ch) - ord('a')).
Add the shift (4).
Apply modulo 26 for wrap-around: (new_value % 26).
Convert back to character using chr(ord('a') + new_value).
Append the encrypted character to encrypted_text.
Return the final encrypted_text.

⚙️ Step 3: Function Interaction
There's only one main function:
encrypt(text) — handles everything internally.
No helper functions are strictly necessary, but we could optionally add a helper for shifting.
Optional:
shift_char(ch, shift) — shifts one character by shift positions.

[Generated code is given below]
"""

def solution2(text): 
    shift = 4
    encrypted_text = ""

    for ch in text:
        if 'a' <= ch <= 'z': 
            new_char = chr(((ord(ch) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += new_char
        else:
            encrypted_text += ch  

    return encrypted_text

#Prompting Strategy: Chain of Thought, LLM: Claude Sonnet 4.5
"""
Input: 
Think step-by-step to solve this problem then write the Python code to solve this problem 
[Pasted question here]

Output:
I'll solve this step-by-step.Step-by-Step Reasoning:
Understand the problem:

"two multiplied to two places" means 2 x 2 = 4 places
Each letter should shift down (forward) by 4 positions in the alphabet
We need to handle wrapping around the alphabet (e.g., 'x' → 'b')

Verify with examples:
'hi' → 'lm'
'h' (position 7) + 4 = 'l' (position 11) ✓
'i' (position 8) + 4 = 'm' (position 12) ✓

'gf' → 'kj'
'g' (position 6) + 4 = 'k' (position 10) ✓
'f' (position 5) + 4 = 'j' (position 9) ✓

'et' → 'ix'
'e' (position 4) + 4 = 'i' (position 8) ✓
't' (position 19) + 4 = 'x' (position 23) ✓

Handle wrapping:

For letters near the end of the alphabet (w, x, y, z), we need to wrap around
Example: 'z' (position 25) + 4 = position 29, which wraps to position 3 = 'd'
Use modulo operation: (position + 4) % 26

Algorithm:

Iterate through each character
If it's a lowercase letter, shift it by 4 positions with wrapping
If it's uppercase, convert to lowercase, shift, then convert back
If it's not a letter, keep it as is
Return the encrypted string

[Generate code is given below]
"""

def solution3(s):
    result = []
    shift = 2 * 2  
    
    for char in s:
        if char.isalpha():
            if char.islower():
                pos = ord(char) - ord('a')
                new_pos = (pos + shift) % 26
                new_char = chr(ord('a') + new_pos)
                result.append(new_char)
            else:
                pos = ord(char) - ord('A')
                new_pos = (pos + shift) % 26
                new_char = chr(ord('A') + new_pos)
                result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

#Prompting Strategy: Self Planning, LLM: Claude Sonnet 4.5
"""
Input:  
Before writing code, outline a plan that describes what functions you will implement and how they will interact. 
Then, based on your plan, write a python code for this problem
[Pasted question here]

Output: 
Plan
I'll create a solution with the following approach:
Functions to Implement:

encrypt(s) - Main function that:

Takes a string as input
Shifts each letter down by 2 * 2 = 4 positions in the alphabet
Wraps around if the shift goes past 'z'
Returns the encrypted string



Algorithm Flow:

Initialize an empty result string
Iterate through each character in the input string
For each character:

Check if it's a lowercase letter (based on examples, assuming lowercase only)
Calculate the new position by shifting 4 positions forward
Handle wraparound using modulo 26 (number of letters in alphabet)
Convert back to a character
Add to result string


Return the encrypted result

Key Considerations:

Shift amount: 2 * 2 = 4 positions
Need to handle wraparound (e.g., 'y' + 4 = 'c')
Based on examples, all inputs appear to be lowercase letters
Use ASCII values: 'a' = 97, 'z' = 122
Formula: new_char = chr((ord(char) - ord('a') + 4) % 26 + ord('a'))

Verification with Examples:

'h' (position 7) + 4 = 'l' (position 11) ✓
'i' (position 8) + 4 = 'm' (position 12) ✓
'a' (position 0) + 4 = 'e' (position 4) ✓
'g' (position 6) + 4 = 'k' (position 10) ✓

Now, let me implement this:

[Generated code is given below]
"""
def solution4(s): 
    result = ""
    shift = 2 * 2 
    
    for char in s:
        if char.isalpha():
            if char.islower():
                new_pos = (ord(char) - ord('a') + shift) % 26
                result += chr(new_pos + ord('a'))
            else:
                new_pos = (ord(char) - ord('A') + shift) % 26
                result += chr(new_pos + ord('A'))
        else:
            result += char
    
    return result

#Solution: 
def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz' 
    out = '' 
    for c in s: 
        if c in d: 
            out += d[(d.index(c)+2*2) % 26] 
        else: 
            out += c 
    return out
        
#Test Cases: 
def check(candidate):  
    # Check some simple cases 
    assert candidate('hi') == 'lm', "This prints if this assert fails 1 (good for debugging!)" 
    assert candidate('asdfghjkl') == 'ewhjklnop', "This prints if this assert fails 1 (good for debugging!)" 
    assert candidate('gf') == 'kj', "This prints if this assert fails 1 (good for debugging!)" 
    assert candidate('et') == 'ix', "This prints if this assert fails 1 (good for debugging!)"  
    assert candidate('faewfawefaewg')=='jeiajeaijeiak', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('hellomyfriend')=='lippsqcjvmirh', "This prints if this assert fails 2 (good for debugging!)" 
    assert candidate('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh')=='hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', "This prints if this assert fails 3 (good for debugging!)"  # Check some edge cases that are easy to work out by hand. assert candidate('a')=='e', "This prints if this assert fails 2 (also good for debugging!)"

if __name__ == "__main__":
    check(solution1)
    print("All tests passed for Solution 1!")
    check(solution2)
    print("All tests passed for Solution 2!")
    check(solution3)
    print("All tests passed for Solution 3!")
    check(solution4)
    print("All tests passed for Solution 4!")