import discord
from discord.ext import commands
import random
import asyncio
intents = discord.Intents.all()
client = commands.Bot(command_prefix=".",intents=intents)



@client.event
async def on_ready():

   
    print("Bot is ready")


    await client.wait_until_ready()
    statuses=[f"{len(client.users)} members",f"on {len(client.guilds)} servers|;command"]

    while not client.is_closed():
        status=random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(5)
client.loop.create_task(on_ready())

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Your role isn't high enough")
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguments")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("Invalid command")


@client.command()
@commands.has_permissions(send_messages=True)
async def membercount(ctx):
    embed=discord.Embed(title="Members",color=discord.Color.blue())
    embed.add_field(name=f"{ctx.guild.member_count}",value=f"{ctx.guild.name}")
    await ctx.send(embed=embed)
    


@client.command()
@commands.has_permissions(ban_members=True)
async def cu(ctx,cnum1,cnum2):
  cnum1=int(cnum1)
  cnum2=int(cnum2)
  for i in range (cnum1,cnum2+1):
    await ctx.send(cnum1)
    cnum1=cnum1+1

@client.command(aliases=['fireblazer','fireblazer1506'])
async def preetham(ctx):
    await ctx.send("my developer")

    
@client.command(aliases=['tida'])
async def adit(ctx):
    await ctx.send("knows only 3 words - you, are and dumb")

@client.command(aliases=['anu'])
async def anurag(ctx):
    await ctx.send("thicc")

@client.command()
async def arnav(ctx):
    #await ctx.send("roll number - 6,gets bullied everyday,doesnt have common sense and he is also known as flamingo. Once he fractured his hand by just falling down on the ground.")
    await ctx.send("wants to get me banned")
    #embed = discord.Embed(title="Arnav", color=discord.Color.purple())
    
    #embed.add_field(name="Gender", value="6"+" 🏳️‍🌈",inline=False)
    #embed.add_field(name="Status", value="In a relationship with Arjun and 2 others",inline=False)
    
    #embed.add_field(name="Hobbies",value="Arguing,Asking Fireblazer for free stuff and then arguing, Crying,flattering ppl, Getting bullied everyday, fracturing his hand again and again and blaming others, Make no sense in conversations, Giving dumb excuses,Addicted to the word hmm Spreading rumours like a typical Indian aunty, Lying, Not being peaceful ",inline=False)
    
    #embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/726311704941690901/851683941580800020/Inkedfunny_pic_LI.jpg")
    #embed.set_image(url="https://cdn.discordapp.com/attachments/841616049732190208/851695741394354196/gay.png")
    #await ctx.send(embed=embed)

@client.command(aliases=['abhi','sheikh'])
async def abhishek(ctx):
    await ctx.send("ishika ka premi but got rejected by her :(")

@client.command(aliases=['shubh','shubhabcd'])
async def shubham(ctx):
    await ctx.send("chutiya")

@client.command(aliases=["clear"])
@commands.has_permissions(manage_messages= True)
async def c(ctx,amount=2):
    await ctx.channel.purge(limit=amount)



@client.command(aliases=['short','tingu'])
async def mantej(ctx):
    await ctx.send("noob")

@client.command(aliases=['anario','anonymous'])
async def anubhav(ctx):
    await ctx.send("he thinks that he doesnt exist")

@client.command(aliases=['kick'])
@commands.has_permissions(kick_members=True)
async def yeet(ctx,member:discord.Member,):
    try:
        await member.kick()
        await ctx.send(member.name+" was yeeted")

    except:
        await ctx.send("role is lower")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member,):
    try:
        
        await member.ban()
        await ctx.send(member.name+" was banned")
    except:
        await ctx.send("role is lower")
        
usermsg=""
dmnum=""

@client.command()
@commands.has_permissions(ban_members=True)
async def spam(ctx,member:discord.Member,usermsg,dmnum):
    dmnum=int(dmnum)
    if dmnum==69 or dmnum<69:
        try:
            for i in range(0,dmnum):
                await member.send(usermsg)
            await ctx.send(member.mention + " check ur dms")
        except:
            await ctx.send(member.mention+" has closed their dms")
    else:
        await ctx.send("limit is 69 dms")

