# backend-intern-assignment 🚀


##### step 1
```bash
source setup.sh
```
It is only create for linux user's.


##### API URL'S

**GET** /tasks?page=1&per_page=10
Pagination api from getting task

Example:-
<br/>
![image](https://github.com/Geeks-Vegeta/backend-intern-assignment/assets/89457811/563924f4-094b-47f3-b981-4c902eafc90a)


**GET** /task
Get all task

Example:-

<br/>

![image](https://github.com/Geeks-Vegeta/backend-intern-assignment/assets/89457811/aeabd131-dd4f-4fc4-a733-16defe793a6a)



**GET** /task?id=2
return user by id
Example:-
<br/>
![image](https://github.com/Geeks-Vegeta/backend-intern-assignment/assets/89457811/6b80c82b-5d9b-465e-ac02-88836608728d)





**POST** /task

```json
{
    "title":"reactjs",
    "description":"create new page",
    "due_date":"1686291663",
}
```
<p>Initial you don't need to use status as it is by default InComplete</p>

Example:-
<br/>
![image](https://github.com/Geeks-Vegeta/backend-intern-assignment/assets/89457811/efdb0c43-bbe6-4a05-8244-09e324fe6f9b)




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
Example:-
<br/>
![image](https://github.com/Geeks-Vegeta/backend-intern-assignment/assets/89457811/f67f10c8-67a2-46d4-bd7c-033fb5bc45fc)




**DELETE** /task?id=1
as **id** is query parameter
delete user

Example:-
<br/>
![image](https://github.com/Geeks-Vegeta/backend-intern-assignment/assets/89457811/63b34fd5-c374-418f-9210-c8aa599fd10a)




I have also added pytest in api's and also generated html reports of pytest.
https://geeks-vegeta.github.io/backend-intern-assignment/
