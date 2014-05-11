def verify_anagrams(word1, word2):
    d = dict()
    word1 = word1.upper()
    word2 = word2.upper()
    for i in range(len(word1)):
        if word1[i] != ' ':
            if word1[i] in d:
                d[word1[i]] += 1
            else:
                d[word1[i]] = 1
    for i in range(len(word2)):
        if word2[i] != ' ':
            if word2[i] in d:
                d[word2[i]] -= 1
            else:
                return False
    return len([v for v in d.values() if v != 0]) == 0

if __name__=='__main__':
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "First"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Second"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "Third"
