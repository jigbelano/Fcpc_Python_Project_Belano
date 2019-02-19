
BadWords = ['fuckshit', 'bullshit', 'idiot', 'bobo', 'bovo', 'weaklings', 'Mama mo', 'bitch', 'shitty',
              'impakto', 'torjakin', 'gayshit']
sentence = input('Enter your sentence: ')
print('------------------------------------')
new = [x for x in sentence.lower().split()]
text = ''
for word in new:
    if word in Badwords:
        a = len(word)
        text += '*' * a + ' '
    else:
        text += word + ' '
print(text)
