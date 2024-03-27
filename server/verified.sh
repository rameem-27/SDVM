#!/bin/bash

uid_value="235865975515"
constitution=$(python3 find_constitution.py "$uid_value")

python3 collect_candidate.py "$constitution"


#Use: find the constitution of the uid_value owner using the place value
#And collect the details of the candidates in the constitution and save it as json