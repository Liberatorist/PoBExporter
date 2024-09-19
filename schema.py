from typing import TypedDict, Optional, Union


class LeagueCategory(TypedDict):
    id: str
    current: Optional[bool]


class LeagueRule(TypedDict):
    id: str
    name: str
    description: Optional[str]


class League(TypedDict):
    id: str
    realm: Optional[str]
    description: Optional[str]
    category: Optional[LeagueCategory]
    rules: Optional[list[LeagueRule]]
    registerAt: Optional[str]
    event: Optional[bool]
    url: Optional[str]
    startAt: Optional[str]
    endAt: Optional[str]
    timedEvent: Optional[bool]
    scoreEvent: Optional[bool]
    delveEvent: Optional[bool]
    ancestorEvent: Optional[bool]
    leagueEvent: Optional[bool]


class Depth(TypedDict):
    default: Optional[int]
    solo: Optional[int]


class Character(TypedDict):
    id: str
    name: str
    level: int
    class_: str
    time: Optional[int]
    score: Optional[int]
    progress: Optional[dict]
    experience: Optional[int]
    depth: Optional[Depth]


class LadderEntry(TypedDict):
    rank: int
    dead: Optional[bool]
    retired: Optional[bool]
    ineligible: Optional[bool]
    public: Optional[bool]
    character: Character
    account: Optional['Account']


class PrivateLeague(TypedDict):
    name: str
    url: str


class EventLadderEntry(TypedDict):
    rank: int
    ineligible: Optional[bool]
    time: Optional[int]
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
    stream: Optional[TwitchStream]


class Challenges(TypedDict):
    set: str
    completed: int
    max: int


class Account(TypedDict):
    name: str
    realm: Optional[str]
    guild: Optional[Guild]
    challenges: Optional[Challenges]
    twitch: Optional[Twitch]


class PvPMatch(TypedDict):
    id: str
    realm: Optional[str]
    startAt: Optional[str]
    endAt: Optional[str]
    url: Optional[str]
    description: str
    glickoRatings: bool
    pvp: bool
    style: str
    registerAt: Optional[str]
    complete: Optional[bool]
    upcoming: Optional[bool]
    inProgress: Optional[bool]


class PvPLadderTeamMember(TypedDict):
    account: Account
    character: Character
    public: Optional[bool]


class PvPLadderTeamEntry(TypedDict):
    rank: int
    rating: Optional[int]
    points: Optional[int]
    games_played: Optional[int]
    cumulative_opponent_points: Optional[int]
    last_game_time: Optional[str]
    members: list[PvPLadderTeamMember]


class ItemSocket(TypedDict):
    group: int
    attr: Optional[str]
    sColour: Optional[str]


class ItemProperty(TypedDict):
    name: str
    values: list[list[Union[str, int]]]
    displayMode: Optional[int]
    progress: Optional[float]
    type: Optional[int]
    suffix: Optional[str]


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
    level: Optional[int]
    progress: Optional[int]
    total: Optional[int]


class UltimatumMod(TypedDict):
    type: str
    tier: int


class Hybrid(TypedDict):
    isVaalGem: Optional[bool]
    baseTypeName: str
    properties: Optional[list[ItemProperty]]
    explicitMods: Optional[list[str]]
    secDescrText: Optional[str]


class Extended(TypedDict):
    category: Optional[str]
    subcategories: Optional[list[str]]
    prefixes: Optional[int]
    suffixes: Optional[int]


