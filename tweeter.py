from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials


# Twitter Stream
class TwitterStreamer:
    """Class that streams and processes live tweets"""
    def stream_tweets(self, tweets_filename, keyword_list):
        listener = AndListener(tweets_filename)
        # authentication occurs here
        auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(credentials.ACCES_TOKEN, credentials.ACCES_TOKEN_SECRET)

        stream = Stream(auth, listener)
        stream.filter(track= keyword_list)


# Stream Listener Class #
class AndListener(StreamListener):
    """Class that saves tweets into json file """
    def __init__(self, tweets_filename):
        self.tweets_filename = tweets_filename

    def on_data(self, data):
        try:
            with open(self.tweets_filename, 'a') as f:
                f.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # returning False on_data method in case rate limet occurs
            return False
        print(status)


if __name__ == "__main__":

    keyword_list = ["corona", "economy", "re-opening"]
    tweets_filename = "tweets.json"
    # streamer object
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(tweets_filename, keyword_list)