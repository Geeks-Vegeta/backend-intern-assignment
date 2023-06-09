# backend-intern-assignment 🚀


##### step 1
```bash
source setup.sh
```
It is only create for linux user's.


##### API URL'S

**GET** /tasks?page=1&per_page=10
Pagination api from getting task
<br/>

**GET** /task
Get all task
<br/>

**POST** /task

```json
{
    "title":"reactjs",
    "description":"create new page",
    "due_date":"1686291663",
}
```
<p>Initial you don't need to use status as it is by default InComplete</p>

**PUT** /task?id=1

as **id** is query parameter

```json
{
    "title":"reactjs",
    "description":"create new page",
    "due_date":"1686291668",
    "status":"InProgress"

}
```

**DELETE** /task?id=1
as **id** is query parameter
delete user

<br/>

**GET** /task?id=1
return user by id


I have also added pytest in api's and also generated html reports of pytest.
