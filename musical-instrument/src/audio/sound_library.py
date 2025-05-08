def load_sounds(sound_files):
    sounds = {}
    for name, file_path in sound_files.items():
        sounds[name] = pygame.mixer.Sound(file_path)
    return sounds

def get_sound_names():
    return ["note_c", "note_d", "note_e", "note_f", "note_g", "note_a", "note_b"]

def get_sound_file_paths():
    return {
        "note_c": "path/to/note_c.wav",
        "note_d": "path/to/note_d.wav",
        "note_e": "path/to/note_e.wav",
        "note_f": "path/to/note_f.wav",
        "note_g": "path/to/note_g.wav",
        "note_a": "path/to/note_a.wav",
        "note_b": "path/to/note_b.wav"
    }