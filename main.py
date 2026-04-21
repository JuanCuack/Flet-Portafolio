import flet as ft
import asyncio

class PortafolioWeb(ft.Container):
    def __init__(self, page_obj: ft.Page):
        super().__init__()
        self.page_ref = page_obj
        self.page_ref.padding = 0
        self.page_ref.title = "Juan José Useche Quesada | Software Engineering"
        self.page_ref.theme_mode = ft.ThemeMode.DARK 
        
        try:
            self.page_ref.fonts = {"Starjhol": "assets/Starjhol.ttf"}
        except:
            pass
            
        self.definir_colores()
        self.setup_ui()

    def definir_colores(self):
        is_dark = self.page_ref.theme_mode == ft.ThemeMode.DARK
        self.acento = "#00C897" 
        self.page_ref.bgcolor = "#0A0A0B" if is_dark else "#F5F5F7"
        self.color_navbar = "#111112" if is_dark else "#FFFFFF"
        self.color_tarjetas = "#161617" if is_dark else "#F2F2F7"
        self.text_primary = "#FFFFFF" if is_dark else "#1D1D1F"
        self.text_secondary = "#A1A1A6" if is_dark else "#6E6E73"

    def setup_ui(self):
        self.page_ref.controls.clear()

        self.cambiar_modo = ft.IconButton(
            icon=ft.Icons.LIGHT_MODE if self.page_ref.theme_mode == ft.ThemeMode.DARK else ft.Icons.DARK_MODE,
            icon_color=self.acento,
            on_click=self.alternar_tema,
        )

        self.animacion = ft.Animation(700, "easeOutCubic")
        
        self.frame_inicio = ft.Container(expand=True, padding=50, animate_offset=self.animacion, offset=ft.Offset(0, 0), content=self.build_inicio())
        self.frame_servicio = ft.Container(expand=True, padding=50, animate_offset=self.animacion, offset=ft.Offset(1.5, 0), content=self.build_servicio())
        self.frame_resumen = ft.Container(expand=True, padding=50, animate_offset=self.animacion, offset=ft.Offset(1.5, 0), content=self.build_resumen())
        self.frame_contacto = ft.Container(expand=True, padding=50, animate_offset=self.animacion, offset=ft.Offset(1.5, 0), content=self.build_contacto())

        self.layout = ft.Column(
            expand=True, spacing=0,
            controls=[
                ft.Container(
                    padding=ft.Padding(40, 15, 40, 15), bgcolor=self.color_navbar,
                    border=ft.Border(bottom=ft.BorderSide(1, "#222222")),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("JUANCUACK", size=24, font_family="Starjhol", color=self.acento, weight="bold"),
                            ft.Row([
                                self.nav_button("Inicio", 0),
                                self.nav_button("Servicios", 1),
                                self.nav_button("Resumen", 2),
                                self.nav_button("Contacto", 3),
                            ], spacing=30),
                            self.cambiar_modo,
                        ]
                    ),
                ),
                ft.Container(expand=True, content=ft.Stack(controls=[self.frame_inicio, self.frame_servicio, self.frame_resumen, self.frame_contacto])),
                ft.Container(
                    padding=20, bgcolor=self.color_navbar,
                    content=ft.Row([ft.Text("Juan José Useche Quesada | Ingeniería de Software - UDEC", size=11, color=self.text_secondary)], alignment=ft.MainAxisAlignment.CENTER)
                )
            ],
        )
        self.page_ref.add(self.layout)

    def nav_button(self, texto, index):
        return ft.TextButton(
            content=ft.Text(texto, color=self.text_primary, size=14, weight="w500"),
            on_click=lambda _: self.cambiar_pagina(index)
        )

    def main_button(self, texto, icon, action=None, url=None, primary=True):
        async def handle_click(e):
            if url: await self.page_ref.launch_url(url)
            elif action: action(e)

        return ft.FilledButton(
            content=ft.Row([ft.Icon(icon, size=18), ft.Text(texto, weight="bold")], tight=True),
            on_click=handle_click,
            style=ft.ButtonStyle(
                bgcolor={"": self.acento if primary else ft.Colors.TRANSPARENT},
                color={"": ft.Colors.WHITE if primary else self.acento},
                side={"": ft.BorderSide(2, self.acento) if not primary else None},
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=20
            )
        )

    def build_inicio(self):
        return ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(col={"xs": 12, "md": 6}, spacing=25, controls=[
                    ft.Container(
                        content=ft.Row([
                            ft.Container(width=8, height=8, bgcolor=self.acento, border_radius=4),
                            ft.Text("INGENIERO DE SOFTWARE", size=12, color=self.acento, weight="bold")
                        ], tight=True),
                        padding=12, border=ft.Border.all(1, self.acento), border_radius=20
                    ),
                    ft.Text("Arquitectura y\nCódigo Eficiente", size=55, weight="bold", color=self.text_primary),
                    ft.Text("Soy Juan José Useche Quesada. Me apasiona resolver problemas complejos mediante software bien estructurado en Python.", size=18, color=self.text_secondary),
                    ft.Row([
                        self.main_button("Mis Proyectos", ft.Icons.ROCKET_LAUNCH_ROUNDED, action=lambda _: self.cambiar_pagina(2)),
                        self.main_button("GitHub", ft.Icons.TERMINAL_ROUNDED, url="https://github.com/JuanCuack", primary=False)
                    ], spacing=15)
                ]),
                ft.Container(
                    col={"xs": 12, "md": 5},
                    content=ft.Image(src="foto.jpg", border_radius=30, fit="cover"),
                    shadow=ft.BoxShadow(blur_radius=40, color=ft.Colors.with_opacity(0.1, self.acento)),
                    border=ft.Border.all(2, self.acento), padding=10, border_radius=40
                )
            ]
        )

    def build_servicio(self):
        return ft.Column(
            scroll=ft.ScrollMode.HIDDEN, spacing=35,
            controls=[
                ft.Text("Servicios Profesionales", size=35, weight="bold", color=self.text_primary),
                ft.ResponsiveRow(
                    spacing=25, run_spacing=25,
                    controls=[
                        self.grid_card("Python & Automation", "Automatización de procesos y lógica de negocio.", ft.Icons.CODE_ROUNDED, 4),
                        self.grid_card("SOLID Design", "Software escalable basado en buenas prácticas.", ft.Icons.ACCOUNT_TREE_ROUNDED, 4),
                        self.grid_card("Flet Desktop", "Aplicaciones de escritorio modernas y rápidas.", ft.Icons.DASHBOARD_ROUNDED, 4),
                        self.grid_card("Data Logic", "Optimización y manejo de bases de datos.", ft.Icons.STORAGE_ROUNDED, 6),
                        self.grid_card("User Interface", "Interfaces intuitivas centradas en el usuario.", ft.Icons.ADJUST_ROUNDED, 6),
                    ]
                )
            ]
        )

    def grid_card(self, t, s, icon, col):
        return ft.Container(
            col={"xs": 12, "md": col}, padding=35, bgcolor=self.color_tarjetas, border_radius=25,
            border=ft.Border.all(1, "#222222"), on_hover=self.efecto_hover,
            content=ft.Column([
                ft.Icon(icon, size=40, color=self.acento),
                ft.Text(t, weight="bold", size=22, color=self.text_primary),
                ft.Text(s, color=self.text_secondary, size=15),
            ], spacing=10)
        )

    def build_resumen(self):
        return ft.Column(
            scroll=ft.ScrollMode.HIDDEN, spacing=35,
            controls=[
                ft.Text("Trayectoria y Skills", size=35, weight="bold", color=self.text_primary),
                ft.ResponsiveRow(
                    spacing=30,
                    controls=[
                        ft.Column(col={"xs": 12, "md": 6}, spacing=20, controls=[
                            ft.Text("PROYECTOS RECIENTES", size=14, color=self.acento, weight="bold"),
                            self.resumen_card("CodeShift", "Videojuego 2D de Programación."),
                            self.resumen_card("Horarius", "Gestión académica de horarios."),
                            self.resumen_card("DarkQuiz Engine", "Motor de cuestionarios dinámicos."),
                        ]),
                        ft.Column(col={"xs": 12, "md": 6}, spacing=20, controls=[
                            ft.Text("COMPETENCIAS", size=14, color=self.acento, weight="bold"),
                            self.skill_card("Python & Flet Ecosystem", 0.95),
                            self.skill_card("OOP & Software Architecture", 0.88),
                            self.skill_card("Git & Collaborative Dev", 0.85),
                        ]),
                    ]
                )
            ]
        )

    def resumen_card(self, t, d):
        return ft.Container(
            padding=20, bgcolor=self.color_tarjetas, border_radius=15, border=ft.Border.all(1, "#222222"),
            height=90,
            content=ft.Row([
                ft.Icon(ft.Icons.SUBDIRECTORY_ARROW_RIGHT_ROUNDED, color=self.acento, size=24),
                ft.Column([ft.Text(t, weight="bold", size=16), ft.Text(d, size=13, color=self.text_secondary)], spacing=2, expand=True)
            ], spacing=15)
        )

    def skill_card(self, t, v):
        return ft.Container(
            padding=20, bgcolor=self.color_tarjetas, border_radius=15, border=ft.Border.all(1, "#222222"),
            height=90,
            content=ft.Column([
                ft.Row([ft.Text(t, weight="bold", size=15), ft.Text(f"{int(v*100)}%", size=13, color=self.acento)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.ProgressBar(value=v, color=self.acento, bgcolor="#222222", height=8)
            ], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        )

    def build_contacto(self):
        return ft.Column(
            scroll=ft.ScrollMode.HIDDEN, spacing=35,
            controls=[
                ft.Text("Contacto", size=35, weight="bold", color=self.text_primary),
                ft.ResponsiveRow(spacing=25, controls=[
                    self.contact_card("Correo", "psnjuan2019@gmail.com", ft.Icons.ALTERNATE_EMAIL_ROUNDED, "https://mail.google.com/mail/?view=cm&fs=1&to=psnjuan2019@gmail.com"),
                    self.contact_card("GitHub", "GitHub: JuanCuack", ft.Icons.HUB_ROUNDED, "https://github.com/JuanCuack"),
                ])
            ]
        )

    def contact_card(self, t, v, icon, url):
        return ft.Container(
            col={"xs": 12, "md": 6}, padding=40, bgcolor=self.color_tarjetas, border_radius=25,
            border=ft.Border.all(1, "#222222"), alignment=ft.Alignment(0, 0),
            content=ft.Column([
                ft.Icon(icon, size=45, color=self.acento),
                ft.Text(t, size=14, color=self.text_secondary),
                ft.Text(v, size=20, weight="bold"),
                self.main_button("Abrir", ft.Icons.OPEN_IN_NEW_ROUNDED, url=url)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
        )

    def cambiar_pagina(self, i):
        frames = [self.frame_inicio, self.frame_servicio, self.frame_resumen, self.frame_contacto]
        for idx, f in enumerate(frames):
            f.offset = ft.Offset(0 if idx == i else 1.5, 0)
        self.page_ref.update()

    def efecto_hover(self, e):
        e.control.border = ft.Border.all(1, self.acento if e.data == "true" else "#222222")
        e.control.update()

    def alternar_tema(self, _):
        self.page_ref.theme_mode = ft.ThemeMode.LIGHT if self.page_ref.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        self.definir_colores()
        self.setup_ui()
        self.page_ref.update()

async def main(page: ft.Page):
    PortafolioWeb(page)

if __name__ == "__main__":
    ft.run(main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
