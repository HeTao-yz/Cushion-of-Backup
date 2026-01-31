from mcdreforged.api.all import *

class Config(Serializable):
    velocity_host:str='127.0.0.1'
    velocity_port:int=25575
    velocity_passwd:str='password'
    lobby_host:str='127.0.0.1'
    lobby_port:int=25575
    lobby_passwd:str='password'
    lobby_server:str='lobby'
    survival_server:str='survival'
    survival_server_start:str='生存服正在启动中...'
    survival_server_startup:str='启动完成！正在将玩家返回至生存服...'
    survival_server_failure:str='生存服崩溃！请反馈至管理员解决。生存服将继续尝试启动。'

_config = None

def initialize_config(server: PluginServerInterface) -> None:
    global _config
    _config = server.load_config_simple(target_class=Config)

def get_config() -> Config:
    """获取配置实例"""
    if _config is None:
        raise RuntimeError(
            "配置未初始化。请确保插件已正确加载"
        )
    return _config

