from cloudywords import CloudyWords

__author__ = 'lus'

def main():
    cw = CloudyWords()

    # add phrase.
    cw.addWords("""
    his is a fantastic phrase, it has been popular and it has worked; testing now starts earlier and testing has a higher profile than ever before, but despite all that, it isn't what we meant or even what we really needed.
    Back in the depths of despair that was the Software Crisis. Testers managed to bellow a rallying cry "Testing should start early!" Testers could be found picketing management and development meetings with 'V-model' placards and T-shirts with 'cost of defect' bar charts emblazoned.
    """)

    # add one word.
    cw.addWords('testing')

    res = cw.cloud()

    # slice out out first 5 elements
    res = res[:5]

    # print whole result
    print res
    print '------------------------------------------------------'

    # if you wanna know weight:
    for word in res:
        # print word and it's weight.
        print word + ' '+ str(cw.weight[word])

if __name__ == "__main__":
    main()