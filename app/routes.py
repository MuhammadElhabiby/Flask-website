from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import UserPrompt
from . import db
import os
import random

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    # Initialize session variables if they don't exist
    if 'entry_count' not in session:
        session['entry_count'] = 0
    if 'prompts' not in session:
        session['prompts'] = []  # Initialize an empty list to store prompts

    if request.method == 'POST':
        prompt_content = request.form.get('text_input')

        if prompt_content:
            # Save the user's prompt to the database
            new_entry = UserPrompt(prompt=prompt_content)
            db.session.add(new_entry)
            db.session.commit()

            # Update session-specific variables
            session['entry_count'] += 1
            session['prompts'].append(prompt_content)  # Add the new prompt to the session list

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

    # Pass session-specific prompts to the template
    return render_template(
        'index.html',
        progress=progress,
        entries=session['entry_count'],
        prompts=session['prompts'],  # Pass the list of prompts to the template
        final_image=random_image
    )
