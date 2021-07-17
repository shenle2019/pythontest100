#!/bin/bash
DATE=$(date +%F" "%H:%M)
IP=$(ifconfig eth0 |awk -F '[ :]+' '/inet/{print $3}')
TOTAL=$(free -m |awk '/Mem/{print $2}')
USE=$(free -m |awk '/Mem/{print $3-$5-$6}')
FREE=$(($TOTAL-$USE))
# 内存小于1G发送报警邮件
if [ $FREE -lt 10240 ]; then
    echo "
    Date: $DATE
    Host: $IP
    Problem: Total=$TOTAL,Use=$USE,Free=$FREE
    "
fi
