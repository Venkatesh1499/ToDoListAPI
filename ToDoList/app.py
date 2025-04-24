from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

tasks = {}

@app.route('/user/tasks/pending/<day>', methods = ['GET'])
def get_task(day):
	#connection object
	 conn = get_connection()
	 cursor = conn.cursor()
	 cursor.execute("SELECT * FROM Tasks WHERE day = ?", (day,))
	 task = cursor.fetchone()
	 conn.commit()
	 conn.close()
	 if task:
	 	return jsonify({
		 		"day": day,
		 		"task": task["task"],
		 		"isDone": bool(task["is_done"])
		 		}), 200
	 return jsonify({"error" : f"task not found in {day}"}), 400

@app.route('/user/tasks/addtask', methods = ['POST'])
def add_task():
	conn = get_connection()
	cursor = conn.cursor()
	task = request.json
	day = task['day']
	task_info = task['info']
	cursor.execute('INSERT INTO Tasks (day, task, is_done) VALUES (?, ? ,?)', (day, task_info['task'], task_info['is_done']))
	conn.commit()
	conn.close()
	return jsonify({"message" : f"Task added successfully {task_info['task']} in {day}"}), 201

@app.route('/user/tasks/delete/<day>', methods = ['PUT'])
def delete_task(day):
	conn = get_connection()
	cursor = conn.cursor()
	task = cursor.execute('SELECT * FROM Tasks WHERE day = ?', (day,)).fetchone()
	if task is None:
		conn.close()
		return jsonify({"error" : f"No {day} in pending tasks"}), 400

	cursor.execute('DELETE FROM Tasks WHERE day = ?', (day,))
	conn.commit()
	conn.close()
	return jsonify({"message" : f"Task added successfully {task[1]} in {day}"}), 200

@app.route('/user/tasks/allpending', methods = ['GET'])
def get_all_pending_tasks():
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Tasks')
	tasks = cursor.fetchall()
	if tasks is None:
		conn.close()
		return jsonify({"error" : f"No pending tasks in {day}"}), 400
	result = []
	for task in tasks:
		result.append({
						 "day": task['day'],
						 "task": task["task"],
						 "isDone": bool(task["is_done"])
					 	})
	conn.commit()
	conn.close()
	return jsonify(result), 200


if __name__ == '__main__':
	app.run()

# @app.route('/user/tasks/pending/<day>', methods = ['GET'])
# def get_task(day):
# 	task = tasks.get(day)
# 	if task:
# 		return jsonify({"day": day, "task": task["t ask"], "isDone": task["isDone"]}), 200
# 	else:
# 		return jsonify({"error" : f"{day} is not added into the tasks list"}) , 404    


# @app.route('/user/tasks/addtask', methods = ['POST'])
# def add_task():
# 	newTask = request.json
# 	day = newTask.get("day")
# 	task_details = newTask.get("info")
# 	if day in tasks:
# 		return jsonify({"error" : "This day is already is occupied. Please select a select a different day"}), 400
# 	tasks[day] = task_details
# 	return jsonify({"message" : "Task added successfully", "data" : task_details}), 200


# @app.route('/user/tasks/delete/<day>', methods = ['PUT'])
# def delete_task(day):
# 	if day in tasks:
# 		task = tasks[day]
# 		del tasks[day]
# 		return jsonify({"message" : "Task deleted successfully", "task": task}), 200
# 	return jsonify({"error" : "Task not found. Please send a valid day"}), 400


# @app.route('/user/tasks/update/<day>', methods = ['PUT'])
# def update_task(day):
# 	if day in tasks:
# 		task_info = request.json
# 		if "task" in task_info:
# 			tasks[day]["task"] = task_info["task"]
# 		if "isDone" in task_info:
# 			tasks[day]["isDone"] = task_info["isDone"]
# 		return jsonify({"message" : "updated successfully", "data" : tasks[day]}), 200
# 	return jsonify({"error" : "Unable to update task details. Please try after some time"}), 401


# @app.route('/user/tasks/allpending', methods = ['GET'])
# def get_all_pending_tasks():
# 	return tasks, 200
