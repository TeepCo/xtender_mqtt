# Xtender mqtt
This is a program for reading parameters and values from  Studer Innotec's xtender battery inverters  via MQTT. It is basically a wrapper around the [scom library](https://github.com/hesso-valais/scom) that handles the MQTT communication.  


##### Communication schema:

```
 ┌────────────┐   serial
 │ PC with    │   connection   ┌───────────┐
 │ this script├────────────────┤ XCom-232i │
 └─────┬──────┘                └─────┬─────┘
       │                             │
       │                             │
       │                             │
       │                             │
       │                     ┌───────┴────────┐
       │                     │                │
   ┌───┴───┐             ┌───┴───┐        ┌───┴───┐
   │ MQTT  │             │       │        │       │
   │message│             │Xtender│        │Xtender│
   │broker │             │   1   │  ...   │   N   │
   └───────┘             │       │        │       │
                         └───────┘        └───────┘
```

## Warning:
In our setup with 6 xtenders, every few days one of them disconnects unexpectedly. Because of that, the other xtenders start sending
invalid values (e.g. unreasonably high output current), so the script has to be restarted. We use a systemd service that restarts
the script automatically and there is a command provided for this purpose (see below).


# Installation:

You have to install _both_ the system and pip packages. After that run `./xtmq install`.

### Dependencies:

#### Install as system package:
- `curl`
- python 3.9:
- - `python3.9-distutils`
- - `python3.9-dev`
- - `python3-urllib3`
 
#### Install with `pip`:
 - `pipenv` (install system-wide on ensure it is runnable form your shell - eg. `sudo pip install pipenv `)
 - `cython` for python 3.9 (`python3.9 -m pip install Cython`)
 
### Configuration:
It is necessary to provide correct values in the `config/user_config.yaml` file.
After you make the changes, you cant stop tracking the file with 
`git update-index --assume-unchanged config/user_config.yaml` so you don't have conflicts in the future, when you update with `git pull`.

# Usage:
You can test your configuration by running the script directly
with `./xtmq run` - by default it will log to the terminal. After you've verified that everything is working correctly, you can run `./xtmq service install` command, which will install a systemd service that restarts the script upon failure (as explained earlier).

# Removal:
If you only want to remove the service run `./xtmq service rmeove` (or delete the file `/etc/systemd/system/xtender_mqtt.service` manualy).


If you want to uninstall the whole project you can do so by running the command `./xtmq uninstall`, which will stop and remove the service and deletes all the files in the xtender_mqtt directory afterwards.