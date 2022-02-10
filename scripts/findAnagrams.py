def findAnagram(array):
    #Use a standard trick: anagrams are equal when sorted.
    #Then sort the array so that anagrams are close to each other.
    sortedWords = [sorted(word) for word in array]
    

if __name__=="__main__":
    import playWordle