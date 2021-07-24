import discord
from discord.ext import commands
import random
import asyncio
intents = discord.Intents.all()
client = commands.Bot(command_prefix=";",intents=intents)



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

#@client.command()
#@commands.has_permissions(ban_members=True)
#async def spam(ctx,member:discord.Member,usermsg,dmnum):
    #dmnum=int(dmnum)
    #if dmnum==69 or dmnum<69:
        #try:
            #for i in range(0,dmnum):
                #await member.send(usermsg)
            #await ctx.send(member.mention + " check ur dms")
        #except:
            #await ctx.send(member.mention+" has closed their dms")
    #else:
        #await ctx.send("limit is 69 dms")

#@client.command()
#@commands.has_permissions(ban_members=True)
#async def ping(ctx,member:discord.Member,pingnum):
    #pingnum=int(pingnum)
    #if pingnum==69 or pingnum<69:
        #for i in range(0,pingnum):
                #await ctx.send(member.mention)

    #else:
        #await ctx.send("limit is 69 pings")
mmsg=""
pingnum2=""
#@client.command()
#@commands.has_permissions(ban_members=True)
#async def mping(ctx,member:discord.Member,mmsg,pingnum2):
    #pingnum2=int(pingnum2)
    #if pingnum2==69 or pingnum2<69:
        #for i in range(0,pingnum2):
                #await ctx.send(member.mention+mmsg)

    #else:
        #await ctx.send("limit is 69 pings")
msg3=""
msgnum3=""
#@client.command()
#@commands.has_permissions(ban_members=True)
#async def mspam(ctx,msg3,msgnum3):
    #msgnum3=int(msgnum3)
    #if msgnum3==69 or msgnum3<69:
        #for i in range(0,msgnum3):
            #await ctx.send(msg3)
    #else:
        #await ctx.send("limit is 69 messages")

@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=851074942296260619&permissions=8&scope=bot")



@client.command()
@commands.has_permissions(send_messages=True)
async def command(ctx):
    embed=discord.Embed(title="Commands List",color=discord.Color.blue())
    embed.add_field(name=";avatar",value="sends avatar of user")
    #embed.add_field(name=";spam",value="spams dm to a user")
    #embed.add_field(name=";ping", value="mass pings a user")
    #embed.add_field(name=";mping", value="pings a user and spams a msg in the server channel")
    #embed.add_field(name=";arnav", value="gives arnav's description")
    embed.add_field(name=";ban", value="bans a user")
    embed.add_field(name=";kick", value="kicks user from the server")
    embed.add_field(name=";mute", value="mutes a user")
    embed.add_field(name=";unmute", value="unmutes a muted user")
    embed.add_field(name=";invite", value="invite the bot to ur server")
    embed.add_field(name=";clear", value="deletes messages")
    #embed.add_field(name=";mspam", value="spams a message in the server channel")
    embed.add_field(name=";membercount", value="sends number of members in the server")
    embed.add_field(name=";cu", value="can be used in #counting to count numbers")
    embed.add_field(name=";tictactoe", value="starts a game of tictactoe")
    embed.add_field(name=";cancel", value="cancels ongoing tictactoe game")
    #embed.add_field(name=";crunchy", value="generates a crunchyroll acc")
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



#@client.command()
#async def crunchy(ctx,member:discord.Member):
    #acc_num = random.randint(0, 108)
    #try:
        #await member.send(crunchy_accs[acc_num])
        #await ctx.send(member.mention+" acc sent in ur dms")
    #except:
        #await ctx.send(member.mention+" has closed their dms")

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
        
        
def add(n: float, n2: float):
    return n + n2

def sub(n: float, n2: float):
    return n - n2

def rando(n: int, n2: int):
    return random.randint(n, n2)

def div(n: float, n2: float):
    return n / n2

def sqrt(n: float):
    return math.sqrt(n)

def mult(n: float, n2: float):
    return n * n2

@client.command()
async def mathadd(ctx, x: float, y: float):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathrando(ctx, x: int, y: int):
	try:
		result = rando(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathdiv(ctx, x: float, y: float):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathmult(ctx, x: float, y: float):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsqrt(ctx, x: float):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass
#hello
client.run("ODUxMDc0OTQyMjk2MjYwNjE5.YLy_Tg.yILCYs0ogWKCEQZdB45RgleeO2c")
