from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور", "مبرمج السورس", "نور"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/b8d877d44850c58363ad7.jpg",
        caption="• Dev Bot ↦  مـطور سـورس  المـيوزك نـور الـحاكم \n ━━━━━━━━━━━━ \n • Dev ↦Cr SoUrce:𓏺𝙽𝙾𝚄𝚁 . \n • Bio ↦- 𓏺 𝐖𝐡𝐨𝐞𝐯𝐞𝐫 𝐡𝐮𝐦𝐛𝐥𝐞𝐬 #𝐡𝐢𝐦𝐬𝐞𝐥𝐟 𝐭𝐨 𝐠𝐨𝐝 𝐰𝐢𝐥𝐥 𝐛𝐞 #𝐞𝐱𝐚𝐥𝐭𝐞𝐝:{@noordot} 𓏺",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙲𝚁 𝙽𝙾𝚄𝚁", url=f"https://t.me/nor_o"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
