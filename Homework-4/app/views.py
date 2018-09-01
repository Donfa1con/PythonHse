from app import app
from flask import render_template, flash, redirect
from .forms import IdForm
from .check_vk_online import check_friends

@app.context_processor 
def inject_enumerate(): 
	return dict(enumerate=enumerate) 

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = IdForm()
    
    list_of_friends = check_friends(form.user_id.data)
    
    return render_template("index.html",
                            form=form,
                            check_friends=check_friends,
                            list_of_friends=list_of_friends)
