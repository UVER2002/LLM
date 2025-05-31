import json
from config import CONV_HISTORY

def log_conversation(user, bot):
    try:
        with open(CONV_HISTORY, "r") as f:
            history = json.load(f)
    except:
        history = []
    history.append({"user": user, "nain": bot})
    with open(CONV_HISTORY, "w") as f:
        json.dump(history, f, indent=2)
