import os
import django


#os.environ.setdefault("DJANGO_SETTING_MODULE","C:/Users/SUMIT/Desktop/FullThrottle/FTL/Project/FTLproject/FTLproject/settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'FTLproject.settings'
django.setup()


from FTLapp.models import Activity_period,Members

from faker import Faker

fakeObj=Faker()


def call(N=10):
    num = 1
    for i in range(N):
        name = fakeObj.name()
        ads = fakeObj.address()
        start=fakeObj.date_time(tzinfo=None, end_datetime=None)
        end=fakeObj.date_time(tzinfo=None, end_datetime=None)
        members_obj = Members.objects.get_or_create(real_name=name, address=ads)[0]
        activity_obj = Activity_period.objects.get_or_create(member_id=members_obj,start_time=start,end_time=end)[0]
        num+=1

if __name__ == '__main__':
    print("Filling random data")
    call(10)
    print("Filling done ")

