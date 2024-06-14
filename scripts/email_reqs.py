from priority_classes.webmail.webmail import Email
from priority_classes.datahandler.datahandler import Handler
import requests, os

hd = Handler()


def get_files_from_mail():
    mail = Email()
    mail.login_imap()
    mail.select_imap()
    hd.delete_files_folder("downloads/pc")
    hd.delete_files_folder("downloads/pa")
    get_PC_attachments_from_webmail(mail)
    get_PA_attachments_from_webmail(mail)


def get_PC_attachments_from_webmail(mail):

    # ids = mail.get_email_ids_by_sender_mail('daniela.pereira@marfrig.com.br')
    # ids = mail.get_email_ids_by_sender_mail('bot@carvalima.com.br')
    subject = "Base Pendencia Transportador - CARVALIMA TRANSPORTES LTDA - PC"
    # subject = subject.encode('utf-8')
    ids = mail.get_email_ids_by_subject(subject)
    atts = mail.get_attachments_from_email_id(ids[-1], "downloads/pc")


def get_PA_attachments_from_webmail(mail):

    # ids = mail.get_email_ids_by_sender_mail('daniela.pereira@marfrig.com.br')
    # ids = mail.get_email_ids_by_sender_mail('bot@carvalima.com.br')
    subject = "Base Pendencia Transportador - CARVALIMA - PA"
    # subject = subject.encode('utf-8')
    ids = mail.get_email_ids_by_subject(subject)
    atts = mail.get_attachments_from_email_id(ids[-1], "downloads/pa")


# if __name__ == "__main__":
#     get_PC_attachments_from_webmail()
