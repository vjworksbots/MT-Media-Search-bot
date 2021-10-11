import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
from utils import Media, get_file_details
from info import TUTORIAL 
from pyrogram.errors import UserNotParticipant
logger = logging.getLogger(__name__)

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
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="**♦️ READ THIS INSTRUCTION ♦️\n ✪ഫയലുകൾ ലഭിക്കുന്നതിനായി  നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ join ചെയ്യണം ശേഷം refresh button അമർത്തുക\n ✪ You Need To Join Our Channel and Press Refresh Button to get the File.!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("⭕️Join Channel ⭕️", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("🔄Try Again🔃", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="Something went Wrong.",
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
                buttons = [
                    [
                        InlineKeyboardButton('🔰CHANNEL🔰', url='https://t.me/joinchat/b2crtyaFjLRiMDQ1')
                    ],
                    [
                        InlineKeyboardButton('🎭GROUP🎭', url='https://t.me/PCLinks')
                    ]
                    ]
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
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**♦️ READ THIS INSTRUCTION ♦️\n ✪ഫയലുകൾ ലഭിക്കുന്നതിനായി  നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ join ചെയ്യണം ശേഷം refresh button അമർത്തുക\n ✪ You Need To Join Our Channel and Press Refresh Button to get the File.!**",           
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⭕️Join Channel⭕️", url=invite_link.invite_link)
                    ]
                ]
            )
        )
    else:
        await cmd.reply_photo(

            photo="https://telegra.ph/file/5c8ddb66e9605f3521bfc.jpg",

            caption=f"<b>Hai</b> {cmd.from_user.mention}  Brooh!🙋,\n\n<b>I'm[☞ 𝙸𝙼𝙳𝙱 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 🤖](https://t.me/VjimdbotFilter_bot) or you can call me as Auto-Filter Bot You Can Use Me As A Auto-filter in Your Group</b> ....\n\n<b>Its Easy To Use Me; Just Add Me To Your Group As Admin, Thats All, i will Provide Movies There</b>...🤓\n\n<b>©️MᴀɪɴᴛᴀɪɴᴇD Bʏ</b>   <a href=tg://user?id=1946514705> Sanoop_Ｔｇ♨</a>",

            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url= "https://t.me/VjimdbotFilter_bot?startgroup=true")
                    ],
                    [
                        InlineKeyboardButton("𝙎𝙚𝙖𝙧𝙘𝙝 𝙝𝙚𝙧𝙚🔎", switch_inline_query_current_chat=''),
                        InlineKeyboardButton("𝘼𝙣𝙮 𝙃𝙚𝙡𝙥 🛠️", url="https://t.me/Sanoob_Achu_18")
                    ],
                    [
                        InlineKeyboardButton("𝙈𝙮 𝘿𝙚𝙫 🤗", url="https://t.me/Sanoob_Achu_18"),
                        InlineKeyboardButton("𝘼𝙗𝙤𝙪𝙩 😎", callback_data="about")
                    ],
                    [
                        InlineKeyboardButton("❕ 𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞 ❕", url="https://t.me/Sanoob_Achu_18")
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
            InlineKeyboardButton('𝐂𝐇𝐀𝐍𝐍𝐄𝐋💗', url='https://t.me/joinchat/AK1vv2n8AZ41NmY1'),
            InlineKeyboardButton('𝐆𝐑𝐎𝐔𝐏⭕️', url='https://t.me/PCLinks')
        ],[
            InlineKeyboardButton('𝐔𝐏𝐃𝐀𝐓𝐄𝐒🎻', url='https://t.me/ottmovies_updates')
        ]]
    await message.reply(text="<b><u>😁എന്തിനാ മോനെ ഇത്രേം സാഹസം കാണിച്ചത് 📃Source Code📃 ന് വേണ്ടിയാണോ🙄ന്തയാലും ഇവിടെ വരെ വന്നില്ലേ🤔 ചാനലിലും ഗ്രൂപ്പിലുമൊക്കെ ജോയിൻ😛 ചെയ്തിട്ട് പൊക്കോ🚶🤧</u></b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
