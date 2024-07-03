from slack_sdk import WebClient
from os import environ
import yaml

# SlackClient = WebClient(token=environ.get("SLACK_BOT_TOKEN"))

def initialize(app_url: str):
    raw_contents = ""
    with open("manifest_template.yml", 'r') as stream:
        raw_contents = stream.read()
        raw_contents = raw_contents.replace("{{app_url}}", app_url)
    
    
    with open("manifest.yml", "w") as stream:
        stream.write(raw_contents)
    print("Written new manifest.yml")