import hikari
from hikari import embeds
import lightbulb
import os
import datetime
import sqlite3
from PyDictionary import PyDictionary
dict=PyDictionary()
from datetime import *
from flask import Flask
import random
import ety
from threading import Thread
import json
from pymongo import MongoClient
from urllib.parse import quote_plus

ALtoENG = {
    "land-of-elves": "alalëa",
    "beautiful-dream" : "lëa",
    "a": "aí",
    "an": "aí",
    "the-dream-itsself" : "elëa",
    "land" : "ala",
    "fertile" : "gaësia",
    "air, wind": "vindr",
    "all": "allr",
    "am": "eddyr",
    "an, a": "aí",
    "and": "un",
    "apple": "hald",
    "are": "eru",
    "arm": "vaupna",
    "armor": "hernskja",
    "arrow": "oro",
    "as": "nen",
    "ask" : "bidja",
    "awaken": "vakna",
    "awry": "vrangr",
    "wandering" : "vrangr",
    "back": "hrygr",
    "back" : "bak",
    "bad": "illr",
    "bad": "vandr",
    "bad" : "íll",
    "burrow grubs": "íllgrathr",
    "badly": "illa",
    "ball, round object": "böllr",
    "banish": "aurboda",
    "bat": "lethrblaka",
    "leather flapper" : "lethrblaka",
    "be": "waíse",
    "be drowned": "drukna",
    "be silent": "theyna",
    "bear": "artos, beor",
    "beautiful": "nuanen",
    "become": "verda",
    "become pale": "blinkna",
    "before": "framvír",
    "big king": "galbatorix",
    "big": "galba",
    "confine": "malthinae",
    "bind": "malthinae",
    "shadow flapper": "sundavrblaka",
    "birth": "burthr",
    "bite": "bita",
    "biter": "bitr",
    "black": "svartr",
    "blade": "blädrn",
    "blanket": "nagz",
    "cloth":"nagz",
    "blasted": "nangoröth",
    "withered": "nangoröth",
    "blood": "blödh",
    "blood-oath": "blödhren",
    "blood-oath celebration": "agaetí blödhren",
    "bloodwolf": "blödhgarm",
    "bond of trust": "yawë",
    "bowl": "skal",
    "branch": "kvïstr",
    "break": "jierda",
    "bright": "bjartr",
    "brightscales": "bjartskular",
    "brightsteel": "bjartstál",
    "unite": "gath",
    "broad": "äenora",
    "broad" : "boetk",
    "brother": "darmthrell",
    "brow": "brun",
    "brush scrub": "ethilnadras",
    "burn": "eldrvarí",
    "but": "mar",
    "cactus found near helgrind": "talos",
    "calf of the leg": "kalfí",
    "carry": "flutningr",
    "chest": "karst",
    "casket" : "karst",
    "report" : "flutningr",
    "catch": "kodthr",
    "celebration": "agaetí",
    "celebratory": "agaetra",
    "change": "moi",
    "chant":"gala",
    "city": "dras",
    "clever": "sláegr",
    "cloth, blanket": "nagz",
    "come": "kausta",
    "compress; thrust": "thringa",
    "confine; to bind or hold in place": "malthinae",
    "create": "malthinae",
    "cripple": "togira",
    "cripple who is whole, the": "togira ikonoka",
    "crust": "hrúthr",
    "cry (to beg/ask)": "bidja",
    "cunning": "sláegr",
    "cut": "kverst",
    "damp": "akr",
    "dart": "daert",
    "daughter": "dautr",
    "day": "dag",
    "hallowed day": "dagshelgr",
    "deadly poison, a": "skilna bragh",
    "deaf": "daufr",
    "death": ["andlát", "baní", "dauthí", "freohr"],
    "death friend": "fricai andlát",
    "death spear": "dauthdaert",
    "delay": "dvelja",
    "desire": "threyja",
    "die": ["deyja","andask"],
    "disease": "mïnen",
    "dispel": "vaetna",
    "do": "ach",
    "dominance": "domia",
    "dominance of fate": "domia abr wyrda",
    "door": "hurdh",
    "dragon": "skulblaka",
    "dragon rider": "shur’tugal",
    "dream": "draumr",
    "drinking cup": "skal",
    "dry": "thurra",
    "dull": "gëuloth",
    "dumb": "dúmbr",
    "dwarf": "dvergr",
    "ear": "eyra",
    "early": "ár",
    "earth, soil": "deloi",
    "elf": "älfa",
    "elf friend": "vinr älfakyn",
    "elves": "älfakyn",
    "empty": "eyddr",
    "if" : "ilf",
    "enchantment": "galdr",
    "enemy": "fjandí",
    "entrap": "taelda",
    "eye": "auga",
    "fabric": "lámarae",
    "family": "breoal",
    "fate": "wyrda",
    "feather": "fethr",
    "field": "vollr",
    "fight": "verrunsmal",
    "find": "finna",
    "fire": "brisingr",
    "fire":"istalrí",
    "flameless lanterns": "erisdar",
    "flapper": "blaka",
    "floater": "flautr",
    "float": "flautja",
    "flowers": "fëon",
    "fly": "flauga",
    "follow": "tauthr",
    "fools wisdom": "orothrim",
    "for": "wiol",
    "forest": "welden",
    "forgetfulness": "vergathos",
    "forsworn": "wyrdfell",
    "forward": "fram",
    "friend": ["fricai", "vinr"],
    "from": "fra",
    "gate": "grind",
    "gates of death, the": "helgrind",
    "gift": "förn",
    "go": "gánga",
    "leave": "eitha",
    "goat": "hafr",
    "gold": "kuldr",
    "good fortune": "esterní",
    "grasp": "thrífask",
    "seize": "thrífa",
    "great king of warriors": "vercingetorix",
    "green-leafed plant with purple flowers": "delois",
    "greetings": "kvetha",
    "hello":"kvetha",
    "grow": "eldhrimner",
    "guard": "vard",
    "guardians": "varden",
    "hall": "hjall",
    "hallowed day": "dagshelgr",
    "halt": "blöthr",
    "gammer": "hamarr",
    "hand": "lam",
    "happiness": "ilian",
    "happy": "ilia",
    "harden": "herdtha",
    "harm": "haina, mïnen",
    "harm": "mïnen",
    "have": "hávr",
    "he": "älfr",
    "heal": "heill",
    "healed": "heill",
    "hear": "hórna",
    "hearth": "hjarta",
    "heart of hearts": "eldunarí",
    "heat": "verma",
    "height": "haedh",
    "hide": "frethya",
    "hit": "jierda",
    "hold": "huildr",
    "hole in ice": "vök",
    "honor": "celöbra",
    "wise woman": "svit-kona",
    "hound": "garm",
    "wolf":"garm",
    "house": "breoal",
    "humble": "midhring",
    "hunger": "grathr",
    "i": "eka",
    "ice": "svell",
    "ice-hole": "vök",
    "illuminator": "islingr",
    "illusion": "dreyma",
    "in": "unin",
    "in front of": "framvír",
    "injury": "mïnen",
    "intend": "algara",
    "invoke": "ethgrí",
    "is": "er",
    "lack": "vanta",
    "is whole": "ikonoka",
    "it": "thäet",
    "its": "vér",
    "kill": "vergarí",
    "killer": "vergandí",
    "king": "könungr",
    "king of killers": "orgetorix",
    "knife": "knífr",
    "know": "kenna",
    "ladies": "ementyr",
    "lasting": "drjugr",
    "leaf": "lauf",
    "leafblade": "laufblädr",
    "leather": "lethr",
    "let": "atra",
    "life": "líf",
    "light-bringer": "islingr",
    "light": "garjzla",
    "lightning": "kveykva",
    "lily": "loivissa",
    "lip-balm": "nalgask",
    "liqueur": "faelnirv",
    "alcohol":"faelnirv",
    "listen": "hórna",
    "little": "litil",
    "live": "lífa",
    "lock": "laesa",
    "look": "sja",
    "lord": "daéda",
    "love": "ástar",
    "luck": "guliä",
    "mad": "orr",
    "magic": "vanyalí",
    "make bright": "naina",
    "marked": "fódhr",
    "master": "ebrithil",
    "may": "sé",
    "me": "edtha",
    "mean": "mulabra",
    "memory": "manin",
    "metal": "malmr",
    "mind": "hugr",
    "misery": "zar’roc",
    "misfortune": "rauthr",
    "mist": "akr",
    "mists": "datia",
    "mix": "blanda",
    "moist": "akr",
    "more": "frëma",
    "morning star": "aiedail",
    "mortal": "dauthleikr",
    "mother": "menoa",
    "mountain": "fell",
    "mourning sage": "osthato chetowä",
    "mourning": "osthato",
    "move": "sharjalví",
    "movement": "sharjalví",
    "my": "pömnuria",
    "myself": "ietdar",
    "name": "nam",
    "names": "namar",
    "night-pine": "dwerva thindr",
    "no": "né",
    "not": "néiat",
    "nothingness": "und",
    "oak": "ekar",
    "promise": "eïnradhin",
    "oath": "ren",
    "oats": "hafrí",
    "of": "abr",
    "on": "äthr",
    "onto": "äthr",
    "open": "ládrin",
    "orb": "böllr",
    "orchid": "niernen",
    "noble-guard": "äthalvard",
    "over": "arúnd",
    "pain": "verkr",
    "palm": "gedwëy",
    "pardon": "elthrimórno",
    "passage": "gata",
    "path": "gata",
    "peace": "mor’ranr",
    "picture": "fairth",
    "pinch": "kremja",
    "pine": "thindr",
    "place": "ília",
    "place-of-sorrow": "ristvak’baen",
    "poem": "rune",
    "poet": "skald",
    "poetic": "kvaedhí",
    "poetic-script": "liduen kvaedhí",
    "possess": "hávr",
    "princess": "dröttningu",
    "project": "skaga",
    "prominence": "edur",
    "promontory": "skagí",
    "protect": "vardi",
    "pulling": "drahtr",
    "queen": "dröttning",
    "quiet": "maela",
    "race": "kynn",
    "rain": "thringa",
    "raise": "reisa",
    "reduce": "brakka",
    "release": "losna",
    "remain": "sitja",
    "rest": "stydja",
    "right": "raehta",
    "rise": "rïsa",
    "rock": "stenr",
    "rune": "vald",
    "rule over": "thelduin",
    "ruler": "valdr",
    "run": "hlaupa",
    "sage": "chetowä",
    "scale": "skul",
    "scale-flapper": "skulblaka",
    "scatter": "vaetna",
    "scintillating": "delling",
    "script": "liduen",
    "sea": "vaer",
    "seaweed": "vaer ethilnadras",
    "see": "sjon",
    "seize": "thrífa",
    "serpent": "orúm",
    "shadow": "sundavr",
    "sharp": "hvass",
    "she": "älfinn",
    "sheath": "skálpr",
    "shell": "skálpr",
    "shield": "skölir",
    "shining palm": "gedwëy ignasia",
    "shining": "bleikr",
    "shirt": "skyrta",
    "shut ones eyes": "blunda",
    "sigh": "silbena",
    "sight": "sven",
    "silent": "hljödhr",
    "silver": "arget",
    "silver hand": "argetlam",
    "sing": "gala",
    "sky": "lotha",
    "sleep": "slytha",
    "slow": "vëoht",
    "smooth": "lunaea",
    "snail": "snal",
    "snails": "snalglí",
    "soft": "blautr",
    "soil": "deloi",
    "song": "söngr",
    "song": "rune",
    "sorrow": "harmr",
    "sound": "sund",
    "sharp sound": "titlingr",
    "speak": "thorta",
    "spear": "daert",
    "spell": "galdr",
    "splendor": "ellesméra",
    "spring": "vara",
    "squeeze": "kremja",
    "star": "evarína, stjarna",
    "stare": "kópa",
    "stay": "sitja",
    "steel": "stál",
    "stick-out": "skaga",
    "stick": "keppr",
    "stone-crag": "hamarr",
    "stone": "stenr",
    "stop": "letta",
    "storm-cleaver": "vervada",
    "strong": "ramr",
    "sun": "solus",
    "swear": "otherúm",
    "sword": "sverd",
    "take": "taka",
    "taunt": "skuta",
    "temper": "tuatha",
    "tempering the fool’s wisdom": "tuatha du orothrim",
    "tempering": "tuatha",
    "than": "thön",
    "thank": "elrun",
    "that": "sem",
    "the": "du",
    "their": "theirra",
    "then": "thae",
    "there": "thar",
    "they": "therr",
    "thicken": "thaefathan",
    "rod": "vöndr",
    "this": "thornessa",
    "thorn": "thin",
    "thornapple": "haldthin",
    "those": "thorna",
    "thought": "hügin",
    "throw": "thrautha",
    "thrust; compress": "thringa",
    "forth": "fortha",
    "to": "eom",
    "prominence": "edur",
    "traverse": "thverr",
    "tree": "traevam",
    "true": "ilumaro",
    "truth": "ilumëo",
    "unconquerable": "edoc’sil",
    "under": "undir",
    "up": "audr",
    "upon": "vel",
    "us": "nosu",
    "vine": "lianí",
    "void": "und",
    "walrus": "hröslvalhr",
    "war": "fyrn",
    "ward": "vard",
    "warders": "varden",
    "warp": "orpin",
    "warped": "orpinn",
    "was": "ero",
    "watch over": "varda",
    "water": "adurna",
    "we": "vae",
    "welcome": "astorí",
    "were": "erní",
    "wet": "akr",
    "whale": "hwal",
    "what": "hvat",
    "white": "hvitr",
    "shiny": "bleikr",
    "will": "weohnata",
    "wind, air": "vindr",
    "wing": "vaengr",
    "wise-man": "chetowä",
    "wise": "svit",
    "with": "medh, oth",
    "without": "laust",
    "woman": "kona",
    "would": "weohnataí",
    "writing": "liduen",
    "wyrm": "orúm",
    "you": "ono",
    "your": "onr",
    "hope": "vaeta",
    "night": "thindarë",
    "twist": "rítha",
    "twisted" : "ríthaí",
    "son": "sönr",
    "yes": "já",
    "still": "entha",
    "whiten": "hvitra",
    "light": "líjothsa",
    "lift": "lyftha",
    "turn": "sving",
    "swing":"sving",
    "no": "né",
    "melt": "melthna"
}


