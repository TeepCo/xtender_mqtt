#!/usr/bin/env python
import sys
import subprocess
import os
args = sys.argv
SCRIPT_NAME = "xtmq"
VERSION = "0.9.1"

COMMANDS_HELP = ["-h","help","--help"]
COMMANDS_VERSION = ["--version","-v","version"]

WORK_DIRECTORY = os.path.dirname(os.path.abspath(sys.argv[0]))

COMMAND_RUN = "run"
COMMAND_INSTALL = "install"
COMMAND_SERVICE = "service"
COMMAND_VERSION = "version"
COMMAND_HELP = "help"
COMMAND_REMOVE = "remove"
COMMAND_UNINSTALL = "uninstall"

PATH_TO_SCRIPT_FOLDER=f"{WORK_DIRECTORY}/../scripts"
PATH_TO_INSTALL_SCRIPT = f"{PATH_TO_SCRIPT_FOLDER}/install.sh"
PATH_TO_RUN_SCRIPT = f"{PATH_TO_SCRIPT_FOLDER}/run.sh"
PATH_TO_SERVICE_INSTALL_SCRIPT = f"{PATH_TO_SCRIPT_FOLDER}/service_install.sh"
PATH_TO_SERVICE_REMOVE_SCRIPT = f"{PATH_TO_SCRIPT_FOLDER}/service_remove.sh"
PATH_TO_UNINSTALL_SCRIPT = f"{PATH_TO_SCRIPT_FOLDER}/uninstall.sh"

STRING_AVAILABLE_COMMANDS ="Available commands:"
PADDING = len(STRING_AVAILABLE_COMMANDS) * " "
EXEC_INTERRUPT_STRING="\nScript execution interrupted by user. Exiting..."
def print_help(file = sys.stdout):
    print(f"Usage: {SCRIPT_NAME} [COMMAND]...\n",file=file)
    print(f"{STRING_AVAILABLE_COMMANDS} {COMMAND_HELP}",file=file)
    print(f"{PADDING} {COMMAND_VERSION}",file=file)
    print(f"{PADDING} {COMMAND_INSTALL}",file=file)
    print(f"{PADDING} {COMMAND_RUN}",file=file)
    print(f"{PADDING} {COMMAND_UNINSTALL}", file=file)
    print(f"{PADDING} {COMMAND_SERVICE} {COMMAND_INSTALL}",file=file)
    print(f"{PADDING} {COMMAND_SERVICE} {COMMAND_REMOVE}",file=file)



def quit_nicely_on_interrupt(function):
    def wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except KeyboardInterrupt:
            print(EXEC_INTERRUPT_STRING)
            sys.exit(1)
    return wrapper


def print_version():
    print(VERSION)

@quit_nicely_on_interrupt
def run():
    subprocess.call(PATH_TO_RUN_SCRIPT)

@quit_nicely_on_interrupt
def install():
        subprocess.call(PATH_TO_INSTALL_SCRIPT)

@quit_nicely_on_interrupt
def uninstall():
        subprocess.call(PATH_TO_UNINSTALL_SCRIPT)

@quit_nicely_on_interrupt
def service_install():
        subprocess.call(PATH_TO_SERVICE_INSTALL_SCRIPT)

@quit_nicely_on_interrupt
def service_remove():
    subprocess.call(PATH_TO_SERVICE_REMOVE_SCRIPT)
def print_help_and_exit_with_error():
    print(f"Invalid argument '{' '.join((args[1:]))}'",file=sys.stderr)
    print_help(file=sys.stderr)
    sys.exit(1)

if len(args) <= 1:
    print("Xtender mqtt version ",end="")
    print_version()
    print(f"Usage: {SCRIPT_NAME} [COMMAND]...")
    print(f"Try '{SCRIPT_NAME} {COMMAND_HELP}' for more information.")


elif args[1] in COMMANDS_HELP:
    print_help()
elif args[1] in COMMANDS_VERSION:
    print_version()
elif args[1] == COMMAND_INSTALL:
    install()
elif args[1] == COMMAND_RUN:
    run()
elif args[1] == COMMAND_UNINSTALL:
    uninstall()
elif args[1] == COMMAND_SERVICE:
    if len(args) != 3:
        print_help_and_exit_with_error()
    elif args[2] == COMMAND_INSTALL:
        service_install()
    elif args[2] == COMMAND_REMOVE:
        service_remove()
    else:
        print_help_and_exit_with_error()
else:
    print_help_and_exit_with_error()






