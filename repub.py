from telethon import TelegramClient, events, Button

API_ID = '13740761'
API_HASH = '4ce319a92c01fab2b02551af8d7f73a4'
BOT_TOKEN = '7911049277:AAEonlYQG7fMeX6jmtIn5u4Ds32P-EG7hEg'

repthon = TelegramClient('ClashBot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# --- رسالة الترحيب ---
START_TEXT = """
**مرحباً بك في بوت كلايش ريبثون 💋**

يمكنك اختيار القسم المناسب لك من الأزرار أدناه للحصول على أرقى كلايش الفحص (STATS) المزخرفة والجاهزة للنسخ.

**اختر ما يناسبك يا بطل :**
"""

@repthon.on(events.NewMessage(pattern='/start'))
async def start(event):
    buttons = [
        [Button.inline("قسم الأولاد 🛡️", data="boys"),
         Button.inline("قسم البنات 🎀", data="girls")],
        [Button.url("قناة السورس ⚡", "https://t.me/Repthon")]
    ]
    await event.respond(START_TEXT, buttons=buttons)

# --- معالج الأزرار ---
@repthon.on(events.CallbackQuery)
async def callback(event):
    data = event.data.decode('utf-8')
    
    if data == "boys":
        clashes = """ 
**إليك كلايش فخمة للأولاد (اضغط للنسخ) 🛡️:**

1. 𓆩 𝐒𝐘𝐒𝐓𝐄𝐌 𝐑𝐄𝐏𝐓𝐇𝐎𝐍 𓆪
`rep_temp_system = \"\"\"
**- 𓆩 𝐒𝐘𝐒𝐓𝐄𝐌 𝐑𝐄𝐏𝐓𝐇𝐎𝐍 𓆪 -**
**— — — — — — — — — — —**
**✥╎𝐎𝐖𝐍𝐄𝐑 :** {mention}
**✥╎𝐏𝐈𝐍𝐆 :** `{ping} ms`
**✥╎𝐔𝐏𝐓𝐈𝐌𝐄 :** `{uptime}`
**✥╎𝐃𝐀𝐓𝐄 :** `{reppa}`
**✥╎𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :** `{repver}`
**— — — — — — — — — — —**
**✥╎𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : @Repthon**\"\"\"`

2. 𓄼 𝐄𝐌𝐏𝐄𝐑𝐎𝐑 𝐎𝐅 𝐑𝐄𝐏𝐓𝐇𝐎𝐍 𓄹
rep_temp_emperor =
```𓄼 𝐄𝐌𝐏𝐄𝐑𝐎𝐑 𝐎𝐅 𝐑𝐄𝐏𝐓𝐇𝐎𝐍 𓄹
╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼
◈╎𝐔𝐒𝐄𝐑 : {mention}
◈╎𝐒𝐏𝐄𝐄𝐃 : {ping} ms
◈╎𝐑𝐔𝐍𝐍𝐈𝐍𝐆 : {uptime}
◈╎𝐇𝐈𝐒𝐓𝐎𝐑𝐘 : {reppa}
◈╎𝐒𝐎𝐔𝐑𝐂𝐄 : {repver}
╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼
◈╎𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 : @Repthon```
"""
        await event.edit(clashes, buttons=[Button.inline("🔙 العودة", data="back")])

    elif data == "girls":
        clashes = """
**إليك كلايش كيوت للبنات (اضغطي للنسخ) 🎀:**

1. 𓆩 𝐌𝐘 𝐋𝐀𝐃𝐘 𝐑𝐄𝐏𝐓𝐇𝐎𝐍 𓆪
rep_temp_lady =
```• 𓆩 𝐌𝐘 𝐋𝐀𝐃𝐘 𝐑𝐄𝐏𝐓𝐇𝐎𝐍 𓆪 •
🖇️ — — — — — — — — — — —
👸🏻╎𝐐𝐔𝐄𝐄𝐍 : {mention}
☁️╎𝐏𝐈𝐍𝐆 : {ping} ms
⏱️╎𝐔𝐏𝐓𝐈𝐌𝐄 : {uptime}
📅╎𝐃𝐀𝐓𝐄 : {reppa}
🎀╎𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : {repver}
🖇️ — — — — — — — — — — —
🧸╎𝐌𝐘 𝐖𝐎𝐑𝐋𝐃 : @Repthon```
"""
        await event.edit(clashes, buttons=[Button.inline("🔙 العودة", data="back")])

    elif data == "back":
        await event.edit(START_TEXT, buttons=[
            [Button.inline("قسم الأولاد 🛡️", data="boys"),
             Button.inline("قسم البنات 🎀", data="girls")],
            [Button.url("قناة السورس ⚡", "https://t.me/Repthon")]
        ])

print("البوت يعمل الآن... 🚀")
repthon.run_until_disconnected()
