from tones import SINE_WAVE, TRIANGLE_WAVE
from tones.mixer import Mixer

def _main():
    m = Mixer(44100, 0.5)
    m.create_track(0, SINE_WAVE)
    m.create_track(1, SINE_WAVE)

    m.add_note(0, note='a', octave=4, duration=2.0)

    m.add_note(0, note='a', octave=4, duration=0.125, endnote='e', endoctave=4)
    m.add_note(0, note='e', octave=4, duration=(2-0.125))

    m.add_note(0, note='e', octave=4, duration=0.125, endnote='c', endoctave=5)
    m.add_note(0, note='c', octave=5, duration=(2-0.125))

    m.add_note(0, note='c', octave=5, duration=0.125, endnote='b', endoctave=4)
    m.add_note(0, note='b', octave=4, duration=(2-0.125))
    
    m.add_note(0, note='b', octave=4, duration=0.125, endnote='d', endoctave=5)
    m.add_note(0, note='d', octave=5, duration=(2-0.125))

    m.add_note(0, note='d', octave=5, duration=0.125, endnote='c', endoctave=5)
    m.add_note(0, note='c', octave=5, duration=(2-0.125))

    m.add_note(0, note='c', octave=5, duration=0.125, endnote='b', endoctave=4)
    m.add_note(0, note='b', octave=4, duration=(2-0.125))
    
    m.add_note(0, note='b', octave=4, duration=0.125, endnote='c', endoctave=5)
    m.add_note(0, note='c', octave=5, duration=(1-0.125))

    m.add_note(0, note='c', octave=5, duration=0.125, endnote='b', endoctave=4)
    m.add_note(0, note='b', octave=4, duration=(2-0.125), vibrato_frequency=.50, vibrato_variance=10, decay=1.0)

    m.add_note(1, note='c', octave=5, duration=1.0)

    m.add_note(1, note='c', octave=5, duration=0.125, endnote='a', endoctave=4)
    m.add_note(1, note='a', octave=4, duration=(2-0.125))

    m.add_note(1, note='a', octave=4, duration=0.125, endnote='c', endoctave=5)
    m.add_note(1, note='c', octave=5, duration=(1-0.125))

    m.add_note(1, note='c', octave=5, duration=0.125, endnote='d', endoctave=5)
    m.add_note(1, note='d', octave=5, duration=(1-0.125))

    m.add_note(1, note='d', octave=5, duration=0.125, endnote='c', endoctave=5)
    m.add_note(1, note='c', octave=5, duration=(1-0.125))

    m.add_note(1, note='c', octave=5, duration=0.125, endnote='e', endoctave=5)
    m.add_note(1, note='e', octave=5, duration=(1-0.125))

    m.add_note(1, note='e', octave=5, duration=0.125, endnote='a', endoctave=4)
    m.add_note(1, note='a', octave=4, duration=(1-0.125))

    m.add_note(1, note='a', octave=4, duration=0.125, endnote='b', endoctave=4)
    m.add_note(1, note='b', octave=4, duration=(1-0.125))

    m.add_note(1, note='b', octave=4, duration=0.125, endnote='e', endoctave=5)
    m.add_note(1, note='e', octave=5, duration=(2-0.125))

    m.add_note(1, note='e', octave=5, duration=0.125, endnote='f', endoctave=5)
    m.add_note(1, note='f', octave=5, duration=(1-0.125))

    m.add_note(1, note='f', octave=5, duration=0.125, endnote='e', endoctave=5)
    m.add_note(1, note='e', octave=5, duration=(1-0.125))

    m.add_note(1, note='e', octave=5, duration=0.125, endnote='c', endoctave=5)
    m.add_note(1, note='c', octave=5, duration=(1-0.125))

    m.add_note(1, note='c', octave=5, duration=0.125, endnote='d', endoctave=5)
    m.add_note(1, note='d', octave=5, duration=(1-0.125))

    m.add_note(1, note='d', octave=5, duration=0.125, endnote='b', endoctave=4)
    m.add_note(1, note='b', octave=4, duration=(1-0.125), decay=2.0)

    m.write_wav('song.wav')

if __name__ == "__main__":
    _main()