import random
from ProMusic.utils.database import get_theme

themes = [
    "nayka1",
    "nayka2",
    "nayka3",
    "nayka4",
    "nayka5",
    "nayka6",
    "nayka7",
    "nayka8",
]


async def check_theme(chat_id: int):
    _theme = await get_theme(chat_id, "theme")
    if not _theme:
        theme = random.choice(themes)
    else:
        theme = _theme["theme"]
        if theme == "Random":
            theme = random.choice(themes)
    return theme
