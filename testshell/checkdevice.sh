#!/bin/bash
CHECK_DIRECTORIES="/home/ubuntu/testshell";
DATE=`date +%m%d%y`;
result_file="/home/ubuntu/testshell"$DATE.rpt; #结果文件
exec > $result_file; #exec重定向标准输出到指定文件中
echo "The disk used of top10:";
for dir_check in $CHECK_DIRECTORIES
do
        echo ""
        echo "The $dir_check directory:"
        sudo du -s $dir_check/* | sort -rn | sed '{11,$d;}' | sed '=' | sed 'N; s/\n/ /' | gawk '{printf $1 ":" "\t" $2 "\t" $3 "\n"}'
done
