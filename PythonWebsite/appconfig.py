import platform

where = platform.uname().release.find("aws")

if where == -1:
    # Local.
    config = {
        "host": "127.0.0.1",
        "database": "commentsDB",       # Enter own information in these slots
        "user": "comment",
        "password": "commentspasswd",
    }
else:
    # Not on PA.
    config = {
        "host": "C00250093.mysql.pythonanywhere-services.com", # Enter own information in these slots
        "database": "C00250093$default",
        "user": "C00250093",
        "password": "pythonanywheremysqlpassword",
    }
