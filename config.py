### ~ Aitech config : aichatbot

from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "28768514")) # get my.telegram.org/apps
API_HASH = getenv("API_HASH", "40761fd256d71926ac455e55fcb71ae1") # get my.telegram.org/apps
OWNER_ID = int(getenv("OWNER_ID", "6634423600")) # Owner ID: get @MissRose_bot /info ...
STRING_SESSION = getenv("STRING_SESSION", "AgG2-QIAvTaF7iATDipXgZ0PqULu8RYo9ZQ94yRkdoPAgVMA35cpyxB8xJkFrFfF2k0d51djiO0O6QW-fx_mFdQf4j8m3gcJrKyL-emNqM0GcNOXCT0xTF8SLHB5AiAeZbkfteToyhEQXnqbgPyfsiTyuVn9jCmYQ5ULycnqbVrkG5RJtrZwRl7Bc2fJekq7ao-xb3Ky1FVjtiRdoxSdgfZ3Wy1ajCVS5hJ8L6Z2_JnNbYIfvSFtgLeiFKjF04iVQjpEr4aIfnUAtmwT9HP3rgWyjie9_12V-YxTsuILy9GgnZWaYQoycs5LaEPCZ0XXZ-Ct0YXigofu9yuNjDw7DLkXFs3g8gAAAAF2FQicAA") # Pyrogram v2 String Session: help @aiteknoloji
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://agautevdragitevsvh:pJSptT6jE0pcw9a4@cluster0.de4uc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Free mongo db url: "mongodb+srv://shikhar:shikhar@cluster0.6xzlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
SUPPORT_GRP = getenv("SUPPORT_GRP", "nezrinsupp")
UPDATE_CHNL = getenv("UPDATE_CHNL", "nezrinlogo")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Thagiyev") # Owner username "@" without 

# Random Start Images
IMG = [
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
]


# Random Stickers 
STICKER = [
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
    "https://graph.org/file/ff8fa5df03aecffd1b010.jpg",
]

# Random Emojios
EMOJIOS = [
    "😍",
    "🌹",
    "😔",
    "❤️",
    "😻",
    "😝",
    "😁",
    "👀",
    "🇦🇿",
    "🤣",
    "🙈",
    "🤨",
    "🥹",
]
