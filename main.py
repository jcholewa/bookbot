def getText():
  with open('books/frankenstein.txt') as f:
    return f.read()

file_contents = getText()

def printFrankenstein():
  print(file_contents)

def numWords():
  words = file_contents.split()
  return len(words)

def countLetters():
  dictionary = {}
  for char in file_contents:
    char = char.lower()
    if char not in dictionary.keys():
      dictionary[char] = 1
    else:
      dictionary[char] += 1
  return dictionary

def sortCharCounts():
  dictionary = countLetters()
  charsInList = [(k, v) for k, v in dictionary.items()]
  charsInList.sort(key = lambda x: (-x[1], x[0]))
  for char in charsInList:
    if char[0].isalpha():
      print(f'The \'{char[0]}\' character was found {char[1]} times')


def printReport():
  print('--- Begin report of books/frankenstein.txt ---')
  numOfWords = numWords()
  print(f'{numOfWords} words found in the document')
  sortCharCounts()
  print('--- End report ---')

printFrankenstein()
countLetters()
printReport()

