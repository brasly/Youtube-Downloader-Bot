from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/TeluguBots")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n\nThis is <b>Youtube Downloader Bot</b>\n\n/help - For more info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
