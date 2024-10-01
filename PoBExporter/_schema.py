from typing import NotRequired, TypedDict, Union


class LeagueCategory(TypedDict):
    id: str
    current: NotRequired[bool]


class LeagueRule(TypedDict):
    id: str
    name: str
    description: NotRequired[str]


class League(TypedDict):
    id: str
    realm: NotRequired[str]
    description: NotRequired[str]
    category: NotRequired[LeagueCategory]
    rules: NotRequired[list[LeagueRule]]
    registerAt: NotRequired[str]
    event: NotRequired[bool]
    url: NotRequired[str]
    startAt: NotRequired[str]
    endAt: NotRequired[str]
    timedEvent: NotRequired[bool]
    scoreEvent: NotRequired[bool]
    delveEvent: NotRequired[bool]
    ancestorEvent: NotRequired[bool]
    leagueEvent: NotRequired[bool]


class Depth(TypedDict):
    default: NotRequired[int]
    solo: NotRequired[int]


Character = TypedDict('Character', {
    "id": str,
    "name": str,
    "realm": str,
    "class": str,
    "league": NotRequired[str],
    "level": int,
    "experience": int,
    "ruthless": NotRequired[bool],
    "expired": NotRequired[bool],
    "deleted": NotRequired[bool],
    "current": NotRequired[bool],
    "equipment": list['Item'],
    "inventory": list['Item'],
    "rucksack": NotRequired[list['Item']],
    "jewels": list['Item'],
    "passives": 'Passives',
    "metadata": 'CharacterMetadata'
})


class LadderEntry(TypedDict):
    rank: int
    dead: NotRequired[bool]
    retired: NotRequired[bool]
    ineligible: NotRequired[bool]
    public: NotRequired[bool]
    character: Character
    account: NotRequired['Account']


class PrivateLeague(TypedDict):
    name: str
    url: str


class EventLadderEntry(TypedDict):
    rank: int
    ineligible: NotRequired[bool]
    time: NotRequired[int]
    private_league: PrivateLeague


class Guild(TypedDict):
    id: int
    name: str
    tag: str


class TwitchStream(TypedDict):
    name: str
    image: str
    status: str


class Twitch(TypedDict):
    name: str
    stream: NotRequired[TwitchStream]


class Challenges(TypedDict):
    set: str
    completed: int
    max: int


class Account(TypedDict):
    name: str
    realm: NotRequired[str]
    guild: NotRequired[Guild]
    challenges: NotRequired[Challenges]
    twitch: NotRequired[Twitch]


class PvPMatch(TypedDict):
    id: str
    realm: NotRequired[str]
    startAt: NotRequired[str]
    endAt: NotRequired[str]
    url: NotRequired[str]
    description: str
    glickoRatings: bool
    pvp: bool
    style: str
    registerAt: NotRequired[str]
    complete: NotRequired[bool]
    upcoming: NotRequired[bool]
    inProgress: NotRequired[bool]


class PvPLadderTeamMember(TypedDict):
    account: Account
    character: Character
    public: NotRequired[bool]


class PvPLadderTeamEntry(TypedDict):
    rank: int
    rating: NotRequired[int]
    points: NotRequired[int]
    games_played: NotRequired[int]
    cumulative_opponent_points: NotRequired[int]
    last_game_time: NotRequired[str]
    members: list[PvPLadderTeamMember]


class ItemSocket(TypedDict):
    group: int
    attr: str
    sColour: str


class ItemProperty(TypedDict):
    name: str
    values: list[tuple[str, int]]
    displayMode: NotRequired[int]
    progress: NotRequired[float]
    type: NotRequired[int]
    suffix: NotRequired[str]


class LogbookFaction(TypedDict):
    id: str
    name: str


class LogbookMod(TypedDict):
    name: str
    faction: LogbookFaction


class ItemReward(TypedDict):
    label: str
    rewards: dict[str, int]


class IncubatedItem(TypedDict):
    name: str
    level: int
    progress: int
    total: int


class Crucible(TypedDict):
    layout: str
    nodes: dict[str, 'CrucibleNode']


class Scourged(TypedDict):
    tier: int
    level: NotRequired[int]
    progress: NotRequired[int]
    total: NotRequired[int]


