import hikari
import lightbulb
from keep_alive import keep_alive

tokeninp = input("What is your token? ")
bot = lightbulb.BotApp(
token=tokeninp,
  prefix="+",
  intents=(hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.GUILD_MEMBERS
           | hikari.Intents.MESSAGE_CONTENT),
  help_slash_command=False,
)
ec = 0x2f3136


# LOGS SECTION
@bot.listen(hikari.MemberCreateEvent)
async def on_member_join(event: hikari.MemberCreateEvent):
  channel = 1234152271558737930
  welcometext = f'''♡ 𝐇𝐞𝐲 𝐭𝐡𝐞𝐫𝐞 <@{event.user.id}>!!

  ๑‧˚₊꒷꒦︶︶︶ **INFO**  🍰

  ⌇ 🪷 ⌇ 𝘨𝘦𝘵 𝘺𝘰𝘶𝘳 𝘳𝘰𝘭𝘦𝘴 𝘪𝘯 : <#1234152279259746426>
  ⌇ 🌙 ⌇ 𝘳𝘦𝘮𝘦𝘮𝘣𝘦𝘳 𝘵𝘰 𝘳𝘦𝘢𝘥  : <#1234152275090477106>
  ⌇  ⌇ 𝘤𝘩𝘢𝘵 𝘪𝘯 : <#1234152282451476550>

    ✦ ₊꒷꒦ෆ꒷꒥꒷ ‧₊˚ 𝐡𝐚𝐯𝐞 𝐟𝐮𝐧!'''
  embed = hikari.Embed(title="    ", description=welcometext, color=ec)
  await bot.rest.create_message(channel, embed.set_image('''https://cdn.discordapp.com/attachments/1233703141145313360/1234422515858673755/R.png?ex=6630ad0e&is=662f5b8e&hm=97c6f534c4a333328947a78a3225eb514bdee4b7c41847880436d6e3134da278&'''))
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
    if event.message.author.id == 1200705803380854905:
      return
    else:
      await bot.rest.create_message(1234407443472318594, msg.set_image('''https://cdn.discordapp.com/attachments/1234152282451476550/1234399732382826576/92a23e6ac048f2849f10f530d20a91f0.jpg?ex=663097d6&is=662f4656&hm=254d15b05a6a70e611f8f306729c4d802ca3fff4064596ec6026653e5da7d6a9&'''))





