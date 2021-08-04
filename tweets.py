tweets = [
    "Hi! \nHere I show how you can write a thread in a txt file and publish it. 🧵 ⬇️⬇️⬇️ \n#python #twitterapi",
    "This thread itself has been generated automatically. \nNote that the numeration of the tweets is also automatic!",
    "First, have a look at the text file ⤵️. It contains two lists: 'tweets' and 'media'",
    "1️⃣ 'tweets' is a list of strings. Each string is one tweet",

    "A tweet can contain a URL, for example the address to this project's repo: https://github.com/E-Dmz/ThreadFromATextFileScript",
    "2️⃣ 'media' is a list of lists. It contains the relative paths (strings) of up to 4 PNG/JPG files (or 1 GIF file) you want to embed.",
    "There should be as many elements in 'tweets' as in 'media': use an empty list if you don't want to embed an image in a tweet.",
    "⏩ Now, have a look at the script ⤵️.",

    "It loops across the tweets. The first tweet is different (the beginning and the end differ). \n\
Most importantly, the first tweet is not a reply to another tweet ('None'), while the others are replies to the previous one ('status.id').",
    "Do you like this method? Please try it, comment, retweet and follow me! #python #twitterapi",
]

media = [
    [],
    [],
    ['Screenshot_tweets_and_media.png'], 
    [],
    
    [],
    ['1.png', '2.png', '3.png', '4.png'],
    [],
    ['Screenshot_notebook.png'],

    [],
    [],
]

