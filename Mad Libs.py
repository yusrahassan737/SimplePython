# Name: Yusra Hassan
# Date: Created June 21, 2020; Edited Nov.25, 2020 and Apr.23, 2021 for coding form, commenting and clarity of messages
# Description: A simple mad libs made from the "Twinkle Twinkle Little Star" nursery rhyme
# Purpose: Fun, Practice with input slices

# Starting message
print("""
  This program turns the \"Twinkle, Twinkle, Little Star\" song into a Mad Libs!
  How creative can you get? Bonus points if you can still make it rhyme!
  For best results, use lower case, avoid typos and follow the syllables indications
  When asked for multiple words, separate with a comma and a space ONLY
""")

# Variables/ Input
inputtedNouns = input("\nGive me three nouns. (1 syll, 2 sylls, 1 syll)\n")
nouns = inputtedNouns.split(", ")
inputtedAdjectives = input("\nGive me three adjectives. (2 sylls, 1 syll, 2 sylls)\n")
adjectives = inputtedAdjectives.split(", ")
verb = input("\nGive me a 2-syllable verb.\n")
fiveW = input("\nGive me one of the 5 Ws.\n")

# Form and print the new nursery rhyme
story = [
  "\n" + verb + ", " + verb + ", " + adjectives[0] + " star,",
  "how I wonder " + fiveW + " you are!",
  "Up above the " + nouns[0] +  " so " + adjectives[1] + ",",
  "like a " + nouns[1] + " in the " + nouns[2] + ".",
  verb + ", " + verb + ", " + adjectives[2] + " star",
  "how I wonder " + fiveW + " you are!"
]
for i in story:
    print(i)
