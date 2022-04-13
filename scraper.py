import time
import discord

TOKEN = "OTI0NDQyMTA2MDgzMzExNjE2.Yce5sw.Sgtz0bhGW4qmGrmm1D7cRnNmKVI"
# bruh moment if there are more messages than this
MESSAGE_LIMIT = 1_000_000_000_000
CHANNELS = [
    ("logic-world", 401255675264761868),
    ("builds", 901195561980543007),
    ("works-in-progress", 930935059886784532),
    ("questions", 901199821212352573),
    ("suggestions", 906825697190895646),
    ("bugs-and-issues", 901158328405729371),
    ("modding", 901659878869844048),
    ("thonk-topics", 631616731282014218),
    ("not-logic-world", 416276124977332226),
    ("also-not-logic-world", 631004929762525204),
    ("memes", 403343343775383552),
    ("spam", 428658408510455810),
    ("voice-chat", 903124059255078943),
]


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        for channel in CHANNELS:
            with open(f"data/{channel[0]}.txt", "a+") as output:
                channel = self.get_channel(channel[1])
                async for message in channel.history(limit=MESSAGE_LIMIT):
                    x = message.content.replace("\n", " <[newline]> ")
                    output.write(f"{message.author}: {x}\n")
                    # jimmy filter code
                    # if message.author.name == "Jimmy" and message.author.discriminator == "8080":
                    #     total_messages += 1
                    #     if total_messages % 100 == 0:
                    #         print(total_messages, "read")
                    #     output.write(message.content+"\n")
                    #     # print(message.content)
                    # print("total message count:", total_messages)
        await self.close()


def main():
    client = MyClient()
    client.run(TOKEN, bot=False)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
