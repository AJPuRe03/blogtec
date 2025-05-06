from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Post
from app.models import Category

categories_bp = Blueprint ('categories',__name__)

@categories_bp.route('/')
def listar_categorias():
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template('categories/listar_categorias.html', posts=posts, categories=categories)