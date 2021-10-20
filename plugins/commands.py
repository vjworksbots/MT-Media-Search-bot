import os
import logging
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
from utils import Media, get_file_details
from pyrogram.errors import UserNotParticipant
logger = logging.getLogger(__name__)

ADMINS = int(os.environ.get("ADMINS", 1745047302))

PHOTO = [
    "https://telegra.ph/file/a215834295195d610949c.jpg",
    "https://telegra.ph/file/140299fcd89dbd4a0ba92.jpg",
    "https://telegra.ph/file/59fefdf363fd828595589.jpg",
    "https://telegra.ph/file/2b2518ccd770b82ceef03.jpg",
    "https://telegra.ph/file/c6f438023c60b1845552e.jpg",
    "https://telegra.ph/file/5ff727c611adfdb209a44.jpg",
    "https://telegra.ph/file/ce9d7001e57ad2eab84e0.jpg",
    "https://telegra.ph/file/10ef288e99b6c7beca9ee.jpg",
    "https://telegra.ph/file/785106a73c34f984d83c9.jpg",
    "https://telegra.ph/file/49778209084d2eba94152.jpg",
    "https://telegra.ph/file/e9b562bef56458ff1df68.jpg",
    "https://telegra.ph/file/bd7538e39549aa639d692.jpg",
    "https://telegra.ph/file/6fbb764c3202a5560e8e1.jpg",
    "https://telegra.ph/file/3b5591a7020591aff9d79.jpg",
    "https://telegra.ph/file/99a2a5b8be0445ebd23ad.jpg"
]

@Client.on_message(filters.command("start"))
async def start(bot, cmd):
    usr_cmdall1 = cmd.text
    if usr_cmdall1.startswith("/start subinps"):
        if AUTH_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
            try:
                user = await bot.get_chat_member(int(AUTH_CHANNEL), cmd.from_user.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="Sorry Sir, You are Banned to use me.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                ident, file_id = cmd.text.split("_-_-_-_")
                await bot.send_photo(
                    chat_id=cmd.from_user.id,
                    photo=f"https://telegra.ph/file/9cb142a92f808f4d2ee6b.jpg",
                   reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔰Join Channel🔰", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton(" 🔄Restart🔃", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_photo(
                    chat_id=cmd.from_user.id,
                    photo=f"https://telegra.ph/file/9cb142a92f808f4d2ee6b.jpg",
                    caption="Something went Wrong.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        try:
            ident, file_id = cmd.text.split("_-_-_-_")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [[
            InlineKeyboardButton('♻️Channel', url='https://t.me/mcnewmovies'),
            InlineKeyboardButton('Group⭕️', url='https://t.me/Movies_Club_2019')
          ],[
            InlineKeyboardButton('➕ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ➕', url= 'https://t.me/Imdbfilter_bot?startgroup=true')
        ]]
                await bot.send_cached_media(
                    chat_id=cmd.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")
    elif len(cmd.command) > 1 and cmd.command[1] == 'subscribe':
        invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        await bot.send_photo(
            chat_id=cmd.from_user.id,
            photo=f"https://telegra.ph/file/9cb142a92f808f4d2ee6b.jpg",
            caption="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔰Join Channel🔰", url=invite_link.invite_link)
                    ]
                ]
            )
        )
    else:
        await cmd.reply_photo(
            photo=f"{random.choice(PHOTO)}",
            caption=START_MSG,
            reply_markup=InlineKeyboardMarkup(
                    [
                    [
                        InlineKeyboardButton("➕ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ➕", url= "https://t.me/Imdbfilter_bot?startgroup=true")
                    ],
                    [
                        InlineKeyboardButton("🔰 Group", url="https://t.me/Movies_Club_2019"),
                        InlineKeyboardButton("📃 Channel", url="https://t.me/mcnewmovies")
                    ],
                    [
                        InlineKeyboardButton("🕵️‍♂️ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋", url="https://t.me/Myfreak123"),
                        InlineKeyboardButton("😊 𝖠𝖻𝗈𝗎𝗍", url="https://t.me/mcallmovies/46")
                    ]    
                ]
            )
         )


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')
@Client.on_message(filters.command('about'))
async def bot_info(bot, message):
    buttons = [[
            InlineKeyboardButton('♻️𝐒𝐄𝐑𝐈𝐄𝐒', url='https://t.me/MoviesClubSeriesonly'),
            InlineKeyboardButton('𝐆𝐑𝐎𝐔𝐏⭕️', url='https://t.me/Movies_Club_2019')
        ],[
            InlineKeyboardButton('🎞️𝐂𝐇𝐀𝐍𝐍𝐄𝐋🎞️', url='https://t.me/mcallmovies')
        ],[
            InlineKeyboardButton('📍𝐔𝐏𝐃𝐀𝐓𝐄𝐒', url='https://t.me/mcallmovies'),
            InlineKeyboardButton('𝐍𝐄𝐖 𝐑𝐄𝐋𝐄𝐀𝐒𝐄💿', url='https://t.me/mcnewmovies')
        ],[
            InlineKeyboardButton('📀𝐂𝐀𝐌 𝐏𝐑𝐈𝐍𝐓𝐒📀', url='https://t.me/MCmoviesall')
        ]]
    await message.reply(text="<b><u>😁എന്തിനാ മോനെ ഇത്രേം സാഹസം കാണിച്ചത് 📃Source Code📃 ന് വേണ്ടിയാണോ🙄ന്തയാലും ഇവിടെ വരെ വന്നില്ലേ🤔 ചാനലിലും ഗ്രൂപ്പിലുമൊക്കെ ജോയിൻ😛 ചെയ്തിട്ട് പൊക്കോ🚶🤧</u></b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
