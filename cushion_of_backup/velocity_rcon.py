from rcon.source import Client
from .config import *
from time import sleep

def vc_rcon_send_command(command:str) -> str:
    """发送RCON命令到Velocity服务器"""
    config = get_config()
    with Client(config.velocity_host, config.velocity_port, passwd=config.velocity_passwd) as client:
        return client.run(command=command)
        
def get_lobby_player() -> list:
    """获取大厅服务器玩家列表"""
    config = get_config()
    response = vc_rcon_send_command('glist all')
    start = response.find(f'[{config.lobby_server}]')
    over = response[start:].find('\n')
    player_line = response[start:start+over][response[start:start+over].find(': ')+2:]
    player_list = player_line.split(', ')
    return player_list

def send_player():
    """
    将玩家自动转发到指定的服务器
    """
    config = get_config()
    player_list = get_lobby_player()
    for player in player_list:
        vc_rcon_send_command(f'send {player} {config.survival_server}')


