import pygame
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((900 , 512)) 
pygame.display.set_caption("Player") 
player = pygame.image.load("pygame/sounds/image.jpeg") #main object
process = True 
playlist = ["pygame/sounds/muz.mp3", "pygame/sounds/muz2.mp3" , "pygame/sounds/muz3.mp3"] #list of musics
index_of_playlist = 0
def play_music():
    pygame.mixer.music.load(playlist[index_of_playlist])
    pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.stop()
def next_track():
    global index_of_playlist
    index_of_playlist = (index_of_playlist + 1) % len(playlist)
    play_music()
def previous_track():
    global index_of_playlist
    index_of_playlist = (index_of_playlist - 1) % len(playlist)
    play_music()
while process :
    pygame.display.update()
    screen.blit(player , (0 , 0))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            process = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                play_music()
            elif event.key == pygame.K_DOWN:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()

pygame.display.flip()
clock.tick(10)
pygame.quit()