app = Flask('')
@app.route('/')
def main():
  return "Hey! Nothing to see here!"

def run():
  app.run(host="0.0.0.0", port=os.environ.get("PORT"))

def keep_alive():
  server = Thread(target=run)
  server.start()


tokeninp = os.environ.get("TOKEN")
import hikari
import lightbulb
import datetime
from datetime import datetime
from datetime import *
import platform
from re import match

bot = lightbulb.BotApp(
token=tokeninp,
  prefix="+",
  intents=(hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.GUILD_MEMBERS
           | hikari.Intents.MESSAGE_CONTENT),
  help_slash_command=True,
)
ec = 0x2f3136


# LOGS SECTION
@bot.listen(hikari.MemberCreateEvent)
async def on_member_join(event: hikari.MemberCreateEvent):
  channel = 1257953871167488111
  welcometext = f'''welcome cuh just have a good time'''
  embed = hikari.Embed(title="    ", description=welcometext, color=ec) 
  await bot.rest.create_message(channel, embed)
  await bot.rest.create_message(channel, f"<@{event.user.id}>")




@bot.listen(hikari.GuildMessageCreateEvent)
async def eventlist(event: hikari.GuildMessageCreateEvent):
    channel = await event.message.fetch_channel()
    print(event.message.content, f" was sent in the channel. <#{event.channel_id}>")
    msg = hikari.Embed(title = f"**Message Logs**", description = f'''
    **`Message ID:`** **{event.message_id}**
    **`Message Author:`** **{event.message.author}**
    **`Author ID:`** **{event.message.author.id}**
    **`Channel ID:`** **{event.channel_id}**
    **`Server ID:`** **{event.guild_id}**
    Message Content
    ```{event.message.content}```'''
    , color = ec)
    if event.message.author.id == 1234471596056510484:
      return
    else:
      await bot.rest.create_message(1258705649399889920, msg)





