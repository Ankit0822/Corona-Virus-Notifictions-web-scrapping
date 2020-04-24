from cx_Freeze import setup, Executable
setup(name='Corona_notifications',
        version='1.0',
        description='You will notified about corona Virus Cases',
        executables= [Executable("Corona_noti.py")]
    )
