#!/usr/bin/env python

# configure
CARREL   = 'homer'
TEMPLATE = 'https://library.distantreader.org/carrels/%s/study-carrel.zip'
CARRELS  = './carrels'
ZIP      = './tmp/study-carrel.zip'

# require
import requests
import sys
import zipfile

# initialize
url = ( TEMPLATE % CARREL )

# cache the remote content
with open( ZIP, 'wb' ) as handle :

	# debug, initialize request, and get length
	sys.stdout.write( "Downloading %s\n" % url )
	response = requests.get( url, stream=True )
	length   = response.headers.get( 'content-length' )

	# do the work
	if length is None : handle.write( response.content )
	else:
		
		# initialize
		downloaded = 0
		length     = int( length )
		
		# download
		for data in response.iter_content( chunk_size=4096 ) :

			# re-initialize
			downloaded += len (data )
			percent    =  int( 50 * downloaded / length )
			
			# debug
			sys.stdout.write("\r[%s%s]" % ( '=' * percent, ' ' * ( 50-percent ) ) )    
			sys.stdout.flush()

			# save
			handle.write( data )

# beautify, unzip, and done
sys.stdout.write( "\n" )
with zipfile.ZipFile( ZIP, 'r' ) as handle : handle.extractall( CARRELS )
exit
