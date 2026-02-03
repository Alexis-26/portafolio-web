import reflex as rx
from portafolio_web import constantes
from portafolio_web.styles.colores import Colores
from portafolio_web.styles.styles import item_redes_style
from portafolio_web.styles.colores import TextColor

# Construccion de icono para red social
def icono_link(tag:str, url:str):
    return rx.link(
        rx.icon(
            tag=tag,
            size=30,
            color=TextColor.BLANCO.value,
            style=item_redes_style
        ),
        href=url,
        is_external=True
    )

# Lista de redes sociales
def redes_sociales():
    return rx.hstack(
        icono_link(constantes.ICONO_GITHUB, constantes.URL_GITHUB),
        icono_link(constantes.ICONO_LINKEDIN, constantes.URL_LINKEDIN),
        icono_link(constantes.ICONO_INSTAGRAM, constantes.URL_INSTAGRAM)
    )