class Item(TypedDict):
    verified: bool
    w: int
    h: int
    icon: str
    support: Optional[bool]
    stackSize: Optional[int]
    maxStackSize: Optional[int]
    stackSizeText: Optional[str]
    league: Optional[str]
    id: Optional[str]
    influences: Optional[dict]
    elder: Optional[bool]
    shaper: Optional[bool]
    searing: Optional[bool]
    tangled: Optional[bool]
    abyssJewel: Optional[bool]
    delve: Optional[bool]
    fractured: Optional[bool]
    synthesised: Optional[bool]
    sockets: Optional[list[ItemSocket]]
    socketedItems: Optional[list['Item']]
    name: str
    typeLine: str
    baseType: str
    rarity: Optional[str]
    identified: bool
    itemLevel: Optional[int]
    ilvl: int
    note: Optional[str]
    forum_note: Optional[str]
    lockedToCharacter: Optional[bool]
    lockedToAccount: Optional[bool]
    duplicated: Optional[bool]
    split: Optional[bool]
    corrupted: Optional[bool]
    unmodifiable: Optional[bool]
    cisRaceReward: Optional[bool]
    seaRaceReward: Optional[bool]
    thRaceReward: Optional[bool]
    properties: Optional[list[ItemProperty]]
    notableProperties: Optional[list[ItemProperty]]
    requirements: Optional[list[ItemProperty]]
    additionalProperties: Optional[list[ItemProperty]]
    nextLevelRequirements: Optional[list[ItemProperty]]
    talismanTier: Optional[int]
    rewards: Optional[list[ItemReward]]
    secDescrText: Optional[str]
    utilityMods: Optional[list[str]]
    logbookMods: Optional[list[LogbookMod]]
    enchantMods: Optional[list[str]]
    scourgeMods: Optional[list[str]]
    implicitMods: Optional[list[str]]
    ultimatumMods: Optional[list[UltimatumMod]]
    explicitMods: Optional[list[str]]
    craftedMods: Optional[list[str]]
    fracturedMods: Optional[list[str]]
    crucibleMods: Optional[list[str]]
    cosmeticMods: Optional[list[str]]
    veiledMods: Optional[list[str]]
    veiled: Optional[bool]
    descrText: Optional[str]
    flavourText: Optional[list[str]]
    flavourTextParsed: Optional[list[Union[str, dict]]]
    flavourTextNote: Optional[str]
    prophecyText: Optional[str]
    isRelic: Optional[bool]
    foilVariation: Optional[int]
    replica: Optional[bool]
    foreseeing: Optional[bool]
    incubatedItem: Optional[IncubatedItem]
    scourged: Optional[Scourged]
    crucible: Optional[Crucible]
    ruthless: Optional[bool]
    frameType: Optional[int]
    artFilename: Optional[str]
    hybrid: Optional[Hybrid]
    extended: Optional[Extended]
    x: Optional[int]
    y: Optional[int]
    inventoryId: Optional[str]
    socket: Optional[int]
    colour: Optional[str]


class PublicStashChange(TypedDict):
    id: str
    public: bool
    accountName: Optional[str]
    stash: Optional[str]
    lastCharacterName: Optional[str]
    stashType: str
    league: Optional[str]
    items: list[Item]


class CrucibleNode(TypedDict):
    skill: Optional[int]
    tier: Optional[int]
    icon: Optional[str]
    allocated: Optional[bool]
    isNotable: Optional[bool]
    isReward: Optional[bool]
    stats: Optional[list[str]]
    reminderText: Optional[list[str]]
    orbit: Optional[int]
    orbitIndex: Optional[int]
    out: Optional[list[str]]
    in_: Optional[list[str]]


class ExpansionJewel(TypedDict):
    size: Optional[int]
    index: Optional[int]
    proxy: Optional[int]
    parent: Optional[int]


class MasteryEffect(TypedDict):
    effect: int
    stats: list[str]
    reminderText: Optional[list[str]]


class PassiveNode(TypedDict):
    skill: Optional[int]
    name: Optional[str]
    icon: Optional[str]
    isKeystone: Optional[bool]
    isNotable: Optional[bool]
    isMastery: Optional[bool]
    inactiveIcon: Optional[str]
    activeIcon: Optional[str]
    activeEffectImage: Optional[str]
    masteryEffects: Optional[MasteryEffect]
    isBlighted: Optional[bool]
    isTattoo: Optional[bool]
    isProxy: Optional[bool]
    isJewelSocket: Optional[bool]
    expansionJewel: Optional[ExpansionJewel]
    recipe: Optional[list[str]]
    grantedStrength: Optional[int]
    grantedDexterity: Optional[int]
    grantedIntelligence: Optional[int]
    ascendancyName: Optional[str]
    isAscendancyStart: Optional[bool]
    isMultipleChoice: Optional[bool]
    isMultipleChoiceOption: Optional[bool]
    grantedPassivePoints: Optional[int]
    stats: Optional[list[str]]
    reminderText: Optional[list[str]]
    flavourText: Optional[list[str]]
    classStartIndex: Optional[int]
    group: Optional[str]
    orbit: Optional[int]
    orbitIndex: Optional[int]
    out: Optional[list[str]]
    in_: Optional[list[str]]


class PassiveGroup(TypedDict):
    x: float
    y: float
    orbits: list[int]
    isProxy: Optional[bool]
    proxy: Optional[str]
    nodes: list[str]


