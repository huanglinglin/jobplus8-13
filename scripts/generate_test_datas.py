import os
import json
from random import randint
from faker import Faker
from jobplus.models import db,User,Job,CompanyDetail

fake = Faker()

def iter_users():
    yield User(
            username='小可爱',
            email='1320816@qq.com',
            password='shiyanlou',
            role = 20
            )

def iter_jobs():
    company = User.query.filter_by(email='1320816@qq.com').first()
    with open(os.path.join(os.path.dirname(__file__),'datas','job.json'))as f:
        jobs = json.load(f)

    for job in jobs:
        yield Job(
                name=job['name'],
                salary_low=job['salary_low'],
                salary_high=job['salary_high'],
                experience_requirement=job['experience_requirement'],
                degree_requirement=job['degree_requirement'],
                company=company

                )

def run():
    for user in iter_users():
        db.session.add(user)

    for job in iter_jobs():
        db.session.add(job)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
