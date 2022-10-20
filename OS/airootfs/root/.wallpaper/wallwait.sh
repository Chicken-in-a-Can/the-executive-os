#!/bin/bash
looper=true
while $looper
do
    if (( $(ps aux | grep -c splash) >= 2 ))
    then
        while (( $(ps aux | grep -c splash) >= 2 ))
        do
            sleep .25
        done
        /root/.wallpaper/wallchange.py
        looper=false
    fi
    sleep .25
done
