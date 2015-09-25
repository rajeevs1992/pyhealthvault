import os

#pyHealthVault library and webapp settings - keys, appids, emplates etc
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_DIR+'/webapp' 
)

HV_APPID 	 = '1371d382-d9d4-40fc-8071-8e3b191e2491'
HV_SHELL_URL	 = 'http://sweden-shell.hvmdev502.grcdev.com'

HV_SERVICE_SERVER  = 'platform.hvmdev502.grcdev.com'

APP_ACTION_URL   = 'http://dev18:8000/mvaultaction/'

APP_PUBLIC_KEY = """0xAD8A0F863F5F2746A3E157D8823D69016CFF42AEE1EC9C680FE50B1DAAE06B9668F8956F9C31A8B8E1BC886CE4A33211AE7931E518BF5A9DE3E0C252F4F737EADC6C58E7CAAF538B93A0A849B5913DF6897B70726A55F62B2B2E292B7D1276504D1CCE61B2AC816252502A417754C938DCE106D98C1518281918743783E522ABE335D7929112E90D90F3779603A3D393F9E0234B99B4516AA83AE5A0CF180770CC2E044D6539B1537695929C40EE3DC6A7B6D880EA29212D49BC52E8C730DD783B0245DC029590192C93FB131B594F097285C2BF4380A9DEF33C54841D9F3D4A6FBDB3F823214BB9B69EA914A3582B68D82CB98753C9C25B632027437BC7C4FB
"""
 
APP_PRIVATE_KEY = """0x0d14098579832747989423f5aa230ca5d1dc0edf75214acc40de670f0e50a96b05702e7ae1cf904296a889b3832b955b65c5b66fe8848b44b8e6b85e5e1dbf7610b48da2b250b240239908f5bd1c3c0a3764391e364b522900b112e33722cc0dd331e78fcf5256d1dd18338709823743f4c974a5b27be87d251f05ab256280514a21c70bc161edbd651093d1d0050d59be265046c57b761e7e17016f3a81d6c94f6776c68b10a5f7fbbdf599df1b35c58f8964ee5c03edc2f0defe07f4a961c5c5142eb232cffdf54dbc495a98b556a6596550478c6bcb51bfc6b5d37e77cce1911f89b680ad3ada1d79558d512f7f635e575c27e566eb7b766ded5c222a4671"""

APP_THUMBPRINT = '7528244C44BE4DF989D3003BBC29D323AAF40CC3'

# Django settings for pyHealthVault project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xr--(48l1whu9keemewf@9j(og2i$3+ty9m%&97o6xkw1g$a#d'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'webapp'
)
