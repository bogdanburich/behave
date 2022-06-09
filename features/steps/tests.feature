Feature: Logged user see his post
  In order to use a blog and see what I wrote
  As a logged user wrote posts
  I want to see posts that was written by me

  Scenario:
    Given logged user and "1" post written by user
    When go to profile page
    Then see my "1" full post