@echo off
chcp 1251
title KappaWeb

cls
echo Starting KappaWeb Services...
sleep 1
start "Redis" cmd /k "title Redis && redis-server redis.conf"
sleep 2
echo Redis started!
start "Celery" cmd /k "title Celery && celery worker -A backend.api --loglevel=info"
sleep 2
echo Celery started!
goto loop

:loop
python manage.py runserver
echo "KappaWeb is crashed!"
echo.
echo "############################################"
echo "#        KappaWeb is restarting now        #"
echo "############################################"
goto loop