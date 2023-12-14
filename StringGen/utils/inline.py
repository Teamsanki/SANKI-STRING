from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="✨Ɠҽɳҽɾαƚҽ ʂҽʂʂισɳ✨", callback_data="gensession")],
        [
            InlineKeyboardButton(text="❤ʂυρρσɾƚ❤", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ", url="https://github.com/skofficial001/StringGenBot"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="😉Ρყɾσɠɾαɱ ʋ1😉", callback_data="pyrogram1"),
            InlineKeyboardButton(text="✨Ρყɾσɠɾαɱ ʋ2✨", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="💀ƚҽʅҽƚԋσɳ💀", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="💔ƚɾყ αɠαιɳ💔", callback_data="gensession")]]
)
