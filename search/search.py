import tweepy
import datetime as dt

class Twitter:

        

        # Function to get the latest tweet from a famous person
        def get_tweet(self,username):
            api_key = "5B5oMakIfY7zuEmDOSP3kEtwQ"
            api_key_secret = "0uamoFuHuLuLO0vgoCrp15zQFYoozKdfy3zzBvZIdVxOdwXhux"
            bearer_token = "AAAAAAAAAAAAAAAAAAAAAOytVgEAAAAAdtgMgAJhL5oBe0W3gU7fKBatO%2FU%3DvmreUDfnLZP7N5oqkR3FBXpCKbZURyn7VLlEUwbLDsRv5G8Szg"
            # api_secret_key = "eGPOjCkIMIMOvrSK7jdvLgDc2doxMIQDstIVjoCG9wq7OTTa5d"
            access_token = "1019687701505806336-UtbYhXqaXeqfihp5SZcXR3ekJpWgwJ"
            access_token_secret = "5viru95PIbuoFROPBSUbfFRy5S8zn1CT7e5Y0EkC6tPmn"

            # Authenticate to Twitter
            auth = tweepy.OAuthHandler(api_key, api_key_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)

          
            begin_date = dt.date(2021, 9, 1)
            end_date = dt.date(2021, 11, 1)
            limit = 10000
            lang =  "english"


            tweets = []
            likes = []
            time = []
            user = username
            tweets= []

            for i in tweepy.Cursor(api.user_timeline, id=user, tweet_mode="extended").items(limit):
                tweets.append(i.full_text)
                likes.append(i.favorite_count)
                time.append(i.created_at)



            return tweets


















       
