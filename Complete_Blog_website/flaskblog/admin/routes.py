import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flaskblog import db, mail
from .forms import  SubscriptionForm, AnnouncementForm
from flaskblog.models import NewsletterSubscription
from flask_login import current_user,login_required
from flask_mail import Message
from functools import wraps

admin = Blueprint('admin', __name__)

@admin.route('/subscribe', methods=['GET', 'POST'])
@login_required
def subscribe():
    form = SubscriptionForm()
    if form.validate_on_submit():
        email = form.email.data
        existing_subscription = NewsletterSubscription.query.filter_by(email=email).first()
        if existing_subscription:
            flash('You are already subscribed!', 'info')
        else:
            new_subscription = NewsletterSubscription(email=email)
            db.session.add(new_subscription)
            db.session.commit()
            # Send confirmation email
            msg = Message('News letter Subscription Confirmation from willyblog.com',
                          sender='williamsolaolu5@gmail.com',
                          recipients=[email])
            msg.body = f'Thank you for subscribing to our daily newsletter, {email}! We will alway keep you updated once a new content or post is out'
            mail.send(msg)
            flash('You have successfully subscribed!', 'success')
            return redirect(url_for('subscribe'))
    return render_template('subscribe.html', form=form, title='Newsletter')

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)        
    return decorated_function
def send_announcement_email(subject, body):
    subscribers = NewsletterSubscription.query.all()
    for subscriber in subscribers:
        msg = Message(subject, sender='williamsolaolu5@gmail.com', recipients=[subscriber.email])
        msg.body = body
        mail.send(msg)

@admin.route('/send_announcement', methods=['GET', 'POST'])
@login_required
@admin_only
def send_announcement_view():
    form = AnnouncementForm()
    if form.validate_on_submit():
        subject = form.subject.data
        body = form.body.data
        send_announcement_email(subject, body)
        flash('Announcement sent successfully!', 'success')
        return redirect(url_for('admin.send_announcement_view'))
    return render_template('send_announcement.html', form=form, title='send announcement')

