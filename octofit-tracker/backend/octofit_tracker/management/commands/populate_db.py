from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        teams = [
            {"name": "Marvel", "members": ["Iron Man", "Captain America", "Thor", "Hulk"]},
            {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman", "Flash"]}
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Thor", "email": "thor@marvel.com", "team": "Marvel"},
            {"name": "Hulk", "email": "hulk@marvel.com", "team": "Marvel"},
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Flash", "email": "flash@dc.com", "team": "DC"}
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Activities
        activities = [
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Batman", "activity": "Cycling", "duration": 45},
            {"user": "Wonder Woman", "activity": "Swimming", "duration": 60}
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"team": "Marvel", "points": 120},
            {"team": "DC", "points": 110}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"user": "Thor", "workout": "Strength", "reps": 100},
            {"user": "Flash", "workout": "Speed", "reps": 200}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
