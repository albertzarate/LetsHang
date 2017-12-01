# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("""

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Selection</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2 class="center-align" >Make a selection</h2>
  <a href="#" class="btn btn-info" role="button">I want to eat!</a>
  <a href="#" class="btn btn-info" role="button">I want to study!</a>
  <a href="#" class="btn btn-info" role="button">I want to work-out!</a>
</div>

</body>
</html>









""")
