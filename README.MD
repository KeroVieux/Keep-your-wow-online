# Keep your wow online
## Requires
- Python >= 3.6 (Pycharm public version is recommended)
- Mac OSx 10.15.1 (or above)
- Windows have not tested (if you have confirm that, I glad to know it.)

## Set up
### install requires via terminal
`pip install -r requirements.txt`

### Catch and mark your launch button on the battleNet UI
1. run `python :path/mousePosition.py`
2. paste the coordinate of your launch button and the login button to **mousePosition.py** from the terminal
3. Edit your random key base on your keyboard which you want to do in your game in **actions.py**

## Start to run forever
`python :path/main.py`

## app logic description
1. Random actions per 3 min
2. Back to the camp page per 30 min
3. Kill the process and relaunch your WOW per 3 hours



