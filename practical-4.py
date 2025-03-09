from gpiozero import LED
# pip install python-telegram-bot
from telegram.ext import Application, CommandHandler


TOKEN = ""
led = LED(13)


async def turn_on(update, context):
    led.on()
    await update.message.reply_text("LED is now ON 💡")


async def turn_off(update, context):
    led.off()
    await update.message.reply_text("LED is now OFF 🌑")


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("on", turn_on))
app.add_handler(CommandHandler("off", turn_off))
app.run_polling()
