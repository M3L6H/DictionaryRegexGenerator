# Dictionary Regex Generator
A simple script that generates a regular expression for the passed dictionary.

This is useful for creating a dictionary of words to spell check against for example.

If there is a list of words that need to be recognized, this will do it.

## How to use

With a file "dictionary.txt" containing the following:

```Text
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

```Regular Expression
/(?:California|South(?:|ern)|e(?:lephant|m(?:erge|phasis)|ntrance)|s(?:ells|he(?:|lls)))/
```

## Flags

Using the `-i` or `--insensitive` flag will convert any upper case words to lower case. Note that it does not automatically add the insensitive flag to the regular expression.

Using the `-w` or `--whole` flag will generate a regular expression that only matches to whole words.

## Speed

The regular expression was tested with ECMAScript. A [10,000 word dictionary](https://www.mit.edu/~ecprice/wordlist.10000) was used and it was matched against [*Beowolf*](http://www.gutenberg.org/cache/epub/16328/pg16328.txt) which has 42,596 words and [*Pride and Predjudice*](https://www.gutenberg.org/files/1342/1342-0.txt) with 124,961 words.

With *Beowolf* the match completed in **114ms**.

*Pride and Predjudice* took a little longer at **197ms**.

The line given by these points has equation
```Mathematica
y=0.001x + 71.1
```
which indicates a base run-time of **71.1ms** for the regular expression, regardless of input size.
