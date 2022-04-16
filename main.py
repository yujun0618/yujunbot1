import discord
import asyncio
import os
import sys
import time
from discord.integrations import Integration
import schedule
import datetime
from datetime import timedelta
import sqlite3
import string
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord_components import DiscordComponents, ComponentsBot, Button, ActionRow, ButtonStyle

client = discord.Client()



def license_gen():
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(12))

def three_send_banner():
    entries = os.listdir('./db')
    for entry in entries:
        con = sqlite3.connect(f"./db/{entry}")
        cur = con.cursor()
        cur.execute("SELECT * FROM info;")
        info = cur.fetchone()
        con.close()
        if info[0] == 30:
            con = sqlite3.connect(f"./db/{entry}")
            cur = con.cursor()
            cur.execute("SELECT * FROM webhook;")
            hookurl = cur.fetchall()
            for h in hookurl:
                if info[1] == 1:
                    try:
                        webhook = DiscordWebhook(username=info[6],url=h[0],content=info[5]+info[4],avatar_url=info[7],thumbnail_url= "https://imgur.com/cQoxNcx.png", rate_limit_retry=True)
                        embed = DiscordEmbed(title=info[9], description=info[2], color=info[8])
                        webhook.add_embed(embed)
                        webhook.execute()
                    except:
                        print("배너전송에러")
                        con = sqlite3.connect(f"./db/{entry}")
                        cur = con.cursor()
                        cur.execute("DELETE FROM webhook WHERE url == ?;", [h[0]])
                        con.commit()
                        con.close()
                else:
                    try:
                        webhook = DiscordWebhook(username=info[6],url=h[0],avatar_url=info[7],thumbnail_url= "https://imgur.com/cQoxNcx.png", content=info[5]+f"{info[4]} \n"+info[2],rate_limit_retry=True)
                        webhook.execute()
                    except:
                        print("배너전송에러")
                        con = sqlite3.connect(f"./db/{entry}")
                        cur = con.cursor()
                        cur.execute("DELETE FROM webhook WHERE url == ?;", [h[0]])
                        con.commit()
                        con.close()

def one_send_banner():
    entries = os.listdir('./db')
    for entry in entries:
        con = sqlite3.connect(f"./db/{entry}")
        cur = con.cursor()
        cur.execute("SELECT * FROM info;")
        info = cur.fetchone()
        con.close()
        if info[0] == 60:
            con = sqlite3.connect(f"./db/{entry}")
            cur = con.cursor()
            cur.execute("SELECT * FROM webhook;")
            hookurl = cur.fetchall()
            for h in hookurl:
                if info[1] == 1:
                    try:
                        webhook = DiscordWebhook(username=info[6],thumbnail_url= "https://imgur.com/cQoxNcx.png", content=info[5]+info[4],url=h[0],avatar_url=info[7],rate_limit_retry=True)
                        embed = DiscordEmbed(title=info[9], description=info[2], color=info[8])
                        webhook.add_embed(embed)
                        webhook.execute()
                    except:
                        print("배너전송에러")
                        con = sqlite3.connect(f"./db/{entry}")
                        cur = con.cursor()
                        cur.execute("DELETE FROM webhook WHERE url == ?;", [h[0]])
                        con.commit()
                        con.close()
                else:
                    try:
                        webhook = DiscordWebhook(username=info[6],url=h[0], avatar_url=info[7],thumbnail_url= "https://imgur.com/cQoxNcx.png", content=info[5]+f"{info[4]} \n"+info[2],rate_limit_retry=True)
                        webhook.execute()
                    except:
                        print("배너전송에러")
                        con = sqlite3.connect(f"./db/{entry}")
                        cur = con.cursor()
                        cur.execute("DELETE FROM webhook WHERE url == ?;", [h[0]])
                        con.commit()
                        con.close()



