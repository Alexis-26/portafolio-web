import reflex as rx
from portafolio_web import constantes
from portafolio_web.styles.colores import Colores
from portafolio_web.styles.colores import TextColor
from portafolio_web.styles.styles import item_lista_style

# Diseño de item de cada uno de los proyectos
def item_lista(icono:str, titulo:str, descripcion:str, url:str):
    return rx.link(
        rx.box(
            rx.hstack(
                rx.icon_button(rx.icon(icono, color=Colores.ICONOS.value), size="4", background="None"),
                rx.vstack(
                    rx.text(titulo, color=TextColor.BLANCO.value),
                    rx.text(descripcion, color=TextColor.GRIS.value),
                    spacing="1"
                ),
                align="center"
            ),
            style=item_lista_style
        ),
        href=url,
        is_external=True,
        underline="none"
    )

# Lista que muestra todos los proyectos
def lista_proyectos():
    return rx.vstack(
        item_lista(constantes.ICONO_SISPOSGRADO, "Sistema Posgrado", constantes.DESC_SISPOSGRADO, constantes.URL_SISPOSGRADO),
        item_lista(constantes.ICONO_COMAL, "COMAL", constantes.DESC_COMAL, constantes.URL_COMAL),
        item_lista(constantes.ICONO_HUERTO, "Dashboard de Estado de una Planta", constantes.DESC_HUERTO, constantes.URL_HUERTO),
        item_lista(constantes.ICONO_KOFI, "KOFI", constantes.DESC_KOFI, constantes.URL_KOFI),
        item_lista(constantes.ICONO_CAZAROSTROS, "Videojuego Cazadores de Rostros", constantes.DESC_CAZAROSTROS, constantes.URL_CAZADOROSTROS),
        spacing="4"
    )