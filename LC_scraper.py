import json

import requests

from selenium import webdriver
from selenium.webdriver import EdgeOptions

from collections import defaultdict

import pathlib

options = EdgeOptions()
options.add_argument("--headless")
driver = webdriver.Edge(options=options)


all_problems = requests.get("https://leetcode.com/api/problems/algorithms/").content
all_problems = json.loads(all_problems)

data = defaultdict(lambda: defaultdict(list))
for problem in all_problems["stat_status_pairs"]:
    url = problem["stat"]["question__title_slug"]
    title = problem["stat"]["question__title"]
    id = problem["stat"]["frontend_question_id"]
    difficulty = problem["difficulty"]["level"]
    paid = problem["paid_only"]
    data[paid][difficulty].append((id,title,url))

difficulties = ['Easy','Medium','Hard']
for paid in data:
    paid_path = f"Leetcode_{'Paid' if paid else 'Free'}"
    pathlib.Path(paid_path).mkdir(parents=True, exist_ok=True)
    for difficulty in data[paid]:
        data[paid][difficulty] = sorted(data[paid][difficulty],key=lambda x: x[0])
        difficulty_path = f"Leetcode_{difficulties[difficulty-1]}"
        pathlib.Path(f'{paid_path}/{difficulty_path}').mkdir(parents=True, exist_ok=True)
        for id,title,url in data[paid][difficulty]:
            with open(f'{paid_path}/{difficulty_path}/{url}.py','w+',encoding="utf-8") as f:
                f.writelines(f'# Leetcode {id}: {title}\n')
                f.writelines(f'# https://leetcode.com/problems/{url}\n')