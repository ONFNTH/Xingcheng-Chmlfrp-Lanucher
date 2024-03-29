from core.initialize import CheckFile
from core.network import ChmlfrpAPI
from core.module import log
from core.g_var import User
import os

# 启动frp
def start(tun_id):
    log.info(f"token:{User.token} ID:{tun_id} 尝试启动")
    # 检查用户是否拥有该隧道
    data=ChmlfrpAPI.user_tun()
    if CheckFile.CheckFrp() and data[0]==True:
        fash=False
        for da in data[1]:
            if da["id"]==tun_id:
                fash=True
                break
        if fash:
            # 驱动frp核心
            if os.name=="nt":
                os.system("start ./frp/frpc.exe"+" -u "+User.token+" -p "+tun_id)
            else:
                os.system("start ./frp/frpc"+" -u "+User.token+" -p "+tun_id)
            log.info(f"启动frp: token:{User.token} ID:{tun_id} 已拉起")
            return False,"已拉起frp核心"
        else:
            log.warn(f"启动frp: ID:{tun_id} 不属于token:{User.token}")
            return False,f"ID:{tun_id} 不属于你"
    else:
        log.error("启动frp: 未知错误")
        return False,"未知错误"