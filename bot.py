from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram.ext import ApplicationBuilder
import os

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
CHANNEL_LINK = "https://t.me/+5olMUPxmjIthNWQ0"

questions = [
    {"q": "Biz yarın akşam saat sekizde sinemaya ........ .",
     "options": ["A) gideceğiz", "B) gidiyorsun", "C) gidiyorduk", "D) giderim"],
     "answer": "A"},

    {"q": "Hava çok soğuk. Siz dışarı çıkmak ........ ?",
     "options": ["A) istiyor musunuz", "B) istemek istiyor musunuz", "C) istiyor musun", "D) istiyor muyuz"],
     "answer": "A"},

    {"q": "Kardeşim her gün çok güzel yemek ........ .",
     "options": ["A) yapıyor", "B) yiyor", "C) pişiriyor", "D) hazırlıyor"],
     "answer": "A"},

    {"q": "........ ........ rengi çok güzel.",
     "options": ["A) Ayşe elbise", "B) Ayşe'nin elbisesi", "C) Ayşe'nin elbisesinin", "D) Ayşe'ye elbisesi"],
     "answer": "B"},

    {"q": "Benim babam ........ ........ .",
     "options": ["A) Türkçenin öğretmeni", "B) Türkçe öğretmenin", "C) Türkçe öğretmeni", "D) Türkçeyi öğretmeni"],
     "answer": "C"},

    {"q": "Gazetede okudum; dün gece İzmir'de şiddetli bir deprem ........ .",
     "options": ["A) oldu", "B) oluyor", "C) olmuş", "D) olacak"],
     "answer": "A"},

    {"q": "Efsaneye göre, bu eski sarayda çok cesur bir ........ yaşıyormuş.",
     "options": ["A) kahraman", "B) tezgahtar", "C) memur", "D) veteriner"],
     "answer": "A"},

    {"q": "Dün akşam televizyon izlerken koltukta uyuyakalmışım. Meğer kapı ........ .",
     "options": ["A) açıkmış", "B) açıktı", "C) açığız", "D) açıkmışsın"],
     "answer": "A"},

    {"q": "Masaldaki cadı, güzel prensese ........ bir elma vermiş.",
     "options": ["A) sarıca", "B) kıpkırmızı", "C) mavimsi", "D) yeşilimsi"],
     "answer": "B"},

    {"q": "Eyvah! Aceleyle evden çıktım, cüzdanımı masanın üzerinde ........ .",
     "options": ["A) unutuyorum", "B) unutmuşum", "C) unuttum", "D) unutacağım"],
     "answer": "B"},

    {"q": "Ayşe: 'Haberin var mı? Ali’nin kardeşi üniversiteden mezun ........ .'",
     "options": ["A) olmuş", "B) oldu", "C) oluyor", "D) olmalı"],
     "answer": "A"},

    {"q": "Dün bütün çikolataları yedim. Keşke çikolataları ........ .",
     "options": ["A) yemem", "B) yemese", "C) yemeseydim", "D) yememişim"],
     "answer": "C"},

    {"q": "Lütfen ben ders ........ beni rahatsız etmeyin.",
     "options": ["A) çalışırken", "B) çalıştığında", "C) çalışınca", "D) çalıştıktan sonra"],
     "answer": "A"},

    {"q": "Mozart ilk eserini ........ kaç yaşındaydı?",
     "options": ["A) yaparken", "B) yaptığında", "C) yaparsa", "D) yapmalı"],
     "answer": "B"},

    {"q": "Yemeği ........ onu yemek zorunda değilsin.",
     "options": ["A) beğenmeseydin", "B) beğenmediysen", "C) beğenmiyorsan", "D) beğenmezken"],
     "answer": "C"},

    {"q": "Belirli bir alanda yeterli deneyimi olan kişiye ne denir?",
     "options": ["A) Vasıfsız", "B) Kalifiye", "C) İşsiz", "D) Memur"],
     "answer": "B"},

    {"q": "Futbol maçını yöneten kişiye ne denir?",
     "options": ["A) Antrenör", "B) Taraftar", "C) Hakem", "D) Kaleci"],
     "answer": "C"},

    {"q": "'Sarı çizmeli Mehmet Ağa' ne anlama gelir?",
     "options": ["A) Zengin kişi", "B) Kimliği bilinmeyen kişi", "C) Şık kişi", "D) Güçlü kişi"],
     "answer": "B"},

    {"q": "Vücudun bir bölgesinin uyuşturulduğu anestezi türü nedir?",
     "options": ["A) Bölgesel", "B) Bedensel", "C) Kişisel", "D) Fiziksel"],
     "answer": "A"},

    {"q": "'Birine aşık olmak' anlamına gelen ifade hangisidir?",
     "options": ["A) dümen yapmak", "B) makaraya almak", "C) abayı yakmak", "D) kazık yemek"],
     "answer": "C"},

    {"q": "Hangi cümlede birleşik zaman vardır?",
     "options": ["A) Gideceğiz", "B) Bitirmiştim", "C) Yaparım", "D) Sevindim"],
     "answer": "B"},

    {"q": "'Böyle tembel tembel ........ iş bulman imkânsız.'",
     "options": ["A) oturdukça", "B) oturduğun sürece", "C) otururken", "D) oturduktan sonra"],
     "answer": "B"},

    {"q": "Birkaç hafta içinde tek başıma trafiğe ........",
     "options": ["A) çıkabiliyorum", "B) çıkabileceğim", "C) çıkamazdım", "D) çıkardım"],
     "answer": "B"},

       {"q": "A: Arkadaşlar, bir okul etkinliği yapmayı düşünüyorduk. Öğrencileri kitap fuarına götürebiliriz.\nB: ........",
     "options": [
         "A) Hayır, kitap okumayı sevmiyorum.",
         "B) Evet, iyi fikir ama yakında bir fuar var mı?",
         "C) Kitaplar çok pahalı, gidemeyiz.",
         "D) Ben gelmek istemiyorum."
     ],
     "answer": "B"},

    {"q": "Güzel güzel akşam yemeğimizi yerken ........ kavga çıkarıp keyfimi kaçırdın.",
     "options": [
         "A) hiç yoktan",
         "B) sanki",
         "C) dursa dursa",
         "D) oysa ki"
     ],
     "answer": "A"}
]
 
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 سلام، به Merhaba Türkçe خوش اومدی!\n\n"
        "اینجا قراره سطح ترکی‌ات رو با یک تست کوتاه و کاربردی بسنجیم.\n\n"
        "📌 تست شامل ۲۵ سواله\n"
        "⏱ حدود ۳ تا ۵ دقیقه زمان می‌بره\n"
        "🎯 آخر تست، سطح تقریبی‌ات مشخص میشه\n\n"
        "برای شروع بزن:\n"
        "/start_test"
    )


