import logging
import logging.config

from config import basedir

logfile_path = basedir

log_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)-15s][%(levelname)s][%(filename)s %(lineno)d %(process)d]: %(message)s",
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '[%(asctime)s][%(levelname)s][%(name)s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': '',
        },
        # 打印到文件的日志,收集info及以上的日志
        # 'default': {
        #     'level': 'DEBUG',
        #     # 'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
        #     # "class": "logging.handlers.TimedRotatingFileHandler",  # 依照时间进行切割
        #     'formatter': 'standard',
        #     # 'filename': logfile_path,  # 日志文件
        #     # 'maxBytes': 1024*1024*5,  # 日志大小 5M
        #     # "when": "h",  # 小时格式
        #     # "interval": 24,  # 24 小时
        #     # 'backupCount': 7,  # 7个
        #     # 'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        # },
    },
    'loggers': {
        'space': {
            'handlers': ['console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
        },
    },
}


class MyLogger(logging.Logger):
    """重写Logger的某些函数，给这些等级的日志输出不同颜色"""

    def info(self, msg, *args, **kwargs):
        """重写info函数"""

        if self.isEnabledFor(20):
            # self._log(20, msg, args, **kwargs)
            self._log(20, "\033[36;1m%s\033[0m" % msg, args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """重写error函数"""

        if self.isEnabledFor(40):
            # self._log(40, msg, args, **kwargs)
            self._log(40, "\033[31;1m%s\033[0m" % msg, args, **kwargs)


logging.setLoggerClass(MyLogger)
logging.config.dictConfig(log_config)
log = logging.getLogger('space')
# log.info("============== log initialized ==============")
