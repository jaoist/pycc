favorite_languages = {
    'jen' : 'python',
    'sarah' : 'ruby',
    'edward' : 'c',
    'phil' : 'python',
    }

# Looping through key-value pairs.
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title()+ ".")

print("\n")

# Looping through keys.
for name in favorite_languages.keys():
    print(name.title())

print("\n")

# Default behavior in python when looping through dict without calling method
# is to access keys.
for name in favorite_languages:
    print(name.title())

# Accessing values associated with keys or values of interest.
friends = ['sarah', 'phil']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

# Use keys method to check for value.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through dictionary keys in (alphabetical)order. Use sorted().
for  name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through all values in a dict.
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Find all unique values in a dict, use set().
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())