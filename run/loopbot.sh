#!/bin/bash
cd ..

trap "exit" INT

echo "############################################"
echo "##                KappaWeb                ##"
echo "############################################"

while true
do
sudo /usr/local/bin/python3 manage.py runserver 127.0.0.1:8080
echo "KappaWen is crashed!"
echo "Rebooting in:"
for i in {3..1}
do
echo "$i..."
done
echo "###########################################"
echo "#                 KappaWeb                #"
echo "###########################################"
done
