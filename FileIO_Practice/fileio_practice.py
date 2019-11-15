def copy(original, copyfile):
    with open(original) as ogFile:
        ogFiletxt = ogFile.read()
    with open(copyfile,"w") as copyFile:
        copyFile.write(ogFiletxt)

copy("story.txt","story_copy.txt")

def copy_and_reverse(original, copyfile):
    with open(original) as ogFile:
        reverseFile = ogFile.read()[::-1]
    with open(copyfile,"w") as copyFile:
        copyFile.write(reverseFile)

copy_and_reverse("story.txt","story_copy.txt")

def statistics(txtfile):
    linecount = 0
    wordcount = 0
    charcount = 0
    with open(txtfile) as File:
        for lines in File:
            linecount += 1
            for char in lines:
                charcount += 1
            words = lines.split()
            for word in words:
                wordcount += 1
    stats = dict([("lines", linecount),("words", wordcount),("characters", charcount)])
    return stats
    
print(statistics("story.txt"))

def find_and_replace(txtfile, ogWord, newWord):
    with open(txtfile,"r+") as File:
        txt = File.read()
        newFile = txt.replace(ogWord, newWord)
        File.seek(0)
        File.write(newFile)
        File.truncate()
                    

find_and_replace("story.txt", "boy", "girl")