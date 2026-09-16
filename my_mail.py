import os
from flask_mail import Mail

MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.qq.com")
MAIL_PORT = int(os.getenv("MAIL_PORT", "465"))
MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "false").lower() == "true"
MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "true").lower() == "true"
MAIL_DEBUG = os.getenv("MAIL_DEBUG", "false").lower() == "true"
MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", MAIL_USERNAME)

mail = Mail()
