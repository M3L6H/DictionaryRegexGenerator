# Dictionary Regex Generator
A simple script that generates a regular expression for the passed dictionary.

This is useful for creating a dictionary of words to spell check against for example.

If there is a list of words that need to be recognized, this will do it.

## How to use

With a file "dictionary.txt" containing the following:

```
emphasis
elephant
emerge
entrance
South
Southern
she
sells
shells
California
```

Run the command `python main.py "./dictionary.txt"` in the directory containing this script. You will find the output in "out.txt". With the above input, it would look something like this:

```
(?:e(?:lephant|m(?:phasis|erge)|ntrance)|South(?:ern)|s(?:he(?:lls)|ells)|California)
```
