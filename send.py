import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ATTACHMENT_PATH = os.path.join(BASE_DIR, "simple.pdf")
TOKEN_FILE = os.path.join(BASE_DIR, 'token.json')
ATTACHMENT_PATH = "e:\\python_projects\\gmail_app\\simple.pdf"


def send_email_with_attachment():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    msg = MIMEMultipart()
    msg['to'] = "rajesh.dev8096@gmail.com"
    msg['subject'] = "Gmail API – Attachment Test ✅"

    msg.attach(MIMEText("Hi 👋\n\nThis email contains an attachment.\n\n— Python Gmail API", "plain"))

    # Attachment
    with open(ATTACHMENT_PATH, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f'attachment; filename="{os.path.basename(ATTACHMENT_PATH)}"'
    )

    msg.attach(part)

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

    sent = service.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()

    print("✅ Email with attachment sent! ID:", sent["id"])
    print("ATTACHMENT_PATH =", ATTACHMENT_PATH)
    print("Exists?", os.path.exists(ATTACHMENT_PATH))
    print("CWD =", os.getcwd())


if __name__ == "__main__":
    send_email_with_attachment()
