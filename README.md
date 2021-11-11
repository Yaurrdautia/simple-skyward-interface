# simple skyward interface

This is a simple skyward interface that allows the average person to interface with skyward easily. 

## if you are in the LWSD
You do not have to change anything in the code. It will do it's thing with the information you give it. Look at the examples in the examples folder for more info. 

## if you are not in the LWSD and use skyward
Make sure to update your base url in the library to match the one that is your dstrict's URL. (Hint: Include everything up until the end of Wservice=)
Make sure that the pages are pointing towards the correct direction. The login page will most likely be fwemnu01 but make sure it is correct before running it. 

## General instructions
This library is still under development. 
You **need** to run setup(username,password) in order for anything to work since these are used for authentication when the session id and encses are grabbed. 
For a example look inside the examples folder. 