def test_send_banner():
    entries = os.listdir('./db')
    for entry in entries:
        con = sqlite3.connect(f"./db/{entry}")
        cur = con.cursor()
        cur.execute("SELECT * FROM info;")
        info = cur.fetchone()
        con.close()
        if info[0] == 1:
            con = sqlite3.connect(f"./db/{entry}")
            cur = con.cursor()
            cur.execute("SELECT * FROM webhook;")
            hookurl = cur.fetchall()
            for h in hookurl:
                if info[1] == 1:
                    try:
                        webhook = DiscordWebhook(username=info[6],avatar_url=info[7],thumbnail_url= "https://imgur.com/cQoxNcx.png", content=info[5]+info[4],url=h[0],rate_limit_retry=True)
                        embed = DiscordEmbed(title=info[9], description=info[2], color=info[8])
                        webhook.add_embed(embed)
                        webhook.execute()
                    except:
                        print("배너전송에러")
                        con = sqlite3.connect(f"./db/{entry}")
                        cur = con.cursor()
                        cur.execute("DELETE FROM webhook WHERE url == ?;", [h[0]])
                        con.commit()
                        con.close()
                else:
                    try:
                        webhook = DiscordWebhook(username=info[6],url=h[0], avatar_url=info[7],thumbnail_url= "https://imgur.com/cQoxNcx.png", content=info[5]+f"{info[4]} \n"+info[2],rate_limit_retry=True)
                        webhook.execute()
                    except:
                        print("배너전송에러")
                        con = sqlite3.connect(f"./db/{entry}")
                        cur = con.cursor()
                        cur.execute("DELETE FROM webhook WHERE url == ?;", [h[0]])
                        con.commit()
                        con.close()



def is_expired(time):
    ServerTime = datetime.datetime.now()
    ExpireTime = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
    if ((ExpireTime - ServerTime).total_seconds() > 0):
        return False
    else:
        return True

def get_expiretime(time):
    ServerTime = datetime.datetime.now()
    ExpireTime = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
    if ((ExpireTime - ServerTime).total_seconds() > 0):
        how_long = (ExpireTime - ServerTime)
        days = how_long.days
        hours = how_long.seconds // 3600
        minutes = how_long.seconds // 60 - hours * 60
        return str(round(days)) + "일 " + str(round(hours)) + "시간 " + str(round(hours)) + "분"
    else:
        return False

def make_expiretime(days):
    ServerTime = datetime.datetime.now()
    ExpireTime = ServerTime + timedelta(days=days)
    ExpireTime_STR = (ServerTime + timedelta(days=days)).strftime('%Y-%m-%d %H:%M')
    return ExpireTime_STR

def search_license(code):
    con = sqlite3.connect("license.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM code WHERE license == ?", (code,))
    result = cur.fetchone()
    con.close()
    return result

def add_time(now_days, add_days):
    ExpireTime = datetime.datetime.strptime(now_days, '%Y-%m-%d %H:%M')
    ExpireTime_STR = (ExpireTime + timedelta(days=add_days)).strftime('%Y-%m-%d %H:%M')
    return ExpireTime_STR

def nowstr():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

schedule.every(1).minutes.do(test_send_banner)
schedule.every(30).minutes.do(three_send_banner)
schedule.every(60).minutes.do(one_send_banner)

