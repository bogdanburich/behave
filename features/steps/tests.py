from behave import *
from views.views import add_post, login, profile

@Given('logged user and "{posts_num:d}" post written by user')
def step_impl(context, posts_num):
    context.login_data = {
        "user": "username",
        "password": "password"
    }

    context.post_data = {
        "title": "title",
        "text": "text",
        "owner": context.login_data.get('user')
    }

    if login(**context.login_data):
        for _ in range(posts_num):
            add_post(context.post_data)


@When('go to profile page')
def step_impl(context):
    context.profile = profile()

@Then('see my "{posts_num:d}" full post')
def step_impl(context, posts_num):
    posts = context.profile.get('posts')
    assert len(posts) == posts_num
    for p in range(posts_num):
        post = posts[p]
        assert post.get('owner') == context.login_data.get('user')
        assert post.get('title') == context.post_data.get('title')
        assert post.get('text') == context.post_data.get('text')
