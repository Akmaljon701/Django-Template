from celery import shared_task
import redis


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


@shared_task
def create_person(name, age):
    person = Person(name, age)
    # Ma'lumotlarni Redisga saqlash
    redis_client.hmset(name, {'age': age})
    print("Created", person)


@shared_task
def read_person(name):
    # Redisdan ma'lumotlarni olish
    person_data = redis_client.hgetall(name)
    if person_data:
        return Person(name, int(person_data[b'age'])).name
    else:
        print("Error")


@shared_task
def update_person(name, age):
    # Ma'lumotlarni yangilash
    if read_person(name):
        redis_client.hmset(name, {'age': age})
        return True
    else:
        print("Error")


@shared_task
def delete_person(name):
    # Ma'lumotlarni o'chirish
    if read_person(name):
        redis_client.delete(name)
        print("Deleted")
    else:
        print("Error")

