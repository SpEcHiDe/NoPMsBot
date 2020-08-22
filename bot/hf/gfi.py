#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Message
)


def get_file_id(msg: Message):
    data_type = None
    content = None
    if msg.media:
        if msg.sticker:
            content = msg.sticker.file_id
            data_type = msg.sticker

        elif msg.document:
            content = msg.document.file_id
            data_type = msg.document

        elif msg.photo:
            content = msg.photo.file_id
            data_type = msg.photo
            
        elif msg.audio:
            content = msg.audio.file_id
            data_type = msg.audio
            
        elif msg.voice:
            content = msg.voice.file_id
            data_type = msg.voice
            
        elif msg.video:
            content = msg.video.file_id
            data_type = msg.video
            
        elif msg.video_note:
            content = msg.video_note.file_id
            data_type = msg.video_note

    return data_type, content
