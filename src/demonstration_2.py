"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).
​
You need to write a function that, given a sequence of words written in this
secret language, and the order of the alien alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.
​
The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".
​
Example 1:
​
{
    0: 'h',
    1: 'l',
    2: 'a',
    ...
    18: 's',
}
​
```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```
​
{
    'h': 0,
    'a': 1
    ...
    'e': 5,
    ...
    's': 18,
    'w': 22,
}
​
Example 2:
​
```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```
​
Example 3:
​
```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```
​
Notes:
​
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str
​
    Output:
    bool
    """
    # Your code here
    # if alpha_order is just the normal alphabet, then 
    # we could just do a normal is_sorted check on the words in the 
    # words list 
​
    # we need to figure out how to represent the alternate ordering 
​
    # we can keep track of the alternate ordering of letters with a 
    # hash table where the keys are the letters and the values are 
    # the letter's index in the alternate alphabet 
​
    # create the lookup table 
    # doing the same thing using a comprehension 
    # lookup_table = {letter: index for index, letter in enumerate(alpha_order)}
    lookup_table = {} 
​
    for index, letter in enumerate(alpha_order):
        lookup_table[letter] = index
​
    # do an is_sorted check but refer to the alternate ordering instead 
    return is_sorted(words, lookup_table)
​
# checks to see if the words in the list are sorted according 
# to the ordering specified by the lookup table 
def is_sorted(words, lookup_table):
    # iterate through our words list two at a time 
    for i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]
​
        # iterate through the chars of the two words we're comparing 
        # we only need to iterate up through the length of the smaller word 
        length_of_shorter_word = min(len(word1), len(word2))
​
        for k in range(length_of_shorter_word):
            # check that the current letter in the first word < the current letter 
            letter1 = word1[k]
            letter2 = word2[k]
​
            # of the next word, according to our lookup table 
            if lookup_table[letter1] > lookup_table[letter2]:
                return False 
​
            # if at any point this isn't the case, return False 
            # otherwise, move on to the next char in each word
​
        # if we get outside this for loop without ever returning false 
        # check if word1's length < word2's length 
        if len(word1) > len(word2):
            return False 
​
    return True 