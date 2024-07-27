try:
    from .plugin import SetHoleDiameterPlugin
    plugin = SetHoleDiameterPlugin()
    plugin.register()
except Exception as e:
    import logging
    root = logging.getLogger()
    root.debug(repr(e))