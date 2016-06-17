#!/bin/bash

echo "Starting vEnv"
source ../pyEnv2_7Jenkins/bin/activate

echo "Starting the Behave tests"
behave --junit