@bot.command
@lightbulb.option("sentence","Sentencec to translate",modifier = lightbulb.commands.OptionModifier.CONSUME_REST)
@lightbulb.command("translate", "English to Ancient Language")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def translate(ctx):
    sentence1 = ctx.options.sentence
    sentence = sentence1.lower()
    translations = ALtoENG
    words = sentence.split()  # Split the sentence into words
    translated_words = []

    # Translate each word in the sentence
    for word in words:
        translation = translations.get(word.lower(), word)  # Use .get() to handle missing translations
        if isinstance(translation, list):
            translated_word = random.choice(translation)  # Pick a random translation from the list
        else:
            translated_word = translation
        translated_words.append(translated_word)

    # Join translated words back into a sentence
    translated_sentence = " ".join(translated_words)
    embed = hikari.Embed(title = "English To Ancient Language", description = f'''
 **Original**
 ```{sentence1}```
 **Translated**
 ```{translated_sentence}```''',color=ec)
    await ctx.respond(embed)




@bot.command
@lightbulb.option("name", "Title of the theory to delete.", required=True)
@lightbulb.command("theorydelete", "Delete a theory by its title")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def theorydelete(ctx):
    title_to_delete = ctx.options.name
    requesting_user_id = ctx.author.id

    conn = sqlite3.connect("theories.db")
    cursor = conn.cursor()

    cursor.execute('''
    SELECT title, author FROM theories WHERE title = ?
    ''', (title_to_delete,))
    theory = cursor.fetchone()

    if theory:
        title, author_id = theory
        if author_id == requesting_user_id:
            cursor.execute('''
            DELETE FROM theories WHERE title = ?
            ''', (title_to_delete,))
            conn.commit()
            conn.close()
            await ctx.respond(hikari.Embed(title='Theory Deletion',description=f"The theory titled **{title_to_delete}** has been deleted.",color=ec))
        else:
            conn.close()
            await ctx.respond("You do not have permission to delete this theory.")
    else:
        conn.close()
        await ctx.respond(f"No theory found with the title '{title_to_delete}'.")

