import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from payment import *
from help import *
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from trans import *
from calcu import *


# -

sython.start()
@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@Source_chithon 1"))
    except BaseException:
        pass
        
@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@YYUUN1"))
    except BaseException:
        pass
      

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@Q_3_I"))
    except BaseException:
        pass  
        
        
y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

hijri_day = tran.translate(str(day), dest="ar")
hijri = f"{Gregorian.today().to_hijri()} - {hijri_day.text}"
LOGS = logging.getLogger(__name__)


logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)


DEVS = [
    5159123009,
]
DEL_TIME_OUT = 60
normzltext = "1234567890"
namerzfont = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await sython(JoinChannelRequest("@Source_chithon 1"))
    except BaseException:
        pass

@sython.on(events.NewMessage(outgoing=True, pattern=".اسم وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"chithon  | {HM}"
        LOGS.info(name)
        try:
            await sython(
                functions.account.UpdateProfileRequest(
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
       

@sython.on(events.NewMessage(outgoing=True, pattern=".بايو وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%H:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = f"chithon  |️ {HM}"
        LOGS.info(bio)
        try:
            await sython(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
 
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اكس او"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await sython.inline_query(bot, "")
    await xo[0].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )


@sython.on(events.NewMessage(outgoing=True, pattern=r".xo"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await sython.inline_query(bot, "")
    await xo[0].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.حجرة ورقة مقص"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await sython.inline_query(bot, "")
    await xo[4].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )

@sython.on(events.NewMessage(outgoing=True, pattern=r".rps"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await sython.inline_query(bot, "")
    await xo[4].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.صورته"))
async def _(event):
    """Gets the profile photos of replied users, channels or chats"""
    id = "".join(event.raw_text.split(maxsplit=2)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
    else:
        photos = await event.client.get_profile_photos(chat)
    if id.strip() == "":
        try:
            await event.client.send_file(event.chat_id, photos)
        except:
            photo = await event.client.download_profile_photo(chat)
            await sython.send_file(event.chat_id, photo)
    else:
        try:
            id = int(id)
            if id <= 0:
                await event.edit("`ايدي الشخص غير صالح !`")
                return
        except:
            await event.edit("`هل انت كوميدي ؟`")
            return
        if int(id) <= (len(photos)):
            send_photos = await event.client.download_media(photos[id - 1])
            await sython.send_file(event.chat_id, send_photos)
        else:
            await event.edit("`ليس لديه صوره يا ذكي !`")
            return


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.ذاتية"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            "يستعمل الامر بالرد على الصورتهة او الفيديو !"
        )
    rr9r7 = await event.get_reply_message()
    await event.delete()
    pic = await rr9r7.download_media()
    await sython.send_file(
        "me", pic, caption=f"تـم حفظ الصورة او الفيديو الذاتي هنا : chithon "
    )


@sython.on(events.NewMessage(pattern=r"\.ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await sython(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)



@sython.on(events.NewMessage(outgoing=True, pattern=r".اذاعة للكروبات"))
async def gcast(event):
    sython = event.pattern_match.group(1)
    if sython:
        msg = sython
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                await event.client.send_message(chat, msg)
                done += 1
                asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة للخاص(?: |$)(.*)"))
async def gucast(event):
    sython = event.pattern_match.group(1)
    if sython:
        msg = sython
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit(" جاري الاذاعه..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
                    asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@sython.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@sython.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
 



@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اشتراكاتي"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    u = 0  # number of users
    g = 0  # number of basic groups
    c = 0  # number of super groups
    bc = 0  # number of channels
    b = 0  # number of bots
    await event.edit("يتم التعداد ..")
    async for d in sython.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            pass
            # logger.info(d.stringify())
    end = datetime.datetime.now()
    ms = (end - start).seconds
    await event.edit("""تم استخراجها في {} ثواني
`الاشخاص :\t{}
المجموعات العادية :\t{}
المجموعات الخارقة :\t{}
القنوات :\t{}
البوتات :\t{}
`""".format(ms, u, g, c, bc, b))


@sython.on(events.NewMessage(pattern=r"\.ملصق", outgoing=True))
async def _(event):

    if event.fwd_from:
        return

    if not event.reply_to_msg_id:
        await event.edit("**يجب الرد على الرسالة**")
        return

    reply_message = await event.get_reply_message()
    if not reply_message.text:

        await event.edit("**يجب الرد على الرسالة**")

        return

    chat = "@QuotLyBot"

    sender = reply_message.sender

    if reply_message.sender.bot:

        await event.edit("**يجب الرد على الرسالة**")

        return

    await event.edit("**جاري التحويل**")

    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True, from_users=1031952739))
            msg = str(reply_message.message)
            await sython.send_message(chat, msg)
            response = await response
        except YouBlockedUserError:
            await event.reply("** قـم بألغاء الحظر من البوت - @QuotLyBot - **")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)



@sython.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("waiting...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
♔ شيثون العرب الاساسي
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
父 𝙹𝙾𝙺𝙴𝚁 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 ✓  (@special_anime9)父
‎⿻┊‌‎‌‎𝙽𝙰𝙼𝙴 𖠄 عمك ٫
‌‎⿻┊‌‎‌‎𝙿𝚈𝚃𝙷𝙾𝙽 𖠄 1.10.5 ٫
‌‎⿻┊‌‎‌‎𝙹𝙾𝙺𝙴𝚁 𖠄 1.25.2 ٫
‌‎⿻┊‌‎‌‎𝚄𝙿𝚃𝙸𝙼𝙴 𖠄 17h:1m:1s ٫
‌‎⿻┊‌‎‌‎‌‎𝙿𝙸𝙽𝙶 𖠄 136.506 ٫
‌‎⿻┊‌‎‌‎‌‎𝚂𝙴𝚃𝚄𝙿 𝙳𝙰𝚃𝙴 𖠄 2023-07-10 ٫
𖠄 J𝗼𝗸𝗲𝗿 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𖠄
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
''')

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.بوتس"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("waiting...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
♔ شيثون العرب الاساسي انشاء بوت
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
لإنشاء بوت تلجرام مع يوزرات البوتات، يمكنك اتباع الخطوات التالية:

1. قم بفتح تطبيق Telegram وابحث عن "BotFather" في قائمة البحث.

2. قم بالتوجه إلى Chat مع "BotFather" وابدأ دردشة جديدة.

3. قم بكتابة "/newbot" لإنشاء بوت جديد.

4. ستُطلب منك اختيار اسم المستخدم الخاص بالبوت، أدخل اسم المستخدم الذي تفضله.

5. في الخطوة التالية، ستُطلب منك اختيار اسم عرض للبوت. أدخل اسمًا مناسبًا للبوت.

6. بعد ذلك، ستحصل على رسالة تأكيد تتضمن رمز API الخاص بالبوت. قم بحفظ هذا الرمز، سيكون لديك حاجة له فيما بعد.

7. الآن، يمكنك إنشاء يوزرات البوتات لبوتك عن طريق الذهاب إلى قسم البوت في تطبيق Telegram والقيام بالخطوات التالية:
   - قم بالنقر على زر "إنشاء يوزر بوت جديد" أو "Create New Bot User".
   - أدخل اسم المستخدم الذي تود استخدامه لليوزر الجديد. يجب أن ينتهي بـ "bot" مثل "mynewbot".
   - قم بتوفير صورة مصغرة (اختيارية) لليوزر الجديد.
   - قم بالنقر على زر "حفظ" أو "Save".

8. ابدأ في تكوين اليوزرات الجديدة وتعيين الصلاحيات والأوامر لكل يوزر حسب احتياجاتك.

بهذه الطريقة، يمكنك إنشاء بوت تلجرام مع يوزرات البوتات وتخصيصها وفقًا لاحتياجاتك. يمكنك تكرار الخطوات 7 و 8 لإنشاء المزيد من يوزرات البوتات إذا لزم الأمر.
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
''')

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.صم"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("waiting...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
♔ شيثون العرب الاساسي انشاء ملصقات
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
لإنشاء ملصقات في تطبيق Telegram، يمكنك اتباع الخطوات التالية:

1. قم بفتح دردشة فردية أو مجموعة في تطبيق Telegram.

2. انقر على أيقونة مرفق في أسفل الشاشة. قد تكون رمزًا عبارة عن ورقة وقلم رصاص أو رمزًا عبارة عن زر زائد "+". قد يكون الرمز في الزاوية اليسرى السفلى أو الزاوية اليمنى السفلى من الشاشة.

3. ستظهر لك قائمة خيارات مرفقة. اختر خيار "الملصقات" أو "Stickers".

4. ستنتقل إلى قائمة الملصقات. انقر على زر "إنشاء ملصق جديد" أو "Create New Sticker".

5. ستطلب Telegram منك اختيار إشارة مرجعية للملصق. يمكنك اختيار إحدى الطرق التالية لإنشاء الملصق:

   - قم بتحميل صورة من جهازك المحمول.
   - قم بالتقاط صورة باستخدام الكاميرا.
   - اختر إشارة مرجعية من الملصقات الموجودة في حسابك.
   - بدلاً من ذلك، يمكنك البحث في الإنترنت عن إشارة مرجعية واستخدام رابط الصورة.

6. بمجرد تحديد إشارة المرجعية للملصق، سترى شاشة تحرير الملصق حيث يمكنك إضافة نصوص أو عناصر أخرى.

7. استخدم أدوات التحرير المتاحة لإضافة نصوص أو تعديل الصورة.

8. بمجرد الانتهاء من تحرير الملصق، انقر على زر "Publish" أو "نشر" لإضافة الملصق إلى المجموعة أو الدردشة.

مبروك! لقد قمت بإنشاء ملصق في تطبيق Telegram. يمكن للمستخدمين الآخرين أيضًا استخدام هذا الملصق عند الدردشة معك في نفس المجموعة أو الدردشة الفردية.
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
''')

@sython.on(events.NewMessage(outgoing=True, pattern=r".م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@sython.on(events.NewMessage(outgoing=True, pattern=r".م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@sython.on(events.NewMessage(outgoing=True, pattern=r".م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@sython.on(events.NewMessage(outgoing=True, pattern=r".م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)


@sython.on(events.NewMessage(outgoing=True, pattern=r".م5"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec5)

@sython.on(events.NewMessage(outgoing=True, pattern=r".م6"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec6)
    
    
@sython.on(events.NewMessage(outgoing=True, pattern=r".م7"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec7)
    
@sython.on(events.NewMessage(outgoing=True, pattern=r".م8"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec8)
    
@sython.on(events.NewMessage(outgoing=True, pattern=r".م9"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec9)
    
@sython.on(events.NewMessage(outgoing=True, pattern=r".م0"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec0)
    
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.التاريخ"))
async def _(event):
    await event.edit(f"""**-- -- -- -- -- -- -- -- --
	`الميلادي : {m9zpi}`
-- -- -- -- -- -- -- -- --
	`الهجري : {hijri}`
-- -- -- -- -- -- -- -- --**"""
                     )


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.ايدي"))
async def _(event):
    reply_message = await event.get_reply_message()
    if reply_message is None:
        try:
            user = (await event.get_sender()).id
            bio = await sython(functions.users.GetFullUserRequest(id=user))
            bio = bio.about
            photo = await sython.get_profile_photos(event.sender_id)
            await sython.send_file(event.chat_id, photo, caption=f'''
    ايديك : `{event.sender_id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await sython.send_message(event.chat_id, f"ايديك : `{event.sender_id}`")
    else:
        id = reply_message.from_id.user_id
        try:
            bio = await sython(functions.users.GetFullUserRequest(id=id))
            bio = bio.about
            photo = await sython.get_profile_photos(id)
            await sython.send_file(event.chat_id, photo, caption=f'''
    ايديه : `{id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await sython.send_message(event.chat_id, f"ايديه : `{id}`")


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.المطور"))
async def _(event):
    photo = await sython.get_profile_photos(DEVS[0])
    await sython.send_file(event.chat_id, photo, caption=f'''
    The best !
      - @Q_3_I
''', reply_to=event)



@sython.on(events.NewMessage(outgoing=True, pattern=r"\.البنك"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("Ok...")
    end = datetime.datetime.now()
    res = (end - start).microseconds / 1000
    await event.edit(f"""**-- -- -- -- -- -- -- -- -- --
chithon  - 𝗵𝘂𝘀𝘀𝗮𝗺
- البنك : `{res}`
-- -- -- -- -- -- -- -- -- --**"""
                     )




@sython.on(events.NewMessage(outgoing=True, pattern=r".فك المحضورين"))
async def _(event):
    list = await sython(functions.contacts.GetBlockedRequest(offset=0, limit=1000000))
    if len(list.blocked) == 0:
        razan = await event.edit(f'**ليس لديك اي شخص محظور**')
    else:
        unblocked_count = 1
        for user in list.blocked:
            UnBlock = await sython(functions.contacts.UnblockRequest(id=int(user.peer_id.user_id)))
            unblocked_count += 1
            razan = await event.edit(f'**جارِ الغاء الحظر : {round((unblocked_count * 100) / len(list.blocked), 2)}%**')
        unblocked_count = 1
        razan = await event.edit(f'**تم الغاء حظر : {len(list.blocked)}**')


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("**جاري اعادة تشغيل السورس**")
    await sython.disconnect()
    await sython.send_message("me", "**اكتملت اعادة تشغيل السورس**")


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف النشر التلقائي"))
async def update(event):
    await event.edit("**جاري ايقاف النشر التلقائي**")
    await sython.disconnect()
    await sython.send_message("me", "**اكتمل ايقاف النشر التلقائي**")

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التكرار"))
async def update(event):
    await event.edit("**جاري ايقاف التكرار**")
    await sython.disconnect()
    await sython.send_message("me", "**اكتمل ايقاف التكرار**")


c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython(JoinChannelRequest('saythonh'))
    channel_entity = await sython.get_entity(bot_username)
    await sython.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BL**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | BL**")

@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython(JoinChannelRequest('saythonh'))
    channel_entity = await sython.get_entity(bot_usernamee)
    await sython.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BL**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | BL**")

@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython(JoinChannelRequest('chithon '))
    channel_entity = await sython.get_entity(bot_usernameee)
    await sython.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BL**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | BL**")


@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython(JoinChannelRequest('chithon '))
    channel_entity = await sython.get_entity(bot_usernameeee)
    await sython.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BL**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع | BL**")



print("♦️ chithon  is Running ♦️")
sython.run_until_disconnected()
