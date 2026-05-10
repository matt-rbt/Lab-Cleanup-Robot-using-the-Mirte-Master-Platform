from enum import IntEnum

class LogType(IntEnum):
    INFO = 1
    WARN = 2
    ERR = 3
    DEBUG = 4

def log(node, msg_type: LogType, msg: str):
    if node is not None:
        match msg_type:
            case LogType.INFO:
                node.get_logger().info(msg)
            case LogType.WARN:
                node.get_logger().warn(msg)
            case LogType.ERR:
                node.get_logger().error(msg)
            case LogType.DEBUG:
                node.get_logger().debug(msg)
            case _:
                node.get_logger().info(msg)
    elif node is None:
        print(msg)