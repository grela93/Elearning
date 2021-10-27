# ELEARNING
## Bước 1: Cài đặt môi trường Python
Vào đường dẫn: https://www.python.org/downloads/ sau đó tải Python 3.10.0 và thêm vào PATH (Windows)

## Bước 2: Cài đặt framework Django và các thư viện hỗ trợ
```terminal
$ git clone https://github.com/grela93/Elearning.git Elearning
$ cd Elearning
$ python get-pip.py
$ pip install virtualenv
$ virtualenv .venv
$ .venv/bin/activate
(.venv)$ pip install -r requirements.txt
```

## Bước 3: Cài đặt MySQL và tạo Database
- Vào đường dẫn: https://dev.mysql.com/downloads/mysql/ để tải và cài đặt MySQL
- Tạo Database:
  - Tên: Elearning
  - Mật khẩu: abc123456(Lưu ý: phải trùng với PASSWORD trong Elearning/root/settings.py)
  - Host: localhost
  - Port: 3306
  
## Bước 4: Kết nối Django với Database trên MySQL
- Vào file Elearning/root/settings.py sửa biến DATABASE
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'elearning',
        'USER': 'root',
        'PASSWORD': 'abc123456',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

## Bước 5: Tạo các bảng trong Database
```terminal
(.venv)$ python manage.py makemigrations
(.venv)$ python manage.py sqlmigrate course 0005
(.venv)$ python manage.py sqlmigrate quiz 0008
(.venv)$ python manage.py sqlmigrate user 0005
(.venv)$ python manage.py migrate
```

## Bước 6: Tạo admin
```terminal
$ python manage.py createsuperuser
```

## Bước 7: Khởi chạy Website Elearning
```terminal
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 27, 2021 - 23:17:17
Django version 3.2.6, using settings 'root.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
- Vào đường dẫn: http://127.0.0.1:8000 để truy cập trang web
- Vào đường dẫn: http://127.0.0.1:8000/admin để thêm tài khoản Giảng viên và Sinh viên (Tài khoản đăng nhập được tạo từ bước 6)
  - Sau khi thêm tài khoản, trở lại đường dẫn: http://127.0.0.1:8000/ để:
  - Đối với tài khoản Giảng viên: Thêm sửa xóa bài giảng, bài Quiz, thống kê điểm
  - Đối với tài khoản Sinh viên: Học các bài giảng và làm bài Quiz
# CHÚC BẠN CÀI ĐẶT THÀNH CÔNG!
