import subprocess
import pathlib
import time

if __name__ == "__main__":
    script_location = pathlib.Path(__file__).parents[2].joinpath("mysql.sh")
    remake_location = pathlib.Path(__file__).parents[2].joinpath("remake_db.sh")
    sql_scripts_location = pathlib.Path(__file__).parents[2].joinpath("sql_scripts")
    mysql_location = pathlib.Path.home().joinpath("bd2_23L_z09_mysql/mysql/bin/mysql")

    # provides clean database to run tests on
    if subprocess.run([script_location, "start"]).returncode == 0:
        time.sleep(2.)
    subprocess.run([remake_location])

    with open(sql_scripts_location.joinpath("testing.sql"), "r") as script:
        description = ""
        command = ""
        wait = False

        while True:
            line = script.readline()
            if not line:
                break

            if len(line) > 1:
                while line[:2] == "--":
                    description += line
                    line = script.readline()

                if len(line) > 1:
                    print(description)
                    description = ""

                    while line[-2] != ";":
                        command += line.strip() + " "
                        line = script.readline()
                    command += line.strip()

                    print(command + "\n")

                    mysql = subprocess.Popen(
                        [
                            mysql_location,
                            "--host=localhost",
                            f"--socket={pathlib.Path.home().joinpath('bd2_23L_z09_mysql')}/mysqld.sock",
                            "-u",
                            "root",
                            "bd2-23L-z09"
                        ],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT
                    )

                    out, _ = mysql.communicate(command.encode())
                    print(*["RESULT: " + result_line for result_line in out.decode().split('\n')[:-1]], sep='\n')

                    command = ""
                    wait = True

                    line = script.readline()

                while line[:2] == "--":
                    description += line
                    line = script.readline()

                if len(description) != 0:
                    print(description)
                    description = ""

                if wait:
                    wait = False
                    input()
