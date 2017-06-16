import wave
import subprocess
from io_parser import IOParser
from tempfile import NamedTemporaryFile
import cv2
import numpy as np


class SpectrogramGenerator(object):
    def __init__(self, input_file, duration):
        self._wav = wave.open(input_file, 'rb')
        self.temp_wav = NamedTemporaryFile('wb', suffix='.wav')
        self.temp_img = NamedTemporaryFile('wb', suffix='.png')
        self.current_frame = 0
        self.duration = duration

    def generate_spectrogram(self, wav_data):
        wav_writer = self.create_wav_writer()
        wav_writer.writeframes(wav_data)
        cmd = ['sox', '-t', 'wav', self.temp_wav.name, '-n', 'spectrogram', '-r', '-o', self.temp_img.name]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result, error = process.communicate()
        if not error:
            try:
                frame = cv2.imread(self.temp_img.name)
                wav_writer.close()
                self.create_new_temp_files()
                return frame
            except cv2.error as error:
                print(error)
        else:
            print(error)
            raise StopIteration

    def create_new_temp_files(self):
        self.temp_wav.close()
        self.temp_img.close()
        self.temp_wav = NamedTemporaryFile('wb', suffix='wav')
        self.temp_img = NamedTemporaryFile('wb', suffix='png')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            total_frames = self._wav.getnframes()
            framerate = self._wav.getframerate()
            while self.current_frame < total_frames:
                new_frame = self.current_frame + (framerate * self.duration)
                wav_data = self._wav.readframes(framerate * self.duration)
                spec = self.generate_spectrogram(wav_data)
                if type(spec) is np.ndarray:
                    self.current_frame = new_frame
                    return spec
                else:
                    raise StopIteration
            raise StopIteration
        except OSError as error:
            print(error)
            raise StopIteration

    def create_wav_writer(self):
        wav_writer = wave.open(self.temp_wav, 'wb')
        wav_writer.setparams(self._wav.getparams())
        return wav_writer


if __name__ == '__main__':
    parser = IOParser()
    sg = SpectrogramGenerator(parser.input_file, 4)
    for spec in sg:
        print(spec.shape)
