from collections     import OrderedDict, namedtuple
from collections.abc import Mapping

# FIXME Support obsolete (#~) and previous (#|) entries, multiple plurals

class ParseError(IOError):
	pass

Token = namedtuple('_Token', ['type', 'value'])
NIL = Token('nil', None)
END = Token('end', None)
def tokens(lines):
	for line in lines:
		line = line.lstrip().rstrip('\n')

		# Empty lines
		if not line or line.isspace():
			yield NIL
			continue

		# Comments
		if line[0] == '#':
			if len(line) == 1 or line[1].isspace():
				yield Token('#', line[1:])
			else:
				yield Token(line[0:2], line[2:])
			continue

		# Keywords
		while line:
			if line[0] == '"':
				i = 1
				while i < len(line):
					if line[i] == '"': break
					i += 2 if line[i] == '\\' else 1
				if i >= len(line):
					raise ParseError("Unterminated string")
				yield Token('string', line[1:i])
				line = line[i+1:]
			elif line[0].isalpha():
				i = 0
				while i < len(line) and line[i].isalpha():
					i += 1
				yield Token('keyword', line[:i])
				line = line[i:]
			else:
				raise ParseError("Unknown character")
			line = line.lstrip()

class Reader:
	__slots__ = ['Entry', 'file', '_header', '_peek', '_tokens']

	def __init__(self, entry, file):
		self.Entry   = entry
		self.file    = file
		self._tokens = tokens(file)

		self._peek = None; self._next() # prime the pump
		self._header = None # FIXME

	def _next(self):
		p, self._peek = self._peek, next(self._tokens, END)
		return p

	def __iter__(self):
		return self

	def __next__(self):
		if self._peek.type == 'end':
			raise StopIteration

		entry = self.Entry()

		# Comments
		while self._peek.type.startswith('#'):
			if self._peek.type in entry:
				raise ParseError("Discontinuous comment")
			key   = self._peek.type
			lines = [self._next().value]
			while self._peek.type == key:
				lines.append(self._next().value)
			entry[key] = tuple(lines)

		# Keywords
		while self._peek.type == 'keyword':
			if self._peek.type in entry:
				raise ParseError("Duplicate keyword")
			key   = self._next().value
			lines = []
			while self._peek.type == 'string':
				lines.append(self._next().value)
			if not lines:
				raise ParseError("No strings after keyword")
			entry[key] = tuple(lines)

		# Empty
		if self._peek.type not in ['nil', 'end']:
			raise ParseError('Expected end of entry')
		while self._peek.type == 'nil':
			self._next()

		return entry

class Writer:
	__slots__ = ['file', '_end']

	def __init__(self, file):
		self.file = file
		self._end = ''

	def write(self, entry):
		print(end=self._end, file=self.file)

		for key in OrderedDict(entry):
			lines = entry[key]
			if key.startswith('#'):
				for line in lines:
					assert not line or line[0].isspace()
					print(key+line, file=self.file)
			else:
				if not lines: continue
				print(key, end=' ', file=self.file)
				for line in lines:
					print('"'+line+'"', file=self.file)

		self._end = '\n'
