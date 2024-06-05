#!/bin/bash
    
if [ "$DEPLOYMENT_GROUP_NAME" == "pythonflask" ]
then
    if [ -e /home/my-temp-dir/.htaccess ]
    then
        echo "Waiting for 2 minutes...."
        sleep 120
        cp -R /home/my-temp-dir/. /var/www/html/pyhtonflask
        sudo rm -rf /home/my-temp-dir
        chown -R ubuntu:ubuntu /var/www/html/pyhtonflask
        cd /var/www/html/pyhtonflask
        sudo apt install -y python3 python3-pip
        pip3 install Flask
        nohup python3 todo_list_flask.py runserver 0.0.0.0:5000 &
    else
        cp -R /home/my-temp-dir/. /var/www/html/pyhtonflask
        sudo rm -rf /home/my-temp-dir
        chown -R ubuntu:ubuntu /var/www/html/pyhtonflask
        cd /var/www/html/pyhtonflask
        sudo apt install -y python3 python3-pip
        pip3 install Flask
        nohup python3 todo_list_flask.py runserver 0.0.0.0:5000 &
    fi
fi
