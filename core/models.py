# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class ContactDetails(models.Model):
    # abstractclass
    telephone = models.TextField()
    street_address = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        # create the contractor on save so we don't have orphaned contact details.
        if not self.contractor:
            Contractor(contact=self).save()

            self.image_small = SimpleUploadedFile(name, small_pic)
        super(Model, self).save(*args, **kwargs)


class Skill(models.Model):
    description = models.TextField()
    skill_code = models.CharField(max_length=30)


class ContractorContactDetails(ContactDetails):
    field = models.TextField()
    name = models.TextField()
    def __str__(self):
        return '{} {}'.format(
            self.name,
            self.town
        )

class HirerContactDetails(ContactDetails):
    invoice_contact = models.EmailField()


RATE_CHOICES = (
    (1, 'Hourly'),
    (2, 'Daily'),
    (3, 'Weekly'),
    (4, '4 Weekly'),
    (5, 'Monthly'),
    (6, 'Annually')
)


class Role(models.Model):
    title = models.TextField(default='')
    rate = models.DecimalField(
        default='0.00',
        decimal_places=2,
        max_digits=8
        )
    rate_type = models.IntegerField(choices=RATE_CHOICES)
    skills = models.ManyToManyField(Skill)


class Contractor(models.Model):
    contact = models.OneToOneField(ContractorContactDetails, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    cscs_card_number = models.IntegerField(default=0000)
    cscs_card_url = models.URLField(null=True)  # upload to S3

    def skill_match(self):
        return Role.objects.filter(role__skills__in=self.skills)

    def location_match(self):
        return Role.objects.filter(role__location__in=self.skills)


class Location(models.Model):
    # Job location
    description = models.TextField(default='')
    postcode = models.TextField(max_length=9, default='XX99 XX99')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Hirer(models.Model):
    company_name = models.CharField(max_length=30)
    company_number = models.IntegerField(blank=True, null=True)


class Agreement(models.Model):
    date = models.DateField()
    company = models.ForeignKey(Hirer, on_delete=models.CASCADE)
    pdf_agreement = models.URLField()  # upload to S3
    rate = models.IntegerField()

# Hirers have many roles
# Candidates have many skills

# Candidate search page (show me candidates in this location, with this skills set)
# Role search (show me roles in this location, with this skills set)