class UltimatumMod(TypedDict):
    type: str
    tier: int


class Hybrid(TypedDict):
    isVaalGem: NotRequired[bool]
    baseTypeName: str
    properties: NotRequired[list[ItemProperty]]
    explicitMods: NotRequired[list[str]]
    secDescrText: NotRequired[str]


class Extended(TypedDict):
    category: NotRequired[str]
    subcategories: NotRequired[list[str]]
    prefixes: NotRequired[int]
    suffixes: NotRequired[int]


class Item(TypedDict):
    verified: bool
    w: int
    h: int
    icon: str
    support: NotRequired[bool]
    stackSize: NotRequired[int]
    maxStackSize: NotRequired[int]
    stackSizeText: NotRequired[str]
    league: NotRequired[str]
    id: str
    influences: NotRequired[dict]
    elder: NotRequired[bool]
    shaper: NotRequired[bool]
    searing: NotRequired[bool]
    tangled: NotRequired[bool]
    abyssJewel: NotRequired[bool]
    delve: NotRequired[bool]
    fractured: NotRequired[bool]
    synthesised: NotRequired[bool]
    sockets: NotRequired[list[ItemSocket]]
    socketedItems: NotRequired[list['Item']]
    name: str
    typeLine: str
    baseType: str
    rarity: str
    identified: bool
    itemLevel: NotRequired[int]
    ilvl: int
    note: NotRequired[str]
    forum_note: NotRequired[str]
    lockedToCharacter: NotRequired[bool]
    lockedToAccount: NotRequired[bool]
    duplicated: NotRequired[bool]
    split: NotRequired[bool]
    corrupted: NotRequired[bool]
    unmodifiable: NotRequired[bool]
    cisRaceReward: NotRequired[bool]
    seaRaceReward: NotRequired[bool]
    thRaceReward: NotRequired[bool]
    properties: NotRequired[list[ItemProperty]]
    notableProperties: NotRequired[list[ItemProperty]]
    requirements: NotRequired[list[ItemProperty]]
    additionalProperties: NotRequired[list[ItemProperty]]
    nextLevelRequirements: NotRequired[list[ItemProperty]]
    talismanTier: NotRequired[int]
    rewards: NotRequired[list[ItemReward]]
    secDescrText: NotRequired[str]
    utilityMods: NotRequired[list[str]]
    logbookMods: NotRequired[list[LogbookMod]]
    enchantMods: NotRequired[list[str]]
    scourgeMods: NotRequired[list[str]]
    implicitMods: NotRequired[list[str]]
    ultimatumMods: NotRequired[list[UltimatumMod]]
    explicitMods: NotRequired[list[str]]
    craftedMods: NotRequired[list[str]]
    fracturedMods: NotRequired[list[str]]
    crucibleMods: NotRequired[list[str]]
    cosmeticMods: NotRequired[list[str]]
    veiledMods: NotRequired[list[str]]
    veiled: NotRequired[bool]
    descrText: NotRequired[str]
    flavourText: NotRequired[list[str]]
    flavourTextParsed: NotRequired[list[Union[str, dict]]]
    flavourTextNote: NotRequired[str]
    prophecyText: NotRequired[str]
    isRelic: NotRequired[bool]
    foilVariation: NotRequired[int]
    replica: NotRequired[bool]
    foreseeing: NotRequired[bool]
    incubatedItem: NotRequired[IncubatedItem]
    scourged: NotRequired[Scourged]
    crucible: NotRequired[Crucible]
    ruthless: NotRequired[bool]
    frameType: NotRequired[int]
    artFilename: NotRequired[str]
    hybrid: NotRequired[Hybrid]
    extended: NotRequired[Extended]
    x: int
    y: int
    inventoryId: str
    socket: NotRequired[int]
    colour: NotRequired[str]


class PublicStashChange(TypedDict):
    id: str
    public: bool
    accountName: NotRequired[str]
    stash: NotRequired[str]
    lastCharacterName: NotRequired[str]
    stashType: str
    league: NotRequired[str]
    items: list[Item]


