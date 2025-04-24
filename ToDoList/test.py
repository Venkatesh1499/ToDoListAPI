import unittest
from app import app
import requests

BASE_URL = "http://127.0.0.1:5000"

get_response = requests.get(f"{BASE_URL}/user/tasks/pending/day1")
print(get_response.json())


new_data = {
	"day": "day1",
	"info": {
			"task": "Learn CRUD operations",
			"is_done": False
	}
}
post_response = requests.post(f"{BASE_URL}/user/tasks/addtask", json=new_data)
print(post_response.json())

all_pending = requests.get(f"{BASE_URL}/user/tasks/allpending")
if all_pending.status_code == 200:
	all_tasks = all_pending.json()
	for task in all_tasks:
		print(f"{task['day']} - {task['task']} - {task['isDone']}")
else:
	print(all_pending.json())
print("All pending tasks", all_pending.json()) 
# for i
# for i in all_pending:
	# print(i.json())

get_response = requests.get(f"{BASE_URL}/user/tasks/pending/day1")
print(get_response.json())

delete_response = requests.put(f"{BASE_URL}/user/tasks/delete/day1")
print(delete_response.json())

# tasks = {
#   	"day1" : {"task" : "Need to learn Flask basics", "isDone": False},
# 	"day2" : {"task" : "Complete Flask deployments", "isDone": False},
# 	"day3" : {"task" : "Need to solve few things", "isDone": False}
# }
# new_data = {
# 	"day": "day1",
# 	"info": {
# 		"task" : "Need to learn Flask basics",
# 		"isDone": False
# 	}
# }

# new_data1 = {
# 	"day": "day2",
# 	"info": {
# 		"task" : "Need to try SQLite",
# 		"isDone": False
# 	}
# }

# post1 = requests.post(f"{BASE_URL}/user/tasks/addtask", json = new_data)
# post2 = requests.post(f"{BASE_URL}/user/tasks/addtask",json = new_data1)
# print(post1.json())
# print(post2.json())

# input()

# get1 = requests.get(f"{BASE_URL}/user/tasks/pending/day1")
# get2 = requests.get(f"{BASE_URL}/user/tasks/pending/day3")
# print(get1.json())
# print(get2.json())

# input()

# delete_response = requests.put(f"{BASE_URL}/user/tasks/delete/day3")
# print(delete_response.json())

# update_data = {
# 	"task": "Solve 100 problems on leetcode"
# }

# input()

# update_response = requests.put(f"{BASE_URL}/user/tasks/update/day1", json=update_data)
# print(update_response.json())

# input()

# get_all = requests.get(f"{BASE_URL}/user/tasks/allpending")
# print(get_all.json())