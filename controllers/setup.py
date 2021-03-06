# -*- coding: utf-8 -*-

# TODO: Check security

def install(x):
    from config import Config
    config = Config(autogetconfig=False)
    config.set_default_config()
    config.get_config(expire=0)
    #at = ['db', 'auth', 'mail', 'crud', 'theme']
    #return dict(message=[config.__getattribute__(item) for item in at])
    return config.theme.name


def getlist(x):
    from config import Config
    config = Config()
    return str(config.get_list('auth', 'privacy'))


def test(x):
    from config import Config
    config = Config()
    return config.mail.sender


def reload(x):
    from config import Config
    config = Config(autogetconfig=False)
    config.get_config(expire=0)
    return getattr(config, request.args(0) or "auth")
