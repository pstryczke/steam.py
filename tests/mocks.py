"""A collection of custom mock objects"""

from typing import Optional
from unittest.mock import MagicMock

import steam
from steam.protobufs.chat import IncomingChatMessageNotification, State

from .test_bot import bot

USER_DATA = {
    "steamid": 1234567890,
    "personaname": "a user",
    "avatarfull": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/fe/"
    "fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_full.jpg",
    "primaryclanid": 103582791443703793,
    "timecreated": 0,
    "lastlogoff": 0,
    "gameextrainfo": "Testing steam.py",
    "gameid": 1337,
    "personastate": 1,
    "communityvisibilitystate": 3,
    "commentpermission": True,
    "profilestate": True,
}


class DataclassesMock:
    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            if item in self.__slots__:
                return MagicMock(name=item)
            raise


class MockUser(steam.User, DataclassesMock):
    def __init__(self):
        super().__init__(bot._connection, USER_DATA)


class MockGroup(steam.Group, DataclassesMock):
    def __init__(self):
        super().__init__(bot._connection, 0)
        self.name = "a group"


class MockGroupChannel(steam.GroupChannel, DataclassesMock):
    def __init__(self, group):
        proto = State(
            chat_id=0,
            chat_name="a group channel",
        )
        super().__init__(bot._connection, group=group, proto=proto)


class MockMessage(steam.Message, DataclassesMock):
    def __init__(self, channel, content: Optional[str] = None):
        proto = IncomingChatMessageNotification(message=content or "a message")
        steam.Message.__init__(self, channel, proto)
        self.author = USER


class MockDMMessage(MockMessage, steam.UserMessage):
    pass


class MockClanMessage(MockMessage, steam.ClanMessage):
    pass


class MockGroupMessage(MockMessage, steam.GroupMessage):
    pass


USER = MockUser()
GROUP = MockGroup()
GROUP_CHANNEL = MockGroupChannel(GROUP)
GROUP._channels = {GROUP_CHANNEL.id: GROUP_CHANNEL}
GROUP_MESSAGE = MockGroupMessage(GROUP_CHANNEL)

TEST_COMMAND_MESSAGE = MockGroupMessage(GROUP_CHANNEL, "!test command")
