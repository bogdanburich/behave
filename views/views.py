posts = []


def add_post(post_data):
    posts.append(post_data)

def profile():
    return {"posts": posts}

def login(*args, **kwargs):
    '''Here would be login implementation'''
    pass
