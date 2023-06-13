import os


def pytest_sessionstart(session):
    os.system("./mysql.sh start || sleep 2; ./remake_db.sh")


def pytest_sessionfinish(session, exitstatus):
    os.system("./remake_db.sh")
