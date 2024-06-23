SMART DIGITAL VOTING MACHINE
It is an entirely new voting procedure with sophisticated method of vote casting with
automatic ID verificaion along withbiometric authentication.

This method doesnot require any manual verification throughout the voting.

So it can significantly reduce the man power

It enable the voters to cast their vote from any polling booth across the country.
#Uses Flask app as web server.
#Uses Raspberry pi as the voting machine

Voting Procedure
1) The voting machine shows live feed from the camera in the touch display.
2) Whenever a voter scan their aadhaar card infront of camera, the machine sends the data from the Aadhaar Card to the Server.
3) Server verifies the ID card by comparing the data with Aadhaar database.
4) Also verifies the elligibility of voter by comparing the data with voters database.
5) If any of the verification returns false, the machine displays appropriate error and return to the live feed.
6) If both the verification is successfull then the voter need to verify there fingerprint.
7) If it fails the machine displays the appropriate error and return to live feed.
8) If fingerprint verification is successfull the server queries for the candidate details in the respective voters constitution.
9) The voter can cast their vote through the touch display.
10) The result will be updated live.


In addition to that also create a website to view the results live.

Also a portal for the election officer to update the voter list
