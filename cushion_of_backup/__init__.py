from mcdreforged.api.all import *
from .config import *
from .lobby_rcon import *
from .velocity_rcon import *

def messages(status:str)->str:
    config=get_config()
    MESSAGES = {
        'starting': f'/tellraw @a {{"text":"{config.survival_server_start}","color":"yellow"}}',
        'success': f'/tellraw @a {{"text":"{config.survival_server_startup}","color":"green"}}',
        'failure': f'/tellraw @a {{"text":"{config.survival_server_failure}","color":"red"}}'
    }
    
    return MESSAGES[status]

def on_load(server: PluginServerInterface, prev_module):
    initialize_config(server)
    server.register_event_listener(on_server_start)
    server.register_event_listener(on_server_startup)
    server.register_event_listener(on_server_stop)

def on_server_start(server: PluginServerInterface):
    send_rcon_command(server, messages('starting'))

def on_server_startup(server: PluginServerInterface):
    send_rcon_command(server, messages('success'))
    send_player()
    
def on_server_stop(server: PluginServerInterface, server_return_code: int):
    if server_return_code != 0:
        send_rcon_command(server,messages('failure'))       
        