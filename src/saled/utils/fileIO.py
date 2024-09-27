from pydub import AudioSegment
import numpy as np
import hashlib
import json
from pathlib import Path

def cache(FILE):

    #with open('./.cached/ledger.json', 'w') as fp:
        #json.dump()
    #    pass
    pass


def check_cache(FILE):
    # Check if ledger exists, if not, create and cache to it.
    if not Path('./.cached/ledger.json').is_file():
        with open('./.cached/ledger.json', 'w') as file:
            file.write("")
            file.close()
        cache(FILE)

    BUF_SIZE = 65536
    md5 =  hashlib.md5()
    sha1 = hashlib.sha1()

    with open(FILE, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)

    key_md5 = md5.hexdigest()
    key_sha1 = sha1.hexdigest()

    # Check ledger
    # Use a dictionary with hash as the key, filename as value.
    # Compare two hashes to avoid non-unique hashes.
    fp = open('./.cached/ledger.json', 'r')
    hashes = json.load(fp)

    try:
        md5_file_name = hashes[key_md5]
        sha1_file_name = hashes[key_sha1]
    except KeyError:
        fp.close()
        cache(FILE)

    if md5_file_name != sha1_file_name:
        fp.close()
        cache(FILE)

    fp.close()


def load_audio(FILE):
    name_components = FILE.split('.')
    extension = name_components[-1]

    match extension:
        case 'mp3':
            raw_audio = AudioSegment.from_mp3(FILE)
        case 'wav':
            raw_audio = AudioSegment.from_wav(FILE)
        case _:
            raise TypeError("Unsupported file format. Please use only WAV or MP3.")
    sample_array = raw_audio.set_channels(1).get_array_of_samples()
    sample_array = np.array(sample_array, dtype=np.float16)
    cache(FILE)
    return sample_array


def load_transcription(FILE):
    """TODO"""
    pass