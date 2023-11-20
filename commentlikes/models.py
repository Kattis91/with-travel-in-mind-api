from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment


class CommentLike(models.Model):
    """
    Like model, related to User and Comment
    Enable users to like the comments
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name='commentlikes',
        on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'comment']

    def __str__(self):
        if self.post:
            return f'{self.owner} {self.comment}'
