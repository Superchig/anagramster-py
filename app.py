import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class AppWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Anagramster")

        grid = Gtk.Grid()
        self.add(grid)

        self.phrase_view = Gtk.Entry()
        self.phrase_view.connect("changed", self.entry_changed)
        self.anagram_view = Gtk.Entry()
        self.anagram_view.connect("changed", self.entry_changed)
        self.output_label = Gtk.Label(label="Output.")
        self.ignore_case = Gtk.CheckButton(label="Ignore Case")
        self.ignore_case.connect("clicked", self.entry_changed)

        grid.add(self.phrase_view)
        grid.attach(self.anagram_view, 1, 0, 1, 1)
        grid.attach(self.ignore_case, 2, 0, 1, 1)
        grid.attach(self.output_label, 0, 1, 2, 1)

    def entry_changed(self, widget):
        markup_text = ""

        anagram_text = self.anagram_view.get_text()
        phrase = self.phrase_view.get_text()
        if self.ignore_case.get_active():
            anagram_text = anagram_text.lower()
            phrase = phrase.lower()
        anagrammed = list(anagram_text)

        for ch in phrase:
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
