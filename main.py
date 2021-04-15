from discord.ext import commands
import discord
import json

client = commands.Bot(command_prefix='.')

file = open('data.json', 'r', encoding='utf-8')
token = json.load(file)['token']
file.close()

@client.event
async def on_ready():
    print(f'{client.user} was ready!')

@client.command()
async def stop(ctx):
    if ctx.author.guild_permissions.adminstrator:
        ctx.send('Youtube Fandom Manager를 종료합니다')
        exit(-1)

@client.command()
async def add_role(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        try:
            try:
                try:
                    await user.add_roles(role)
                    await ctx.send(f"님 성공적으로 역할 {role.mention}이(가) {user.mention}에게 추가되었습니다")
                except commands.errors.CommandInvokeError:
                    await ctx.send('이 역할은 추가할 수 없습니다')
            except commands.errors.RoleNotFound:
                await ctx.send('이 역할은 존재하지 않습니다')
        except discord.errors.Forbidden:
            await ctx.send('이 역할은 부여할 수 없습니다')

@client.command()
async def remove_role(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        try:
            try:
                try:
                    await user.remove_roles(role)
                    await ctx.send(f"성공적으로 역할 {role.mention}이(가) {user.mention}에게서 제거되었습니다")
                except ommands.errors.CommandInvokeError:
                    await ctx.send('이 역할은 제거할 수 없습니다')
            except commands.errors.RoleNotFound:
                await ctx.send('이 역할은 존재하지 않습니다')
        except discord.errors.Forbidden:
            await ctx.send('이 역할은 부여할 수 없습니다')

@client.command()
async def add_youtube_watcher(ctx, user: discord.Member):
    global youtuber_names

    check_youtuber = False
    is_vaild_youtuber = False
    youtuber_name = ""
    for role in ctx.guild.roles:
        if role.name == "유튜버":
            check_youtuber = True
            for role in ctx.guild.roles:
                if role.name in youtuber_names:
                    is_vaild_youtuber = True
                    youtuber_name = role.name
                    break
                
            if is_vaild_youtuber:
                break
            else:
                ctx.send(f'당신은 등록된 유튜버가 아닙니다')
                break

    if is_vaild_youtuber:
        target_role = discord.utils.find(lambda r: r.name == youtuber_name + ' 팬', ctx.guild.roles)
        if not target_role in user.roles:
            await user.add_roles(target_role)
            await ctx.send('해당 유저를 당신의 팬으로 등록하였습니다')
        else:
            await ctx.send('해당 유저는 이미 당신의 팬으로 등록되어 있습니다')

@client.command()
async def remove_youtube_watcher(ctx, user: discord.Member):
    global youtuber_names

    check_youtuber = False
    is_vaild_youtuber = False
    youtuber_name = ""
    for role in ctx.guild.roles:
        if role.name == "유튜버":
            check_youtuber = True
            for role in ctx.guild.roles:
                if role.name in youtuber_names:
                    is_vaild_youtuber = True
                    youtuber_name = role.name
                    break
                
            if is_vaild_youtuber:
                break
            else:
                ctx.send(f'당신은 등록된 유튜버가 아닙니다')
                break

    if is_vaild_youtuber:
        target_role = discord.utils.find(lambda r: r.name == youtuber_name + ' 팬', ctx.guild.roles)
        if target_role in user.roles:
            await user.remove_roles(target_role)
            await ctx.send('해당 유저를 당신의 팬에서 박탈하였습니다')
        else:
            await ctx.send('해당 유저는 당신의 팬으로 등록되어 있지 않습니다')
            
@client.command()
async def add_twitch_watcher(ctx, user: discord.Member):
    global youtuber_names

    check_youtuber = False
    is_vaild_youtuber = False
    youtuber_name = ""
    for role in ctx.guild.roles:
        if role.name == "스트리머":
            check_youtuber = True
            for role in ctx.guild.roles:
                if role.name in twitch_streamer_names:
                    is_vaild_youtuber = True
                    youtuber_name = role.name
                    break
                
            if is_vaild_youtuber:
                break
            else:
                ctx.send(f'당신은 등록된 스트리머가 아닙니다')
                break

    if is_vaild_youtuber:
        target_role = discord.utils.find(lambda r: r.name == youtuber_name + ' 팬', ctx.guild.roles)
        if not target_role in user.roles:
            await user.add_roles(target_role)
            await ctx.send('해당 유저를 당신의 팬으로 등록하였습니다')
        else:
            await ctx.send('해당 유저는 이미 당신의 팬으로 등록되어 있습니다')

@client.command()
async def remove_twitch_watcher(ctx, user: discord.Member):

    global youtuber_names

    check_youtuber = False
    is_vaild_youtuber = False
    youtuber_name = ""
    for role in ctx.guild.roles:
        if role.name == "스트리머":
            check_youtuber = True
            for role in ctx.guild.roles:
                if role.name in twitch_streamer_names:
                    is_vaild_youtuber = True
                    youtuber_name = role.name
                    break
                
            if is_vaild_youtuber:
                break
            else:
                ctx.send(f'당신은 등록된 스트리머가 아닙니다')
                break

    if is_vaild_youtuber:
        target_role = discord.utils.find(lambda r: r.name == youtuber_name + ' 팬', ctx.guild.roles)
        if target_role in user.roles:
            await user.remove_roles(target_role)
            await ctx.send('해당 유저를 당신의 팬에서 박탈하였습니다')
        else:
            await ctx.send('해당 유저는 당신의 팬으로 등록되어 있지 않습니다')

youtuber_names = ['메이데이', '망토토']
twitch_streamer_names = ['망토토']
#Invite Link = https://discord.com/oauth2/authorize?client_id=822293801526624306&permissions=8&scope=bot
client.run(token)

print('코드실행함')
while True:
    a = 0
