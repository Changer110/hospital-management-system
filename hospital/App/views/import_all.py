

import os
from App.models import *
from dateutil import parser
from App.models.forms import *
from django.conf import settings
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, timedelta
from django.shortcuts import render, redirect


from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from PIL import Image as PILImage
from reportlab.lib.units import inch




def convert_date(value):
    date = parser.parse(value).strftime("%Y-%m-%d")
    return datetime.strptime(date, "%Y-%m-%d").date()

def date_time_now():
    value = timezone.now() + timedelta(hours=2)
    return value