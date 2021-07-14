# (c) @AbirHasan2005

import asyncio
from helpers.database.access_db import db
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def OpenSettings(event: Message, user_id: int):
    try:
        await event.edit(
            text="Aquí puede establecer su configuración:",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"Subir como documento {'✅' if ((await db.get_upload_as_doc(user_id)) is True) else '❌'}",
                                          callback_data="triggerUploadMode")],
                    [InlineKeyboardButton("✏️ Nombre del archivo ✏️", callback_data="triggerPrefix")],
                    [InlineKeyboardButton("🖼 Miniatura 🖼", callback_data="triggerThumbnail")],
                    [InlineKeyboardButton("🏷 Subtítulo 🏷", callback_data="triggerCaption")],
                    [InlineKeyboardButton("❎ Cerrar ❎", callback_data="closeMeh")]
                ]
            )
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await OpenSettings(event, user_id)
    except MessageNotModified:
        pass
