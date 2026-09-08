# Project

This is a fun project aimed at learning more about the RESTful interactions with an Aruba AOS-CX switch. I will be using it to gather data about the switch for custom graphs and dashboards.

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
# Resources

HPE API documentation:

https://support.hpe.com/hpesc/public/docDisplay?docId=a00108359en_us
