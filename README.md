# CloudyWords
word's/tag's cloud in Python for Humans.

# Introduction
even wondered what words are most popular in particular string/document, entries ?
Now it's easy to find out with **CloudyWords**.

#Usage
    from cloudywords import CloudyWords
    cw = CloudyWords()

    # add phrase.
    cw.add_words("""
    his is a fantastic phrase, it has been popular and it has worked; testing now starts earlier and testing has a 
    higher profile than ever before, but despite all that, it isn't what we meant or even what we really needed.
    Back in the depths of despair that was the Software Crisis. Testers managed to bellow a rallying cry "Testing 
    should start early!" Testers could be found picketing management and development meetings with 'V-model' 
    placards and T-shirts with 'cost of defect' bar charts emblazoned.""")

    # add one word.
    cw.add_words('testing')

    res = cw.cloud()

    # slice out out first 5 elements
    res = res[:5]

    # print whole result
    print res
    print '------------------------------------------------------'

    # if you wanna know weight:
    for word in res:
        # print word and it's weight.
        print '{} {}'.format(word, cw.weight[word])

**Result:**

    ['testing', 'testers', 'worked', 't-shirts', 'starts']
    ------------------------------------------------------
    testing 3
    testers 2
    worked 1
    t-shirts 1
    starts 1

### Please feel free to improve it if you like :)
