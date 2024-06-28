#Install repo to /etc/cybernet

#dependencies
pip install scapy

#Put cybernet.service file in directory /etc/systemd/system/cybernet

sudo systemctl enable cybernet.service
sudo systemctl start cybernet.service

log file in network_activity.log


