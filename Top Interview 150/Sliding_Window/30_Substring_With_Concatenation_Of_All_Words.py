"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
We return an empty array.
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
"""
To solve this problem, we can use a sliding window approach along with a hashmap to efficiently check if the current substring is a concatenated substring:
First, we create a hashmap word_count to store the frequency of each word in the words array.
Then, we iterate over each possible starting index of the substring in s.
For each starting index, we iterate through substrings of length len(words) * len(words[0]) (the total length of concatenated words) and check if the substring forms a concatenated substring.
To check if the substring is a concatenated substring, we maintain a hashmap substring_count to keep track of the frequency of words encountered in the current substring. We compare substring_count with word_count to see if they are identical. If they are identical, it means the substring is a concatenated substring.
If a substring is found to be a concatenated substring, we append the starting index to the result list.
Finally, we return the result list containing the starting indices of all concatenated substrings found.
"""
class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        word_length = len(words[0])
        total_length = len(words) * word_length
        result = []

        for i in range(len(s) - total_length + 1):
            substring_count = {}
            j = 0
            while j < total_length:
                word = s[i + j:i + j + word_length]
                if word not in word_count:
                    break
                substring_count[word] = substring_count.get(word, 0) + 1
                if substring_count[word] > word_count.get(word, 0):
                    break
                j += word_length
            if j == total_length:
                result.append(i)

        return result
        
solution = Solution()
# Test Case 1
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(solution.findSubstring(s1, words1))  # Output should be [0, 9]

# Test Case 2
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(solution.findSubstring(s2, words2))  # Output should be []

# Test Case 3
s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(solution.findSubstring(s3, words3))  # Output should be [6, 9, 12]