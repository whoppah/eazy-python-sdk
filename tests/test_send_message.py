from dotenv import load_dotenv
from os import getenv

from eazy import Client as EazyClient, EazyException

load_dotenv()

client = EazyClient(
    api_key=getenv("API_KEY"),
)


def test_send_message():
    response = client.messages_create(
        channelJid=getenv("SMS_CHANNEL_JID"),
        contactJid=getenv("SMS_CONTACT_JID"),
        params={
            "message": {
                "body": "Tim, do you know Gods of death love apples?",
                "type": "text",
            }
        },
    )
    print(response)
