from dotenv import load_dotenv
import os
# Use the package we installed
from slack_bolt import App
from pycloudflared import try_cloudflare

tc = try_cloudflare(port=3000)

print(tc.tunnel + '/slack/events')

load_dotenv()  # take environment variables from .env.

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
@app.command("/echo")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{command['text']}")

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
