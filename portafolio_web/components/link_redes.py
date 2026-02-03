import reflex as rx
from portafolio_web import constantes
from portafolio_web.styles.colores import Colores
from portafolio_web.styles.styles import item_redes_style

# Construccion de icono para red social
def icono_link(tag:str, url:str):
    return rx.icon_button(
        rx.icon(tag=tag),
        radius="full",
        size="3",
        on_click=rx.redirect(path=url, is_external=True),
        style=item_redes_style
    )

# Lista de redes sociales
def redes_sociales():
    return rx.hstack(
        icono_link(constantes.ICONO_GITHUB, constantes.URL_GITHUB),
        icono_link(constantes.ICONO_LINKEDIN, constantes.URL_LINKEDIN),
        icono_link(constantes.ICONO_INSTAGRAM, constantes.URL_INSTAGRAM)
    )