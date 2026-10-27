
__version__ = "1.0.0"

import random
from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

BG = (0.06, 0.09, 0.12, 1)
PANEL = (0.11, 0.16, 0.20, 1)
ACCENT = (0, 0.75, 0.65, 1)
WHITE = (1, 1, 1, 1)
MUTED = (0.65, 0.75, 0.80, 1)


class SealApp(App):
    def build(self):
        self.clicks = 0
        Window.clearcolor = BG

        root = BoxLayout(
            orientation="vertical",
            padding=dp(24),
            spacing=dp(14)
        )

        root.add_widget(Widget(size_hint_y=0.3))

        title = Label(
            text="🦭 Seal App",
            font_size="32sp",
            bold=True,
            color=ACCENT,
            size_hint_y=None,
            height=dp(60)
        )
        root.add_widget(title)

        subtitle = Label(
            text="Твоё приложение на Python",
            font_size="16sp",
            color=MUTED,
            size_hint_y=None,
            height=dp(40)
        )
        root.add_widget(subtitle)

        self.counter_label = Label(
            text="Нажатий: 0",
            font_size="28sp",
            bold=True,
            color=WHITE
        )
        root.add_widget(self.counter_label)

        self.status = Label(
            text="Добро пожаловать!",
            font_size="16sp",
            color=MUTED
        )
        root.add_widget(self.status)

        btn = Button(
            text="Нажми меня!",
            font_size="18sp",
            bold=True,
            color=WHITE,
            background_normal="",
            background_color=ACCENT,
            size_hint_y=None,
            height=dp(56)
        )
        btn.bind(on_press=self.click_button)
        root.add_widget(btn)

        msg = Button(
            text="Показать сообщение",
            font_size="16sp",
            background_normal="",
            background_color=PANEL,
            size_hint_y=None,
            height=dp(52)
        )
        msg.bind(on_press=self.show_message)
        root.add_widget(msg)

        reset = Button(
            text="Сбросить счётчик",
            font_size="16sp",
            background_normal="",
            background_color=PANEL,
            size_hint_y=None,
            height=dp(52)
        )
        reset.bind(on_press=self.reset_counter)
        root.add_widget(reset)

        root.add_widget(Widget(size_hint_y=0.3))

        footer = Label(
            text="Создано на Python 🐍",
            color=MUTED,
            font_size="12sp",
            size_hint_y=None,
            height=dp(30)
        )
        root.add_widget(footer)

        return root

    def click_button(self, instance):
        self.clicks += 1
        self.counter_label.text = f"Нажатий: {self.clicks}"
        self.status.text = random.choice([
            "Отлично! Так держать!",
            "Кнопка работает!",
            "Python — это круто!",
            "Продолжай экспериментировать!"
        ])

    def show_message(self, instance):
        from kivy.uix.popup import Popup

        content = Label(
            text="Привет! Это твоё приложение Seal App!"
        )
        popup = Popup(
            title="Привет!",
            content=content,
            size_hint=(0.85, 0.35)
        )
        popup.open()

    def reset_counter(self, instance):
        self.clicks = 0
        self.counter_label.text = "Нажатий: 0"
        self.status.text = "Счётчик сброшен."


if __name__ == "__main__":
    SealApp().run()
