from music21 import stream, harmony, meter, tempo, key, metadata, instrument, note

# Cria a partitura e adiciona metadados
score = stream.Score()
score.metadata = metadata.Metadata(title="Tempo de Marés", composer="Composição Original")

# ========== Parte de Acordes ==========
chords_part = stream.Part()
chords_part.insert(0, instrument.AcousticGuitar())
chords_part.append(key.Key('C'))
chords_part.append(meter.TimeSignature('4/4'))
chords_part.append(tempo.MetronomeMark(number=72))  # 72 bpm

# Progressão de acordes
chord_symbols = [
    ['Cmaj7', 'Am7', 'Dm7', 'G13'],
    ['Cmaj7', 'Em7', 'Fmaj7', 'G7']
]

# Cria acordes
def create_chord_symbol(symbol, duration=4.0):
    c = harmony.ChordSymbol(symbol)
    c.quarterLength = duration
    return c

# Adiciona acordes
for progression in chord_symbols:
    for sym in progression:
        chords_part.append(create_chord_symbol(sym))

# ========== Parte da Melodia ==========
melody_part = stream.Part()
melody_part.insert(0, instrument.Flute())  # Pode mudar para Piano() se preferir

# Melodia simples para os dois primeiros versos

melody_notes = [
    ('E4', 1), ('G4', 1), ('A4', 1), ('G4', 1),   # "O mar voltou pra areia"
    ('E4', 1), ('D4', 1), ('C4', 1), ('B3', 1),   # "Desenhou teus passos"

    ('C4', 1), ('D4', 1), ('E4', 2),             # "As ondas levaram segredos"
    ('G4', 1), ('F4', 1), ('E4', 1), ('D4', 1)    # "Que guardávamos"
]

# Adiciona notas à melodia
for pitch, dur in melody_notes:
    n = note.Note(pitch)
    n.quarterLength = dur
    melody_part.append(n)

# ========== Junta as Partes ==========
score.append(chords_part)
score.append(melody_part)

# Exporta para MIDI
score.write('midi', fp='Tempo_de_Marés_com_Voz.mid')
