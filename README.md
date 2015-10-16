TSFilter is a typescript filter for Django Compressor on Heroku. The filter will precompile TypeScript to JavaScript and will cache the compilation to save time during development. In the future the precompile caching feature should be available in compressor out of the box without this package via COMPRESS_CACHEABLE_PRECOMPILERS. The setup script will also attempt to setup node and typescript on the heroku machine. Its a hack, and there are probably better ways (like the Heroku post install hook) so *please use with caution*.

To install:

    pip install git+https://github.com/squebe/tsfilter.git

To use:

    COMPRESS_PRECOMPILERS = (
        ('text/typescript', 'tsfilter.TypeScriptFilter'),
    )