import lightbulb
import hikari
import re
from collections import Counter


# Function to read the document
def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to find keyword in sentences
def find_keyword_in_sentences(text, keyword):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    keyword_sentences = [sentence for sentence in sentences if keyword.lower() in sentence.lower()]
    return keyword_sentences

# Function to find keyword in paragraphs
def find_keyword_in_paragraphs(text, keyword):
    paragraphs = text.split('\n\n')
    keyword_paragraphs = [paragraph for paragraph in paragraphs if keyword.lower() in paragraph.lower()]
    return keyword_paragraphs

# Lightbulb command to search the document
@bot.command
@lightbulb.option("maxresults", "Max amount of results", type=int, required=True)
@lightbulb.option("keyword", "Keyword to search for", required=True)
@lightbulb.command("searchdocument", "Search a document for a keyword")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def searchdocument(ctx):

    # Function to rank and get top matches
    def rank_and_get_top_matches(matches, keyword, top_n):
        color_start = '[31m'  # ANSI escape code for red text
        color_end = '[0m'  # ANSI escape code to reset text color

        # Shuffle matches to randomize the results
        random.shuffle(matches)

        ranked_matches = sorted(matches, key=lambda x: Counter(re.findall(r'\b' + re.escape(keyword) + r'\b', x, re.IGNORECASE)).get(keyword.lower(), 0), reverse=True)
        highlighted_matches = [re.sub(r'(?i)\b' + re.escape(keyword) + r'\b', color_start + r'\g<0>' + color_end, match) for match in ranked_matches[:top_n]]
        return highlighted_matches

    # Main function to search the document
    def search_document(file_path, keyword, search_by):
        text = read_document(file_path)

        if search_by == 'sentence':
            matches = find_keyword_in_sentences(text, keyword)
        elif search_by == 'paragraph':
            matches = find_keyword_in_paragraphs(text, keyword)
        else:
            raise ValueError("search_by must be either 'sentence' or 'paragraph'")

        top_matches = rank_and_get_top_matches(matches, keyword, ctx.options.maxresults)
        return top_matches

    file_path = 'books.txt'  # Replace with the path to your text document
    keyword = ctx.options.keyword
    search_by = "paragraph"

    top_matches = search_document(file_path, keyword, search_by)

    if top_matches:
        embed = hikari.Embed(
            title=f"Top matches for **{keyword}**",
            color=0x2f3136
        )
        for i, match in enumerate(top_matches, 1):
            embed.add_field(name=f"Match {i}", value=f'''```ansi
{match}```''', inline=False)
        await ctx.respond(embed)
    else:
        await ctx.respond(f"No matches found for '{keyword}'.")



