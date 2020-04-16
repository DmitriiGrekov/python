from converter import Converter
conv = Converter()

info = conv.probe('test.mp4')

convert = conv.convert('test.mp4', 'test.avi', {
    'format': 'avi',
    'audio': {
        'codec': 'aac',
        'samplerate': 11025,
        'channels': 2
    },
    'video': {
        'codec': 'hevc',
        'width': 720,
        'height': 400,
        'fps': 60 
    }})

for timecode in convert:
    print(f'\rConverting ({timecode:.2f}) ...')
