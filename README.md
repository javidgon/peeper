Peeper - Thin events' recorder library
======================================

In a nutshell
-------------

```
peeper = Peeper(github: {'mode': 'show_all_events',
						 'auth': True
						 'user': '<username>',
						 'password': '<password>'
						 })
						 
peeper.get_stream_from_service(service='github')

# Output: [{u'actor': {u'avatar_url': u'https:...-420.png', u'gravatar_id'...
```

Changelog
---------

v.0.1: Add Github support.

Contributing
------------

If you'd like to contribute, just Fork the repository, create a branch with
your changes and send a pull request. Don't forget appending your name to AUTHORS ;)

