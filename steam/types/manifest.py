"""Licensed under The MIT License (MIT) - Copyright (c) 2020 James. See LICENSE"""

from __future__ import annotations

from multidict import MultiDict
from typing_extensions import Any, Literal, NotRequired, Required

from .vdf import TypedVDFDict, VDFDict, VDFInt, VDFList


class GameInfoDict(TypedVDFDict):
    appid: str
    common: CommonDict
    extended: NotRequired[ExtendedDict]
    config: VDFDict
    depots: DepotDict | VDFDict
    ufs: MultiDict[VDFInt]
    sysreqs: MultiDict[MultiDict[Any]]
    localization: MultiDict[MultiDict[VDFDict]]


Bools = Literal["0", "1"]


class CommonDict(TypedVDFDict, total=False):
    name: Required[str]
    type: Required[str]
    has_adult_content: Bools
    has_adult_content_violence: Bools
    market_presence: Bools
    workshop_visible: Bools
    community_hub_visible: Bools
    community_visible_stats: Bools
    controller_support: Literal["full", "partial", "none"]
    associations: VDFList[CommonDictAssociations]
    languages: MultiDict[Bools]
    steam_release_date: str
    review_score: str
    review_percentage: str
    oslist: str
    icon: str
    logo: str
    parent: int


class CommonDictAssociations(TypedVDFDict):
    name: str
    type: str


class ExtendedDict(TypedVDFDict, total=False):
    isfreeapp: Bools
    listofdlc: str
    homepage: str


class DepotDict(TypedVDFDict, total=False):
    name: str
    config: Required[MultiDict[str]]
    manifests: MultiDict[VDFInt]  # {branch name: id}
    encryptedmanifests: MultiDict[MultiDict[VDFInt]]  # {branch name: {encrypted_gid2: VDFInt}}
    branches: MultiDict[BranchDict]
    maxsize: VDFInt
    depotfromapp: VDFInt
    sharedinstall: VDFInt  # bool
    system_defined: VDFInt  # bool


class BranchDict(TypedVDFDict):
    buildid: VDFInt
    timeupdated: VDFInt
    pwdrequired: NotRequired[bool]
    description: NotRequired[str]


class PackageInfoDict(TypedVDFDict):
    packageid: int
    billingtype: int
    licensetype: int
    status: int
    extended: ExtendedPackageInfoDict
    appids: VDFList[int]
    depotids: VDFList[int]
    appitems: VDFList[int]


class ExtendedPackageInfoDict(TypedVDFDict):
    excludefromsharing: NotRequired[int]
    allowpurchasefromrestrictedcountries: NotRequired[bool]
    purchaserestrictedcountries: NotRequired[str]
