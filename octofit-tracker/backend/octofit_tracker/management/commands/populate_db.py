from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Teams
        teams = [
            {"name": "Marvel", "description": "Team Marvel Superheroes"},
            {"name": "DC", "description": "Team DC Superheroes"}
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"}
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {"user": "spiderman@marvel.com", "activity": "Running", "duration": 30},
            {"user": "ironman@marvel.com", "activity": "Cycling", "duration": 45},
            {"user": "wonderwoman@dc.com", "activity": "Swimming", "duration": 60},
            {"user": "batman@dc.com", "activity": "Yoga", "duration": 40}
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"team": "Marvel", "points": 75},
            {"team": "DC", "points": 100}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"name": "Super Strength", "description": "Strength workout for heroes"},
            {"name": "Agility Training", "description": "Agility and speed drills"}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
