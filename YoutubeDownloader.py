import os
import shutil
import time
import wget
import moviepy.editor as mp
from pytube import YouTube

def rainbowequals(repeat=1):
    """Imprime 7 '=' de colores."""
    for x in range(repeat):
        for color in range(31,38):
            print(f'\033[1;{color};40m' + '=', end='')
    print('\x1b[0m')

def white_text(texto=str):
    """Convierte el texto entregado a color blanco."""
    return '\033[1;37;40m' + texto + '\033[0;0m'

def Menuprint():
    """Imprime el menu del programa."""
    rainbowequals(6)
    print('\033[1;37;40mBienvenid@ a', '\033[1;30;47m' + 'You', '\033[1;37;41m' + 'Tube' + '\x1b[0m', '\033[1;37;40mdownloader.    V1.0\n')
    print(white_text('Made with ') + '\033[1;31m♥\033[0;0m' + white_text(' by ') + '\033[1;32mFudy\033[0;0m')

    print('\n\033[1;37;40mSelecciona una opción:', end='')
    print('''
    1.- Video
    2.- Audio
    3.- Miniatura
    4.- Cerrar''')
    rainbowequals(6)

def Menu():
    """
    Menu inicial del programa.
    Retorna la opcion elegida por el usuario.
    """
    while True:
        Menuprint()
        try:
            option = int(input('>>'))
            if option == 1 or option == 2 or option == 3 or option == 4:
                break
            else:
                print('Opcion no valida.')
                time.sleep(1)
                os.system('clear')
        except:
            print('Opcion no valida.')
            time.sleep(1)
            os.system('clear')

    return option

def VideoDownloader(Link = str):
    """Proceso de descarga de video. Directorio de descarga predeterminado es 'Desktop'."""
    try:
        video = YouTube(Link)
        os.system('clear')
        rainbowequals(7)
        print(white_text('Video a descargar será:\n'))
        print(white_text('Titulo: ') +  video.title)
        print(white_text('Canal:  ') + video.author)
    
        output = r"C:\Users\{}\Desktop".format(os.getlogin())
        print('')
        print('\033[1;30;41mDescargando...\033[0;0m')
        print(white_text('Video guardado en: ') + f'\033[1;30;41m{video.streams.get_highest_resolution().download(output_path=output)}\033[0;0m')
        rainbowequals(7)
        print('\n')
        input(white_text('Presiona Enter para cerrar...'))
    except:
        print('\n\033[1;31;41mHa ocurrido un error, ¿Has ingresado un link valido?\033[0;0m\n')
        input(white_text('Presiona Enter para cerrar...'))

def AudioDownloader(Link = str):
    """Proceso de descarga de audio. Descarga el mp4 del video y lo convierte en mp3. Directorio de descarga predeterminado es 'Desktop'."""
    try:
        audio = YouTube(Link)
        os.system('clear')
        rainbowequals(7)
        print(white_text('Audio a descargar será:\n'))
        print(white_text('Titulo: ') + audio.title)
        print(white_text('Canal:  ') + audio.author)

        output = r"C:\Users\{}\Desktop".format(os.getlogin())
        print('')
        print('\033[1;30;41mDescargando...\033[0;0m')

        archivo = audio.streams.get_highest_resolution().download(output_path=output)

        print('\033[1;30;41mConvirtiendo audio...\033[0;0m')

        #Cargamos el fichero .mp4
        clip = mp.VideoFileClip(archivo)

        #Lo escribimos como audio y `.mp3`
        clip.audio.write_audiofile(f'{audio.title}.mp3')

        #Lo movemos a la ubicacion predeterminada
        script_dir = os.path.abspath( os.path.dirname( __file__ ) )
        shutil.move(f'{script_dir}\\{audio.title}.mp3', output)
        clip.close()
        
        #elimina el archivo mp4 base
        os.remove(f'{output}\\{audio.title}.mp4')

        print(white_text(f'Audio guardado en: \033[1;30;41m{output}\\{audio.title}.mp3\033[0;0m'))

        rainbowequals(7)
        print('\n')
        input(white_text('Presiona Enter para cerrar...'))
    except:
        print('\n\033[1;31;41mHa ocurrido un error, ¿Has ingresado un link valido?\033[0;0m\n')
        input(white_text('Presiona Enter para cerrar...'))

def thumbnailGetter(Link):
    """Proceso de descarga de miniaturas. Directorio de descarga predeterminado es 'Desktop'."""
    try:
        image = YouTube(Link)
        os.system('clear')
        rainbowequals(7)
        print(white_text('Imagen a descargar será:\n'))
        print(white_text('Titulo: ') + image.title)
        print(white_text('Canal:  ') + image.author)

        print('\033[1;30;41mDescargando...\033[0;0m')
        url = image.thumbnail_url
        filename = wget.download(url)

        #Mueve el archivo al directorio de salida (desktop)
        output = r"C:\Users\{}\Desktop".format(os.getlogin())
        script_dir = os.path.abspath( os.path.dirname( __file__ ) )
        shutil.move(f'{script_dir}\\{filename}', output)
        os.rename(f'{output}\\{filename}', f'{output}\\{image.title}.jpg')
        print('')

        print(white_text('Imagen guardada en:') + f'\033[1;30;41m{output}\\{image.title}.jpg\033[0;0m')
        rainbowequals(7)
        print('\n')
        input(white_text('Presiona Enter para cerrar...'))
    except:
        print('''\n\033[1;31;41mHa ocurrido un error.
¿Has ingresado un link valido?
¿El archivo ya existe en el destino?\033[0;0m\n''')
        input(white_text('Presiona Enter para cerrar...'))

def Main():
    option = Menu()
    if option == 1:
        print(white_text('Ingrese el link del video: '))
        LinkVideo = input('>>')
        VideoDownloader(LinkVideo)
    elif option == 2:
        print(white_text('Ingrese el link del audio: '))
        LinkAudio = input('>>')
        AudioDownloader(LinkAudio)
    elif option == 3:
        print(white_text('Ingrese el link de la imagen: '))
        LinkImagen = input('>>')
        thumbnailGetter(LinkImagen)
    elif option == 4:
        exit()


if __name__ == "__main__":
    Main()