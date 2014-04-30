import os

try:
    import local_settings
except ImportError:
    local_settings = object()



########################
# Django dependencies
########################

INSTALLED_APPS = (
    "fle_utils.django_utils",  # templatetags
    "securesync",  # for querying data
    "kalite.i18n",  # video info
    "kalite.main",  # timeline of *Log syncing
    "kalite.topic_tools",  # for video stats, need to map youtube_id to video_id
    "centralserver.i18n",  # for redirecting to resource paths
)


#######################
# Set module settings
#######################

STATS_DATA_PATH = ROOT_DATA_PATH #os.path.join(os.path.dirname(__file__), "data")
INSTALLER_BASE_URL = getattr(local_settings, 'INSTALLER_BASE_URL', 'https://www.dropbox.com/s/cy3aznnt25xv0xl/')
INSTALLER_BASE_URL += (INSTALLER_BASE_URL[-1] != '/' and '/') or ''  # make sure there's a trailing slash.
