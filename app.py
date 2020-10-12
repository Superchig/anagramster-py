import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class AppWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello, World Example")

        grid = Gtk.Grid()
        self.add(grid)

        self.phrase_view = Gtk.Entry()
        self.phrase_view.connect("changed", self.entry_changed)
        self.anagram_view = Gtk.Entry()
        self.anagram_view.connect("changed", self.entry_changed)
        self.output_label = Gtk.Label(label="Output.")

        grid.add(self.phrase_view)
        grid.attach(self.anagram_view, 1, 0, 1, 1)
        grid.attach(self.output_label, 0, 1, 2, 1)

    def on_button_clicked(self, widget):
        print("Hello, world!")

    def entry_changed(self, entry):
        markup_text = ""
        anagrammed = list(self.anagram_view.get_text())
        for ch in self.phrase_view.get_text():
            if ch in anagrammed:
                markup_text += ch
                anagrammed.remove(ch)
            else:
                markup_text += f"<span foreground='gray'>{ch}</span>"

        for ch in anagrammed:
            markup_text += f"<span foreground='red'>{ch}</span>"

        self.output_label.set_markup(markup_text)

win = AppWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