@client.command()
@commands.has_permissions(ban_members=True)
async def ping(ctx,member:discord.Member,pingnum):
    pingnum=int(pingnum)
    if pingnum==69 or pingnum<69:
        for i in range(0,pingnum):
                await ctx.send(member.mention)

    else:
        await ctx.send("limit is 69 pings")
mmsg=""
pingnum2=""
@client.command()
@commands.has_permissions(ban_members=True)
async def mping(ctx,member:discord.Member,mmsg,pingnum2):
    pingnum2=int(pingnum2)
    if pingnum2==69 or pingnum2<69:
        for i in range(0,pingnum2):
                await ctx.send(member.mention+mmsg)

    else:
        await ctx.send("limit is 69 pings")
msg3=""
msgnum3=""
@client.command()
@commands.has_permissions(ban_members=True)
async def mspam(ctx,msg3,msgnum3):
    msgnum3=int(msgnum3)
    if msgnum3==69 or msgnum3<69:
        for i in range(0,msgnum3):
            await ctx.send(msg3)
    else:
        await ctx.send("limit is 69 messages")

@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=851074942296260619&permissions=8&scope=bot")



@client.command()
@commands.has_permissions(send_messages=True)
async def command(ctx):
    embed=discord.Embed(title="Commands List",color=discord.Color.blue())
    embed.add_field(name=";avatar",value="sends avatar of user")
    embed.add_field(name=";spam",value="spams dm to a user")
    embed.add_field(name=";ping", value="mass pings a user")
    embed.add_field(name=";mping", value="pings a user and spams a msg in the server channel")
    embed.add_field(name=";arnav", value="gives arnav's description")
    embed.add_field(name=";ban", value="bans a user")
    embed.add_field(name=";kick", value="kicks user from the server")
    embed.add_field(name=";mute", value="mutes a user")
    embed.add_field(name=";unmute", value="unmutes a muted user")
    embed.add_field(name=";invite", value="invite the bot to ur server")
    embed.add_field(name=";clear", value="deletes messages")
    embed.add_field(name=";mspam", value="spams a message in the server channel")
    embed.add_field(name=";membercount", value="sends number of members in the server")
    embed.add_field(name=";cu", value="can be used in #counting to count numbers")
    embed.add_field(name=";tictactoe", value="starts a game of tictactoe")
    embed.add_field(name=";cancel", value="cancels ongoing tictactoe game")
    embed.add_field(name=";crunchy", value="generates a crunchyroll acc")
    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx,member:discord.Member):
    embed=discord.Embed(title=member.name, color=discord.Color.red())
    embed.add_field(name="Avatar",value=member.id)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def nsfw(ctx):
    await ctx.send("go to horny jail. bonk!")

@client.command(aliases=["m"])
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member:discord.Member):
    guild=ctx.guild
    mutedRole=discord.utils.get(guild.roles,name="Muted")
    if not mutedRole:
        mutedRole=await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,speak=False,send_messages=False,read_message_history=True,read_messages=False)
    await member.add_roles(mutedRole)
    await ctx.send(member.mention+" has been silenced")

@client.command(aliases=["unm"])
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member:discord.Member):
    mutedRole=discord.utils.get(ctx.guild.roles,name="Muted")
    await member.remove_roles(mutedRole)
    await ctx.send(member.mention+" has been unmuted")

