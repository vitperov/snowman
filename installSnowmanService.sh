#!/bin/bash

SERVICENAME=snowman
SERVICES=/etc/init.d

sudo cp $SERVICENAME $SERVICES
sudo chmod 755 $SERVICES/$SERVICENAME
sudo chown root:root $SERVICES/$SERVICENAME

sudo update-rc.d $SERVICENAME defaults
sudo update-rc.d $SERVICENAME enable
