import requests
from random import randint
import json
from pprint import pprint
from configparser import ConfigParser

config = ConfigParser()
config.read('bot.ini')

from faker import Faker

fake = Faker()


def test_check_status_code_equals_200():
    base_url = 'http://127.0.0.1:8000/api/v1/'
    response = requests.get(base_url)
    assert response.status_code == 200


def sign_up():
    registration_url = 'http://127.0.0.1:8000/api/v1/rest-auth/registration/'

    random_name = fake.first_name()
    random_email = fake.ascii_free_email()
    random_pass = fake.pystr()

    registration_data = {
        'username': random_name,
        'email': random_email,
        'password1': random_pass,
        'password2': random_pass,
    }
    response = requests.post(url=registration_url, json=registration_data)

    user_token = json.loads(response.text).get('key')
    if not user_token:
        return None
    return random_name, random_pass, random_email, user_token


def post_fake_post(author_id):
    fake = Faker()
    fake_post = fake.paragraph()

    url_post = 'http://127.0.0.1:8000/api/v1/'

    data = {
        'author': author_id,
        'body': fake_post,
    }
    response = requests.post(url=url_post, json=data)
    # print(response)
    return None


def post_like(user_token, author_id, post_to_like):

    url_like = 'http://127.0.0.1:8000/api/v1/likes/'

    data = {
        'author': author_id,
        'post': post_to_like,
    }
    header = {'Authorization': 'Token ' + user_token}

    response = requests.post(url=url_like, json=data, headers=header)
    return None


def post_dislike(user_token, author_id, post_to_like):
    url_dislike = 'http://127.0.0.1:8000/api/v1/dislikes/'

    data = {
        'author': author_id,
        'post': post_to_like,
    }
    header = {'Authorization': 'Token ' + user_token}

    response = requests.post(url=url_dislike, json=data, headers=header)
    return None


def main(**kwargs):
    number_of_users = kwargs.get('number_of_users')
    max_posts_per_user = kwargs.get('max_posts_per_user')
    max_likes_per_user = kwargs.get('max_likes_per_user')
    max_dislikes_per_user = kwargs.get('max_dislikes_per_user')

    users = {}
    for u in range(1, number_of_users+1):
        fake_user = sign_up()
        if fake_user:
            users[u] = fake_user

    for u in users:
        for p in range(1, max_posts_per_user+1):
            post_fake_post(author_id=u)

    for u in users:
        name, passw, email, user_token = users[u]
        for p in range(1, max_likes_per_user+1):
            post_like(
                user_token=user_token,
                author_id=randint(1, number_of_users),
                post_to_like=randint(1, number_of_users)
            )
        for p in range(1, max_dislikes_per_user + 1):
            post_dislike(
                user_token=user_token,
                author_id=randint(1, number_of_users),
                post_to_like=randint(1, number_of_users)
            )
    print(f'Created {len(users)} users with posts and likes, dislikes')
    # pprint(users)
    print('End main')
    return None


if __name__ == '__main__':
    main(
        number_of_users=eval(config['DEFAULT']['number_of_users']),
        max_posts_per_user=eval(config['DEFAULT']['max_posts_per_user']),
        max_likes_per_user=eval(config['DEFAULT']['max_likes_per_user']),
        max_dislikes_per_user=eval(config['DEFAULT']['max_dislikes_per_user']),
    )


