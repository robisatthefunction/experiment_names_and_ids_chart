# Create Chart of all of your experiment names and their experiment ids
By running this Python script in your own Python 3 environment you will be able to get all of your Optimizely X experiment names and their experiment ids for a specific Optimizely project, excluding experiments that haven't started yet.

## Steps
If you have Python 3 downloaded and installed on your computer then begin with step 1, if not, download and install Python 3 on your computer [here](https://www.python.org/downloads/)

In your CLI
1. Clone this github repository
2. cd into the experiment_names_and_ids_chart directory
* Optional: Activate your virtual environment
3. Run
```
pip3 install requests
```
4. Generate your own [Optimizely v2 REST API Token](https://developers.optimizely.com/x/rest/getting-started/)
5. Run
```
python3 app.py <your project id> <your API token>
```

The script will return a csv file called experiment_names_and_ids in this directory with two columns, one for experiment name and one for experiment id. The rows will be each experiment. You can see an example file in this director
