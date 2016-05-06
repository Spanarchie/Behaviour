#!/bin/bash
apt-get install idle-python3
if [ ! -d "pyEnvJenkins" ]; then
        virtualenv pyEnvJenkins
fi
. pyEnvJenkins/bin/activate
pip install -r requirements.txt
cd BrowserStackBehave/
behave --junit

deactivate
