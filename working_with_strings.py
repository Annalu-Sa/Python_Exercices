#Working with Strings:
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper()) #two functons in serie
print(len(phrase)) #how may char there are insede this
print(phrase[0]) #get the first charr of the string; string get index startedin zero
print(phrase.index("Acad")) #will retun the index of where some string start
print(phrase.replace("Giraffe", "Elephant")) #first value is the thing we will substitute