@client.event
async def on_ready():
    DiscordComponents(client)
    print("ready")
    while True:
        await client.change_presence(activity=discord.Game(f"{len(client.guilds)}개 서버에서 작동중 ㅣ !도움말, !배너"),status=discord.Status.online)
        schedule.run_pending()
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.content.startswith("!배너"):
        if os.path.exists(f"./db/{message.guild.id}.db"):
            if not message.author.guild_permissions.administrator:
                embed = discord.Embed(color=0xff0000)
                embed.title = "관리자만 사용 가능합니다."
                embed.description = "관리자 권한을 가지고 명령어를 입력해주세요"
                await message.channel.send(embed=embed)
                await message.delete()
            else:
                # await message.delete()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER"
                embed.description = "원하시는 버튼을 클릭하세요"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await message.channel.send(
                    embed=embed,
                    components = [
                        # ActionRow(
                        #     Button(style=ButtonStyle.green,label = "웹훅설정",custom_id="webhook_seting"),
                        #     Button(style=ButtonStyle.blue,label = "각종 설정",custom_id="BOT_SASF"),
                        #     Button(style=ButtonStyle.green,label = "BANNER_Contents",custom_id="bot_invite"),
                        # ),
                        # ActionRow(
                        #     Button(style=ButtonStyle.green,label = "웹훅추가",custom_id="add_webhook"),
                        #     Button(style=ButtonStyle.green,label = "웹훅제거",custom_id="remove_webhook"),
                        # ),
                        # ActionRow(
                        #     Button(style=ButtonStyle.green,label = "미리보기",custom_id="preview"),
                        #     Button(style=ButtonStyle.green,label = "웹훅출력",custom_id="print_webhook"),
                        #     Button(style=ButtonStyle.red,label = "웹훅 주소 초기화",custom_id="resetes"),
                        # ),
                        # ActionRow(
                        #     Button(style=ButtonStyle.green,label = "멘트설정",custom_id="set_msg"),
                        #     Button(style=ButtonStyle.green,label = "초대코드",custom_id="set_link"),
                        # ),
                        # ActionRow(
                        #     Button(style=ButtonStyle.green,label = "30분",custom_id="30m"),
                        #     Button(style=ButtonStyle.blue,label = "1시간",custom_id="60m"),
                        #     Button(style=ButtonStyle.green,label = "임베드 O",custom_id="embed_o"),
                        #     Button(style=ButtonStyle.blue,label = "임베드 X",custom_id="embed_x"),
                        # ),
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "메뉴",custom_id="menu"),
                            Button(style=ButtonStyle.blue,label = "라이센스",custom_id="license"),
                            Button(style=ButtonStyle.red,label = "BANNER_Contents",custom_id="bot_invite"),
                        )
                    ]
                )
        else:
            embed = discord.Embed(color=0xff0000)
            embed.title = "라이센스가 등록되지 않은 서버입니다"
            embed.description = "라이센스를 등록해주세요"
            await message.channel.send(embed=embed)
            await message.delete()
            return

    if message.content.startswith("!등록"):
        if os.path.exists(f"./db/{message.guild.id}.db"):
            embed = discord.Embed(color=0xff0000)
            embed.title = "이미 등록된 서버입니다"
            embed.description = "연장을 원하시면 !배너 를 입력하세요"
            await message.channel.send(embed=embed)
            return
        if not message.author.guild_permissions.administrator:
            embed = discord.Embed(color=0xff0000)
            embed.title = "관리자만 사용 가능합니다."
            embed.description = "관리자 권한을 가지고 명령어를 입력해주세요"
            await message.channel.send(embed=embed)
            return
        else:
            try:
                code = message.content.split(" ")[1]
                result = search_license(code)
                if not result == None:
                    con = sqlite3.connect("license.db")
                    cur = con.cursor()
                    cur.execute("DELETE FROM code WHERE license == ?",(code,))
                    con.commit()
                    con.close()
                    con = sqlite3.connect(f"./db/{message.guild.id}.db")
                    extime = make_expiretime(result[1])
                    print(extime)
                    with con:
                        cur = con.cursor()
                        cur.execute("""CREATE TABLE "info" ("time" INTEGER,"isembed" INTEGER,"msg" TEXT, "expire" TEXT, "link" TEXT, "everyone" TEXT, "name" TEXT, "pro_url" TEXT, "color" TEXT, "tite" TEXT)""")
                        con.commit()
                        cur.execute("""CREATE TABLE "webhook" ("url" TEXT)""")
                        con.commit()
                        cur.execute("INSERT INTO info VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (60,1,"메세지가 설정되지 않았습니다",extime,"지훈 BANNER","@everyone","지훈 banner","https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif","00ff00","지훈 banner"))
                        con.commit()
                    con.close()
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "라이센스 등록에 성공하셨습니다"
                    embed.description = f"만료일 : {extime}"
                    await message.channel.send(embed=embed)
                    embed = discord.Embed(title='라이센스 등록에 성공하셨습니다',color=0x00ff00)
                    embed.description = f"만료일 : {extime}"
                    embed.add_field(name='!배너', value='버튼 메뉴를 불러옵니다', inline=False)
                    embed.set_footer(text='https://discord.gg/pPKE7SMFwS')
                    await message.author.send(embed=embed)
                else:
                    embed = discord.Embed(color=0xff0000)
                    embed.title = "없거나 사용된 코드입니다"
                    embed.description = "코드를 구매하세요!"
                    await message.channel.send(embed=embed)
            except Exception as e:
                print(e)
                embed = discord.Embed(color=0xff0000)
                embed.title = "라이센스 등록에 실패하였습니다"
                embed.description = "올바른 코드를 입력하세요"
                await message.channel.send(embed=embed)


    if message.content.startswith("!라센생성"):
        if message.author.id == 942023864903401502 :
        # if message.author.id == 901452337661476884 or message.author.id == 847664131502768149:
            day = message.content.split(" ")[2]
            am = message.content.split(" ")[1]
            con = sqlite3.connect("license.db")
            cur = con.cursor()
            f = open("slicense.txt", 'w')
            for i in range(int(am)):
                sscode = "jihun-" + license_gen()
                cur.execute("INSERT INTO code VALUES(?, ?);",(sscode,int(day)))
                con.commit()
                f.write(f"코드 : {sscode} 기간 : {day}"+"\n")
            f.close()
            con.close()
            file = discord.File("slicense.txt")
            await message.author.send("출력되었습니다",file=file)
            os.remove("slicense.txt")
    
    if message.content.startswith("!라센목록"):
        if message.author.id == 901452337661476884:
        # if message.author.id == 889500804036309003 or message.author.id == 847664131502768149:
            await message.channel.send(content="DM을 확인해주세요")
            con = sqlite3.connect("license.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM code;")
            wurl = cur.fetchall()
            con.close()
            f = open("license.txt", 'w')
            for i in wurl:
                if i[0] == "":
                    print("비어")
                    continue
                else:
                    f.write(f"코드 : {i[0]} 기간 : {i[1]}"+"\n")
            f.close()
            file = discord.File("license.txt")
            await message.author.send("출력되었습니다",file=file)
            os.remove("license.txt")
    
    if message.content.startswith("!라센삭제"):
        if message.author.id == 901452337661476884:
        # if message.author.id == 889500804036309003 or message.author.id == 847664131502768149:
            try:
                lcd = message.content.split(" ")[1]
                con = sqlite3.connect("license.db")
                cur = con.cursor()
                cur.execute("DELETE FROM code WHERE license == ?;", [lcd])
                con.commit()
                con.close()
                await message.channel.send('제거되었습니다')
            except:
                await message.channel.send("에에러어 없는 코드거나 잘못친고임")
    
    if message.content.startswith("!라센검색"):
        if message.author.id == 901452337661476884:
        # if message.author.id == 889500804036309003 or message.author.id == 847664131502768149:
            try:
                lcd = message.content.split(" ")[1]
                cinfo = search_license(lcd)
                await message.channel.send(f"코드 : {cinfo[0]}\n기간 : {cinfo[1]}일")
            except:
                await message.channel.send("에에러어 없는 코드거나 잘못친고임")

    if message.content.startswith("$관리자"):
        if message.author.id == 901452337661476884:
                await message.delete()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER 관리자"
                embed.description = "원하시는 버튼을 클릭하세요"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await message.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.red,label = "재시작 하기",custom_id="rebot"),
                            Button(style=ButtonStyle.green,label = "BANNER_Contents",custom_id="bot_invite"),
                        ),
                    ]
                )
    if message.content == '!도움말':
        if not message.author.guild_permissions.administrator:
            embed = discord.Embed(title='명령어창을 불러오지 못했습니다.', description='24시간동안 자동으로 웹훅을 보내주는 봇.',color=0xff0000)
            embed.set_footer(text='지훈#3333')
        else:
            embed = discord.Embed(title='도움말',color=0x00ff00)
            embed.add_field(name='!등록 [라이센스]\nㄴ연장은 메뉴를 불러와주세요.', value='\u200b', inline=False)
            embed.add_field(name='!배너', value='버튼 메뉴를 불러옵니다', inline=False)
            embed.set_footer(text='지훈#3333')
        await message.channel.send(f'{message.author.mention} 디엠을 확인해주세요')
        await message.author.send(embed=embed)

