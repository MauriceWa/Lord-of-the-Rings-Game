import pygame
import os


def start_muziek() -> None:
    pygame.mixer.init()
    muziek_pad = os.path.join(os.path.dirname(__file__), f"../assets/muziek/intro.mp3")
    pygame.mixer.music.load(muziek_pad)
    pygame.mixer.music.play(-1)

    pygame.mixer.music.set_volume(.7)
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)


def easter_egg_muziek() -> None:
    # change muziek to easter egg muziek
    muziek_pad = os.path.join(os.path.dirname(__file__), "../assets/muziek/the-sheiter.mp3")
    pygame.mixer.music.load(muziek_pad)
    pygame.mixer.music.play(-1)


def verander_muziek(track_naam) -> None:
    # change muziek to easter egg muziek
    muziek_pad = os.path.join(os.path.dirname(__file__), f"../assets/muziek/{track_naam}.mp3")
    pygame.mixer.music.load(muziek_pad)
    pygame.mixer.music.play(-1)


def verkrijg_volume() -> float:
    return float(pygame.mixer.music.get_volume() * 100)


def verander_volume(volume: float) -> None:
    pygame.mixer.music.set_volume(float(volume) / 100)


def pauzeer_muziek() -> None:
    pygame.mixer.music.pause()


def hervat_muziek() -> None:
    pygame.mixer.music.unpause()


def verkrijg_muziek_status() -> bool:
    return pygame.mixer.music.get_busy()
