def copy(original, copyfile):
    with open(original) as ogFile:
        ogFiletxt = ogFile.read()
    with open(copyfile,"w") as copyFile:
        copyFile.write(ogFiletxt)

copy("story.txt","story_copy.txt")

'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(original, copyfile):
    with open(original) as ogFile:
        ogFilereverse = reversed(ogFile.read())
        print(ogFilereverse)
    