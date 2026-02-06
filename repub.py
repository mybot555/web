from telethon import TelegramClient, events, Button
from pyvault import PyVault
import os

# --- الإعدادات ---
API_ID = '13740761'
API_HASH = '4ce319a92c01fab2b02551af8d7f73a4'
BOT_TOKEN = '7911049277:AAEonlYQG7fMeX6jmtIn5u4Ds32P-EG7hEg'

repthon = TelegramClient('ClashBot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

START_TEXT = """
**مرحباً بك في بوت كلايش ريبثون 💋**

يمكنك اختيار القسم المناسب لك، أو **إرسال أي ميديا** لرفعها والحصول على رابط مباشر.

**اختر ما يناسبك يا بطل :**
"""

# --- استقبال الميديا للرفع (باستخدام كودك الأول) ---
@repthon.on(events.NewMessage)
async def handle_uploads(event):
    if event.media and not event.text.startswith('/'):
        msg = await event.reply("⚙️ **جاري الرفع الدائم...**")
        path = await event.download_media()
        result = PyVault.upload(path)
        if result["ok"]:
            await msg.edit(f"✅ **تم الرفع بنجاح!**\n\n🔗 الرابط المباشر:\n`{result['url']}`")
        else:
            await msg.edit(f"❌ **فشل الرفع:** {result['error']}")
        if os.path.exists(path):
            os.remove(path)

# --- رسالة الترحيب ---
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
        clashes = "**إليك كلايش فخمة للأولاد 🛡️...**"
        await event.edit(clashes, buttons=[Button.inline("🔙 العودة", data="back")])

    elif data == "girls":
        clashes = "**إليك كلايش كيوت للبنات 🎀...**"
        await event.edit(clashes, buttons=[Button.inline("🔙 العودة", data="back")])

    elif data == "back":
        await event.edit(START_TEXT, buttons=[
            [Button.inline("قسم الأولاد 🛡️", data="boys"),
             Button.inline("قسم البنات 🎀", data="girls")],
            [Button.url("قناة السورس ⚡", "https://t.me/Repthon")]
        ])

print("البوت يعمل الآن PyVault... 🚀")
repthon.run_until_disconnected()
