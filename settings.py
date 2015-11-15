import os

#pyHealthVault library and webapp settings - keys, appids, emplates etc
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_DIR+'/webapp' 
)

HV_APPID 	 = '841f8f25-352d-4cb1-8c36-bdb6dd875b64'
#HV_APPID 	 = '50f5b816-e31c-4670-bc99-b2e4c64ad2b7'
HV_SHELL_URL	 = 'https://account.healthvault-ppe.com'

HV_SERVICE_SERVER  = 'https://platform.healthvault-ppe.com/platform/wildcat.ashx'

APP_ACTION_URL   = 'http://127.0.0.1:8000/mvaultaction/'

APP_PUBLIC_KEY = '0xb02787173236d9883e08a101b3307f7fc8ef950df2de44d282b6ba66d066cb10ac1770a148401fca55523fa26665aa392d96d2a516435e9de14850debf69cd2751d330efc796dae6735c4a8d9b4365e274f74453878d2d4f5ebf609555082f9d98dae8adcfe83bde161e6775bd90b187fd8d19fcfc23ffaabdb6fc64c2bc9e45b5eb49da1da8b0881797ac153a4be3060f0356937fc207cd8431cdd766c785cd6ddac3481c8a461e661890499f725fa42e869cff9b4114eb22293cc436dec6192911c520f4f50fed09475c97eca5b33f64add8e6debf5759a0d81174f48b6c0b323d661d11c4ba7e002127ebbcf29ef1a2793f0db6b9bd3b0cb548808a256cdd'

APP_PRIVATE_KEY = '0x12818492ae46cee19e4abfc772f0c4644352d020f003e3cd0dc86e9ac0881c0b3b59170f0a8d1a09e29eca6aa0414bf9c7cd5181e06de171caaa133ce37515056d76376ce955f2d745054c1bc654f54e2e258ffb0a818d620a3d26c369747bb41dcbd9a7f0f09fe17c0763ad1de6269077d5ac0644e2ef481bb82e99d34f877cf49853e9f005769e6633e27b07619e02b9497226fc49819e8d9df0aa61e3636c068c1e66d6542174e088b78db441567a003dc8813e104b048a47116e00df6978eee1362ab7424b3ff65732de5c46c0b1b1c89a513c09acaff4539bcdaf136457ea7f00795920bd99912d602ff53fcdd84344cfba272e601436452b880b24638d'

APP_THUMBPRINT = '047C6964F1DA4E397277C4E9D29BE9FAB2F2F13C'

# Django settings for pyHealthVault project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db'             # Or path to database file if using sqlite3.
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
