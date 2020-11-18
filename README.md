# Memento
### Designed by Erwan Vivien and Hugo Bois

This is a fork of https://github.com/TheToto/chronos-ics

-[![Build Status](https://travis-ci.org/epita/chronos-ics.svg?branch=master)](https://travis-ci.org/epita/chronos-ics)
-[![Requirements Status](https://requires.io/github/epita/chronos-ics/requirements.svg?branch=master)](https://requires.io/github/epita/chronos-ics/requirements/?branch=master)
-
-Provide ICS files for students @ EPITA (http://chronos.epita.net/).
-
-Our school happens to use ADE Entreprise to advertise students schedules. It is usable but tedious to use as is. This project scraps its web pages and creates the calendar files that can be exposed to students and used to back Google Calendar, Apple iCal and so on.
-
-## Install
-
-```
-pip install -r requirements.txt
-```
-## Run
-
-- get a chrnos token and set "CHRONOS_AUTH_TOKEN" env var
-- run server with `python server.py`
-- maybe adjust groups in cron.py