async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_data[user_id] = {"index": 0, "score": 0}

    await update.message.reply_text(
        "🎯 تست تعیین سطح شروع شد\n\n"
        "لطفاً با دقت جواب بده.\n"
        "تا پایان تست، جواب درست و غلط نمایش داده نمی‌شود.\n"
        "نتیجه نهایی در آخر برایت ارسال می‌شود.\n\n"
        "Başlayalım 🚀"
    )

    await send_question(update, user_id)


async def send_question(update: Update, user_id: int):
    data = user_data[user_id]
    index = data["index"]

    if index >= len(questions):
        await show_result(update, user_id)
        return

    question = questions[index]

    text = (
        f"📌 Soru {index + 1}/{len(questions)}\n\n"
        f"{question['q']}\n\n"
        + "\n".join(question["options"])
    )

    keyboard = [["A", "B"], ["C", "D"]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await update.message.reply_text(text, reply_markup=reply_markup)


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_id not in user_data:
        await update.message.reply_text("برای شروع تست بزن:\n/start_test")
        return

    data = user_data[user_id]
    index = data["index"]

    if index >= len(questions):
        return

    user_answer = update.message.text.strip().upper()
    correct_answer = questions[index]["answer"]

    if user_answer == correct_answer:
        data["score"] += 1

    data["index"] += 1
    await send_question(update, user_id)


async def show_result(update: Update, user_id: int):
    score = user_data[user_id]["score"]
    total = len(questions)

    percentage = (score / total) * 100

    if percentage <= 35:
        level = "A1"
        note = "تو هنوز در ابتدای مسیر ترکی هستی، اما با تمرین روزانه خیلی سریع پیشرفت می‌کنی."
    elif percentage <= 60:
        level = "A2"
        note = "تو پایه‌های ترکی رو بلدی، ولی برای روان صحبت کردن به تمرین منظم نیاز داری."
    elif percentage <= 85:
        level = "B1"
        note = "تو سطح خوبی داری. حالا وقتشه ترکی رو طبیعی‌تر، روان‌تر و کاربردی‌تر یاد بگیری."
    else:
        level = "B2"
        note = "سطحت خوبه. با تمرین هدفمند می‌تونی ترکی رو حرفه‌ای‌تر و طبیعی‌تر استفاده کنی."

    message = (
        f"🎯 نتیجه تست شما: {score}/{total}\n\n"
        f"📌 سطح تقریبی شما: {level}\n\n"
        f"{note}\n\n"
        "در کانال Merhaba Türkçe قرار نیست با درس‌های سنگین خسته‌ات کنیم.\n"
        "اینجا هر روز فقط یک قدم کوچک جلو می‌ری:\n\n"
        "✔ یک جمله کاربردی\n"
        "✔ یک دیالوگ واقعی\n"
        "✔ یک نکته کوتاه\n"
        "✔ یک تمرین ساده\n\n"
        "🌱 شعار ما:\n"
        "هر روز یک قدم از دیروزت بهتر شو.\n\n"
       f"👇 برای شروع یادگیری رایگان وارد کانال شو:\n{CHANNEL_LINK}"
    )

    await update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())
    del user_data[user_id]


async def main():
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    await app.bot.delete_webhook(drop_pending_updates=True)

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("start_test", start_test))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))

    await app.run_polling()

import asyncio
asyncio.run(main())
