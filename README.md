# PITCH APP
This a python application using the flask micro framework that allows users to post one minute pitches. The users in this case can make a pitch in any  given category of choice and they acn also leave comments on other pitches by other users. It incorporates a database where user details are stored once they sign up.

## Author
Nicollette Ochola

## BDD
| Behaviour     |  Input          | Output        |
| :-----------: |:---------------:| :-----------: |
|Register new user|Username,email,password|Login form|
|Login user with the registered credentials|email and password|Home page of the app with latest pitches displayed|
|Create new pitch|Titile, the pitch and the category of the pitch|Succes message for pitch creation and pitch added to latest pitches|
|Add new comment|The comment(click on submit button)|Success message and the comment on pitch|

## Technologies Used
- Python 3.6
- HTML/CSS
- Bootstrap (MDB bootstrap)
- Javascript

## Setup Requirements
- Python 3.6
- Internet Connection
- Run the following commands on your terminal:
`$ git clone https://github.com/NicolletteOchola/PitchApp.git`
- Navigate to the folder
 `$ cd <folder/file name>`
- To run the application;
 `$ python3.6 PitchApp.py`

## Testing
- To run the tests on the application run `$ test_user.py` and `test_comment.py`

## Known Bugs
No known bugs, if you encounter any, feel free to contact me.


## Contacts
nicoeochola@gmail.com
+254 726 868063

## License
MIT Licence (c) Nicollette Ochola 2020


