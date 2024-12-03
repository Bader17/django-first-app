import os
import json
import requests

# Step 1: List all .txt files in the directory
feedback_directory = "C:\\Python311\\django\\feedbackProject\\data\\feedback"
feedback_files = [f for f in os.listdir (feedback_directory) if f.endswith('.txt')]

# Step 2: Read and parse each file
feedback_list = []
for feedback_file in feedback_files:
    with open(os.path.join(feedback_directory, feedback_file), 'r') as file:
        lines = file.readlines()
        feedback_dict = {
            'title': lines[0].strip(),
            'name': lines[1].strip(),
            'date': lines[2].strip(),
            'feedback': ' '.join(line.strip() for line in lines[3:])
        }
        feedback_list.append(feedback_dict)

# Step 3: Post data using the requests module
url = 'http://35.227.191.94/feedback/?format=api'
for feedback in feedback_list:
    response = requests.post(url, json=feedback)
    if response.status_code == 201:
        print(f'Successfully posted feedback from {feedback["name"]}')
    else:
        print(f'Failed to post feedback from {feedback["name"]}: {response.status_code}')

