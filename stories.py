# Stories for Friday 27 November 2026 — researched fresh from live news
# (BBC, Reuters, AP, NYT, India Today, Morningstar, Barron's, NZ Herald).
# Every item happened, or was first reported, on 27 November 2026.
# Fields: number, headline, one-line body, source, region, status, scene kind.

DATE_LINE = "FRIDAY 27 NOVEMBER 2026"
TITLE = "50 stories, 10 regions, a UTC timeline, map and date check"
LEAD = "Iranian drone kills 2 Italians in Kuwait; Thanksgiving storm floods the US"

# status labels: CONFIRMED = named source confirms it happened;
# REPORTED = a named outlet reports it; CLAIM = a person claims it;
# ONGOING = still developing at press time.
HERO = [
    (1, "Iranian drone kills 2 Italians in Kuwait",
     "Kuwait says it downed an Iranian drone; two Italian defence "
     "technicians were killed. Iran denies any military operation.",
     "New York Times", "MIDDLE EAST", "REPORTED", "drone"),
    (2, "Israeli strikes kill 10 in Gaza",
     "Health officials say 10 Palestinians were killed in Gaza City "
     "as strikes continue; Hamas weighs its response and the "
     "ceasefire frays.",
     "Reuters", "MIDDLE EAST", "CONFIRMED", "explosion"),
    (3, "Thanksgiving storm floods the US",
     "A major storm postponed the 100th Macy's parade for the first "
     "time and cut power to 500,000+ homes as 80m people travelled.",
     "BBC", "NORTH AMERICA", "CONFIRMED", "storm"),
]

CARDS = [
    (4, "Black Friday: $12.9bn online in a day",
     "US online sales are forecast at a record $12.9bn today; "
     "holiday online spending is tipped to hit $275bn.",
     "Adobe Analytics", "NORTH AMERICA", "REPORTED", "shopping"),
    (5, "Markets roar back from the brink",
     "The Dow swung from a 1,100-point loss to a 167-point gain; "
     "S&P futures rose 0.7% as Europe rallied.",
     "Barron's", "WORLD MARKETS", "CONFIRMED", "chart"),
    (6, "Zelenskyy: new mass strike coming",
     "Ukraine's president warns Russia is preparing a new mass "
     "strike on energy sites in the coming days.",
     "Reuters", "EUROPE", "REPORTED", "missile"),
    (7, "Mayon volcano erupts in Philippines",
     "Mount Mayon sent ash 3,000m into the sky, raising fears of "
     "a larger eruption to follow.",
     "AP", "SOUTHEAST ASIA", "CONFIRMED", "volcano"),
    (8, "Diesel tanker capsizes off Ibiza",
     "A tanker carrying up to 7,000 tonnes of diesel capsized "
     "north of Ibiza; one crew member was killed.",
     "BBC", "EUROPE", "CONFIRMED", "tanker"),
    (9, "Bangkok refinery blast injures 9",
     "An explosion and fire at the Bangchak refinery injured nine "
     "people, three critically; schools evacuated.",
     "AP", "SOUTHEAST ASIA", "CONFIRMED", "fire"),
    (10, "Gukesh-Sindarov: marathon draw",
     "Game 3 of the World Chess Championship ended in a marathon "
     "draw; nothing separates the pair after three games.",
     "India Today", "SOUTH ASIA", "CONFIRMED", "chess"),
    (11, "Sinner out of Australian Open 2027",
     "Jannik Sinner will miss the 2027 Australian Open with a "
     "knee injury.",
     "AP", "EUROPE", "CONFIRMED", "tennis"),
    (12, "UK migration lowest since 1997",
     "Net migration to Britain fell to its lowest since 1997, "
     "excluding the pandemic years.",
     "New York Times", "EUROPE", "REPORTED", "chart"),
    (13, "Depardieu to stand trial for rape",
     "A French court ruled Gerard Depardieu will stand trial over "
     "an alleged rape of an actress in 2018.",
     "BBC", "EUROPE", "CONFIRMED", "court"),
]

