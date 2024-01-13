# test_team_api


## How to install

1) Open Terminal and open folder to clone project in.

2) Clone repository into a desirable folder:

    ```
    https://github.com/OlehShumov/test_team_api.git
    ```

3) Open cloned folder in terminal

4) If you don't have **pip** installed  [install it here](https://pip.pypa.io/en/stable/installation/#).

5) Create and activate **Virtual environment**:
   
   **Windows**
   ```
   python -m venv venv
   ```
   
   ```
   venv\Scripts\activate
   ```
   
   **MacOS**
   ```
   python3 -m venv venv
   ```
   
   ```
   source venv/bin/activate
   ```
   
6) Open cloned folder and install needed requirements using:

    ```
    pip install -r requirements.txt
    ```

7) Make migrations and migrate:

   ```
   python manage.py makemigrations
   ```
   ```
   python manage.py migrate
   ```

8) Install database fixture:

   ```
   python manage.py loaddata data.json
   ```

9) Run server:
   
   ```
   python manage.py runserver
   ```

10) Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
