import sublime, sublime_plugin, os

class ExtendedSwitcherCommand(sublime_plugin.WindowCommand):
	# declarations
	open_files = []
	open_views = []
	window = []
	settings = []

	# lets go
	def run(self, list_mode):
		# self.view.insert(edit, 0, "Hello, World!")
		self.open_files = []
		self.open_views = []
		self.window = sublime.active_window()
		self.settings = sublime.load_settings('ExtendedSwitcher.sublime-settings')
		folders = self.window.folders()
		
		for f in self.getViews(list_mode):
			# if skip the current active is enabled do not add the current file it for selection
			if self.settings.get('skip_current_file') == True:
				if f.id() == self.window.active_view().id():
					continue

			self.open_views.append(f) # add the view object
			file_name = f.file_name() # get the full path
			file_path = ''

			if file_name:
				for folder in folders:
					if os.path.commonprefix([folder, file_name]) == folder:
						file_path = os.path.relpath(file_name, folder)

				if f.is_dirty():
					file_name += self.settings.get('mark_dirty_file_char') # if there are any unsaved changes to the file

				if self.settings.get('show_full_file_path') == True:
					self.open_files.append([os.path.basename(file_name), file_path]) 
				else:
					self.open_files.append([os.path.basename(file_name), '']) 
			elif f.name():
				if f.is_dirty():
					self.open_files.append([f.name() + self.settings.get('mark_dirty_file_char'), ''])
				else:
					self.open_files.append([f.name(), ''])
			else:
				if f.is_dirty():
					self.open_files.append(["Untitled"+self.settings.get('mark_dirty_file_char'), ''])
				else:
					self.open_files.append(["Untitled", ''])

		if self.check_for_sorting() == True:
			self.sort_files()
 
		self.window.show_quick_panel(self.open_files, self.tab_selected, False, -1) # show the file list

	# display the selected open file
	def tab_selected(self, selected):
		if selected > -1:
			self.window.focus_view(self.open_views[selected])

		return selected

	# sort the files for display in alphabetical order
	def sort_files(self):
		open_files = self.open_files
		open_views = []

		open_files.sort()

		for f in open_files:
			f = f[0]
			for fv in self.open_views:
				if fv.file_name():
					f = f.replace(" - " + os.path.dirname(fv.file_name()),'')
					if (f == os.path.basename(fv.file_name())) or (f == os.path.basename(fv.file_name())+self.settings.get('mark_dirty_file_char')):
						open_views.append(fv)
						self.open_views.remove(fv)
				elif fv.name() == f or fv.name()+self.settings.get('mark_dirty_file_char') == f:
					open_views.append(fv)
					self.open_views.remove(fv)
				elif f == "Untitled" and not fv.name():
					open_views.append(fv)
					self.open_views.remove(fv)

				
		self.open_views = open_views



	# flags for sorting
	def check_for_sorting(self):
		if self.settings.has("sort"):
			return self.settings.get("sort", False)


	def getViews(self, list_mode):
		views = []
		# get only the open files for the active_group
		if list_mode == "active_group":
			views = self.window.views_in_group(self.window.active_group())

		# get all open view if list_mode is window or active_group doesn't have any files open
		if (list_mode == "window") or (len(views) < 1):
			views = self.window.views()

		return views