@bot.command
@lightbulb.option("name", "Title of the theory.", required=True)
@lightbulb.command("theoryview", "Open a theory")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def test(ctx):
        search_query = ctx.options.name
        conn = sqlite3.connect("theories.db")
        cursor = conn.cursor()
        cursor.execute('''
        SELECT title, body, reasons_for, reasons_against, author FROM theories WHERE title LIKE ?
        ''', ('%' + search_query + '%',))
        theory = cursor.fetchone()
        conn.close()

        if theory:
            title, body, reasons_for, reasons_against, author = theory
            embed = hikari.Embed(
                title=f"**{title}**",
                description=f'''```{body}```
                **Reasons For:**
                {reasons_for}
                **Reasons Against:**
                {reasons_against}

                **Author**
                <@{author}>
                ''',
                color=0x2f3136
            )
            await ctx.respond(embed)
        else:
            await ctx.respond("No theory found with that title.")





@bot.command
@lightbulb.command("theorylist", "List of all theories")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def theories(ctx):
    conn = sqlite3.connect("theories.db")
    cursor = conn.cursor()
    cursor.execute('SELECT title, author FROM theories')
    rows = cursor.fetchall()
    conn.close()
    embed = hikari.Embed(title="List of Theories", color=ec)
    for row in rows:
        embed.add_field(name=row[0], value=f"Author: <@{row[1]}>", inline=False)
    embed2 = embed.set_footer(
        text=f"Requested by {ctx.member.display_name}",
        icon=ctx.member.avatar_url or ctx.member.default_avatar_url
    )
    await ctx.respond(embed2)
        
