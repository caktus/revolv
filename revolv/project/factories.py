import datetime

import factory
from revolv.project.models import Project


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    funding_goal = 50.0
    title = "Hello"
    video_url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
    impact_power = 50.5
    location = "Berkeley"
    end_date = datetime.date.today() - datetime.timedelta(days=1)  # tomorrow
    mission_statement = "We do solar!"
    cover_photo = None
    org_start_date = datetime.date.today() + datetime.timedelta(days=1)  # today
    actual_energy = 25.5
    amount_repaid = 29.25
    ambassador = factory.SubFactory("revolv.base.factories.RevolvUserProfileFactory")


class ActiveProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    funding_goal = 50.0
    title = "Hello"
    video_url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
    impact_power = 50.5
    location = "Berkeley"
    end_date = datetime.date.today() - datetime.timedelta(days=1)  # tomorrow
    mission_statement = "We do solar!"
    cover_photo = None
    org_start_date = datetime.date.today() + datetime.timedelta(days=1)  # today
    actual_energy = 25.5
    amount_repaid = 29.25
    ambassador = factory.SubFactory("revolv.base.factories.RevolvUserProfileFactory")
    project_status = Project.ACTIVE


class ProjectFactories(object):
    base = ProjectFactory
    active = ActiveProjectFactory
