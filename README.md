# Project

This is a fun project aimed at learning more about the RESTful interactions with an Aruba AOS-CX switch. I will be using it to gather data about the switch for custom graphs and dashboards.

# Requirements

Since this is primarily for playing with an Aruba AOS-CX switch, one of those is needed. The one I'm using is a 12-port 6100 switch running version 10.13 code. If I feel like it, I may extend this to use Cisco switches as well, but that would be down the line

- Linux - this was built on Debian
- Python3.14 or later (probably works on earlier versions of Python but built with 3.14)
- time and patience

# Set up

Clone repo
```sh
git clone git@github.com:jzmack/fun_switch.git
```

Create virtual env
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Create .env file. It should be structured as so:
```
SWITCH_IP=<ip_address>
SWITCH_USER=<username>
SWITCH_PASSWORD=<password>
```

Run init_db.py to create database file. This will create a SQLite database file named `aox_cx_fun.db` in your working directory.

Set up cronjob to run fetch_data.sh every 5 minutes.

Here's mine for example:
```sh
*/5 * * * * /home/jzm/workspace/fun_switch/fetch_data.sh
```

Set up `.streamlit/` directory. This needs to contain a .toml file to access the SQLite database.

```plain
[connections.aos_cx_fun]
url = "sqlite:///aos_cx_fun.db"
```


# Resources

HPE documentation:
https://arubanetworking.hpe.com/techdocs/AOS-CX/10.13/PDF/rest_v10-0x.pdf
https://arubanetworking.hpe.com/techdocs/AOS-CX/10.13/PDF/fundamentals_8100-83xx-9300-10000.pdf
https://arubanetworking.hpe.com/techdocs/AOS-CX/10.13/HTML/rest_v10-0x/Content/Chp_REST_ref/aru-cx-res-api-ref-sum-10.htm

Streamlit docs:
https://docs.streamlit.io/get-started/fundamentals/main-concepts

Other:
https://crontab.guru
https://www.sqlitetutorial.net/sqlite-python/