conn = sqlite3.connect("theories.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS theories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    reasons_for TEXT,
    reasons_against TEXT,
    author INTEGER NOT NULL
)
''')
import time
from datetime import time
ethanid = 877673438213439529
@bot.command
@lightbulb.option("sentence", "Words", required=True,modifier = lightbulb.commands.OptionModifier.CONSUME_REST)
@lightbulb.command("echo", "Repeat")
@lightbulb.implements(lightbulb.PrefixCommand)
async def theorize(ctx):
    if ctx.author.id == 877673438213439529:
        await ctx.event.message.delete()
        await ctx.respond(ctx.options.sentence)
    elif ctx.author.id == 1229726486504800268:
        await ctx.event.message.delete()
        await ctx.respond(ctx.options.sentence)
    else:
        await ctx.respond("You're not him!")
        







@bot.command
@lightbulb.option("word", "Word to find the etymology of", required=True)
@lightbulb.command("etymology", "Simple etymology finder",aliases=["ety"])
@lightbulb.implements(lightbulb.PrefixCommand)
async def etymology(ctx):
    word = ctx.options.word
    etymology = ety.tree(word)
    embed = hikari.Embed(title="**Etymology**", description=f'```{etymology}```', color=ec)
    embed2 = embed.set_footer(
        text=f"Requested by {ctx.member.display_name}",
        icon=ctx.member.avatar_url or ctx.member.default_avatar_url
    )
    await ctx.respond(embed2)

    
@bot.command
@lightbulb.option("reasonsfor", "Reasons for the theory", required=True)
@lightbulb.option("reasonsagainst", "Reasons against the theory", required=True)
@lightbulb.option("body", "The body of the theory", required=True)
@lightbulb.option("title", "Title of the theory", required=True)
@lightbulb.command("theorize", "Make a theory")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def theorize(ctx):
    embed = hikari.Embed(
        title=f"**{ctx.options.title}**",
        description=f'''```{ctx.options.body}```
        **Reasons For:**
        {ctx.options.reasonsfor}
        **Reasons Against:**
        {ctx.options.reasonsagainst}

        **Author**
        <@{ctx.author.id}>
        ''',
        color=0x2f3136
    )
    embed2 = embed.set_footer(
        text=f"Written by {ctx.member.display_name}",
        icon=ctx.member.avatar_url or ctx.member.default_avatar_url
    )

    theory = {
        "title": ctx.options.title,
        "body": ctx.options.body,
        "reasons_for": ctx.options.reasonsfor,
        "reasons_against": ctx.options.reasonsagainst,
        "author": ctx.author.id
    }

    conn = sqlite3.connect("theories.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO theories (title, body, reasons_for, reasons_against, author) VALUES (?, ?, ?, ?, ?)
    ''', (theory["title"], theory["body"], theory["reasons_for"], theory["reasons_against"], theory["author"]))

    conn.commit()
    conn.close()
    await ctx.respond(embed2)
    
