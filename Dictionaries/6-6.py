# Poll friends favorite languages. Create list of names. 
# If name does not have favorite language, 
# print a message saying that they should take the poll.

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'ruby',
    'edward' : 'c',
    'phil' : 'python',
    }

friend_list = ['jackson', 'desmond', 'rutherford', 'sarah', 'niles', 'edward',
    'phil', 'jen']

for name in friend_list:
    if name in favorite_languages.keys():
        print("Thanks for taking the programming poll, " + name.title()) + "."
    else:
        print("Bummer! " + name.title() + ", you should really take the poll.") 