CrucibleNode = TypedDict('CrucibleNode', {
    "skill": NotRequired[int],
    "tier": NotRequired[int],
    "icon": NotRequired[str],
    "allocated": NotRequired[bool],
    "isNotable": NotRequired[bool],
    "isReward": NotRequired[bool],
    "stats": NotRequired[list[str]],
    "reminderText": NotRequired[list[str]],
    "orbit": NotRequired[int],
    "orbitIndex": NotRequired[int],
    "out": list[str],
    "in": list[str]
})


class ExpansionJewel(TypedDict):
    size: NotRequired[int]
    index: NotRequired[int]
    proxy: NotRequired[int]
    parent: NotRequired[int]


class MasteryEffect(TypedDict):
    effect: int
    stats: list[str]
    reminderText: NotRequired[list[str]]


PassiveNode = TypedDict('PassiveNode', {
    "skill": NotRequired[int],
    "name": NotRequired[str],
    "icon": NotRequired[str],
    "isKeystone": NotRequired[bool],
    "isNotable": NotRequired[bool],
    "isMastery": NotRequired[bool],
    "inactiveIcon": NotRequired[str],
    "activeIcon": NotRequired[str],
    "activeEffectImage": NotRequired[str],
    "masteryEffects": NotRequired[list[MasteryEffect]],
    "isBlighted": NotRequired[bool],
    "isTattoo": NotRequired[bool],
    "isProxy": NotRequired[bool],
    "isJewelSocket": NotRequired[bool],
    "expansionJewel": NotRequired[ExpansionJewel],
    "recipe": NotRequired[list[str]],
    "grantedStrength": NotRequired[int],
    "grantedDexterity": NotRequired[int],
    "grantedIntelligence": NotRequired[int],
    "ascendancyName": NotRequired[str],
    "isAscendancyStart": NotRequired[bool],
    "isMultipleChoice": NotRequired[bool],
    "isMultipleChoiceOption": NotRequired[bool],
    "grantedPassivePoints": NotRequired[int],
    "stats": NotRequired[list[str]],
    "reminderText": NotRequired[list[str]],
    "flavourText": NotRequired[list[str]],
    "classStartIndex": NotRequired[int],
    "group": NotRequired[str],
    "orbit": NotRequired[int],
    "orbitIndex": NotRequired[int],
    "out": list[str],
    "in": list[str]
})


class PassiveGroup(TypedDict):
    x: float
    y: float
    orbits: list[int]
    isProxy: NotRequired[bool]
    proxy: NotRequired[str]
    nodes: list[str]


class Subgraph(TypedDict):
    groups: dict[str, PassiveGroup]
    nodes: dict[str, PassiveNode]


class ItemJewelData(TypedDict):
    type: str
    radius: NotRequired[int]
    radiusMin: NotRequired[int]
    radiusVisual: NotRequired[str]
    subgraph: NotRequired[Subgraph]


class CharacterMetadata(TypedDict):
    version: str


class Passives(TypedDict):
    hashes: list[int]
    hashes_ex: list[int]
    mastery_effects: dict[str, int]
    skill_overrides: NotRequired[dict[str, 'PassiveNode']]
    bandit_choice: NotRequired[str]
    pantheon_major: NotRequired[str]
    pantheon_minor: NotRequired[str]
    jewel_data: dict[str, ItemJewelData]
    alternate_ascendancy: NotRequired[str]


class StashTabMetaDict(TypedDict):
    public: NotRequired[bool]
    folder: NotRequired[bool]
    colour: NotRequired[str]


class StashTab(TypedDict):
    id: str
    parent: NotRequired[str]
    name: str
    type: str
    index: NotRequired[int]
    metadata: StashTabMetaDict
    children: NotRequired[list['StashTab']]
    items: NotRequired[list[Item]]


class AtlasTreeInfo(TypedDict):
    name: str
    hashess: list[int]


class AtlasTreeInfoOld(TypedDict):
    hashes: list[int]


class LeagueAccount(TypedDict):
    atlas_passives: NotRequired[AtlasTreeInfoOld]
    atlas_passive_trees: list[AtlasTreeInfo]


class ValidationDetails(TypedDict):
    valid: bool
    version: NotRequired[str]
    validated: NotRequired[str]


class ItemFilter(TypedDict):
    id: str
    filter_name: str
    realm: str
    description: str
    version: str
    type: str
    public: NotRequired[bool]
    filter: NotRequired[str]
    validation: NotRequired[ValidationDetails]
