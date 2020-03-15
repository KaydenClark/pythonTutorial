msg = input('> ')
words = msg.split(' ')

emojis = {
    ':)': '😀',
    ':D': '😁',
    'LOL': '😂',
    ':|': '😑',
    "':)": '😅',
    'XD': '😆',
    ';)': '😉',
    'B)': '😎',
    ":'(": '😭'
}

printMsg = ''

for word in words:
    printMsg += emojis.get(word, word) + ' '

print(printMsg)