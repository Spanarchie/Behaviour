#!/bin/bash

. pyEnv2_7Jenkins/bin/activate
pip install -r requirements.txt

behave --junit

deactivate
