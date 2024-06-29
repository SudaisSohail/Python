import re

text = """

abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Metacharacters (need to be escaped):
. ^ $ * + ? \ | ( ) { } [ ]

sudaisahmed710@gmail.com

0333-9847521
0321.1147609

https://www.google.com
http://sudais.gov
https://youtube.com
http://www.cbek.edu

Mr. Ammar
Mr Abdul Musawwir
Mrs Dayan
Ms Hamza
Mrs. Saqlain
"""

sentence = 'Start a sentence and then bring the sentence to an end'

pattern1 = re.compile(r"abc")
phone_num_pat = re.compile(r"\d{4}[-.]\d{7}")   # Pattern to match a phone number
email_pat = re.compile(r'[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-z]+')    # Pattern to match an email
url_pat = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
name_pat = re.compile(r"(Mr|Mrs|Ms)\.?[A-Za-z]+[^\.][A-Za-z]")
pattern2 = re.compile(r"Start ")
pattern3 = re.compile(r"sentence")

match1 = pattern1.findall(text)      # Only gives the match, if match is not there, returns nothing
match2 = pattern1.finditer(text)     # finditer also gives the details about the match, if match is not there, returns nothing
match3 = phone_num_pat.finditer(text)
match4 = email_pat.findall(text)
match5 = url_pat.finditer(text)
match6 = name_pat.finditer(text)
match7 = pattern2.match(sentence)    # Match searches the pattern from the beginning of the string
match8 = pattern3.match(sentence)    # Match returns nothing if the pattern is not matched
match9 = pattern3.search(sentence)   # Returns only the first match and ignores the rest matches

for match in match1:
    print(match)

for matched in match2:
    print(matched)
    
for i in match3:
    print(i)
    
for e in match4:
    print(e)

for url in match5:
    print(url.group(3))  # Returns only the third group from the search
    
subbed_urls = url_pat.sub(r"\2\3", text)  # Returns group 2 and group 3 of all the searches of urls in the text
print(subbed_urls)

for name in match6:
    print(name)

print(match7)
print(match8)
print(match9)

flag1 = re.compile(r"StaRt", re.IGNORECASE)  # Doesn't care about upper or lower case leeters; becomes case insensitive or {re.I}
flagged = flag1.findall(sentence)
for flag in flagged:
    print(flag)
    
flag2 = re.compile(r"^M*", re.MULTILINE)  # Considers each line as a separate string; Carrot matches "M" on beginning of each line instead 
# of the whole string. Can also be written as {re.M}

flagged = flag2.findall(text)
for flag in flagged:
    print(flag)
    
flag3 = re.compile(r"123.*", re.DOTALL) # "." also matches newline characters. Can also be written as {re.S}
flagged = flag3.findall(text)
for flag in flagged:
    print(flag)
    
flag4 = re.compile(r"\w+ # This is a comment", re.VERBOSE)  # Does not cosider spaces and allows to write comments {re.X}
flagged = flag4.findall(text)
for flag in flagged:
    print(flag)


"""
.         -> Any Character Except Newline
\d        -> Digit (0, 9)
\D        -> Not a Digit (0, 9)
\w        -> Word Character (a-z, A-Z, 0-9, _)
\W        -> Not a Word Character
\s        -> Whitespace (space, tab, newline)
\S        -> Not Whitespace (space, tab, newline)

\b        -> Word Boundary
\B        -> Not a Word Boundry
^         -> Beginning of a string
$         -> End of a string

[]        -> Matches characters in brackets    
[^ ]      -> Matches characters NOT in brackets
|         -> Either Or
( )       -> Group

Quantifiers:

*         -> 0 or More
+         -> 1 or More
?         -> 0 or 1
{3}       -> Exact Number
{3, 4}    -> Range of numbers (Minimum, Maximum)

"""