@client.event
async def on_button_click(interaction):
    if interaction.responded:
        return
    if interaction.user.guild_permissions.administrator:
        if os.path.exists(f"./db/{interaction.guild.id}.db"):
            if interaction.custom_id == "add_webhook":
                await interaction.respond(embed=discord.Embed(title="30초안에 추가할 웹훅을 입력해주세요",description="올바른 URL을 입력하지 않을 시 배너가 전송되지 않을 수 있습니다",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="add_webhook"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    hooks = msg.content.split("""
""")
                    con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                    cur = con.cursor()
                    for i in hooks:
                        cur.execute("INSERT INTO webhook VALUES(?);", [i])
                        con.commit()
                    con.close()
                    await msg.delete()
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**등록 완료**"
                    embed.description = "등록 완료 되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )

            if interaction.custom_id == "remove_webhook":
                await interaction.respond(embed=discord.Embed(title="30초안에 제거할 웹훅을 입력해주세요",description="올바른 URL을 입력하지 않을 시 제거되지 않을 수 있습니다",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="remove_webhook"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    try:
                        await msg.delete()
                        con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                        cur = con.cursor()
                        cur.execute("DELETE FROM webhook WHERE url == ?;", [msg.content])
                        con.commit()
                        con.close()
                        await interaction.channel.send('제거되었습니다')
                    except:
                        await interaction.channel.send('웹훅이 존재하지 않습니다')

            if interaction.custom_id == "print_webhook":
                await interaction.message.delete()
                await interaction.respond(content="DM을 확인해주세요")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM webhook;")
                wurl = cur.fetchall()
                con.close()
                f = open(f"{interaction.guild.id}.txt", 'w')
                for i in wurl:
                    if i[0] == "":
                        print("비어")
                        continue
                    else:
                        f.write(i[0]+"\n")
                f.close()
                file = discord.File(f"{interaction.guild.id}.txt")
                await interaction.user.send("출력되었습니다",file=file)
                os.remove(f"{interaction.guild.id}.txt")
            
            if interaction.custom_id == "set_send":
                await interaction.respond(content="전송메뉴를 열었습니다")
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER"
                embed.description = "원하시는 버튼을 클릭하세요"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.blue,label = "30분",custom_id="30m"),
                            Button(style=ButtonStyle.red,label = "1시간",custom_id="60m"),
                            Button(style=ButtonStyle.blue,label = "임베드 O",custom_id="embed_o"),
                            Button(style=ButtonStyle.red,label = "임베드 X",custom_id="embed_x"),
                        ),
                        ActionRow(
                            Button(style=ButtonStyle.blue,label = "제목",custom_id="tite"),
                            Button(style=ButtonStyle.green,label = "취소",custom_id="cancel"),
                        )
                    ]
                )
            if interaction.custom_id == "cancel":
                await interaction.message.delete()

            if interaction.custom_id == "30m":
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("UPDATE info SET time = ? WHERE rowid = 1;", [30])
                con.commit()
                con.close()
                await interaction.respond(content='변경되었습니다')
                # await interaction.message.delete()
            
            if interaction.custom_id == "60m":
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("UPDATE info SET time = ? WHERE rowid = 1;", [60])
                con.commit()
                con.close()
                await interaction.respond(content='변경되었습니다')
                # await interaction.message.delete()
            
            if interaction.custom_id == "embed_o":
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("UPDATE info SET isembed = ? WHERE rowid = 1;", [1])
                con.commit()
                con.close()
                await interaction.respond(content='변경되었습니다')
                # await interaction.message.delete()
            
            if interaction.custom_id == "embed_x":
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("UPDATE info SET isembed = ? WHERE rowid = 1;", [0])
                con.commit()
                con.close()
                await interaction.respond(content='변경되었습니다')
                # await interaction.message.delete()
            
            if interaction.custom_id == "everyone_o":
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("UPDATE info SET everyone = ? WHERE rowid = 1;", ["@everyone"])
                con.commit()
                con.close()
                await interaction.respond(content='변경되었습니다')
                # await interaction.message.delete()
            
            if interaction.custom_id == "everyone_x":
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("UPDATE info SET everyone = ? WHERE rowid = 1;", [""])
                con.commit()
                con.close()
                await interaction.respond(content='변경되었습니다')
                # await interaction.message.delete()

            if interaction.custom_id == "propl":
                await interaction.respond(embed=discord.Embed(title="30초안에 프로필 이름를 입력해주세요",description="적용을 안할시 지훈ㄴ banner로 전송이 될것입니다",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="propl"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    await msg.delete()
                    con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                    cur = con.cursor()
                    cur.execute("UPDATE info SET name = ? WHERE rowid = 1;", [msg.content])
                    con.commit()
                    con.close()
                    await interaction.channel.send('수정이 되었습니다')


            if interaction.custom_id == "propl_url":
                await interaction.respond(embed=discord.Embed(title="30초안에 프로필 주소를 입력해주세요",description="올바른 프로필 주소를 입력하지 않을 시 프로필이 적용되지 않고 전송되지 않을 수 있습니다",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="propl_url"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    await msg.delete()
                    con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                    cur = con.cursor()
                    cur.execute("UPDATE info SET pro_url = ? WHERE rowid = 1;", [msg.content])
                    con.commit()
                    con.close()
                    await interaction.channel.send('수정이 되었습니다')

            if interaction.custom_id == "tite":
                await interaction.respond(embed=discord.Embed(title="30초안에 제목를 입력해주세요",description="올바른 제목를 입력하지 않을 시 지훈 banner라는 제목으로 전송이 될것입니다",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="propl_url"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    await msg.delete()
                    con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                    cur = con.cursor()
                    cur.execute("UPDATE info SET tite = ? WHERE rowid = 1;", [msg.content])
                    con.commit()
                    con.close()
                    await interaction.channel.send('수정이 되었습니다')
                    




            if interaction.custom_id == "color_set":
                await interaction.respond(embed=discord.Embed(title="30초안에 색상 코드를 입력해주세요",description="https://www.rapidtables.org/ko/web/color/RGB_Color \n **# 은 제외 하고 작성해주세요** \n 올바른 색상 코드를 입력하지 않을 시 색상이 적용되지 않고 전송되지 않을 수 있습니다",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="color_set"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    await msg.delete()
                    con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                    cur = con.cursor()
                    cur.execute("UPDATE info SET color = ? WHERE rowid = 1;", [msg.content])
                    con.commit()
                    con.close()
                    await interaction.channel.send('수정이 되었습니다')

            if interaction.custom_id == "set_msg":
                await interaction.respond(embed=discord.Embed(title="30초안에 배너 멘트을 입력해주세요",description="올바른 멘트을 입력하지 않을 시 배너가 전송되지 않을 수 있습니다",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="set_msg"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    await msg.delete()
                    con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                    cur = con.cursor()
                    cur.execute("UPDATE info SET msg = ? WHERE rowid = 1;", [msg.content])
                    con.commit()
                    con.close()
                    await interaction.channel.send('등록되었습니다')
            
            if interaction.custom_id == "license":
                await interaction.respond(content="라이센스 메뉴를 열었습니다")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                namt = get_expiretime(result[3])
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER"
                embed.description = f"만료일 : {result[3]}\n남은기간 : {namt}"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "연장하기",custom_id="extend"),
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )
            
            if interaction.custom_id == "extend":
                await interaction.respond(embed=discord.Embed(title="30초안에 라이센스 코드를 입력해주세요",description="올바른 코드를 입력하세요",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="extend"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    await msg.delete()
                    result = search_license(msg.content)
                    if not result == None:
                        con = sqlite3.connect("license.db")
                        cur = con.cursor()
                        cur.execute("DELETE FROM code WHERE license == ?",(msg.content,))
                        con.commit()
                        con.close()
                        con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                        cur = con.cursor()
                        cur.execute("SELECT * FROM info;")
                        nowd = cur.fetchone()
                        con.close()
                        namt = add_time(nowd[3],result[1])
                        con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                        cur = con.cursor()
                        cur.execute("UPDATE info SET expire = ? WHERE rowid = 1;", [namt])
                        con.commit()
                        con.close()
                        embed = discord.Embed(color=0x00ff00)
                        embed.title = "**등록 완료**"
                        embed.description = "등록 완료 되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                        embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                        await interaction.channel.send(
                        embed=embed,
                        components = [
                            ActionRow(
                                Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                             )
                            ]
                        )
                    else:
                        embed = discord.Embed(color=0xff0000)
                        embed.title = "없거나 사용된 코드입니다"
                        embed.description = "코드를 구매하세요!"
                        await interaction.channel.send(embed=embed)
            
            if interaction.custom_id == "set_webhook":
                await interaction.respond(content="웹훅설정 메뉴를 열었습니다")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER" 
                embed.description = f"EMBED 설정 : {result[1]}\n전송 주기 : {result[0]}"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "미리보기",custom_id="preview"),
                            Button(style=ButtonStyle.green,label = "초기화",custom_id="reset"),
                            Button(style=ButtonStyle.green,label = "웹훅출력",custom_id="print_webhook"),
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )
            if interaction.custom_id == "BOT_SASF":
                await interaction.respond(content="봇 관련 패널을 열었습니다")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER"
                embed.description = f"지훈 BANNER 각종 설정 \n 전송설정ㅣ멘트설정ㅣ초대코드"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.blue,label = "전송설정",custom_id="set_send"),
                            Button(style=ButtonStyle.blue,label = "멘트설정",custom_id="set_msg"),
                            Button(style=ButtonStyle.green,label = "초대코드",custom_id="set_link"),
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )

            if interaction.custom_id == "webhook_seting":
                await interaction.respond(content="봇 관련 패널을 열었습니다")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER"
                embed.description = f"지훈 BANNER 각종 설정 \n 웹훅추가ㅣ웹훅제거ㅣ웹훅설정"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "웹훅추가",custom_id="add_webhook"),
                            Button(style=ButtonStyle.green,label = "웹훅제거",custom_id="remove_webhook"),
                            Button(style=ButtonStyle.green,label = "웹훅설정",custom_id="set_webhook"),
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )

            if interaction.custom_id == "bot_invite":
                await interaction.respond(content="봇 관련 패널을 열었습니다")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER"
                embed.description = f"지훈 BANNER 봇 관련 \n 패널 초대/구매/이벤트"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.URL,label = "배너봇_초대",url='https://discord.com/api/oauth2/authorize?client_id=904291964592209991&permissions=10240&scope=bot'),
                            Button(style=ButtonStyle.green,label = "구매문의",custom_id="buy_tick"),
                            # Button(style=ButtonStyle.green,label = "구매처",custom_id="city"),
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )

            if interaction.custom_id == "menu":
                await interaction.respond(content="메뉴 패널을 열었습니다")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER 메뉴"
                embed.description = f"지훈 BANNER 메뉴"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "웹훅추가",custom_id="add_webhook"),
                            Button(style=ButtonStyle.green,label = "웹훅제거",custom_id="remove_webhook"),
                        ),
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "미리보기",custom_id="preview"),
                            Button(style=ButtonStyle.green,label = "웹훅출력",custom_id="print_webhook"),
                            Button(style=ButtonStyle.red,label = "웹훅 주소 초기화",custom_id="resetes"),
                        ),
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "멘트설정",custom_id="set_msg"),
                            Button(style=ButtonStyle.green,label = "초대코드",custom_id="set_link"),
                        ),
                        # ActionRow(
                        #     Button(style=ButtonStyle.green,label = "30분",custom_id="30m"),
                        #     Button(style=ButtonStyle.green,label = "1시간",custom_id="60m"),
                        #     Button(style=ButtonStyle.green,label = "임베드 O",custom_id="embed_o"),
                        #     Button(style=ButtonStyle.red,label = "임베드 X",custom_id="embed_x"),
                        # ),
                        # ActionRow(
                        #     Button(style=ButtonStyle.green,label = "에브리원",custom_id="everyone_o"),
                        #     Button(style=ButtonStyle.red,label = "에브리원",custom_id="everyone_x"),
                        # ),
                        ActionRow(
                            Button(style=ButtonStyle.red,label = "프로필 설정",custom_id="send_pro_menu"),
                            Button(style=ButtonStyle.red,label = "전송 설정",custom_id="send_menu"),
                        ),
                        ActionRow(
                            Button(style=ButtonStyle.red,label = "백업",custom_id="backup"),
                            Button(style=ButtonStyle.blue,label = "라이센스",custom_id="license"),
                            Button(style=ButtonStyle.red,label = "BANNER_Contents",custom_id="bot_invite"),
                        )
                    ]
                )
            if interaction.custom_id == "send_menu":
                await interaction.respond(content="메뉴 패널을 열었습니다")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER 전송 메뉴"
                embed.description = f"지훈 BANNER 전송 메뉴"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "30분",custom_id="30m"),
                            Button(style=ButtonStyle.green,label = "1시간",custom_id="60m"),
                            Button(style=ButtonStyle.green,label = "임베드 O",custom_id="embed_o"),
                            Button(style=ButtonStyle.red,label = "임베드 X",custom_id="embed_x"),
                        ),
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "에브리원",custom_id="everyone_o"),
                            Button(style=ButtonStyle.red,label = "에브리원",custom_id="everyone_x"),
                        ),
                        ActionRow(
                            Button(style=ButtonStyle.blue,label = "제목",custom_id="tite"),
                            Button(style=ButtonStyle.green,label = "임베드 색상",custom_id="color_set"),
                        ),
                    ]
                )

            if interaction.custom_id == "send_pro_menu":
                await interaction.respond(content="메뉴 패널을 열었습니다")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                embed = discord.Embed(color=0x00ff00)
                embed.title = "지훈 BANNER 프로필 메뉴"
                embed.description = f"지훈 BANNER 프로필 메뉴"
                embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "프로필 이름",custom_id="propl"),
                            Button(style=ButtonStyle.green,label = "프로필 사진 (주소)",custom_id="propl_url"),
                        )
                    ]
                )



            if interaction.custom_id == "invite":
                await interaction.message.delete()
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                if result[1] == 1:
                    embed = discord.Embed(title='지훈 BANNER', description="[[초대하기]]()", color=0x00ff00)
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )

            if interaction.custom_id == "city":
                await interaction.message.delete()
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                if result[1] == 1:
                    embed = discord.Embed(title='지훈 BANNER', description="[**[구매처]**](https://discord.gg/pPKE7SMFwS)", color=0x00ff00)
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )

            if interaction.custom_id == "buy_tick":
                # await interaction.message.delete()
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                if result[1] == 1:
                    embed = discord.Embed(title='지훈 BANNER', description="연장 문의: 지훈#3333", color=0x00ff00)
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.URL,label = "판매점 접속",url='https://discord.gg/pPKE7SMFwS'),
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )
            
            if interaction.custom_id == "preview":
                # await interaction.message.delete()
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                if result[1] == 1:
                    await interaction.respond(embed=discord.Embed(title="미리보기",thumbnail_url= "https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif",description=result[2],color=0x00ff00))
                    # embed = discord.Embed(title='Lisa BANNER', description=result[2], color=0x00ff00)
                    # await interaction.channel.send(content="@everyone")
                    # await interaction.channel.send(embed=embed)
                else:
                    await interaction.channel.send(content="@everyone\n" + result[2])

            if interaction.custom_id == "backup":
                await interaction.respond(content="DM을 확인해주세요")
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM webhook;")
                wurl = cur.fetchall()
                con.close()
                file = discord.File(f"./db/{interaction.guild.id}.db")
                await interaction.user.send("출력되었습니다",file=file)

            if interaction.custom_id == "resetes":
                # await interaction.message.delete()
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM info;")
                result = cur.fetchone()
                con.close()
                if result[1] == 1:
                    embed = discord.Embed(title='지훈 BANNER', description="정말로 **초기화**를 하시겠습니까? \n 계속 진행을 원하시면 아래에있는 계속 하기를 눌러주세요.", color=0x00ff00)
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.red,label = "계속하기",custom_id="reset"),
                            Button(style=ButtonStyle.red,label = "취소",custom_id="cancel"),
                        )
                    ]
                )
            if interaction.custom_id == "reset":
                await interaction.message.delete()
                con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                cur = con.cursor()
                cur.execute("DROP TABLE webhook;")
                con.commit()
                cur.execute("""CREATE TABLE "webhook" ("url" TEXT)""")
                con.commit()
                con.close()
                
            if interaction.custom_id == "set_link":
                
                await interaction.respond(embed=discord.Embed(title="30초안에 링크를 입력해주세요",description="올바른 URL을 입력하지 않을 시 등록되지 않을 수 있습니다",color=0x00ff00))
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                try:
                    msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    embed = discord.Embed(color=0x00ff00)
                    embed.title = "**시간 초과**"
                    embed.description = "30초 이내로 입력이 되지않아 취소되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                    embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                    await interaction.channel.send(
                    embed=embed,
                    components = [
                        ActionRow(
                            Button(style=ButtonStyle.green,label = "다시 시도하기",custom_id="set_link"),
                            Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                         )
                        ]
                    )
                else:
                    try:
                        await msg.delete()
                        con = sqlite3.connect(f"./db/{interaction.guild.id}.db")
                        cur = con.cursor()
                        cur.execute("UPDATE info SET link = ? WHERE rowid = 1", [msg.content])
                        con.commit()
                        con.close()
                        embed = discord.Embed(color=0x00ff00)
                        embed.title = "**등록 완료**"
                        embed.description = "등록 완료 되었습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                        embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                        await interaction.channel.send(
                        embed=embed,
                        components = [
                            ActionRow(
                                Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                             )
                            ]
                        )
                    except:
                        embed = discord.Embed(color=0x00ff00)
                        embed.title = "**오류**"
                        embed.description = "DB 존재하지 않습니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
                        embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
                        await interaction.channel.send(
                        embed=embed,
                        components = [
                            ActionRow(
                                Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                             )
                            ]
                        )


        else:
            embed = discord.Embed(color=0x00ff00)
            embed.title = "**오류**"
            embed.description = "등록되지 않은 서버입니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
            embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
            await interaction.channel.send(
            embed=embed,
            components = [
                ActionRow(
                    Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
                 )
                ]
            )
    else:
        embed = discord.Embed(color=0x00ff00)
        embed.title = "**권한 부족**"
        embed.description = "관리자만 사용가능합니다. \n **닫기를 누르시면 메세지가 닫힙니다**"
        embed.set_footer(text="지훈 BANNER", icon_url="https://cdn.discordapp.com/attachments/964589302178787328/964804473144885278/EB2CD432-CF6D-45FD-A682-1B1D058F450E.gif")
        await interaction.channel.send(
        embed=embed,
        components = [
            ActionRow(
                Button(style=ButtonStyle.red,label = "닫기",custom_id="cancel"),
             )
            ]
        )
        

        # async def on_message(message):
        # if message.content.startswith("!리붓"):



access_token = os.environ['BOT_TOKEN']
client.run("access_token")
