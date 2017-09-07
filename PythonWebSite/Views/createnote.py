from flask import Blueprint, render_template, request, redirect
import random

bp = Blueprint(__name__, __name__,
                        template_folder='Templates')

def random_string(length=16):
	final_string=''
	chars='abcdefghijklmnopqrstuvwxyz0123456789'

	for i in range(0, length):
		final_string += chars[random.randint(0, len(chars)-1)]
	return final_string;

@bp.route('/createnote', methods=['POST', 'GET'])

def show():
	if request.method == 'POST':
		if request.form.get('createnote'):
			text = request.form.get('notetext').encode('utf-8');

			with open('PythonWebSite/notes/{}.txt'.format(random_string()), 'w' ) as file:
				file.write(text);
			file.close();
			return redirect('/')

	return render_template('createnote.html')