@bot.command
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.command("serverinfo",
                   "Show's the information of the current server",
                   aliases=["si", "servinfo"],
                   auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def serverinfo(ctx: lightbulb.Context):
  guild = ctx.bot.cache.get_guild(
    ctx.guild_id) or await ctx.bot.rest.fetch_guild(ctx.guild_id)
  roles = await guild.fetch_roles()
  all_roles = [r.mention for r in roles]
  id = str(guild.id)
  created = int(guild.created_at.timestamp())
  owner = await guild.fetch_owner()
  members = len(guild.get_members().keys())
  verif = guild.verification_level.name.upper()
  role_count = len(guild.get_roles().keys())
  channels = len(guild.get_channels().keys())
  level = guild.premium_tier.value
  boost = guild.premium_subscription_count

  emb = hikari.Embed(color=0x2f3136,
                     title=f"Server info for {guild.name}",
                     colour=ctx.author.accent_color,
                     timestamp=datetime.now().astimezone())

  emb.set_thumbnail(guild.icon_url)
  emb.set_image(guild.banner_url)
  emb.add_field(name="ID", value=id, inline=False)
  emb.add_field(name="Owner", value=f"{owner} ({owner.mention})", inline=False)
  emb.add_field(name="Created At",
                value=f"<t:{created}:d>\n(<t:{created}:R>)",
                inline=False)
  emb.add_field(name="Member Count", value=f"{members} Members", inline=False)
  emb.add_field(name="Channel Count",
                value=f"{channels} Channels",
                inline=False)
  emb.add_field(name="Verification Level", value=verif, inline=False)
  emb.add_field(name="Server Level",
                value=f"Level {level} ({boost} Boosts.)",
                inline=False)

  if "COMMUNITY" in guild.features:
    emb.add_field(name="Rule Channel",
                  value=f"<#{guild.rules_channel_id}>",
                  inline=False)
  if guild.afk_channel_id:
    emb.add_field(name="AFK Channel",
                  value=f"<#{guild.afk_channel_id}> ({guild.afk_timeout})",
                  inline=False)

  if guild.features:
    features = guild.features
    emb.add_field(name="Guild Features",
                  value=", ".join(features).replace("_", " ").title(),
                  inline=False)

  emb.add_field(name=f"Roles ({role_count})",
                value=", ".join(all_roles)
                if len(all_roles) < 10 else f"{len(all_roles)} roles",
                inline=False)
  await ctx.respond(embed=emb)




@bot.command
@lightbulb.option("target", "The member to get information about.", hikari.Member, required=False)
@lightbulb.command("memberinfo", "Get info on a server member.", aliases=["mi","profile","minfo", "ui", "userinfo"], auto_defer=True, pass_options = True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def  member_info(ctx: lightbulb.Context, target: hikari.Member) -> None:
    if target is None:
        target = ctx.member

    user = ctx.bot.cache.get_guild(ctx.guild_id).get_member(target)
    banner = user.banner_url
    if not user:
        await ctx.respond("That user is not in the server")
        return

    created_at = int(user.created_at.timestamp())
    joined_at = int(user.joined_at.timestamp())

    roles = (await user.fetch_roles())[1:]  # All but @everyone



    emb = hikari.Embed(
        title=f"User Info - {user.username}#{user.discriminator}",
        description=f"ID: `{user.id}`",
        colour=ec,
        timestamp=datetime.now().astimezone(),
    )
    emb.set_footer(
        text=f"Requested by {ctx.member.display_name}",
        icon=ctx.member.avatar_url or ctx.member.default_avatar_url
    )
    emb.set_thumbnail(user.avatar_url or user.default_avatar_url)
    emb.add_field(
        "Bot?",
        str(user.is_bot),
        inline=True,
    )
    emb.add_field(
        "Created account on",
        f"<t:{created_at}:F>\n(<t:{created_at}:R>)",
        inline=False,
    )
    emb.add_field(
        "Joined server on",
        f"<t:{joined_at}:F>\n(<t:{joined_at}:R>)",
        inline=False,
    )
    emb.add_field(
        "Roles",
        ", ".join(r.mention for r in roles) or "No Roles.",
        inline=False,
    )
    emb.add_field(
        "Mention", 
        user.mention, 
        inline=False
    )

    await ctx.respond(emb.set_image(banner))

@bot.command
@lightbulb.command("law", "Get the server rules")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def law(ctx):
  embed = hikari.Embed(title = "**Server Rules**", description=f'''
*Here you'll find some general rules for the server. Remember to always follow Discord's TOS. That's important, and we'll enforce it too.*

 ` 1A `  Do not disrespect your fellow server members.

 ` 2A `  Do not talk over other people in vc, It is considered to be ignorant and is rude.

 ` 3A `  Do not use Slurs against others.

 ` 4A `  Do not beg for promotions, roles or anything else containing power.

 ` 5A `  Do not disrespect staff.

 ` 6A `  Do not judge people for expressing their belief's and hobbies, THIS INCLUDES: Race, Religion, Dress up, Gender, and more.

 ` 7A `  If you use a loop hole to avoid these laws you will be punished more harshly.

 ` 8A `  Gore and any form of Pornography or anything depicting Pornography will be prohibited.

 ` 9A `  Nazism and Extremism is prohibited. 

 ` 10A ` Posting unrelated media or gifs is prohibited.'''
                       ,
                       color=0x2f3136)
  embedimage = "https://cdn.discordapp.com/attachments/1258728657166532659/1259048633077334099/botav.png?ex=668a43ea&is=6688f26a&hm=e66de52112dcea76f6abb278a685c133bd289845f2f61c6f9cb40b532ef42168&"
  embedtrue = embed.set_footer(text = "More rules may be enacted soon, keep watch for any changes.", icon = embedimage)
  embedmore = embedtrue.set_thumbnail(embedimage)
  await ctx.respond(embedmore)



@bot.command
@lightbulb.add_cooldown(3, 3, lightbulb.UserBucket)
@lightbulb.option("target", "The member to get the banner.", hikari.User, required=False)
@lightbulb.command("banner", "Get a member's banner.", auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def user_banner(ctx: lightbulb.Context, target: hikari.User):
    """Show the banner of a user, if any"""
    if target is None:
        target = ctx.user

    user = await ctx.bot.rest.fetch_user(target)

    if not user:
        await ctx.respond("That user is not in the server.")
        return

    banner = user.banner_url
    # If statement because the user may not have a banner
    if banner:
        bnr = hikari.Embed(
                description=f"**{user.mention}**'s Banner",
                title="Banner Viewer",
                color=ec,
                timestamp=datetime.now().astimezone(),
            )
        bnr.set_image(banner)
        await ctx.respond(embed=bnr)
    else:
        await ctx.respond(embed=hikari.Embed(description="This User has no banner set."))

@bot.command
@lightbulb.option("server", "Get the server avatar instead?", bool, required = False, default = False)
@lightbulb.option("target", "The member to get the avatar.", hikari.Member , required=False)
@lightbulb.command("avatar", "Get a member's avatar.", auto_defer=True, aliases=["pp", "pfp","ava","icon"], pass_options = True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def user_avatar(ctx: lightbulb.Context, target: hikari.Member, server: bool):
    """Show avatar of a user, if any"""
    if target is None:
        target = ctx.member

    user =  ctx.bot.cache.get_guild(ctx.guild_id).get_member(target)

    if not user:
        await ctx.respond("That user is not in the server.")
        return

    if server:
        try:
            pfp = user.guild_avatar_url
        except AttributeError:
            return await ctx.respond("That user doesn't have server-specific avatar.")
    else:
        pfp = target.avatar_url or target.default_avatar_url
    # If statement because the user may not have a custom avatar
    if pfp:
        ava = hikari.Embed(
                description=f"**{user.mention}**'s Avatar",
                title="Avatar Viewer",
                color=ec,
                timestamp=datetime.now().astimezone(),
            )
        ava.set_image(pfp)
        await ctx.respond(embed=ava)
    else:
        await ctx.respond(embed=hikari.Embed(description="This User has no avatar set."))









@bot.command
@lightbulb.command("ping", "measure the ping of the bot", auto_defer=True, aliases=["pong"])
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    heartbeat = ctx.bot.heartbeat_latency * 1000
    txt = (f"*Pong*")

    if isinstance(ctx, lightbulb.PrefixContext):
        if ctx.invoked_with == "pong":
            txt = (f"*Ping*")

    if heartbeat > 1000:
        colours = hikari.Colour(0xFF0000)
    elif heartbeat > 500:
        colours = hikari.Colour(0xFFFF00)
    else:
        colours = hikari.Colour(0x26D934)

    ping = hikari.Embed(
            title="Current Ping:",
            description=f"```{heartbeat:,.2f}ms```",
            color=ec,
        )
    await ctx.respond(embed=ping)


@bot.command()
@lightbulb.add_cooldown(3, 3, lightbulb.UserBucket)
@lightbulb.option("word", "The text you want to define", str, required=True, modifier = lightbulb.commands.OptionModifier.CONSUME_REST)
@lightbulb.command("define", "Look up the definition of a word", aliases=["def", "dictionary"], auto_defer=True, pass_options = True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def dictionary(ctx: lightbulb.Context, word) -> None:
    word = ctx.options.word
    defi = dictionary.meaning(word)
    syn = dictionary.synonym(word)
    ant = dictionary.antonym(word)
    embed = hikari.Embed(title=f"Analysis of {word}", description=f'''
**Definition:**
{defi}
**Synonyms:**
{syn}
**Antonyms:**
{ant}''', color=ec)
    await ctx.respond(embed)

@bot.command
@lightbulb.command('databackup', 'Admin command')
@lightbulb.implements(lightbulb.SlashCommand,lightbulb.PrefixCommand)   
async def backup(ctx):
    f = hikari.File('theories.db')
    await ctx.respond(f)
    
keep_alive()
bot.run(
    status=hikari.Status.DO_NOT_DISTURB,
    activity=hikari.Activity(
        name="Library of Arcaena",
        type=hikari.ActivityType.LISTENING,
    ),
)
