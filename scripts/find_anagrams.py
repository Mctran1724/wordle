def findAnagram(array):
    #Use a standard trick: anagrams are equal when sorted.
    #Then sort the array so that anagrams are close to each other.
    sortedWords = ["".join(sorted(word)) for word in array]
    #sortedWords.sort()
    
    from collections import Counter
    
    return Counter(sortedWords)

if __name__=="__main__":
    from playWordle import loadAnswers
    import csv
    d = findAnagram(loadAnswers())
    with open("anagram_counts.csv", "w+") as f:
        for key, value in sorted(d.items(), key = lambda x: x[-1], reverse=True):
            f.write(f"{key},{value}\n")

