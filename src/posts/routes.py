from flask import render_template, url_for, flash, redirect, request,abort,Blueprint
from src.models import Post
from src.posts.forms import PostForm

posts = Blueprint('posts', __name__) # here we are creating an instance of the blueprint class 