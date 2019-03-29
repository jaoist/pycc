# Using arbitrary keyword arguments. ** followed by an argument creates an empty
# dictionary with the name of the argument.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): # key/value from user_info 
        profile[key] = value
    return profile

user_profile = build_profile('david', 'koresh', location = 'texas',
                                occupation = 'cult leader')

print(user_profile)