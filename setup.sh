#!/usr/bin/env bash

echo "Running setup script..."

sudo apt update
sudo apt install python3.14-venv
sudo apt install python3-pip

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo ""
echo "Enter details to be saved in .env file"
read -p "Enter switch IP: " switch_ip
read -p "Enter switch API user: " switch_user
read -sp "Enter API user password (input is hidden): " switch_password
echo ""

cat << EOF > .env
SWITCH_IP="${switch_ip}"
SWITCH_USER="${switch_user}"
SWITCH_PASSWORD="${switch_password}"
EOF

echo ".env file created with input provided."

echo "Initializing database"
./init_db.py

echo "Setting up streamlit directory"
mkdir .streamlit
echo "[connections.aos_cx_fun]" > .streamlit/secrets.toml
echo 'url="sqlite:///aos_cx_fun.db"' >> .streamlit/secrets.toml

echo "Fetching initial data..."
./fetch_data.sh

echo "When ready, start the app with the following command:
echo "streamlit run streamlit_app.py"
