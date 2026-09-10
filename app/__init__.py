import re
import urllib.parse


def is_email_command(command):
    """
    Check whether the user's command is related to Gmail/email.
    """
    if not command:
        return False

    command = command.lower()

    keywords = [
        "email",
        "e-mail",
        "gmail",
        "send mail",
        "send an email",
        "write an email",
        "compose email",
        "compose an email",
        "mail"
    ]

    return any(keyword in command for keyword in keywords)


def extract_email(command):
    """
    Extract an email address from the user's command.
    """
    if not command:
        return ""

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        command
    )

    if match:
        return match.group(0)

    return ""


def create_email_url(subject, body, recipient=""):
    """
    Create a Gmail compose URL.
    """

    params = urllib.parse.urlencode({
        "view": "cm",
        "fs": "1",
        "to": recipient or "",
        "su": subject or "",
        "body": body or ""
    })

    return f"https://mail.google.com/mail/u/0/?{params}"


# Alias used by app/__init__.py
create_gmail_url = create_email_url
