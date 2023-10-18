from uuid import uuid4

from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import DomainManager, LanguageManager


def get_extension(filename):
    extension = search(r'.*(\..*)$', filename)

    if extension:
        extension = extension.group(1)

    return extension


def random_path(instance, filename):
    if type(instance) == User:
        user_id = instance.id
    else:
        user_id = instance.user.id
    return f'{user_id}/{uuid4().hex}{get_extension(filename)}'


class Domain(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(verbose_name=_("name"), max_length=150, unique=True)

    objects = DomainManager()

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return self.name


class Language(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    code = models.CharField(max_length=2, unique=True, verbose_name=_("code"))
    name_language = models.CharField(max_length=30, verbose_name=_("natural name"))
    name_english = models.CharField(max_length=30, verbose_name=_("english name"))

    objects = LanguageManager()

    def natural_key(self):
        return (self.code,)

    def __str__(self):
        return self.name_english


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    domains = models.ManyToManyField(Domain, verbose_name=_("domains"), related_name="users")
    languages = models.ManyToManyField(Language, verbose_name=_("spoken languages"), related_name="users")

    def natural_key(self):
        return (self.username,)

    def __str__(self):
        if self.last_name and self.first_name:
            return f"{self.last_name}, {self.first_name}"
        return self.username


class Paper(models.Model):
    class PaperStatus(models.TextChoices):
        SUBMITTED = "SUBMITTED", _("Submitted")
        REVIEW_PENDING = "REVIEW_PENDING", _("Awaiting reviews")
        APPROVED = "APPROVED", _("Approved")
        REJECTED = "REJECTED", _("Rejected")

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.TextField(verbose_name=_("paper title"), unique=True)
    filename = models.CharField(max_length=128)
    file = models.FileField(upload_to=random_path)
    domains = models.ManyToManyField(Domain, related_name='papers', verbose_name=_("domain"))
    language = models.ForeignKey(Language, related_name='papers', on_delete=models.CASCADE, verbose_name=_("language"))
    keywords = models.TextField(verbose_name=_("keywords"), null=True, blank=True)
    authors = models.ManyToManyField(
        User,
        related_name='papers',
        verbose_name=_("authors")
        # TODO: migrations do not work with following line returning:
        # django.db.utils.OperationalError: no such table: auth_group
        #
        # limit_choices_to={"groups": Group.objects.get(name="authors")}
    )
    date_submitted = models.DateField(editable=False, auto_created=True, verbose_name=_("submission date"))
    date_approved = models.DateField(null=True, editable=False, verbose_name=_("approved date"))
    status = models.CharField(
        choices=PaperStatus.choices,
        default=PaperStatus.SUBMITTED,
        max_length=20,
        verbose_name=_("paper status")
    )

    def natural_key(self):
        return (self.title,)

    def __str__(self):
        return self.title[:50]


class Review(models.Model):
    class ReviewStatus(models.TextChoices):
        REQUESTED = "REQUESTED", _("Requested")
        IN_PROGRESS = "IN_PROGRESS", _("In progress")
        CANCELLED = "CANCELLED", _("Cancelled")
        DONE = "DONE", _("Done")

    class ReviewResult(models.TextChoices):
        APPROVED = "APPROVED", _("Approved")
        REJECTED = "REJECTED", _("Rejected")

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, verbose_name=_("paper"), related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("reviewer"), related_name="reviews")
    cancelled_reason = models.CharField(max_length=100, editable=False, null=True, verbose_name=_("cancelled reason"))
    status = models.CharField(
        choices=ReviewStatus.choices,
        default=ReviewStatus.REQUESTED,
        max_length=20,
        verbose_name=_("review status")
    )
    result = models.CharField(
        choices=ReviewResult.choices,
        null=True,
        max_length=20,
        verbose_name=_("review result")
    )
    feedback = models.TextField(verbose_name=_("Reviewer's feedback"))

    def natural_key(self):
        return self.reviewer, self.paper

    def __str__(self):
        "-".join((str(self.reviewer), str(self.paper)))
