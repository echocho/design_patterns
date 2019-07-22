class Amplifier(object):
    @staticmethod
    def on():
        print("Turning amplifier on ...")

    @staticmethod
    def off():
        print("Turning amplifier off ...")

    @staticmethod
    def set_cd():
        print("Set CD in amplifier ...")

    @staticmethod
    def set_dvd():
        print("Set DVD in amplifier ...")

    @staticmethod
    def set_surround_sound():
        print("Set surround sound in amplifier ...")

    @staticmethod
    def set_volume(level: int):
        print(f"Setting volume to {level} in amplifier ...")


class Tuner(object):
    @staticmethod
    def on():
        print("Turning tuner on ...")

    @staticmethod
    def off():
        print("Turning tuner off ...")


class DVDPlayer(object):
    @staticmethod
    def on():
        print("Turning DVD player on ...")

    @staticmethod
    def off():
        print("Turning DVD player off ...")

    @staticmethod
    def play(movie: str):
        print(f"DVD player playing {movie} ...")

    @staticmethod
    def set_surround_audio():
        print("Set surround audio in CD Player ...")


class Projector(object):
    @staticmethod
    def on():
        print("Turning projector on ...")

    @staticmethod
    def off():
        print("Turning projector off ...")

    @staticmethod
    def wide_screen_mode():
        print("Set wide screen mode in projector ...")

    @staticmethod
    def tv_mode(mode: str):
        print(f"Setting projector to {mode} mode ...")


class Screen(object):
    @staticmethod
    def up():
        print("Pulling up screen ...")

    @staticmethod
    def down():
        print("Pulling down screen ...")


class PopcornPopper(object):
    @staticmethod
    def on():
        print("Turning on popcorn popper ...")

    @staticmethod
    def pop():
        print("Preparing popcorn ...")

    @staticmethod
    def off():
        print("Turning off popcorn popper ...")


class TheaterLights(object):
    @staticmethod
    def on():
        print("Turning on lights ...")

    @staticmethod
    def off():
        print("Turning off lights")

    @staticmethod
    def dim():
        print("Dimming lights")
