def countWords(text):
    words = text.split()
    return len(words)

def countChars(text):
    countDict = {}
    for char in text:
        lowerChar = char.lower()
        if lowerChar in countDict:
            countDict[lowerChar] += 1
        else:
            countDict[lowerChar] = 1

    return countDict

def sortDict(dictionary):
    sort = dict(reversed(sorted(dictionary.items(), key=lambda item: item[1])))
    # Create a set that contains alphabetical characters
    alphabet = {
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
                }
    alphabetSort = {}
    for char in sort:
        if char in alphabet:
            alphabetSort[char] = sort[char]
        else:
            continue
    return alphabetSort

def displayDict(dictionary):
    for char in dictionary:
        print(f"The '{char}' character was found {dictionary[char]} times")

def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    wordCount = countWords(file_contents)
    characterCount = countChars(file_contents)
    sortedDict = sortDict(characterCount)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in the document\n")
    displayDict(sortedDict)
    print("--- End report ---")

main()
