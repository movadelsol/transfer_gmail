import imapclient
import ssl
from icecream import ic
from my_gmail_account import APPLICATION_SPECIFIC_PASSWORD
import pprint
import mailparser
from datetime import datetime
from notify import notify


def check_inbox():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)
    r1 = imap_obj.login("movadelsol", APPLICATION_SPECIFIC_PASSWORD)
    r2 = imap_obj.select_folder("INBOX")

    today_str = datetime.today().strftime("%d-%b-%Y")
    last_str = "06-Aug-2025"
    UIDs = imap_obj.search(["ON", today_str, "FROM", "info@video-research.jp"])
    # ic(UIDs)
    msg = ":nothing\n"
    for uid in UIDs:
        raw_msg = imap_obj.fetch([uid], ["BODY[]"])[uid][b"BODY[]"]
        mail = mailparser.parse_from_bytes(raw_msg)
        notify(mail.text_plain)
        # print(mail.subject)
        # print(mail.from_)
        # print(mail.to)
        # print(mail.text_plain)
        msg = ":received\n"
    imap_obj.logout()
    now = datetime.now().strftime("%Y%m%d%a%H%M")
    with open('up.log','a') as f:
        f.write(now+msg)
    # ic("IMAP connection closed.")
    # for i, _str in enumerate(mail.text_plain):
    #     ic(f"{i}:{_str}")
    # if UIDs:
    #     notify(mail.text_plain)
    # text = "株式会社ビデオリサーチ 新聞広告調査 事務局"
    # notify(text)


if __name__ == "__main__":
    check_inbox()
    ic("Inbox checked.")
