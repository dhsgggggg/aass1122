from pyrogram import Client, filters

# اسم المجموعة التي سيتم إنشاؤها
GROUP_NAME = "تخزين_شيثون"

# اسم الملف الذي سيتم استخدامه كمفتاح لحفظ حالة تنصيب السورس
SESSION_NAME = "my_session"

# تهيئة العميل
app = Client(SESSION_NAME)

# دالة لإنشاء المجموعة عند تنصيب السورس
@app.on_client_created()
async def on_client_created(client, _):
    # عند تنصيب السورس، يتم إنشاء المجموعة
    await client.create_group(GROUP_NAME, "This is a group created by my Python code.")

# تشغيل العميل
app.run()
