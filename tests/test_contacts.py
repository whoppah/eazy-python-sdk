from dotenv import load_dotenv
from os import getenv

from eazy import Client as EazyClient, EazyException

load_dotenv()

client = EazyClient(
    api_key=getenv("API_KEY"),
)


def test_contact_create():
    response = client.contacts_create(
        channelJid=getenv("SMS_CHANNEL_JID"),
        params={
            "jid": getenv("SMS_CONTACT_JID"),
            "name": "John Doe",
            "reference": "Merchant #",
        },
    )
    print(response)
    assert False


def test_contact_update():
    response = client.contacts_update(
        channelJid=getenv("SMS_CHANNEL_JID"),
        contactJid=getenv("SMS_CONTACT_JID"),
        params={
            "name": "John Doe",
            "reference": "Merchant #",
            "email": "john.doe@gmail.com",
            "customFields": {
                "random": "link"
            }
        },
    )
    print(response)
    assert False
