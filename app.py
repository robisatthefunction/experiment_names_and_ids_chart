import requests,csv, argparse

def create_chart():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", help="paste the project ID as the first argument")
    parser.add_argument("token", help="paste your Optimizely v2 REST API token as the second argument")
    args = parser.parse_args()
    project_id = args.project_id
    token = args.token

    experiment_list = requests.get("https://api.optimizely.com/v2/experiments?project_id=%s" % project_id, headers={'Authorization': 'Bearer %s' % token})

    if experiment_list.status_code == 200:
        with open('experiment_names_and_ids.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for exp in experiment_list.json():
                if exp['status'] != 'not_started':
                    filewriter.writerow([str(exp['name']), str(exp['id'])])

create_chart()
