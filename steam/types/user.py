from typing_extensions import TypedDict


class UserDict(TypedDict):
    steamid: str
    personaname: str
    primaryclanid: str
    profileurl: str
    realname: str
    # enums
    communityvisibilitystate: int
    profilestate: int
    commentpermission: int
    personastate: int
    personastateflags: int
    # avatar
    avatar: str
    avatarmedium: str
    avatarfull: str
    avatarhash: str
    # country stuff
    loccountrycode: str
    locstatecode: int
    loccityid: int
    # game stuff
    gameid: str  # game app id
    gameextrainfo: str  # game name
    # unix timestamps
    timecreated: int
    lastlogoff: int
    # we pass these ourselves
    last_logon: int
    last_seen_online: int
    rich_presence: dict[str, str]
