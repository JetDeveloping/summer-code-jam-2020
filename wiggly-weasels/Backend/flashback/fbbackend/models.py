from django.db import models
from uuid import uuid4
from django.contrib.postgres.fields import ArrayField


class Account(models.Model):  # A model containing user information
    '''

    email: The user's email (which they used to sign up)
    hashed_pass: A Hashed Version of their password, so they can login
    identification: A Randomly Generated Unique ID
    nickname: The user's nickname on the IRC and Forum
    bot: A boolean to indicate whether a user is a bot

    '''
    # Technical Information
    email = models.EmailField(max_length=100)
    hashed_pass = models.CharField(max_length=64)
    identification = models.CharField(max_length=100, default=uuid4().hex)

    # Display
    nickname = models.CharField(max_length=20)
    bot = models.BooleanField(default=False)


class Message(models.Model):
    '''

    writer: the creator of the message
    content: the content within the message

    '''
    writer = models.CharField(max_length=100)  # The ID of the User
    content = models.CharField(max_length=1000)  # The Content
    identification = models.CharField(max_length=100, default=uuid4().hex)

    def __str__(self):  # Returns "content" when using the str() function
        return self.content


class Group(models.Model):
    '''

    creator: creator of the chatroom
    identification: A randomly generated Unique ID
    messages: An array containing an array for each message.
        ar[0] = Creator ID
        ar[1] = Content
    name: The name of group

    '''
    creator = models.CharField(max_length=100)  # The ID of the User
    identification = models.CharField(max_length=100, default=uuid4().hex)
    messages = ArrayField(  # ArrayField Containing Messages
        ArrayField(
            models.CharField(max_length=1000),
            size=2
        )
    )

    name = models.CharField(max_length=20)


class Post(models.Model):
    '''

    creator: The user who posts the thread
    identification: A randomly generated Unique ID
    comments: An array containing an array for each message.
        ar[0] = Commenter ID
        ar[1] = Content
    title: The title of the thread

    '''

    identification = models.CharField(max_length=100, default=uuid4().hex)
    creator = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=35)

    comments = ArrayField(  # ArrayField Containing Messages
        ArrayField(
            models.CharField(max_length=1000),
            size=2
        )
    )