# User authentication service Project :user: :closed_lock_with_key:

## Description :page_facing_up:

### Project intended to learn about:
+ What user authentication means.
+ What the purpose of authentication is.
+ How to implement a log in and log out system.
+ How to store passwords securely.
---

## Language and Libraries :globe_with_meridians: :hammer_and_wrench:
### Language:
- `Python 3.7`

### Libraries:
> use the provided `requirements.txt` file to install the necessary libraries using pip.
```bash
$ pip3 install -r requirements.txt
```
---

## Tasks :white_check_mark:

+ [x] 0. **User model**
    + Create a SQLAlchemy model named User for a database table named users
    + The model must have the following attributes:
        + `id`, representing a column of type `Integer`, that can't be null and is a primary key
        + `email`, representing a column of type `String(250)`, that can't be null and must be unique
        + `hashed_password`, representing a column of type `String(250)` that can't be null
        + `session_id`, representing a column of type `String(250)` that can be null
        + `reset_token`, representing a column of type `String(250)` that can be null

+ [x] 1. **Create user**
    + In this task, you will complete the DB class provided below to implement the add_user method.
    + The method add_user takes mandatory email and hashed_password arguments.
    + The method should save the user to the database and return the user object.

+ [x] 2. **Find user**
    + In this task, you will complete the DB class provided below to implement the find_user_by method.
    + The method find_user_by takes a list of keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments.
    + The method should return an instance of the User model.

+ [x] 3. **Update user**
    + In this task, you will complete the DB class provided below to implement the update_user method.
    + The method update_user takes two mandatory arguments: the first argument is the user_id and the second argument is a dictionary of the user attributes to update.
    + The method should return None.
---

## RESOURCES :bookmark_tabs:
- [Flask Documentation](https://intranet.alxswe.com/rltoken/lKExyvivrrW4eh0eI8UV6A)
- [Requests module](https://intranet.alxswe.com/rltoken/py7LuuD1u2MUwcaf8wnDzQ)
- [HTTP status codes](https://intranet.alxswe.com/rltoken/cj-mc5ZHp_KyXn1yikHC0A)
