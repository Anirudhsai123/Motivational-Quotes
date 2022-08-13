def main(inputs):
    import random
    numbers = list(range(0, 10))
    random.shuffle(numbers)
    a = numbers.pop()
    quote = ['''Nothing is impossible, the word itself says i'm possible.''',
             'Reach for the moon, you will land among the stars.',
             'Failure is just a step to success.',
             '''Tomorrow is a mystery, yesterday is a mystery, today is a gift.
             that is why it is called the ''present''. - Oogway ''',
             'It always seems impossible until it is done. - Nelson Mandela',
             '''It's not the years in your life that count.
             It's the life in your years. - Abraham Lincoln''',
             '''Your time is limited, so don't waste it living someone
             else's life. - Steve Jobs''',
             '''However difficult life may seem, there is always something
             you can do and succeed at. - Stephen Hawking''',
             '''Happiness is not something readymade, it comes
             from your own actions. - The Dalai Lama''',
             '''Believe you can and you're halfway there.
             - Theodore Roosevelt''',
             '''All our dreams can come true, if we have the courage to
             pursue them. - Walt Disney''']
    actualquote = quote[a]
    if a > 20:
        print('lol')
    return {
        "quote": actualquote
    }
print(main())
