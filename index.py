from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import os
# Use the package we installed

from pycloudflared import try_cloudflare
from commands.import_users import handle as userImportHandle
from lib.slack_client import initialize
from lib.slack_app import app

tc = try_cloudflare(port=3000)

print(tc.tunnel + '/slack/events')
initialize(tc.tunnel)


@app.command("/echo")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{command['text']}")

@app.command("/scheduler_import_users")
def import_users(ack, respond, command):
    ack()
    userImportHandle(command)
    
    
    respond("Users imported")
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
