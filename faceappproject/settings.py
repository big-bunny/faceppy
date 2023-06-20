# Django settings
SECRET_KEY = '@$o70l1i#0_p-+2$k_$ux80lguvknglwb_+@cu*)v#kaa($a$9'
INSTALLED_APPS = [
    # ...
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'faceapp',
     'corsheaders',
    # ...
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
     'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Add your frontend URL here
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['*']

# Root URL configuration
ROOT_URLCONF = 'faceappproject.urls'

# Other settings...
