from dotenv import load_dotenv
import os
# Use the package we installed
from slack_bolt import App

load_dotenv()  # take environment variables from .env.

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))