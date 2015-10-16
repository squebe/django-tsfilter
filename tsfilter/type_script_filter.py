import hashlib
from compressor.cache import cache
from compressor.conf import settings
from compressor.filters.base import CompilerFilter


def get_precompiler_cachekey(command, contents):
	return hashlib.sha1('precompiler.%s.%s' % (command, contents)).hexdigest()


class TypeScriptFilter(CompilerFilter):

	def __init__(self, content, command=None, *args, **kwargs):
		command = "tsc --out {outfile} {infile}"
		super(TypeScriptFilter, self).__init__(content, command, *args, **kwargs)

	def input(self, **kwargs):
		key = self.get_cache_key()
		data = cache.get(key)
		if data is not None:
			return data
		filtered = super(TypeScriptFilter, self).input(**kwargs)
		cache.set(key, filtered, settings.COMPRESS_REBUILD_TIMEOUT)
		return filtered

	def get_cache_key(self):
		return get_precompiler_cachekey(self.command, self.content)