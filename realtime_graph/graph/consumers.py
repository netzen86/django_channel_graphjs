import json
from random import randint
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer


def get_day():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    index = 0

    while True:
        yield days[index]

        index += 1

        if index > 6:
            index = 0


class GraphConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        super().__init__()
        self.days_get = get_day()

    async def connect(self):
        await self.accept()

        for i in range(1000):
            num = randint(-20, 20)
            day = next(self.days_get)
            await self.send(json.dumps({"value": num, "day": day}))
            await sleep(1)
