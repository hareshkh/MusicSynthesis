import pretty_midi
import hashlib

piano_c_chord = pretty_midi.PrettyMIDI()
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)

input_string = raw_input("Type a string to convert to music: \n")

hash_object = hashlib.sha256(input_string)
string = hash_object.hexdigest()

def get_note_from_char(x):
	if (x == '0'):
		return 'C5'
	elif (x == '1'):
		return 'C#5'
	elif (x == '2'):
		return 'D5'
	elif (x == '3'):
		return 'D#5'
	elif (x == '4'):
		return 'E5'
	elif (x == '5'):
		return 'F5'
	elif (x == '6'):
		return 'F#5'
	elif (x == '7'):
		return 'G5'
	elif (x == '8'):
		return 'G#5'
	elif (x == '9'):
		return 'A5'
	elif (x == 'a'):
		return 'A#5'
	elif (x == 'b'):
		return 'B5'
	elif (x == 'c'):
		return 'C6'
	elif (x == 'd'):
		return 'C#6'
	elif (x == 'e'):
		return 'D6'
	elif (x == 'f'):
		return 'D#6'

i=0
for c in string:
	note_name = get_note_from_char(c)
	note_number = pretty_midi.note_name_to_number(note_name)
	note = pretty_midi.Note(velocity=100, pitch=note_number, start = i, end = i + 0.3)
	piano.notes.append(note)
	i = i + 0.5

piano_c_chord.instruments.append(piano)

piano_c_chord.write(input_string+'.mid')