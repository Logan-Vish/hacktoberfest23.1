# Importing Libraries
import instaloader
import pandas as pd

USERNAME = ""
PASSWORD = ""

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
bot.login(user=USERNAME, passwd=PASSWORD)

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, USERNAME)

# Retrieving the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Converting the data to a DataFrame
followers_df = pd.DataFrame(followers)

# Storing the results in a CSV file
followers_df.to_csv('followers.csv', index=False)

# Retrieving the usernames of all followings
followings = [followee.username for followee in profile.get_followees()]

# Converting the data to a DataFrame
followings_df = pd.DataFrame(followings)

# Storing the results in a CSV file
followings_df.to_csv('followings.csv', index=False)

df_followers = pd.read_csv("./followers.csv")
df_followings = pd.read_csv("./followings.csv")
followers = list(df_followers.iloc[:,0].values)
followings = list(df_followings.iloc[:,0].values)

non_followers = sorted([acc for acc in followings if acc not in followers])
print(len(non_followers))
print(*non_followers, sep="\n")
