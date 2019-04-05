def split_tweet(message):
    start = 0
    length = len(message)
    raw_math = length / 140
    num_tweets = int(raw_math)
    if(raw_math % 1 > 0):
        num_tweets = num_tweets + 1
    split_message = []
    for i in range(0, num_tweets):
        start = i * 140
        sub_tweet = ""
        iterate = 0
        for j in range(0, 140):
            if(start + j == length): #stop if we've reached the end
                break
            sub_tweet = sub_tweet + message[start + j]
        split_message.append(sub_tweet)
    return split_message
    

def main():
    message = str(input())
    split_message = split_tweet(message)
    for i in range(0, len(split_message)):
        print(split_message[i], end="///\n")
    print("\n")

main()