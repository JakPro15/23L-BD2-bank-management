import sys
import os
from contextlib import contextmanager

# allow imports just like in the main program by adding repo directory to PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.database.database import Database  # noqa: E402


@contextmanager
def testing_database():
    os.system("./mysql.sh start > /dev/null && sleep 2; ./remake_db.sh")
    yield Database()
    os.system("./remake_db.sh")
