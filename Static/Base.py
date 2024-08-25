import instaloader
import json

L = instaloader.Instaloader()
username = 'here'
password = 'and here'
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, username)
followers = [follower.username for follower in profile.get_followers()]
try:
    with open('followers.json', 'r') as f:
        old_followers = json.load(f)
except FileNotFoundError:
    old_followers = []
unfollowers = set(old_followers) - set(followers)
if unfollowers:
    unfollowers_list = '\n'.join(unfollowers)
with open('followers.json', 'w') as f:
    json.dump(followers, f)
with open('unfollowers.json', 'w') as z:
    json.dump(list(unfollowers), z)