#導入 Discord.py
import random
import re
from discord.utils import get
import discord
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('python才學沒多久硬要寫BOTㄉㄑㄜ就是屑')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
#當有訊息時
async def on_message(message, var=None):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    if message.content.startswith('拜託了另一個我'):
        channel = message.channel
        await channel.send('打招呼\nㄅㄅ\n哭\n垃圾機器人\n說/:  (想他說ㄉ話)\n猜拳 (剪刀/石頭/布)\n幸運抉擇(比大小)\n笑死我了\n應急食品\n摸摸頭\n欸嘿\nB嘴\n拍手\n好刑\n骰子\n更改狀態 (要改ㄉ狀態)\n邀請網址(誰會想用這機器人啦')
    if message.content.startswith('打招呼'):
        channel = message.channel
        await channel.send('嗨嗨嗨嗨嗨!')
    if message.content.startswith('ㄅㄅ'):
        channel = message.channel
        await channel.send('ㄅㄅㄅㄅㄅ!')
    if "哭" in message.content:
        channel = message.channel
        await channel.send('嗚嗚嗚嗚嗚!')
    if "乆" in message.content:
        channel = message.channel
        await channel.send('乆乆乆乆乆')
    if message.content.startswith('垃圾機器人'):
        channel = message.channel
        await channel.send('人家在努力ㄌQQ')
    # 如果以「說」開頭
    if message.content.startswith('說'):
        # 分割訊息成兩份
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("說啥?")
        else:
            await message.channel.send(tmp[1])
    # 如果以「:」開頭
    if message.content.startswith(':'):
        if len(message.content) == 1:
            await message.channel.send("?")
        else:
            #刪除訊息
            await message.delete()
            await message.channel.send(message.content)
    #自製猜拳遊戲
    if message.content.startswith('猜拳'):
        # 分割訊息成兩份
        tmpd = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmpd) == 1:
            await message.channel.send("出拳啊484想作弊蛤?")
        else:
            caiquannum=random.randint(0,2)
            if caiquannum==0:
                await message.channel.send("剪刀")
            elif caiquannum==1:
                await message.channel.send("石頭")
            elif caiquannum==2:
                await message.channel.send("布")
            if tmpd[1]=="剪刀":
                if caiquannum==0:
                    await message.channel.send("平手~")
                elif caiquannum==1:
                    await message.channel.send("哈哈你輸ㄌ")
                elif caiquannum==2:
                    await message.channel.send("可惡你贏ㄌ")
            elif tmpd[1]=="石頭":
                if caiquannum==1:
                    await message.channel.send("平手~")
                elif caiquannum==2:
                    await message.channel.send("哈哈你輸ㄌ")
                elif caiquannum==0:
                    await message.channel.send("可惡你贏ㄌ")
            elif tmpd[1]=="布":
                if caiquannum==2:
                    await message.channel.send("平手~")
                elif caiquannum==0:
                    await message.channel.send("哈哈你輸ㄌ")
                elif caiquannum==1:
                    await message.channel.send("可惡你贏ㄌ")
            else:
                await message.channel.send("沒有這種拳啦!")
    # 自製簡易版幸運抉擇
    if message.content.startswith('幸運抉擇'):
        channel = message.channel
        ln = random.randint(1, 13)
        cn = random.randint(1, 13)
        await channel.send(f'{ln}')
        def checkmessage(m):
            return m.content == '大' or m.content == '小' and m.channel == channel
        message = await client.wait_for('message', check=checkmessage)
        await channel.send(f'{cn}')
        if '大' in message.content:
            channel = message.channel
            if cn > ln:
                await channel.send("猜對啦!")
            elif cn == ln:
                await channel.send("一樣ㄝ!")
            else:
                await channel.send("猜錯囉")
        elif '小' in message.content:
            channel = message.channel
            if cn > ln:
                await channel.send("猜錯囉")
            elif cn == ln:
                await channel.send("一樣ㄝ!")
            else:
                await channel.send("猜對啦!")
    if "笑死" in message.content:
        channel = message.channel
        await channel.send('／ ￣￣ ＼　\n|　～　～ \　 ／￣￣￣￣￣￣￣￣￣￣＼\n|　 ◉　◉    |   |　                                            \ \n\　　 ▱　/ ∠             笑死我了                  |\n ＼　　 イ　 \ \n／　　　\     \-————————————/\n|　|阿釜   | |')
    if message.content.startswith('應急食品'):
        channel = message.channel
        await channel.send('⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⠛⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⡀⠀⢀⠀⢻⡄⣠⠶⣆⠀⣸⣀⣀⠀⠀⡀⠀⢀⠀⢀⠀⠀\n⠀⠀⠀⠁⠀⠀⢀⡠⠬⠛⢓⣏⠉⣾⣉⣀⠉⢹⡀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠐⠀⢀⡖⠋⣠⠴⠛⠙⢹⠞⢳⢀⣨⡵⠚⠀⠀⠀⠐⠀⠀⠂⠀\n⠀⠀⠀⣰⠋⡠⠎⠁⣀⠤⠒⠚⠛⠙⠒⠳⠤⣄⡀⠀⠠⠀⠀⠄⠀⠠\n⠀⠀⠀⠘⠐⢼⠖⠋⠀⠀⢀⠀⠀⠀⠀⠀⠀⠘⣌⡒⠲⢹⠀⠀⠀⠀\n⠀⠀⠈⠀⡸⠁⠀⠀⠀⠀⡆⠀⠀⠐⠀⠢⣄⠀⡽⡙⡲⠑⠒⠒⡒⠁\n⢀⡠⠴⠚⠀⠀⠀⠀⠀⣕⠝⣄⡀⢀⠀⠀⡇⠵⢍⠚⢾⡀⢠⠖⠁⠀\n⠈⠦⣄⣀⠀⡔⠀⠀⢁⡞⠀⠉⠲⣄⡀⢲⢼⠀⢀⠳⡄⠁⠀⢣⠀⠀\n⠀⠀⣠⠃⢐⠄⠀⠀⠴⠅⠠⡊⡢⠀⠉⠉⠁⠀⢆⠕⠹⡀⠀⠈⡆⠀\n⠀⠠⡇⠀⡸⠀⠀⠀⠨⡅⠀⠒⠈⠀⢄⠠⠠⠔⠀⠀⠀⢻⠀⠀⢣⠀\n⠀⢸⠅⠀⡕⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⡏⠀⠀⢸⠀\n⠀⠈⡇⠀⣣⠀⠀⠈⠀⠸⡦⠴⠲⢚⢚⠙⠝⠙⠍⠝⣱⠏⢠⠀⢸⠅\n⠀⠀⠙⣆⠘⣄⠀⠠⣄⠀⠹⣌⠌⠀⠂⠐⢈⠄⡁⢌⠳⣺⠏⢀⡞⠀\n⠀⠀⠀⠀⠙⠺⠛⣲⠜⠟⡓⡚⣏⣔⡀⡌⣀⢂⣔⠴⠋⢏⠒⠁⠀⠀​')
    if message.content.startswith('摸摸頭'):
        channel = message.channel
        await channel.send('欸嘿嘿~')
    if message.content.startswith('請多多指教'):
        channel = message.channel
        await channel.send('多指教多指教~')
    if message.content.startswith('欸嘿'):
        channel = message.channel
        await channel.send('欸嘿得囊打油!!')
    if message.content.startswith('B嘴'):
        channel = message.channel
        await channel.send('過分QQ')
    if message.content.startswith('拍手'):
        channel = message.channel
        await channel.send('%%%%%%%%%%%%')
    if message.content.startswith('好刑'):
        channel = message.channel
        await channel.send('。      🌲/         🚔|     \ \n        🌲/          🚔 |       \ \n      🌲/           🚔  |         \ \n    🌲/          🚔     |           \ \n  🌲/         🚔        |             \ \n🌲/🚘: 我沒有煉銅！！！\ ')
    #骰子功能ㄉ呦
    if message.content.startswith('骰子'):
        channel = message.channel
        dice=random.randint(1,6)
        await channel.send(f'你骰到{dice}')
    if message.content.startswith('更改狀態'):
        # 切兩刀訊息
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("蛤啦你到底要改成怎樣啦==")
        else:
            game = discord.Game(tmp[1])
            # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
            await client.change_presence(status=discord.Status.online, activity=game)
            await message.channel.send("在改ㄌ在改ㄌ")
    if message.content.startswith('交出你的身家'):
        channel = message.channel
        await channel.send('https://discord.com/developers/applications/979210652491063376/information')
    if message.content.startswith('邀請網址'):
        channel = message.channel
        await channel.send('https://discord.com/api/oauth2/authorize?client_id=979210652491063376&permissions=2048&scope=applications.commands%20bot')
client.run(token)
