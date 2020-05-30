# ShowAllCharacters

A Sublime 3 plugin to toggle showing all characters.

## Motivation

I've been using Sublime a great deal but have always missed the feature of being able so see all characters like what Notepad++ does. After searching around and failing to find such a feature or plugin, I gave it a shot myself. Right now I feel like it gets the job done enough for me (kinda, see [Notes](#notes)).

Feel free to give it a go and hack away if you so desire.


## Installation

### Manual

Only manual installation is supported.

Clone the repo into the packages directory. The default for OSX is at `~/Library/Application Support/Sublime Text 3/Packages/`


## Usage

When installed it will add a submenu at `View > Show Symbol > Toggle showing all characters`.


## Notes

Sublime converts line endings to a line feed (LF, `\n`). Thus this plugin does not correctly show the actual line ending characters in files; should it contain the LF,  Carriage return (CR, `\r`) or CR LF.

On large files, this is slow; beware.

The plugin, after activation, does not update the visual characters upon modification.