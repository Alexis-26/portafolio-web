from .colores import ColoresBackground

BASE_STYLE = {
    #"background_color": ColoresBackground.PRIMARIO.value,
    "background": f"radial-gradient(circle at top left, {ColoresBackground.PRIMARIO.value}, {ColoresBackground.SECUNDARIO.value})"
}

# Estilo para los items de proyectos
item_lista_style = {
    "background": "rgba(255, 255, 255, 0.03)", # Apenas visible
    "border_radius": "12px",
    "padding": "1em",
    "width": "100%",
    "transition": "all 0.2s ease",
    "border": "1px solid transparent",
    "cursor": "pointer",
    "_hover": {
        "background": "rgba(56, 189, 248, 0.1)", # Brillo cyan (#38bdf8) muy suave
        "border_color": "rgba(56, 189, 248, 0.3)", # Borde cyan sutil
        "transform": "translateY(-2px)",
    }
}

# Estilo para los items de redes sociales
item_redes_style = {
    "cursor": "pointer",
}