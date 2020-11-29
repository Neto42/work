from django.contrib import admin

from comment.models import CommentAd, CommentOrganization, CommentAnswer, CommentQuestion

admin.site.register(CommentAd)
admin.site.register(CommentOrganization)
admin.site.register(CommentQuestion)
admin.site.register(CommentAnswer)
