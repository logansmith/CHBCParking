from flask import Blueprint, render_template, request, redirect
import glob, random


bp = Blueprint(__name__, __name__,
                        template_folder='Templates')

def fetch_notes():
	final_notes = []
	notes= glob.glob('PythonWebSite/notes/*.txt')

	for note in notes:
		with open(note) as file:
			#final_notes.append(file.read().replace('\n', '</br> \n'))
			spot = make_parkingspot(file.readline(), file.readline(), file.readline());
			final_notes.append(spot)
		file.close();
	return final_notes;

class ParkingSpot(object):
    lnum = ""
    pnum = ""
    spotnum = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, spotnum, lnum, pnum):
        self.spotnum = spotnum
        self.lnum = lnum
        self.pnum = pnum

def make_parkingspot(spotnum, lnum, pnum):
    parkingspot = ParkingSpot(spotnum, lnum, pnum)
    return parkingspot



def random_string(length=16):
	final_string=''
	chars='abcdefghijklmnopqrstuvwxyz0123456789'

	for i in range(0, length):
		final_string += chars[random.randint(0, len(chars)-1)]
	return final_string;

def get_file_id(id):
	file_id = ''
	print('id: ',str(id))
	notes= glob.glob('PythonWebSite/notes/*.txt')
	for note in notes:
		with open(note) as file:
			test = file.readline(2);
			print('test:',test)
			if test==id:
				print('in the if state:')
				file_id= note
		file.close();
		print('filid',file_id)
	return file_id


@bp.route('/', methods=['POST', 'GET'])
def show():
	if request.method == 'POST':
		if request.form.get('createnote'):
			text1 = request.form.get('notetext').encode('utf-8');
			text2 = request.form.get('phonenumber').encode('utf-8');
			text3 = request.form.get('parkingid').encode('utf-8');
			if get_file_id(text3):
				with open('{}'.format(get_file_id(text3)), 'w' ) as file:
					file.truncate();
					file.write(text3);
					file.write('\n');
					file.write(text1);
					file.write('\n');
					file.write(text2);
				file.close();
				return redirect('/')
			else:
				with open('PythonWebSite/notes/{}.txt'.format(random_string()), 'w' ) as file:
					file.write(text3);
					file.write('\n');
					file.write(text1);
					file.write('\n');
					file.write(text2);
				file.close();
				return redirect('/')
	if request.method=='GET':
		id = request.form.get('parkingid');
		return render_template('index.html', notes=fetch_notes());