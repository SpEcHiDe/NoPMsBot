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


from pyrogram.types import Message


def get_file_id(msg: Message):
    data_type = None
    content = None
    if msg.media:
        for message_type in ('sticker', 'document', 'photo',
                             'audio', 'voice', 'video', 'video_note'):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id
