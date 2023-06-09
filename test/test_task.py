from app import app
import json


def test_create_task():

    data={
        "title": "dancdindg_dssd",
        "description": "dance dfast",
        "due_date":"1686291663",
    }
    response = app.test_client().post("/task", data=json.dumps(data),
                headers={"Content-Type": "application/json"})
    data = json.loads(response.data.decode("utf-8"))
    global ids
    ids = data['id']

    assert response.status_code == 201


def test_get_task():
    response = app.test_client().get(f"/task?id={ids}",
                headers={"Content-Type": "application/json"})
    assert response.status_code == 200


def test_update_task():
    data={
        "title": "dancing dmwh_ans",
        "description": "dance dfast",
        "due_date":"1686291661",
        "status":"InProgress"
    }
    response = app.test_client().put(f"/task?id={ids}", data=json.dumps(data),
                headers={"Content-Type": "application/json"})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200


def test_delete_task():
    response = app.test_client().delete(f"/task?id={ids}",
                headers={"Content-Type": "application/json"})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200