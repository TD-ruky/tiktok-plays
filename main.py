from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
import json

from keyActions import keyAction
from screenActions import screenAction

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@botsgames")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)




# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")
    with open("data.json", "r") as infile:
        data = json.load(infile)

    # modify data
    if event.user.nickname in data:
        data[event.user.nickname]["posts"] += 1
    else:
        data[event.user.nickname]={"posts" : 1}

    keyAction(event.comment)
    screenAction(event.comment)
    
    # open json file to write
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)



# Define handling an event via "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()