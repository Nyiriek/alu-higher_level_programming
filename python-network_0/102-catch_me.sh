#!/bin/bash
# A script that makes a request to 0.0.0.0:5000/catch_me that responds with "You got me!".
curl -sL -XH PUT "Origin=HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
