import datetime
import os

import yagmail

from forcuanteller.main.utils.paths import report_dir


def main(run_id, sender_address, sender_password, receiver_address):
    yag = yagmail.SMTP(sender_address, sender_password)

    filename = "report_{}".format(run_id)
    jpg_filepath = os.path.join(report_dir, filename + ".jpg")

    subject = "Reports for {}".format(datetime.datetime.now().strftime("%Y-%m-%d"))

    yag.send(
        to=receiver_address,
        subject=subject,
        contents=yagmail.inline(jpg_filepath),
    )
