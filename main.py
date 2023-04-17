# Zadanie 1
users = {}
filepath = "students1.txt"

with open(filepath) as file_object:
    for line in file_object:
        tymcz = line.split(",")
        user = {"email": tymcz[0], "imie": tymcz[1],
                "nazwisko": tymcz[2], "punkty": tymcz[3],
                "ocena_koncowa": tymcz[4], "status": tymcz[5]}
        email = user["email"]
        users[email] = user

print(users)
# Zadanie 2
POINTS_TO_GRADE = {
    range(0, 51): 2,
    range(51, 61): 3,
    range(61, 71): 3.5,
    range(71, 81): 4,
    range(81, 91): 4.5,
    range(91, 101): 5
}


def przypisz_oceny(studenci):
    for email, data in studenci.items():
        if 'ocena-koncowa' not in data and data.get('status') not in ('GRADED', 'MAILED'):
            points = int(data['punkty'])
            for point_range, grade in POINTS_TO_GRADE.items():
                if points in point_range:
                    data['ocena_koncowa'] = grade


# Zadanie 3

def dodaj_studenta(students, email, imie, nazwisko, punkty, ocena_koncowa=None, status=''):
    if email not in students:
        students[email] = {"imie": imie,
                           "nazwisko": nazwisko, "punkty": float(punkty)}
        if ocena_koncowa is not None:
            students[email]['ocena_koncowa'] = ocena_koncowa
        if status != '':
            students[email]['status'] = status

        return True
    return False


# Zadanie 4

import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Tekst maila')
msg['Subject'] = 'Temat maila'
msg['From'] = 'adres_wysyłającego@mail.com'
msg['To'] = 'adres_odbiorcy@mail.com'

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('adres_wysyłającego@mail.com', 'hasło')
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()
