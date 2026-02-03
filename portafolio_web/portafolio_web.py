import reflex as rx
from portafolio_web.styles import styles
from portafolio_web.styles.colores import TextColor, Colores
from portafolio_web import constantes
from portafolio_web.components.link_redes import redes_sociales
from portafolio_web.components.lista_contenido import lista_proyectos


def index() -> rx.Component:
    return rx.center(
        rx.vstack(

            # Informacion importante
            rx.hstack(
                rx.avatar(src=constantes.FOTO, radius="full", size="8", border=f"4px, solid {Colores.ICONOS.value}"),
                rx.vstack(
                    rx.text(constantes.NOMBRE, size="8", weight="bold", color=TextColor.BLANCO.value),
                    rx.text(constantes.CARRERA, size="3", color=TextColor.BLANCO.value),
                    redes_sociales()
                )
            ),

            # Descripcion
            rx.text(
                constantes.DESCRIPCION,
                color=TextColor.GRIS.value
            ),

            # Contenido
            rx.vstack(
                rx.text("Proyectos", size="6", weight="bold", color=TextColor.BLANCO.value),
                lista_proyectos(),
            ),

            background="rgba(30, 41, 59, 0.7)",
            backdrop_filter="blur(12px)",
            width="100%",
            height="100%",
            max_width="550px",
            padding="20px",
            border_radius="24px",
            spacing="6",
            border="1px solid rgba(255, 255, 255, 0.1)",
            box_shadow="0 8px 32px 0 rgba(0, 0, 0, 0.3)",
        ),
        padding="20px"
    )


app = rx.App(style=styles.BASE_STYLE, theme=rx.theme(appearance="dark", has_background=True))
app.add_page(index)
