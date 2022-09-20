import csv
import os
from django.core.management.base import BaseCommand
from reviews.models import (Category, Genre, User, Title,
                            GenreTitle, Review, Comments)
from api_yamdb.settings import BASE_DIR


CSV_ROOT = os.path.join(BASE_DIR, 'data')


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(CSV_ROOT + '/users.csv', encoding='utf-8') as csvfile:
            user = csv.reader(csvfile)
            for row in user:
                User.objects.get_or_create(
                    pk=row[0],
                    username=row[1],
                    email=row[2],
                    role=row[3].upper()
                )
                self.stdout.write(
                    self.style.SUCCESS('User fixture loaded!')
                )
        with open(CSV_ROOT + '/category.csv', encoding='utf-8') as csvfile:
            category = csv.reader(csvfile)
            for row in category:
                Category.objects.get_or_create(
                    name=row[1],
                    slug=row[2]
                )
                self.stdout.write(
                    self.style.SUCCESS('Category fixture loaded!')
                )
        with open(CSV_ROOT + '/genre.csv', encoding='utf-8') as csvfile:
            genre = csv.reader(csvfile)
            for row in genre:
                Genre.objects.get_or_create(
                    name=row[1],
                    slug=row[2]
                )
                self.stdout.write(
                    self.style.SUCCESS('Genre fixture loaded!')
                )
        with open(CSV_ROOT + '/titles.csv', encoding='utf-8') as csvfile:
            title = csv.reader(csvfile)
            for row in title:
                Title.objects.get_or_create(
                    name=row[1],
                    year=row[2],
                    category=Category.objects.get(pk=row[3])
                )
                self.stdout.write(
                    self.style.SUCCESS('Titles fixture loaded!')
                )
        with open(CSV_ROOT + '/genre_title.csv', encoding='utf-8') as csvfile:
            genre_title = csv.reader(csvfile)
            for row in genre_title:
                GenreTitle.objects.get_or_create(
                    title=Title.objects.get(pk=row[1]),
                    genre=Genre.objects.get(pk=row[2])
                )
                self.stdout.write(
                    self.style.SUCCESS('Genre-titles fixture loaded!')
                )
        with open(CSV_ROOT + '/review.csv', encoding='utf-8') as csvfile:
            review = csv.reader(csvfile)
            for row in review:
                Review.objects.get_or_create(
                    title=Title.objects.get(pk=row[1]),
                    text=row[2],
                    author=User.objects.get(pk=row[3]),
                    score=row[4],
                    pub_date=row[5]
                )
                self.stdout.write(
                    self.style.SUCCESS('Review fixture loaded!')
                )
        with open(CSV_ROOT + '/comments.csv', encoding='utf-8') as csvfile:
            comments = csv.reader(csvfile)
            for row in comments:
                Comments.objects.get_or_create(
                    review=Review.objects.get(pk=row[1]),
                    text=row[2],
                    author=User.objects.get(pk=row[3]),
                    pub_date=row[4]
                )
                self.stdout.write(
                    self.style.SUCCESS('Comments fixture loaded!')
                )
        self.stdout.write(
            self.style.SUCCESS('All data completely loaded!')
        )
