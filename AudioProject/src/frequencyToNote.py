import math

def GetFrequencyNote(frequency):
    
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    note_number = 12 * math.log2(frequency / 440) + 49  
    note_number = round(note_number)
    
    note = (note_number - 1 ) % len(notes)
    note = notes[note]
    
    octave = (note_number + 8 ) // len(notes)
    print(note,octave)
    return note, octave

def TuneFrequencyToNote(note):
    noteFreqChart ={'A':27.50, 'A#':29.14, 'B':30.87, 'C':16.35, 'C#':17.32, 'D':18.35, 'D#':19.45, 'E':20.60, 'F':21.83, 'F#':23.12, 'G':24.50, 'G#':25.96}
    i = noteFreqChart[note[0]]
    for j in range(note[1]):
        i=i*2
    return i
    
