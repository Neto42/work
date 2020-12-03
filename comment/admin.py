from django.contrib import admin

from comment.models import CommentAnswer, CommentQuestion

admin.site.register(CommentQuestion)
admin.site.register(CommentAnswer)