@bot.command
@lightbulb.command("test", "Run Test")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def test(ctx):
    embed = hikari.Embed(title = "**TEST**", description=f'''

```   T E S T I N G   ```''', color =  0x2f3136)
    await ctx.respond(embed)

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

 ` 10A ` Posting unrelated media or gifs is prohibited.

 ` 11A ` Anime is recognised as a mental illness in this country, PFPs are allowed on a minimal level (joke)

 ` 1I ` No leaking intel.'''
                       ,
                       color=0x2f3136)
  embedimage = '''https://cdn.discordapp.com/attachments/1234152271558737930/1234398092128944189/e6fd77fa975588e4c3bfe4598a0452fb.png?ex=6630964f&is=662f44cf&hm=1256774af719e93da2aa5e2646207b5181dddedad11f8b29083d0978c8bb3bcb&'''

  embed_withimage = embed.set_image("https://cdn.discordapp.com/attachments/1234152271558737930/1234400990241755187/ffb382b6878e0907097dd82025a1e4302354539c803d472de75cb659845bbe4b_1.png?ex=66309902&is=662f4782&hm=12b86ba85c6b73d68d3441ffef517f54328c915172fbd104b6c8f50571c632c5&")
  embedtrue = embed_withimage.set_footer(text = "More rules may be enacted soon, keep watch for any changes.", icon = embedimage)
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
    try:
        #--Connect to unofficial Google Dictionary API and get results--#
        async with ctx.bot.d.aio_session.get(f'https://api.dictionaryapi.dev/api/v1/entries/en/{word}') as r:
            #--Now we decode the JSON and get the variables, replacing them with None if they fail to define--#
            result = await r.json()
            word = result[0]['word']
            try:
                origin = result[0]['origin']
            except KeyError:
                origin = None
            try:
                noun_def = result[0]['meaning']['noun'][0]['definition']
            except KeyError:
                noun_def = None
            try:
                noun_eg = result[0]['meaning']['noun'][0]['example']
            except KeyError:
                noun_eg = None
            try:
                verb_def = result[0]['meaning']['verb'][0]['definition']
            except KeyError:
                verb_def = None
            try:
                verb_eg = result[0]['meaning']['verb'][0]['example']
            except KeyError:
                verb_eg = None
            try:
                prep_def = result[0]['meaning']['preposition'][0]['definition']
            except KeyError:
                prep_def = None
            try:
                prep_eg = result[0]['meaning']['preposition'][0]['example']
            except KeyError:
                prep_eg = None
            try:
                adverb_def = result[0]['meaning']['adverb'][0]['definition']
            except KeyError:
                adverb_def = None
            try:
                adverb_eg = result[0]['meaning']['adverb'][0]['example']
            except KeyError:
                adverb_eg = None
            try:
                adject_def = result[0]['meaning']['adjective'][0]['definition']
            except KeyError:
                adject_def = None
            try:
                adject_eg = result[0]['meaning']['adjective'][0]['example']
            except KeyError:
                adject_eg = None
            try:
                pronoun_def = result[0]['meaning']['pronoun'][0]['definition']
            except KeyError:
                pronoun_def = None
            try:
                pronoun_eg = result[0]['meaning']['pronoun'][0]['example']
            except KeyError:
                pronoun_eg = None
            try:
                exclaim_def = result[0]['meaning']['exclamation'][0]['definition']
            except KeyError:
                exclaim_def = None
            try:
                exclaim_eg = result[0]['meaning']['exclamation'][0]['example']
            except KeyError:
                exclaim_eg = None
            try:
                poss_determ_def = result[0]['meaning']['possessive determiner'][0]['definition']
            except KeyError:
                poss_determ_def = None
            try:
                poss_determ_eg = result[0]['meaning']['possessive determiner'][0]['example']
            except KeyError:
                poss_determ_eg = None
            try:
                abbrev_def = result[0]['meaning']['abbreviation'][0]['definition']
            except KeyError:
                abbrev_def = None
            try:
                abbrev_eg = result[0]['meaning']['abbreviation'][0]['example']
            except KeyError:
                abbrev_eg = None
            try:
                crossref_def = result[0]['meaning']['crossReference'][0]['definition']
            except KeyError:
                crossref_def = None
            try:
                crossref_eg = result[0]['meaning']['crossReference'][0]['example']
            except KeyError:
                crossref_eg = None
            embed = hikari.Embed(
                title=f":blue_book: Google Definition for {word}", color=0x8253c3)
            #--Then we add see if the variables are defined and if they are, those variables to an embed and send it back to Discord--#
            if origin == None:
                pass
            else:
                embed.add_field(name="Origin:", value=origin, inline=False)
            if noun_def == None:
                pass
            else:
                if noun_eg == None:
                    embed.add_field(
                        name="As a Noun:", value=f"**Definition:** {noun_def}", inline=False)
                else:
                    embed.add_field(
                        name="As a Noun:", value=f"**Definition:** {noun_def}\n**Example:** {noun_eg}", inline=False)
            if verb_def == None:
                pass
            else:
                if verb_eg == None:
                    embed.add_field(
                        name="As a Verb:", value=f"**Definition:** {verb_def}", inline=False)
                else:
                    embed.add_field(
                        name="As a Verb:", value=f"**Definition:** {verb_def}\n**Example:** {verb_eg}", inline=False)
            if prep_def == None:
                pass
            else:
                if prep_eg == None:
                    embed.add_field(
                        name="As a Preposition:", value=f"**Definition:** {prep_def}", inline=False)
                else:
                    embed.add_field(
                        name="As a Preposition:", value=f"**Definition:** {prep_def}\n**Example:** {prep_eg}", inline=False)
            if adverb_def == None:
                pass
            else:
                if adverb_eg == None:
                    embed.add_field(
                        name="As an Adverb:", value=f"**Definition:** {adverb_def}", inline=False)
                else:
                    embed.add_field(
                        name="As a Adverb:", value=f"**Definition:** {adverb_def}\n**Example:** {adverb_eg}", inline=False)
            if adject_def == None:
                pass
            else:
                if adject_eg == None:
                    embed.add_field(
                        name="As an Adjective:", value=f"**Definition:** {adject_def}", inline=False)
                else:
                    embed.add_field(
                        name="As an Adjective:", value=f"**Definition:** {adject_def}\n**Example:** {adject_eg}", inline=False)
            if pronoun_def == None:
                pass
            else:
                if pronoun_eg == None:
                    embed.add_field(
                        name="As a Pronoun:", value=f"**Definition:** {pronoun_def}", inline=False)
                else:
                    embed.add_field(
                        name="As a Pronoun:", value=f"**Definition:** {pronoun_def}\n**Example:** {pronoun_eg}", inline=False)
            if exclaim_def == None:
                pass
            else:
                if exclaim_eg == None:
                    embed.add_field(
                        name="As an Exclamation:", value=f"**Definition:** {exclaim_def}", inline=False)
                else:
                    embed.add_field(
                        name="As an Exclamation:", value=f"**Definition:** {exclaim_def}\n**Example:** {exclaim_eg}", inline=False)
            if poss_determ_def == None:
                pass
            else:
                if poss_determ_eg == None:
                    embed.add_field(name="As a Possessive Determiner:",
                                    value=f"**Definition:** {poss_determ_def}", inline=False)
                else:
                    embed.add_field(name="As a Possessive Determiner:",
                                    value=f"**Definition:** {poss_determ_def}\n**Example:** {poss_determ_eg}", inline=False)
            if abbrev_def == None:
                pass
            else:
                if abbrev_eg == None:
                    embed.add_field(
                        name="As an Abbreviation:", value=f"**Definition:** {abbrev_def}", inline=False)
                else:
                    embed.add_field(
                        name="As an Abbreviation:", value=f"**Definition:** {abbrev_def}\n**Example:** {abbrev_eg}", inline=False)
            if crossref_def == None:
                pass
            else:
                if crossref_eg == None:
                    embed.add_field(
                        name="As a Cross-Reference:", value=f"**Definition:** {crossref_def}", inline=False)
                else:
                    embed.add_field(
                        name="As a Cross-Reference:", value=f"**Definition:** {crossref_def}\n**Example:** {crossref_eg}", inline=False)
            await ctx.respond(embed=embed)
    except:
        #--Send error message if command fails, as it's assumed a definition isn't found--#
        await ctx.respond(content=":x: Sorry, I couldn't find that word. Check your spelling and try again.")


bot.run(
    status=hikari.Status.DO_NOT_DISTURB,
    activity=hikari.Activity(
        name="Library of Arcaena",
        type=hikari.ActivityType.LISTENING,
    ),
)

keep_alive()
