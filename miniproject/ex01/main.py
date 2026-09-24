import sys
from checkmate import board_is_valid, find_king, king_in_check


def read_board(path):
	try:
		with open(path, "r") as file:
			content = file.read()
	except OSError:
		return None
	rows = content.split('\n')
	if rows and rows[-1] == '':
		rows.pop()
	return rows


def main():
	if len(sys.argv) < 2:
		print("Error")
		return

	for path in sys.argv[1:]:
		rows = read_board(path)
		if rows is None or not board_is_valid(rows):
			print("Error")
			continue

		king = find_king(rows)
		if king is None:
			print("Error")
			continue

		if king_in_check(rows, king):
			print("Success")
		else:
			print("Fail")


if __name__ == "__main__":
	main()