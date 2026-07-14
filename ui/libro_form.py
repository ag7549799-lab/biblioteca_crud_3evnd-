import flet as ft 

def libro_form():
    titulo_input =ft.TextField(
        label ="Autor", 
        width=400

    )

    autor_input =ft.TextField
    label ="ISBN: ", 
    width=400
    
autor_input =ft.TextField
label ="ISBN: ", 
width=400
mensaje =ft.Text(
    "",
    color =ft.Colors.GREEN
)


return  ft.Container(
    padding =30,
    content = ft.Column(
        controls =[
            ft.Text(
                "Insertar nuevo libro"
                size =24,
                weight=ft.FontWeight.BOLD
            ), 
            ft.Text(
                "Capture los datos basicos del libro,"
                size=14,
                color = ft.Colors.BLUE_GREY_600
            ),
        titulo_input,
        autor_input,
        isbn_input,

        ft.ElevatedButton(
            "Guardar",
            icon =ft.Icons.SAVE,
        ),
        mensaje
        ],
        spacing =15*
