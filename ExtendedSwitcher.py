import sublime, sublime_plugin, os

class ExtendedSwitcherCommand(sublime_plugin.TextCommand):
	# declarations
	open_files = []
	open_views = []
	window = []
	settings = []

	# lets go
	def run(self, edit):
		# self.view.insert(edit, 0, "Hello, World!")
		self.open_files = []
		self.open_views = []
		self.window = sublime.active_window()
		self.settings = sublime.load_settings('ExtendedSwitcher.sublime-settings')
		
		for f in sublime.active_window().views():
			self.open_views.append(f) # add the view object
			file_name = f.file_name() # get the full path
			if f.is_dirty():
				file_name += "*" # if there are any unsaved changes to the file

			if file_name:
				self.open_files.append(os.path.basename(file_name))
			else:
				self.open_files.append("Untitled")

		if self.check_for_sorting() == "true":
			self.sort_files()

		self.window.show_quick_panel(self.open_files, self.tab_selected) # show the file list

	# display the selected open file
	def tab_selected(self, selected):
		if selected > -1:
			self.window.focus_view(self.open_views[selected])

		print selected

	def sort_files(self):
		open_files = self.open_files
		open_views = []

		open_files.sort()

		for f in open_files:
			for fv in self.open_views:
				if fv.file_name():
					if (f == os.path.basename(fv.file_name())) or (f == os.path.basename(fv.file_name())+"*"):
						open_views.append(fv)

				if f == "Untitled" and not fv.file_name():
					open_views.append(fv)
					
		self.open_views = open_views



	# flags for sorting
	def check_for_sorting(self):
		if self.settings.has("sort"):
			return self.settings.get("sort", False)

		



