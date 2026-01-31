from mcdreforged.api.all import *
from .config import *

def send_rcon_command(server: PluginServerInterface, command: str) -> bool:
    """
    通过RCON发送命令到大厅服务器
    """
    config=get_config()
    RCON_ADDRESS = config.lobby_host
    RCON_PORT = config.lobby_port
    RCON_PASSWORD = config.lobby_passwd
    try:
        rcon = RconConnection(RCON_ADDRESS, RCON_PORT, RCON_PASSWORD)
        if rcon.connect():
            result = rcon.send_command(command)
            return True
        else:
            server.logger.error('无法连接到目标服务器')
            return False
    except Exception as e:
        server.logger.error(f'发送RCON命令时出错: {e}')
        return False
    finally:
        if 'rcon' in locals():
            rcon.disconnect()
