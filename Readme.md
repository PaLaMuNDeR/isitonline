## Is it online

Checks if the websites in the array of check_services.py are up and sends automated email. If a website is down, it would notify you. Running at 8.45 AM every morning to have an overview of the state of the systems you maintain.

1. Setup the list of the urls you want to be checked at [check_services.py](check_services.py)
2. Setup an account at [Mailgun](https://mailgun.com) and insert the API and domain link.

3. Create python3 venv and add it in the crontab path. Install requests with:
`pip install requests`

4. setup crontab to run everyday at 08:45 AM with:
```
crontab -e

45 8 * * * cd /<DOWNLOADED_FOLDER>/isitonline/ && ./venv/bin/python3.6 check_services.py 

```
