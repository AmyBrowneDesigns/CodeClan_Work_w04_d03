from flask import Flask, render_template, redirect, request

from repositories import task_repository
from repositories import user_repository
from models.task import Task

from flask import Blueprint

tasks_blueprint = Blueprint("tasks", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@tasks_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all() # NEW
    return render_template("tasks/index.html", all_tasks = tasks)


# NEW
# GET '/tasks/new'
@tasks_blueprint.route("/tasks/new")
def new_task():
    users = user_repository.select_all()
    return render_template("/tasks/new.html", all_users=users)


# CREATE
# POST '/tasks'
@tasks_blueprint.route("/tasks", methods=["POST"])      #default is ["GET"] so doesnt need to be decalred for get.
def create_task():
    description = request.form["description"]
    user_id = request.form["user_id"]
    duration = request.form["duration"]
    completed = request.form["completed"]
    user = user_repository.select(user_id)

    task = Task(description, user, duration, completed)

    task_repository.save(task)

    return redirect('/tasks')


# SHOW                                                  # for showing one thing in detail. {{task.description}} in the html can be placed inside an <a></a> tag
# GET '/tasks/<id>'

# EDIT                                                  # slightly harder code
# GET '/tasks/<id>/edit'

# UPDATE                                                # slightly harder code
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'