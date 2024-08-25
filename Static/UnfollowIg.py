import instaloader
import json
from dotenv import load_dotenv
from datetime import datetime
import os
import ctypes
import time

# Instructions

# U only need to configure the environment variables on ur computer or in a .env file (named Authentication.env).
# Another option it's delete the code (except the librarys imports) just before the line L = instaloader.Instaloader and write the following lines there (whithout the symbol #):
# username= ('your Instagram username here')
# password= ('your Instagram password here')
# With this in mind, u can now run the code, which will tell you who unfollowed you and create two .json files with a dictionary of your followers and unfollowers.
# Be careful, don't overuse executions, as Instagram's API may cause issues with your acc.

load_dotenv('Authentication.env')
username = os.getenv('INSTA_USERNAME')
password = os.getenv('INSTA_PASSWORD')

if not username or not password:
    raise ValueError("Credentials are not configured. Please set the INSTA_USERNAME & INSTA_PASSWORD environment variables.")

L = instaloader.Instaloader()

try:
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, username)
except instaloader.exceptions.ConnectionException as e:
    print(f"Connection error: {e}")
    exit(1)

followers = {follower.username: datetime.now().strftime('%Y-%m-%d') for follower in profile.get_followers()}

try:
    with open('followers_history.json', 'r') as f:
        old_followers_history = json.load(f)
except FileNotFoundError:
    old_followers_history = {}

unfollowers = []
for old_follower, dates in old_followers_history.items():
    if old_follower not in followers:
        unfollowers.append((old_follower, dates[-1]))  # last follow date

# Update followers history
for follower, date in followers.items():
    if follower in old_followers_history:
        old_followers_history[follower].append(date)
    else:
        old_followers_history[follower] = [date]

# Sort history alphabetically
sorted_followers_history = dict(sorted(old_followers_history.items()))

with open('sorted_followers_history.json', 'w') as y:
    json.dump(sorted_followers_history, y, indent=4)

with open('unfollowers.json', 'w') as z:
    json.dump(unfollowers, z, indent=4)

# Show the number of old and current followers
old_followers_count = len(old_followers_history)
current_followers_count = len(followers)

print(f"Followers before: {old_followers_count}")
print(f"Followers now: {current_followers_count}")
print(f"Unfollowers: {unfollowers}")
print("Process completed.")

# Create the message
message = f"Followers before: {old_followers_count}\nFollowers now: {current_followers_count}\nUnfollowers: {unfollowers}\nProcess completed."

# Display the message in a MessageBox
ctypes.windll.user32.MessageBoxW(0, message, "UnfollowIg Results", 0x40 | 0x1)

