import pretty_midi
import hashlib

cello_c_chord = pretty_midi.PrettyMIDI()
cello_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
cello = pretty_midi.Instrument(program=cello_program)

hash_object = hashlib.sha256(b'sdsmdg')
string = hash_object.hexdigest()

def get_note_from_char(x):
	if (x == '0'):
		return 'C4'
	elif (x == '1'):
		return 'C#4'
	elif (x == '2'):
		return 'D4'
	elif (x == '3'):
		return 'D#4'
	elif (x == '4'):
		return 'E4'
	elif (x == '5'):
		return 'F4'
	elif (x == '6'):
		return 'F#4'
	elif (x == '7'):
		return 'G4'
	elif (x == '8'):
		return 'G#4'
	elif (x == '9'):
		return 'A4'
	elif (x == 'a'):
		return 'A#4'
	elif (x == 'b'):
		return 'B4'
	elif (x == 'c'):
		return 'C5'
	elif (x == 'd'):
		return 'C#5'
	elif (x == 'e'):
		return 'D5'
	elif (x == 'f'):
		return 'D#5'

i=0
for c in string:
	note_name = get_note_from_char(c)
	note_number = pretty_midi.note_name_to_number(note_name)
	note = pretty_midi.Note(velocity=100, pitch=note_number, start = i, end = i + 0.4)
	cello.notes.append(note)
	i = i + 0.5

cello_c_chord.instruments.append(cello)

cello_c_chord.write('mdg_music_2.mid')