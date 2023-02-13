import requests
import json


TIMEOUT = 180
API_ENDPOINT = "https://api.eazy.im/v3"


class Client:
    def __init__(self, api_key: str, timeout: int = TIMEOUT) -> None:
        self.timeout = timeout

        assert api_key, "api_key cannot be empty."

        self.api_key = api_key

    def request(self, path: str, method: str = "GET", params=None, **kwargs):
        try:
            response = requests.request(
                method=method,
                url=API_ENDPOINT + path,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}",
                },
                timeout=self.timeout,
                data=json.dumps(params),
                **kwargs,
            )
            return response.json()

        except requests.RequestException as e:
            raise EazyException(e)

    def messages_create(
        self, channelJid: str = None, contactJid: str = None, params=None
    ):
        return self.request(
            f"/channels/{channelJid}/messages/{contactJid}", "POST", params
        )

    def contacts_create(self, channelJid: str = None, params=None):
        return self.request(f"/channels/{channelJid}/contacts", "POST", params)

    def contacts_read(
        self, channelJid: str = None, contactJid: str = None, params=None
    ):
        return self.request(
            f"/channels/{channelJid}/contacts/{contactJid}", "GET", params
        )

    def contacts_update(
        self, channelJid: str = None, contactJid: str = None, params=None
    ):
        return self.request(
            f"/channels/{channelJid}/contacts/{contactJid}", "PATCH", params
        )


class EazyException(Exception):
    def __init__(self, result):
        self.result = result
        self.code = None
        self.message = None

        try:
            self.type = result.get("message")
            self.message = result.get("errors")
        except:
            self.type = ""
            self.message = result

        Exception.__init__(self, self.message)
