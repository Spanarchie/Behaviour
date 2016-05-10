#!/bin/bash
apt-get install idle-python3
if [ ! -d "pyEnvJenkins" ]; then
        virtualenv pyEnvJenkins
        . pyEnvJenkins/bin/activate
        pip install -r requirements.txt
fi
. pyEnvJenkins/bin/activate
pip install -r requirements.txt

behave --junit

deactivate
