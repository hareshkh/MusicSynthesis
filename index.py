import pretty_midi
import hashlib
import random

midi = pretty_midi.PrettyMIDI()
instrument_program = pretty_midi.instrument_name_to_program('Music Box')
instrument = pretty_midi.Instrument(program=instrument_program)

input_string = raw_input("Type a string to convert to music: \n")

hash_object = hashlib.sha256(input_string)
string = hash_object.hexdigest()


def get_note_from_int(x):
	if (x == 0):
		return 'C6'
	elif (x == 1):
		return 'C#6'
	elif (x == 2):
		return 'D6'
	elif (x == 3):
		return 'D#6'
	elif (x == 4):
		return 'E6'
	elif (x == 5):
		return 'F6'
	elif (x == 6):
		return 'F#6'
	elif (x == 7):
		return 'G6'
	elif (x == 8):
		return 'G#6'
	elif (x == 9):
		return 'A6'
	elif (x == 10):
		return 'A#6'
	elif (x == 11):
		return 'B6'
	elif (x == 12):
		return 'C7'
	elif (x == 13):
		return 'C#7'
	elif (x == 14):
		return 'D7'
	elif (x == 15):
		return 'D#7'

begin_time = 0
play_time = 0
delay_time = 0
prev_x = -1

for c in string:
	x = int(c,16)
	if(prev_x!=-1):
		for index in range(prev_x + 1,x):
			play_time = 0.05
			delay_time = 0.0
			note_name = get_note_from_int(index)
			note_number = pretty_midi.note_name_to_number(note_name)
			note = pretty_midi.Note(velocity=100, pitch=note_number, start = begin_time, end = begin_time + play_time)
			instrument.notes.append(note)
			begin_time = begin_time + play_time + delay_time

	prev_x = x
	play_time = 0.8
	delay_time = 0.0
	note_name = get_note_from_int(x)
	note_number = pretty_midi.note_name_to_number(note_name)
	note = pretty_midi.Note(velocity=100, pitch=note_number, start = begin_time, end = begin_time + play_time)
	instrument.notes.append(note)
	begin_time = begin_time + play_time + delay_time

midi.instruments.append(instrument)

midi.write(input_string + '.mid')
