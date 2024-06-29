languages = ["Java" , "C++" , "C" , "Python" , "JavaScript"]

print("What are you looking for?")

lang = input()

for language in languages:
    print(language)
    if language == lang:
        print("we found" , lang)
        break
else:
    print(lang , "not found")