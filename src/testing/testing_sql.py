import subprocess
import pathlib
import time
import os
import re

def print_line():
    line = "=" * os.get_terminal_size().columns
    print(f"\033[92m{line}\033[0m\n")

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
        count = 0

        line = script.readline()
        print("\033c")

        while True:
            if not line:
                print_line()
                break

            while line[:2] == "--":
                description += line
                line = script.readline()

            if len(line) > 1:
                if count == 0:
                    print_line()

                print(f"\033[93m{description}\033[0m")
                description = ""

                while line[-2] != ";":
                    command += line
                    line = script.readline()
                command += line.strip()

                print(f"\033[1m{command}\033[0m\n")

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
                if(len(out) > 0):
                    result_lines = out.decode().split('\n')[:-1]
                    result_lines = [re.sub(r"(\.\d*?)0+([^\d]|$)", lambda matched: matched.group(1) + matched.group(2), line) for line in result_lines]
                    result_lines = [re.sub(r"\.([^\d]|$)", lambda matched: matched.group(1), line) for line in result_lines]
                    result_words = [line.split('\t') for line in result_lines]
                    max_lens = [0 for _ in result_words[0]]
                    for line in result_words:
                        for i, word in enumerate(line):
                            max_lens[i] = max(max_lens[i], len(word))
                    result_lines = ["".join([f"{line[i]:<{max_lens[i] + 4}}" for i in range(len(line))]) for line in result_words]
                                
                    print(
                        *["\033[34;1mDBMS OUTPUT:\033[0m " + result_line for result_line in result_lines],
                        sep='\n'
                    )
                    print()

                command = ""
                wait = True

                line = script.readline()

            while line[:2] == "--":
                description += line
                line = script.readline()

            if len(description) != 0:
                print(f"\033[93m{description}\033[0m")
                description = ""

            count = 0
            while len(line) == 1:
                count += 1
                line = script.readline()

            if wait:
                wait = False
                if count == 2:
                    print_line()
                    count = 0
                    input()
                    print("\033c")
                elif count == 1:
                    print("\033[2A")
                    input()
