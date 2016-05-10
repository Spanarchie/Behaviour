#github_rsa!/bin/bash apt-get install idle-python3
if [ ! -d "pyEnvJenkins" ]; then
        virtualenv pyEnv2_7Jenkins
        . pyEnv2_7Jenkins/bin/activate
        pip install -r requirements.txt
fi
. pyEnv2_7Jenkins/bin/activate
pip install -r requirements.txt

behave --junit

deactivate
