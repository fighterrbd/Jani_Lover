from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from NEXIOMUSIC import app

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("‷𓆩᪵⟶͇̽[ɪ⃪ϻ̱̱֯༏𐏓⃪꯭𓆩꯭𝗝꯭ᴀ꯭፝֟͠ɴ꯭ɪ꯭꯭ ꯭꯭꯭꯭꯭꯭𔘓꯭𓃭͜ ⃟⛦⃕ ̶꯭𝅥ͦ𝆬 ⃪͢,", url="https://t.me/Jani_RP_Lover")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
 
        [
            InlineKeyboardButton("‷𓆩᪵⟶͇̽[ɪ⃪ϻ̱̱֯༏𐏓⃪꯭𓆩꯭𝗝꯭ᴀ꯭፝֟͠ɴ꯭ɪ꯭꯭ ꯭꯭꯭꯭꯭꯭𔘓꯭𓃭͜ ⃟⛦⃕ ̶꯭𝅥ͦ𝆬 ⃪͢,", url="https://t.me/Jani_RP_Lover"),
        ],
        [
            InlineKeyboardButton("ᴛєᴄʜ", url="https://t.me/Jani_RP"),
        ],
        [
            InlineKeyboardButton("ᴄʜᴧᴛ ɢᴄ", url="https://t.me/+AaI_GATiYwQ5NjU1"),
            InlineKeyboardButton("🅙︎⃞𝗮𝗻𝗶 ♡︎ 🅒︎⃞𝗵𝗮𝘁", url="https://t.me/+AaI_GATiYwQ5NjU1"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("ᴧʙσυᴛ", url="https://t.me/Jani_RP"),
            InlineKeyboardButton("ʜєʟᴘ | ɪηғσ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("ʙᴧsɪᴄ ɢυɪᴅє", callback_data="ABOUT_BACK HELP_GUIDE"),
            InlineKeyboardButton("ᴅσηᴧᴛє", callback_data="ABOUT_BACK HELP_DONATE"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
