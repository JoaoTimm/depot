import os

SERVER_HOST = "0.0.0.0"
SERVER_POST = 8000

# Define the application directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# The database URI that should be used for the connection.
# Example: SQLALCHEMY_DATABASE_URI = "dialect+driver://username:password@host:port/database"
# For further information, 
# See http://pythonhosted.org//Flask-SQLAlchemy/config.html#connection-uri-format
# Default value is sqlite:////current/directory/depot.db
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'depot.db')

# SQLALCHEMY_ECHO = True

# Upload destination setting
UPLOAD_BASE_DIR = os.path.join(BASE_DIR, "/storage/")

# This must be located under UPLOAD_BASE_DIR and must not starts with slash.
UPLOAD_DIRECTORY = "depot"

# Statement for enabling the development environment
DEBUG = True

SECRET_KEY = os.urandom(30)

############################################################################
##### ENSURE THIS VARIABLE IS SET TO FALSE AFTER CREATING NEEDED USERS #####
############################################################################

ENABLE_SIGNUP = True

################################### API ####################################

# Option for API functions for third-party client.
## Default value is True
ENABLE_API = True

# Option for remote browser.
# Set to False if you don't want uploader to browse your local directories.
# Browser API only returns directories and files in UPLOAD_BASE_DIR.
### Default value is False
ENABLE_REMOTE_BROWSER = False

# Option for group zipping.
# Compression might slow down your server; set ENABLE_ZIP to False to disable
# zipping feature or set ZIP_METHOD to zipfile.ZIP_STORED to just 
# gather - not compressing - files into one zip file.
### Default values are: 
##### ENABLE_ZIP = False
##### ZIP_METHOD = zipfile.ZIP_DEFLATED
import zipfile
ENABLE_ZIP = False
# ZIP_STORED or ZIP_DEFLATED
ZIP_METHOD = zipfile.ZIP_DEFLATED

############################# Transport Method #############################

# RECOMMENDED: Set to True if you usually deal with large files.
# XSendFile allows application to serve files more efficiently by
# sending only path to httpd, then httpd reads directly from the given path and
# sends it to client.
HTTPD_USE_X_SENDFILE = False
HTTPD_TYPE = "nginx"

# Set base directory if you use nginx for proxy.
HTTPD_BASE_DIR = "/"

################################ GeoIP ####################################

ENABLE_GEOIP = False

GEOIP_DATABASE_PATH = "/path/to/geoip2/database"

############################################################################
###################### DO NOT TOUCH BELOW THIS LINE ########################
############################################################################

UPLOAD_FULL_DIRECTORY = os.path.join(UPLOAD_BASE_DIR, UPLOAD_DIRECTORY)