# headline, source, region — stories 14-50, listed with a source each.
LISTED = [
    (14, "Pope Leo XIV to vote in US midterms by mail", "AP", "NORTH AMERICA"),
    (15, "French students plan nationwide protests", "BBC", "EUROPE"),
    (16, "EU and Canada deepen AI cooperation", "Reuters", "EUROPE"),
    (17, "Audi profits slide on weak China sales", "Reuters", "EUROPE"),
    (18, "Egypt tanker fire kills 30 in Giza", "AP", "AFRICA"),
    (19, "China launches Earth observation satellites", "Xinhua", "EAST ASIA"),
    (20, "Musk: every US child gets two SpaceX shares", "The Hindu", "NORTH AMERICA"),
    (21, "India top court rules on PMLA bench", "Times of India", "SOUTH ASIA"),
    (22, "India clears Rs 11,000 cr equipment scheme", "All India Radio", "SOUTH ASIA"),
    (23, "Ramaphosa wins bid to scrap impeachment report", "Reuters", "AFRICA"),
    (24, "Kim vows to build more nuclear weapons", "AP", "EAST ASIA"),
    (25, "US Army blows up lead explosives stockpile", "AP", "NORTH AMERICA"),
    (26, "Hong Kong marks the tower-fire anniversary", "BBC", "EAST ASIA"),
    (27, "Cheaper HIV prevention jab reaches Africa", "BBC", "AFRICA"),
    (28, "Myanmar rejects parts of ICJ genocide ruling", "BBC", "SOUTHEAST ASIA"),
    (29, "Pakistani TV screenings cancelled in India", "BBC", "SOUTH ASIA"),
    (30, "France's mainstream faces vote debacle", "BBC", "EUROPE"),
    (31, "German boat dealer 'supplied Channel gangs'", "BBC", "EUROPE"),
    (32, "Pregnant US inmate escapes in prison van", "BBC", "NORTH AMERICA"),
    (33, "Egypt arrests driver in tanker crash", "BBC", "AFRICA"),
    (34, "AP Gaza journalists win Rory Peck prize", "AP", "MIDDLE EAST"),
    (35, "Melania Trump reunites 7th group of children", "AP", "NORTH AMERICA"),
    (36, "Houthis close in on Aden", "AP", "MIDDLE EAST"),
    (37, "Zaporizhzhia strike kills 2, wounds 48", "AP", "EUROPE"),
    (38, "NZ final election results are out", "NZ Herald", "OCEANIA"),
    (39, "NZ: 1 in 3 Black Friday 'deals' no bargain", "Consumer NZ", "OCEANIA"),
    (40, "Barrett to captain All Blacks vs England", "NZ Herald", "OCEANIA"),
    (41, "India bowl in 2nd Test at Christchurch", "AP", "OCEANIA"),
    (42, "Sandpapergate probe to cover 2017-18 Ashes", "BBC", "OCEANIA"),
    (43, "Met Police 'ruined life' of wrongly jailed man", "BBC", "EUROPE"),
    (44, "Yemen: civilians suffer as donors look away", "UN", "MIDDLE EAST"),
    (45, "Iraq blocks two Kurdistan border crossings", "Reuters", "MIDDLE EAST"),
    (46, "Estonia to end rail border with Russia", "ERR", "EUROPE"),
    (47, "Saudi-Turkish defence summit in Islamabad", "Reuters", "SOUTH ASIA"),
    (48, "Turkey sets 2028 vote; Erdogan to run again", "Reuters", "EUROPE"),
    (49, "EU report: Trump gave Russian energy a lifeline", "EU", "EUROPE"),
    (50, "Congo Ebola outbreak passes 12,000 cases", "Reuters", "AFRICA"),
]

# Region counts, computed from the 50 stories above.
REGIONS = [
    ("EUROPE", 15), ("NORTH AMERICA", 7), ("MIDDLE EAST", 6),
    ("AFRICA", 5), ("SOUTH ASIA", 5), ("OCEANIA", 5),
    ("EAST ASIA", 3), ("SOUTHEAST ASIA", 3), ("WORLD MARKETS", 1),
]

FIELDS = "War 10 - Disaster 8 - Politics 8 - Society 8 - Sport 5 - Courts 4 - Markets 4 - Tech 3"

# Five big numbers drawn from the day's stories.
KPI = [
    ("10", "killed in Gaza strikes"),
    ("2", "Italians killed in Kuwait"),
    ("7,000 t", "diesel adrift off Ibiza"),
    ("$12.9bn", "Black Friday online sales"),
    ("500,000+", "US homes without power"),
]

# The day in UTC — first-reported times, 27 November 2026.
TIMELINE = [
    ("01:00", "Kuwait: Iranian drone kills 2 Italians"),
    ("02:26", "Gaza: Israeli strikes kill 10"),
    ("03:31", "Ibiza: diesel tanker capsizes, 1 dead"),
    ("06:00", "Mayon volcano erupts, ash 3,000m up"),
    ("13:00", "Black Friday trading opens in New York"),
]

# Stories deliberately left OUT — they are not 27 November news.
DATE_CHECK = [
    ("25 Nov", "RSF drone strikes kill 19 in Sudan"),
    ("25 Nov", "Kremlin rejects 700,000 war-dead leak"),
    ("25 Nov", "Bangladesh garment wage up 36%"),
    ("22 Nov", "COP31 climate deal rejected"),
    ("18-23 Nov", "Earth: 6 days straight above 2C"),
    ("26 Nov", "Ford unveils GT41 hypercar"),
]

# Map pins: story number -> (longitude, latitude).
PINS = {
    1: (47.5, 29.3), 2: (34.5, 31.5), 3: (-74.0, 40.7), 4: (-95.0, 37.0),
    5: (-74.0, 40.7), 6: (30.5, 50.4), 7: (123.7, 13.3), 8: (1.5, 39.0),
    9: (100.5, 13.7), 10: (77.2, 28.6), 11: (12.5, 41.9), 12: (-0.1, 51.5),
    13: (2.3, 48.9),
}

ALL_STORIES = HERO + CARDS + [
    (n, h, "", s, r, "REPORTED", "globe") for (n, h, s, r) in LISTED
]
