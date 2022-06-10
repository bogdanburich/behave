posts = []


def add_post(post_data):
    posts.append(post_data)


def profile():
    return {"posts": posts}


def login(*args, **kwargs):
    user = kwargs.get('user')
    password = kwargs.get('password')
    return user and password
