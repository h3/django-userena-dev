from userena_dev.conf.settings.default import *

DEBUG = True
DEV = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    },
}

#MIDDLEWARE_CLASSES += MIDDLEWARE_CLASSES + (
#    'debug_toolbar.middleware.DebugToolbarMiddleware', 
#)

#HIDE_DJANGO_SQL = True
#INTERNAL_IPS = ('127.0.0.1',)

#INSTALLED_APPS = INSTALLED_APPS + (
#   'debug_toolbar',
#)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
   #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
   #'HIDE_DJANGO_SQL': True,
   #'ENABLE_STACKTRACES' : True,
}

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static/')

THUMBNAIL_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'cache/') 
THUMBNAIL_MEDIA_URL = '/media/cache/'
