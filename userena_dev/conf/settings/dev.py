# Development environment settings

from userena_dev.conf.settings.default import *

TEMPLATE_LOADERS = (
    # Remove cached template loader
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')
THUMBNAIL_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'cache/') 

DEV = True
DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'CACHE+' + SECRET_KEY
    }
}
