Extended tab switcher for Sublime Text
==================================================

**This plugin is inspired by the default tab switcher in netbeans**	 which displays the open files to choose from. View all open files (sorted/unsorted) for switching between them.


## Key Bindings

* On pressing `ctrl+alt+tab` all open files will be displayed for selection.
* On pressing `ctrl+alt+shift+tab` only open files in the active group will be displayed for selection.


User can change the default key binding at `Preferences -> Package Settings -> Extended Tab Switcher -> Key Bindings User`



## Configurations
User can overwrite the following configurations by adding flags in the User - Settings section which can be access by `Preferences -> Package Settings -> Extended Tab Switcher -> Settings - User`

* Sorting

	By default the the files are sorted in the order of "open files" in the side bar. To enable the sorting the user can change the defauly key binding and adding the following flag in the settings

	```javascript
	{
		"sort": "true"
	}
	```

* Skip current file

	By default the current active file/view is also displayed within the selection of the open files. This can be overwritten by adding the following flag in the settings

	```javascript
	{
		"skip_current_file": "true"
	}
	```


* Mark dirty file

	By default all the dirty/unsaved files are marked with "*". This can be overwritten by adding the following flag in the settings


	Tip: This character can be also use to view all the unsaved files while searching the open files


	```javascript
	{
		"mark_dirty_file_char": "<your-char>" 
	}

	```



## Credits

Rajesh Vaya (@rajeshvaya) [GitHub](https://github.com/rajeshvaya)

Kohichi Aoki (@drikin) [GitHub](https://github.com/drikin)

Philip Oliver (@phildopus) [GitHub](https://github.com/phildopus)



This projected is licensed under the terms of the MIT license.

```
The MIT License (MIT)

Copyright (c) [2014] [Rajesh Vaya <vaya.rajesh@gmail.com>]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
