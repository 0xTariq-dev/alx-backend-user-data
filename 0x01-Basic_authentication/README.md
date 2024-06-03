# Basic Authentication Project :closed_lock_with_key:

## Description :page_facing_up:
A project to learn about basic authentication using the `auth` module in the `flask` library.
---

## Language and Libraries :globe_with_meridians: :hammer_and_wrench:
### Language:
- Python 3.7

### Libraries:
> use the provided `requirements.txt` file to install the necessary libraries using pip.
```bash
$ pip3 install -r requirements.txt
```
---

## Tasks :white_check_mark:

+ [x] 0. **Simple-basic-API**
    + Setup requirements and start the server:
    ```bash
    bob@dylan:~$ pip3 install -r requirements.txt
    ...
    bob@dylan:~$
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
     * Serving Flask app "app" (lazy loading)
    ...
    bob@dylan:~$
    ```

    + Use the API (in another tab or in your browser):
    ```bash
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
    *   Trying 0.0.0.0...
    * TCP_NODELAY set
    * Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
    > GET /api/v1/status HTTP/1.1
    > Host: 0.0.0.0:5000
    > User-Agent: curl/7.54.0
    > Accept: */*
    >
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < Content-Length: 16
    < Access-Control-Allow-Origin: *
    < Server: Werkzeug/1.0.1 Python/3.7.5
    < Date: Mon, 18 May 2020 20:29:21 GMT
    <
    {"status":"OK"}
    * Closing connection 0
    bob@dylan:~$
    ```
