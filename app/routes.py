from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import UserPrompt
from . import db
import os
import random

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    if 'entry_count' not in session:
        session['entry_count'] = 0

    if request.method == 'POST':
        prompt_content = request.form.get('text_input')

        if prompt_content:
            new_entry = UserPrompt(prompt=prompt_content)
            db.session.add(new_entry)
            db.session.commit()
            session['entry_count'] += 1

        return redirect(url_for('main.home'))

    progress = (session['entry_count'] / 20) * 100  # Percentage for the progress bar

    # Construct an absolute path for the image folder
    image_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static', 'final_goal_images'))

    # Check if the directory exists
    if not os.path.exists(image_folder):
        return "Image directory not found", 500

    # Select a random image for the final goal
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    random_image = random.choice(image_files) if image_files else None

    return render_template('index.html', progress=progress, entries=session['entry_count'], final_image=random_image)
