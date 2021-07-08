# By @Damantha_Jasinghe
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.command(["edit", "editor"]))
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="💡 Bright", callback_data="bright"),
                        InlineKeyboardButton(text="🖼 Mixed", callback_data="mix"),
                        InlineKeyboardButton(text="🔳 B&W", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="🟡 Circle", callback_data="circle"),
                        InlineKeyboardButton(text="🩸 Blur", callback_data="blur"),
                        InlineKeyboardButton(text="🌌 Border", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="🎉 Sticker", callback_data="stick"),
                        InlineKeyboardButton(text="↩️ Rotate", callback_data="rotate"),
                        InlineKeyboardButton(text="🔦 Contrast", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="🌇 Sepia", callback_data="sepia"),
                        InlineKeyboardButton(text="✏️ Pencil", callback_data="pencil"),
                        InlineKeyboardButton(text="🐶 Cartoon", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="🔄 Invert", callback_data="inverted"),
                        InlineKeyboardButton(text="🔮 Glitch", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="✂️ Remove BG", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="CLOSE", callback_data="close_e"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
