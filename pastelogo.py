import os
from PIL import Image

# input path for the images to be modified in batch
input_path = "C:/Users/something/rest_of_the_path/"

# path for the logo to be added
logo_file = "C:/Users/something/rest_of_the_path/logo.png"

# percentage of the image to be covered by the logo
relative_size = 20

# output path for the modified images
output_path = "C:/Users/something/rest_of_the_path/result/"

def agregar_logo(imagen_path, logo_path, relative_size):
    # open files
    imagen = Image.open(imagen_path)
    
    # set size of the logo
    logo = Image.open(logo_path)
    W_logo, H_logo = logo.size
    nW_logo = int(imagen.width * relative_size / 100)
    nH_logo = int(H_logo * (nW_logo / W_logo))
    newsize_logo = logo.resize((nW_logo, nH_logo))
    
    # place the logo in the image
    posicion = (round(nW_logo*0.3), round(nH_logo*0.3)) # top left corner with offset

    # combine the images
    imagen.paste(newsize_logo, posicion, newsize_logo)
    
    # save the image
    image_name = os.path.basename(imagen_path)  # use the original name
    save_path = os.path.join(output_path, image_name)
    imagen.save(save_path)
    

# rinse and repeat
for nombre_archivo in os.listdir(input_path):
    if nombre_archivo.endswith(".jpg") or nombre_archivo.endswith(".png"):
        ruta_completa = os.path.join(input_path, nombre_archivo)
        agregar_logo(ruta_completa, logo_path, relative_size)