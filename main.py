from time import sleep
from sys import stdout


def main():
    lyrics = [
        'Suki yo Ima anata ni omoi nosete',
        'Hora, sunao ni naru no watashi',
        'Kono saki motto soba ni ite mo ii ka na?',
        'Koi to koi ga kasanatte',

        'Suki yo Ima anata ni omoi todoke',
        'Nee, kizuite kuremasen ka?',
        'Doushiyou mo nai kurai',
        'Kokoro made suki ni natteiku'
    ]
    delays = [0.15, 0.14, 0.15, 0.14, 0.16, 0.18, 0.16, 0.16]
    for i, lyric in enumerate(lyrics):
        char_delay = delays[i]
        for char in lyric:
            stdout.write(char)
            stdout.flush()
            sleep(char_delay)
        print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
