PIECES = "KQRBP"


def board_is_valid(rows):
	size = len(rows)
	if size == 0:
		return False
	for row in rows:
		if not isinstance(row, str):
			return False
		if len(row) != size:
			return False
	return True


def find_king(rows):
	king = None
	count = 0
	for y in range(len(rows)):
		for x in range(len(rows[y])):
			if rows[y][x] == 'K':
				king = (y, x)
				count += 1
	if count != 1:
		return None
	return king


def piece_attacks_king(rows, y, x, piece, king):
	size = len(rows)

	if piece == 'P':
		return (y - 1, x - 1) == king or (y - 1, x + 1) == king

	directions = []
	if piece == 'R' or piece == 'Q':
		directions += [(-1, 0), (1, 0), (0, -1), (0, 1)]
	if piece == 'B' or piece == 'Q':
		directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

	for dy, dx in directions:
		ny, nx = y + dy, x + dx
		while 0 <= ny < size and 0 <= nx < size:
			cell = rows[ny][nx]
			if cell in PIECES:
				if (ny, nx) == king:
					return True
				break
			ny += dy
			nx += dx
	return False


def king_in_check(rows, king):
	size = len(rows)
	for y in range(size):
		for x in range(size):
			piece = rows[y][x]
			if piece in "QRBP" and piece_attacks_king(rows, y, x, piece, king):
				return True
	return False


def checkmate(*args):
	if len(args) == 1 and isinstance(args[0], str):
		rows = args[0].split('\n')
	else:
		rows = list(args)

	if not board_is_valid(rows):
		return

	king = find_king(rows)
	if king is None:
		return

	if king_in_check(rows, king):
		print("Success")
	else:
		print("Fail")