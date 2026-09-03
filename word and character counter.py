text=input("enter your text:")
if text=='':
    print("enter some sentence")
else:
    character=len(text)
    word=len(text.split())
    space=text.count("")
    sentences=text.count('.')+text.count("!")+ text.count("?")

    print("character",character)
    print("word",word)
    print("space",space)
    print("sentence",sentences)


