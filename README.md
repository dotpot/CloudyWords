# CloudyWords
word's/tag's cloud in Python for Humans.

# Introduction
even wondered what words are most popular in particular string/document, entries ?
Now it's easy to know with **CloudyWords**.

#Usage
    from cloudywords import CloudyWords
    cw = CloudyWords()

    # Add phrase.
    cw.addWords("""
    his is a fantastic phrase, it has been popular and it has worked; testing now starts earlier and testing has a higher profile than ever before, but despite all that, it isn't what we meant or even what we really needed.
    Back in the depths of despair that was the Software Crisis. Testers managed to bellow a rallying cry "Testing should start early!" Testers could be found picketing management and development meetings with 'V-model' placards and T-shirts with 'cost of defect' bar charts emblazoned.
    """)

    cw.addWords('testing')

    res = cw.cloud()

    # slice out out first 5 elements
    res = res[:5]

    for r in res:
        # print word and it's weight.
        print r + ' '+ str(cw.wordsHash[r])

    # print whole list
    print res

**Result:**

    testing 3
    testers 2
	worked 1
	t-shirts 1
	starts 1
	['testing', 'testers', 'worked', 't-shirts', 'starts']

### Please feel free to improve it if you like :)

![image](http://img193.imageshack.us/img193/5605/tumblrlznr805hcb1r3zat8.png)