class Subgraph(TypedDict):
    groups: dict[str, PassiveGroup]
    nodes: dict[str, PassiveNode]


class ItemJewelData(TypedDict):
    type: str
    radius: Optional[int]
    radiusMin: Optional[int]
    radiusVisual: Optional[str]
    subgraph: Optional[Subgraph]


class CharacterMetadata(TypedDict):
    version: Optional[str]


class Passives(TypedDict):
    hashes: list[int]
    hashes_ex: list[int]
    mastery_effects: dict[str, int]
    skill_overrides: Optional[dict[str, 'PassiveNode']]
    bandit_choice: Optional[str]
    pantheon_major: Optional[str]
    pantheon_minor: Optional[str]
    jewel_data: dict[str, ItemJewelData]
    alternate_ascendancy: Optional[str]


class Character(TypedDict):
    id: str
    name: str
    realm: str
    class_: str
    league: Optional[str]
    level: int
    experience: int
    ruthless: Optional[bool]
    expired: Optional[bool]
    deleted: Optional[bool]
    current: Optional[bool]
    equipment: Optional[list[Item]]
    inventory: Optional[list[Item]]
    rucksack: Optional[list[Item]]
    jewels: Optional[list[Item]]
    passives: Optional[Passives]
    metadata: Optional[CharacterMetadata]


class StashTabMetaDict(TypedDict):
    public: Optional[bool]
    folder: Optional[bool]
    colour: Optional[str]


class StashTab(TypedDict):
    id: str
    parent: Optional[str]
    name: str
    type: str
    index: Optional[int]
    metadata: StashTabMetaDict
    children: Optional[list['StashTab']]
    items: Optional[list[Item]]


class AtlasTreeInfo(TypedDict):
    name: str
    hashess: list[int]


class AtlasTreeInfoOld(TypedDict):
    hashess: list[int]


class LeagueAccount(TypedDict):
    atlas_passives: Optional[AtlasTreeInfoOld]
    atlas_passive_trees: list[AtlasTreeInfo]


class ValidationDetails(TypedDict):
    valid: bool
    version: Optional[str]
    validated: Optional[str]


class ItemFilter(TypedDict):
    id: str
    filter_name: str
    realm: str
    description: str
    version: str
    type: str
    public: Optional[bool]
    filter: Optional[str]
    validation: Optional[ValidationDetails]


class PassiveGroup(TypedDict):
    x: float
    y: float
    orbits: list[int]
    isProxy: Optional[bool]
    proxy: Optional[str]
    nodes: list[str]


class MasteryEffect(TypedDict):
    effect: int
    stats: list[str]
    reminderText: Optional[list[str]]


class ExpansionJewel(TypedDict):
    size: Optional[int]
    index: Optional[int]
    proxy: Optional[int]
    parent: Optional[int]


class PassiveNode(TypedDict):
    skill: Optional[int]
    name: Optional[str]
    icon: Optional[str]
    isKeystone: Optional[bool]
    isNotable: Optional[bool]
    isMastery: Optional[bool]
    inactiveIcon: Optional[str]
    activeIcon: Optional[str]
    activeEffectImage: Optional[str]
    masteryEffects: Optional[list[MasteryEffect]]
    isBlighted: Optional[bool]
    isTattoo: Optional[bool]
    isProxy: Optional[bool]
    isJewelSocket: Optional[bool]
    expansionJewel: Optional[ExpansionJewel]
    recipe: Optional[list[str]]
    grantedStrength: Optional[int]
    grantedDexterity: Optional[int]
    grantedIntelligence: Optional[int]
    ascendancyName: Optional[str]
    isAscendancyStart: Optional[bool]
    isMultipleChoice: Optional[bool]
    isMultipleChoiceOption: Optional[bool]
    grantedPassivePoints: Optional[int]
    stats: Optional[list[str]]
    reminderText: Optional[list[str]]
    flavourText: Optional[list[str]]
    classStartIndex: Optional[int]
    group: Optional[str]
    orbit: Optional[int]
    orbitIndex: Optional[int]
    out: list[str]
    in_: list[str]


class CrucibleNode(TypedDict):
    skill: Optional[int]
    tier: Optional[int]
    icon: Optional[str]
    allocated: Optional[bool]
    isNotable: Optional[bool]
    isReward: Optional[bool]
    stats: Optional[list[str]]
    reminderText: Optional[list[str]]
    orbit: Optional[int]
    orbitIndex: Optional[int]
    out: list[str]
    in_: list[str]
