#!/usr/bin/env python


# configure
CATALOG = 'https://library.distantreader.org/catalog/catalog.json'

# require
import requests

# initialize
catalog = requests.get( CATALOG ).json()

# process each item in the catalog
for carrel in catalog :
	
	# parse
	name     = carrel[ 'shortname' ]
	date     = carrel[ 'date-created' ]
	keywords = carrel[ 'keywords' ]
	items    = carrel[ 'items' ]
	words    = carrel[ 'words' ]
	flesch   = carrel[ 'flesch' ]
	bytes    = carrel[ 'size' ]

	# output
	print( '      name: %s' % name )
	print( '      date: %s' % date )
	print( '  keywords: %s' % keywords )
	print( '     items: %s' % items )
	print( '     words: %s' % words )
	print( '     bytes: %s' % bytes )
	print()
	
# done
exit