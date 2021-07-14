# (c) @AbirHasan2005

import os
import shutil


async def delete_all(root: str):
    """
    Eliminar una carpeta.

    :param root: Pase la ruta de la carpeta como cadena.
    """

    try:
        shutil.rmtree(root)
    except Exception as e:
        print(e)


async def delete_one(file: str):
    """
    Intente eliminar un archivo específico.

    :param file: Pasar ruta de archivo.
    """

    try:
        os.remove(file)
    except:
        pass
