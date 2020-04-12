import requests

sites = [
    "https://google.com",
    "https://yahoo.com"
]
MAILGUN_DOMAIN_URL = "https://api.eu.mailgun.net/v3/<YOUR_DOMAIN_NAME_GOES_HERE>/messages"
MAILGUN_API_KEY = "<YOUR_MAILGUN_KEY_GOES_HERE>"
SENDER_EMAIL = "My Email <my@email.com>"
RECIPIENT_EMAIL = "recipient@mail.com"


def is_it_online(websites):
    """
        Checks if a website is online. If it is failing - send an email
    """

    error = False
    for url in websites:
        response = requests.get(url)
        code = response.status_code

        if code != 200:
            error = True
            send_error_message(url)

    if not error:
        send_final_ok_message()


def send_error_message(url):
        return requests.post(
            MAILGUN_DOMAIN_URL,
            auth=("api", MAILGUN_API_KEY),
            data={"from": SENDER_EMAIL,
                  "to": [RECIPIENT_EMAIL],
                  "subject": "Website Maintenance ❌ {}".format(url),
                  "text": "Website {} is down! 🤷‍♂️".format(url)})


def send_ok_message(url):
        return requests.post(
            MAILGUN_DOMAIN_URL,
            auth=("api", MAILGUN_API_KEY),
            data={"from": SENDER_EMAIL,
                  "to": [RECIPIENT_EMAIL],
                  "subject": "{} is up! 👍".format(url),
                  "text": "Website {} is up!".format(url)})


def send_final_ok_message():
        return requests.post(
            MAILGUN_DOMAIN_URL,
            auth=("api", MAILGUN_API_KEY),
            data={"from": SENDER_EMAIL,
                  "to": [RECIPIENT_EMAIL],
                  "subject": "All good - ✅👍",
                  "text": "Everything is calm."})


is_it_online(sites)
