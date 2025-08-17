
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from pyrogram.enums import ChatMemberStatus

# ==== YOUR CREDENTIALS (from your message) ====
API_ID = 21070449
API_HASH = "4dc5e9048e32773f94847d46e93a43d3"
BOT_TOKEN = "7892515968:AAGVdDdpDnQtnd-rAGqtX8DK-TAESprY9rs"

# ==== BOT SETTINGS ====
CHANNEL_USERNAME = "files_vincenzo"   # without @
OWNER_USERNAME = "ISHOWSPEED_12"      # without @

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
app = Client("files_toolbox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# ==== TEXT CONTENT ====
RATE_TEXT = (
    "𝐍𝐄𝐖 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐑𝐀𝐓𝐄 𝐋𝐈𝐒𝐓 🤑🤑\n\n"
    "1 - 5 𝐒𝐄𝐓𝐒 = ₹2.5🤑\n"
    "6 - 14 𝐒𝐄𝐓𝐒 = ₹3.3🤑\n"
    "15 - 25 𝐒𝐄𝐓𝐒 = ₹3.7🤑\n"
    "26 - 40 𝐒𝐄𝐓𝐒 = ₹4🤑\n"
    "41 - 69 𝐒𝐄𝐓𝐒 = ₹4.2🤑\n"
    "70 - 100+ 𝐒𝐄𝐓𝐒 = ₹5🤑\n\n"
    "@ISHOWSPEED_12\n"
    "IF YOU ARE INTERESTED THEN YOU CAN DM ME @ISHOWSPEED_12\n"
    "AGAR AAP MERE SAATH KAAM KARNA CHAHTE HAIN TO MUJHE MSG KARE @ISHOWSPEED_12"
)

EARN_TEXT = (
    "🌟 WITHOUT INVESTMENT EARNING AVAILABLE ON THIS CHANNEL 👑\n\n"
    "😊 SEE WORK AND NEW RULE H — 1-1-1-1-1-1 MEMBERS KARKE ADD KARNA H — BHOT EASY WORK H 😶⭐️\n\n"
    "😃 AND YE JO FILES H ADMIN, NAVY AND CUSTOMERS KI — WO SAB MA DUNGA AAPKO — ONLY ADD KARNE HONGE MEMBERS ✔️🙂\n\n"
    "⚠️ AGAR 1-1-1-1 SE ZYADA ADD KIYA TO WHATSAPP BAN HO JATA ~6 HOURS KE LIYE — RISK BILKUL NAHI H GUYS\n"
    "❤️ 1 CRORE LOG KARTE HAIN ISSE 🌸"
)

BOSS_TEXT = (
    "✨ Trusted Boss ID Available ✨🙏🏻\n\n"
    "Brazil ✅ price 129 rs\n"
    "Indonesian ✅ price 110 rs\n"
    "China ✅ price 150 rs\n"
    "Russia ✅ price 100 rs\n"
    "South Africa ✅ price 99 rs\n"
    "Singapore ✅ price 89 rs\n"
    "USA ✅ price 99 rs\n"
    "Malaysia ✅ price 99 rs\n"
    "Indian ✅ price 79 rs\n\n"
    "DM for Boss ID\n\n"
    "Note - Paid hai Boss ID\n"
    "Buy karne wale hi DM kare @ISHOWSPEED_12"
)

INFO_TEXT = (
    "🔥 Powered by @ISHOWSPEED_12 🔥\n"
    "⚡ Trusted by 100+ satisfied members & 30+ bulkers 💯\n"
    "🌟 Always delivering best & genuine work.\n\n"
    "“Main Telegram pe aisi files provide karta hu jisme WhatsApp contacts hote hain. "
    "Ye contacts advertisement aur promotion ke liye useful hote hain. Inhe WhatsApp groups me add karke "
    "clients apne ads aur services promote karte hain. Mera kaam hamesha safe, fast aur proof ke sath hota hai, "
    "aur mujh par 100+ members aur 30+ bulkers trust karte hain.”"
)


# ==== KEYBOARDS ====
def join_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
            [InlineKeyboardButton("✅ I've Joined, Check", callback_data="check_join")],
        ]
    )


def menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💰 rate", callback_data="rate"),
                InlineKeyboardButton("💼 want to earn", callback_data="earn"),
            ],
            [
                InlineKeyboardButton("🆔 want to buy boss id", callback_data="boss"),
                InlineKeyboardButton("ℹ️ more info", callback_data="info"),
            ],
        ]
    )


# ==== HELPERS ====
async def is_member(user_id: int) -> bool:
    try:
        m = await app.get_chat_member(CHANNEL_USERNAME, user_id)
        return m.status in (ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER)
    except Exception:
        return False


# ==== HANDLERS ====
@app.on_message(filters.private & filters.command("start"))
async def start_handler(client: Client, message: Message):
    if not await is_member(message.from_user.id):
        await message.reply_text(
            "🚫 Access Denied!\n\n"
            "Must join official Telegram channel.\n"
            "Trusted by 100+ members and 30+ bulkers\n"
            "Powered by @ISHOWSPEED_12",
            reply_markup=join_keyboard(),
        )
        return

    await message.reply_text("🧰 TOOL BOX\nChoose an option below 👇", reply_markup=menu_keyboard())


@app.on_callback_query()
async def callback_handler(client: Client, cq: CallbackQuery):
    data = cq.data
    user_id = cq.from_user.id

    # For all actions except re-check, enforce membership
    if data != "check_join":
        if not await is_member(user_id):
            await cq.message.edit_text(
                "🚫 Access Denied!\n\n"
                "Must join official Telegram channel.\n"
                "Trusted by 100+ members and 30+ bulkers\n"
                "Powered by @ISHOWSPEED_12",
                reply_markup=join_keyboard(),
            )
            await cq.answer("Join the channel to use the bot.", show_alert=True)
            return

    if data == "rate":
        await cq.message.edit_text(RATE_TEXT, reply_markup=menu_keyboard())
        await cq.answer()
    elif data == "earn":
        # Per your instruction: send caption text only (no video)
        await cq.message.edit_text(EARN_TEXT, reply_markup=menu_keyboard())
        await cq.answer()
    elif data == "boss":
        await cq.message.edit_text(BOSS_TEXT, reply_markup=menu_keyboard())
        await cq.answer()
    elif data == "info":
        await cq.message.edit_text(INFO_TEXT, reply_markup=menu_keyboard())
        await cq.answer()
    elif data == "check_join":
        if await is_member(user_id):
            await cq.message.edit_text("🧰 TOOL BOX\nChoose an option below 👇", reply_markup=menu_keyboard())
            await cq.answer("You're in! ✅")
        else:
            await cq.answer("Not joined yet. Please join and try again.", show_alert=True)


if __name__ == "__main__":
    app.run()
