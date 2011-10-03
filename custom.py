import sublime_plugin


class IsoTodayCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        from datetime import datetime
        for region in self.view.sel():
            self.view.insert(edit, region.begin(), datetime.now().strftime("%Y-%m-%d"))