crunchy_accs=["beatdown7478@yahoo.com:Ohnedich2 | Telegram id:  - Subscribed to: anime|drama|manga",
"isaiahjb1@yahoo.com:06251996Ijb | Telegram id:  - Subscribed to: anime|drama|manga",
"steve_o6139@hotmail.com:692013009 | Telegram id:  - Subscribed to: anime|drama|manga",
"Rilikb@gmail.com:sk8later | Telegram id:  - Subscribed to: anime|drama|manga",
"isernhas3@hotmail.com:goo00gle1 | Telegram id: - Subscribed to: anime|drama|manga",
"marcusrneely@Yahoo.com:seeker12 | Telegram id:  - Subscribed to: anime|drama|manga",
"johndonglong@yahoo.com:Undone1337 | Telegram id:  - Subscribed to: anime|drama|manga",
"cdavisdrafting@aol.com:Wh1skers | Telegram id:  - Subscribed to: anime|drama|manga",
"mka1232002@gmail.com:memo2002 | Telegram id:  - Subscribed to: anime|drama|manga",
"redsoxboy826@aol.com:Password9 | Telegram id:  - Subscribed to: anime|drama|manga",
"naomiortiz720@gmail.com:Angelena2001 | Telegram id:  - Subscribed to: anime|drama|manga",
"trevor9453@gmail.com:wild9453 | Telegram id:  - Subscribed to: anime|drama|manga",
"namitown@gmail.com:Mira4242564 | Telegram id:  - Subscribed to: anime|drama|manga",
"mysticgilford101@yahoo.com:Gearfried12 | Telegram id:  - Subscribed to: anime|drama|manga",
"baseballallstar227@gmail.com:Bossness8 | Telegram id:  - Subscribed to: anime|drama|manga",
"sydpasterczyk@gmail.com:37Sniper | Telegram id:  - Subscribed to: anime|drama|manga",
"samoneal631@gmail.com:gohawks23 | Telegram id:  - Subscribed to: anime|drama|manga",
"freerunnertk@yahoo.com:Urbanno1! | Telegram id:  - Subscribed to: anime|drama|manga",
"crosillo23@gmail.com:Cars1993 | Telegram id:  - Subscribed to: anime|drama|manga",
"chris.arroyo@yahoo.com:Ilovemay25 | Telegram id:  - Subscribed to: anime|drama|manga",
"jitb50801@gmail.com:nobissmeu1 | Telegram id:  - Subscribed to: anime|drama|manga",
"nasereenali@gmail.com:Tut3ankhamon | Telegram id:  - Subscribed to: anime|drama|manga",
"exia0094@gmail.com:rklssfre94 | Telegram id:  - Subscribed to: anime|drama|manga",
"chancebroadway@yahoo.com:Annieb94 | Telegram id:  - Subscribed to: anime|drama|manga",
"dustman075@aol.com:422520dw | Telegram id:  - Subscribed to: anime|drama|manga",
"Morpice@gmail.com:DDadc664 | Telegram id:  - Subscribed to: anime|drama|manga",
"victordancona@hotmail.com:janeiro04 | Telegram id:  - Subscribed to: anime|drama|manga",
"slaytontreven@yahoo.com:Karnell23 | Telegram id:  - Subscribed to: anime|drama|manga",
"Tanno_55@hotmail.com:tanman12 | Telegram id:  - Subscribed to: anime|drama|manga",
"mccall.carl8@gmail.com:unlockm3 | Telegram id:  - Subscribed to: anime|drama|manga",
"seabrick22@mail.com:Kaeldane2 | Telegram id:  - Subscribed to: anime|drama|manga",
"rm.magnisalis@gmail.com:MaxMagni | Telegram id:  - Subscribed to: anime|drama|manga",
"moomization@gmail.com:pickles2 | Telegram id:  - Subscribed to: anime|drama|manga",
"bryan.interiano@gmail.com:Panda4217 | Telegram id:  - Subscribed to: anime|drama|manga",
"sergiowork22@gmail.com:Checho14 | Telegram id:  - Subscribed to: anime|drama|manga",
"matu_miami@hotmail.com:agramon14 | Telegram id:  - Subscribed to: anime|drama|manga",
"kingcj86@aol.com:Bonjour@86 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"allenm_09@yahoo.com:qazwsxedc9 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"garethcodling@yahoo.com:spiderman1 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"xbuji6@gmail.com:vacavaca321 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"zanyzander24@yahoo.com:Angryveve1 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"ovanovicoff94@gmail.com:26715877 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"krisgbb13273@yahoo.com:cobraKD20 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"mikefreyer4@gmail.com:quins444 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"gleeliza@aol.com:Mommy777 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"kyenodanna@yahoo.com:Shonen303 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"kverburgt@yahoo.com:Cooper21 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"vincentervinii@yahoo.com:Ilovemyfamily3# | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"gsoccerfan101@aol.com:naruto00 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"mark_fleming_3@hotmail.com:Starcraft12 | Telegram id: @PremiumHostTG - Subscribed to: anime|drama|manga",
"marijan.lacko@gmail.com:mlacko66 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 11:12:18 PM | Telegram id: @PremiumHostTG - ",
"bigcrozier56@gmail.com:Notlad95 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 12:56:44 AM | Telegram id: @PremiumHostTG - ",
"onehundredandfirsta.s.t@gmail.com:a.m604817 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 12:57:59 AM | Telegram id: @PremiumHostTG -",
"eathan.is.epic@gmail.com:cucu1904 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 12:58:59 AM | Telegram id: @PremiumHostTG - ",
"emaguilerar@gmail.com:Shadown1 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 12:59:31 AM | Telegram id: @PremiumHostTG - ",
"corbett_christopher@yahoo.com:dougless1 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:00:00 AM | Telegram id: @PremiumHostTG -",
"devante21watson@yahoo.com:watson22 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:01:53 AM | Telegram id: @PremiumHostTG - ",
"this.davi@gmail.com:91352400 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:03:22 AM | Telegram id: @PremiumHostTG - ",
"n.gigin@web.de:Cassie17 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:03:31 AM | Telegram id: @PremiumHostTG - ",
"cristianncht@yahoo.com:criscool99 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:17:18 AM | Telegram id: @PremiumHostTG -",
"brboobug73@aol.com:Brettjr12 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:24:56 AM | Telegram id: @PremiumHostTG - ",
"cindi.gaines@yahoo.com:dominique5 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:28:23 AM | Telegram id: @PremiumHostTG -",
"alyssaankney@gmail.com:buddy1 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:30:09 AM | Telegram id: @PremiumHostTG - ",
"kajunior14@gmail.com:Charger0519 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:30:20 AM | Telegram id: @PremiumHostTG - ",
"nessa_bor@hotmail.com:89032460 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:31:38 AM | Telegram id: @PremiumHostTG - ",
"aarteaga3150@yahoo.com:Tonyhawk01 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:34:16 AM | Telegram id: @PremiumHostTG -",
"nick.aladar.young@gmail.com:nottey69 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:34:35 AM | Telegram id: @PremiumHostTG -",
"lucas.rachewsky@hotmail.com:lksbabu12 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:34:39 AM | Telegram id: @PremiumHostTG - ",
"snowdvl@msn.com:Phantom1 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:34:49 AM | Telegram id: @PremiumHostTG - ",
"will.nikaido@gmail.com:Gor3ds0x | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:39:05 AM | Telegram id: @PremiumHostTG -",
"saint0fst33l@gmail.com:Harryharry1 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:39:27 AM | Telegram id: @PremiumHostTG -",
"msitton@gmail.com:Mms09428- | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:44:10 AM | Telegram id: @PremiumHostTG - ",
"youngturner96@gmail.com:Psychology1 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:44:57 AM | Telegram id: @PremiumHostTG -",
"dennis.eigner55@gmail.com:vampirsaft535 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:45:59 AM | Telegram id: @PremiumHostTG - ",
"jonathans2700@yahoo.com:Krypton27 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 1:58:44 AM | Telegram id: @PremiumHostTG - ",
"luiz.tyler@gmail.com:luiz5704 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:02:08 AM | Telegram id: @PremiumHostTG - ",
"direarchangelblade@gmail.com:dragonslayer1 | Type = premium_plus | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:05:46 AM | Telegram id: @PremiumHostTG -",
"chaury07@gmail.com:CleBrowns07 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:11:53 AM | Telegram id: @PremiumHostTG - ",
"callumphillip13579@gmail.com:grimmond | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:13:06 AM | Telegram id: @PremiumHostTG -",
"jboss260@gmail.com:Class201 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:14:32 AM | Telegram id: @PremiumHostTG - ",
"ramiro_g84@hotmail.com:2004243001 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:15:08 AM | Telegram id: @PremiumHostTG -",
"erickg1730@gmail.com:123456skyrim | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:18:07 AM | Telegram id: @PremiumHostTG - ",
"henriquez.salinas1@gmail.com:133133aa | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:19:04 AM | Telegram id: @PremiumHostTG -",
"amberlambert1@aol.com:Morgan2004 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:22:42 AM | Telegram id: @PremiumHostTG - ",
"c3ser93@gmail.com:21601141cf | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:23:53 AM | Telegram id: @PremiumHostTG - ",
"erikbb22@gmail.com:birthday15 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:24:19 AM | Telegram id: @PremiumHostTG -",
"nahuelgenessi@gmail.com:argentina22 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:25:39 AM | Telegram id: @PremiumHostTG - ",
"escaflownely@gmail.com:Sm1701n79e | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:28:34 AM | Telegram id: @PremiumHostTG - ",
"Kehoeusmc@gmail.com:MMass3ff3ct | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:29:08 AM | Telegram id: @PremiumHostTG - ",
"poisonfrat@gmail.com:Bobismy13 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:30:11 AM | Telegram id: @PremiumHostTG - ",
"hickstyler7@gmail.com:020801Ty | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:30:46 AM | Telegram id: @PremiumHostTG -",
"rossymcfall@gmail.com:M00nclan | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:30:55 AM | Telegram id: @PremiumHostTG - ",
"iv.riveros@gmail.com:runaway69 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:31:21 AM | Telegram id: @PremiumHostTG - ",
"scrappysea@gmail.com:haloreach2 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:32:04 AM | Telegram id: @PremiumHostTG - ",
"mbealfahim@gmail.com:pokerface101 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:32:13 AM | Telegram id: @PremiumHostTG - ",
"valentinomascitti@gmail.com:farwestar12 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:32:23 AM | Telegram id: @PremiumHostTG -",
"matheussmpinheiro@gmail.com:dohv4eq4 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:35:30 AM | Telegram id: @PremiumHostTG - ",
"thach.steven@gmail.com:leilong788 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:37:11 AM | Telegram id: @PremiumHostTG - ",
"marcuslynch32@gmail.com:person97 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:43:34 AM | Telegram id: @PremiumHostTG - ",
"heathystockton23@gmail.com:Hmms2010 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:47:44 AM | Telegram id: @PremiumHostTG -",
"sauro1094@gmail.com:Ericaholly10 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:48:58 AM | Telegram id: @PremiumHostTG - ",
"mmarcus41@yahoo.com:Damien10 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:50:28 AM | Telegram id: @PremiumHostTG - ",
"lasterblade@gmail.com:master/157 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:52:17 AM | Telegram id: @PremiumHostTG - ",
"zach.grant96@live.com:tua9kana6 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:52:53 AM | Telegram id: @PremiumHostTG - ",
"tommyoc0328@gmail.com:Sham0328 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:53:00 AM | Telegram id: @PremiumHostTG -",
"donovanmarine@gmail.com:ScionxB24 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:54:01 AM | Telegram id: @PremiumHostTG -",
"rthorne80@gmail.com:trebor1880 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:54:13 AM | Telegram id: @PremiumHostTG - ",
"spidersqshr7@gmail.com:adam2002 | Type = premium | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:54:44 AM | Telegram id: @PremiumHostTG - ",
"laritzad@gmail.com:lara2323 | Type = fan | Category = anime|drama|manga | ExpireDate = 5/9/2021 2:56:37 AM | Telegram id: @PremiumHostTG - "]

@client.command()
async def crunchy(ctx,member:discord.Member):
    acc_num = random.randint(0, 108)
    try:
        await member.send(crunchy_accs[acc_num])
        await ctx.send(member.mention+" acc sent in ur dms")
    except:
        await ctx.send(member.mention+" has closed their dms")

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the ;tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@client.command()
async def cancel(ctx):
    global gameOver
    gameOver=True
    await ctx.send("Game has been cancelled")
        
        
        
        
        
client.run("ODUxMDc0OTQyMjk2MjYwNjE5.YLy_Tg.yILCYs0ogWKCEQZdB45RgleeO2c")
