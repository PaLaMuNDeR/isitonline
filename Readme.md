Checks if the websites in the array of check_services.py are up and sends automated email.

1. Setup the list of the urls you want to be checked at (check_services.py)[check_services.py]
2. Setup an account at (Mailgun)[https://mailgun.com] and insert the API and domain link.

create python3 venv and add it in the crontab path

setup crontab to run everyday at 08:45 AM with:
```
crontab -e

45 8 * * * cd /<DOWNLOADED_FOLDER>/isitonline/ && ./venv/bin/python3.6 check_services.py 

```
