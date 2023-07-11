import pygame
pygame.init()

pygame.mixer.music.load("images\\music\\00-Menu.wav")  # Ruta de tu canción en formato mp3
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.quit()
