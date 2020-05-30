import sublime
import sublime_plugin


phantom_symbol = """
<body id="show-all-characters">
  <style>
  .symbol {
    display: block;
    position: relative;
    top: 0;
    left: 0;
    margin: 0.125rem 0;
    padding: -0.125rem 0.25rem;

    font-size: 0.75rem;
    font-family: monospace;
    font-weight: bold;
    border-radius: 0.125rem;
    color: #000;
    background-color: #fff;
  }
  </style>
  <span class="symbol">%s</span>
"""

phantom_sets = {}


def plugin_unloaded():
  for phantom_set in phantom_sets.values():
    phantom_set.update([])
  phantom_sets.clear()


class ShowAllCharactersCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view_id = self.view.id()
    if view_id in phantom_sets:
      phantom_sets[view_id].update([])
      del phantom_sets[view_id]
    else:
      phantoms = [sublime.Phantom(region,
                                  phantom_symbol % chr(9216 + ord(self.view.substr(region))),
                                  sublime.LAYOUT_INLINE)
                  for region in self.view.find_all(r"[\x00-\x1F]")]

      if len(phantoms) > 0:
        phantom_set = sublime.PhantomSet(self.view, "show-all-characters")
        phantom_set.update(phantoms)
        phantom_sets[view_id] = phantom_set
