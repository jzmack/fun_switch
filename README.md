# Project

This is a fun project aimed at learning more about the RESTful interactions with an Aruba AOS-CX switch (running version 10.13). I will be using it to gather data about the switch for custom graphs and dashboards.

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

HPE documentation:
https://arubanetworking.hpe.com/techdocs/AOS-CX/10.13/PDF/rest_v10-0x.pdf
https://arubanetworking.hpe.com/techdocs/AOS-CX/10.13/PDF/fundamentals_8100-83xx-9300-10000.pdf
https://arubanetworking.hpe.com/techdocs/AOS-CX/10.13/HTML/rest_v10-0x/Content/Chp_REST_ref/aru-cx-res-api-ref-sum-10.htm

Streamlit docs:
https://docs.streamlit.io/get-started/fundamentals/main-concepts