# Method1: build a suffix array in O(nlognlogn) time
# Idea: sort all suffixes using the first 2 chars, then using the first 4 chars, then using the first 8 chars, ....
# Each sort is based on the result of the previous sort, so that each sort can be done in O(nlogn) time
# There are total O(logn) sorts need to be done
# Reference: https://www.youtube.com/watch?v=_TUeAdu-U_k

def buildSuffixArray(s):
    suffixes = [[0, 0, 0] for _ in range(len(s))] # [rank0, rank1, index]
    for i in range(len(s)):
        suffixes[i][0] = ord(s[i]) - ord('a')
        suffixes[i][1] = ord(s[i+1]) - ord('a') if i+1 < len(s) else -1
        suffixes[i][2] = i
    suffixes.sort()
    k = 4
    while k < 2*len(s):
        rank = [0 for _ in range(len(s))]
        invIdx = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if i > 0 and (suffixes[i][:2] == suffixes[i-1][:2]):
                rank[i] = rank[i-1]
            elif i > 0:
                rank[i] = rank[i-1] + 1
            invIdx[suffixes[i][2]] = i          
        for i in range(len(s)):
            suffixes[i][0] = rank[i]
            idx = suffixes[i][2] + k//2
            suffixes[i][1] = rank[invIdx[idx]] if idx < len(s) else -1
        suffixes.sort()
        k *= 2
    return [s[2] for s in suffixes]
  
if __name__ == "__main__":
    print(buildSuffixArray("banana"))

    
# Method2: build a suffix array in O(n) time using the skew algorithm (SA12)
# Idea: divide and conquer
# divide the problem into 2 sub-problems: 
#    (1) sort suffixes whose start idx % 3 != 0
#    (2) sort suffixes whose start idx % 3 == 0
# merge the 2 sorted suffixes into one as the final answer
# Time complexity recurence relationship: T(n) = T(2/3n) + O(n) => T(n) = O(n)
# Reference: https://www.youtube.com/watch?v=x6j44AtzFmU
# Reference: Simple Linear Work Suffix Array Construction, Juha Karkkainen and Peter Sanders



    

