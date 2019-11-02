from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from apps.accounts.models import UserProfile, IndividualIdentifier
import random


FIRST_NAME = ["Adam", "Ben", "Colin", "Derek", "Edward", "Fred", "George", "Henry", "Ian", "John", "Kevin",
              "Larry", "Michael", "Norman", "Oliver", "Peter", "Quin", "Roger", "Steven", "Trevor", "Ulrich",
              "Victor", "William", "Xavier", "Yan", "Zen"]

LADY_NAME = ["Avril", "Britney", "Carly", "Denise", "Erica", "Franchesca", "Gabriella", "Henrietta", "Ileen",
             "July", "Karen", "Lisa", "Mellisa", "Nancy", "Ophelia", "Penny", "Quennie", "Rachel", "Sally",
             "Tammy", "Unice", "Veronica", "Wanda", "Xavier", "Yolanda", "Zara"]

LAST_NAME = ["Adamson", "Bell", "Campbell", "Drane", "Edwards", "Fox", "Garrison", "Howard", "Ingle", "Jameson",
             "Kline", "Lamb", "Marks", "North", "Overton", "Pendle", "Queen", "Rogers", "Standish", "Thompson",
             "Underwood", "Vargas", "Winston", "Xander", "Young", "Zoo"]

SEX_CHOICE = ['male', 'female']

SUB_DIVISION = ["AL", "AK",	"AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI",
                "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN",
                "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
                "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                "WV", "WI", "WY"]


class Command(BaseCommand):
    help = 'Create Sample VMI Users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-u', '--userprefix', type=str, help='Define a username prefix')
        parser.add_argument('-p', '--pwdprefix', type=str, help='Define a password prefix')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        userprefix = kwargs['userprefix']
        pwdprefix = kwargs['pwdprefix']

        if userprefix:
            u_p = userprefix
        else:
            u_p = ""

        if pwdprefix:
            p_p = pwdprefix
        else:
            p_p = ""

        for i in range(total):
            mod = i % 2
            if mod > 0:
                sex = SEX_CHOICE[1]
                first = LADY_NAME[random.randrange(25)]
            else:
                sex = SEX_CHOICE[0]
                first = FIRST_NAME[random.randrange(25)]

            i_padded = "{0:07d}".format(i)
            password = p_p + i_padded + "!"
            print(u_p + i_padded, password)

            u = User.objects.create_user(
                username=u_p + i_padded,
                first_name=first,
                last_name=LAST_NAME[random.randrange(25)],
                email=u_p + i_padded + "@" + u_p + ".com"
            )

            u.set_password(password)
            u.is_staff = False
            u.is_superuser = False
            u.is_active = True
            u.save()

            print(u.password)

            profile = UserProfile.objects.create(user=u)
            profile.sex = sex
            profile.save()

            identifier = IndividualIdentifier.objects.create(
                user=u,
                type="PATIENT_ID_FHIR",
                country="US",
                subdivision=random.randrange(50),
                value=i_padded,
                name="%s:%s[PATIENT_ID_FHIR for %s,%s]" % (u_p, i_padded, u.first_name, u.last_name)
            )



