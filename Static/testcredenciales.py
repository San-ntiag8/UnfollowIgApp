from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv('Authentication.env')

# Check if the variables have been loaded correctly
print("Environment variables loaded:")
for key, value in os.environ.items():
    if key in ['INSTA_USERNAME', 'INSTA_PASSWORD']:
        print(f'{key}: {value}')

username = os.getenv('INSTA_USERNAME')
password = os.getenv('INSTA_PASSWORD')

print(f'username: {username}')
print(f'password: {password}')

