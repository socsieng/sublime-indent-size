import sublime
import sublime_plugin

class IndentSizeCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Tab size:", "", self.on_done, None, None)

    def on_done(self, text):
        try:
            tab_size = int(text)

            if self.window.active_view():
                view = self.window.active_view()
                settings = view.settings()
                is_spaces = settings.get('translate_tabs_to_spaces')
                current_tab_size = settings.get('tab_size')

                if tab_size == current_tab_size:
                    return

                if is_spaces:
                    settings.set('translate_tabs_to_spaces', False)
                    view.run_command('unexpand_tabs', { 'set_translate_tabs': True })
                    print('unexpand_tabs')

                settings.set('tab_size', tab_size)

                if is_spaces:
                    settings.set('translate_tabs_to_spaces', True)
                    view.run_command('expand_tabs', { 'set_translate_tabs': True })
                    print('expand_tabs')

        except ValueError:
            pass
