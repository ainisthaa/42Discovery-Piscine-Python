import io
import sys
from checkmate import checkmate


if __name__ == "__main__":
    tests = [
        # --- SUCCESS CASES (โดนรุก) ---
        {
            "name": "Success: Pawn รุกจากด้านล่างทแยงขึ้นบน",
            "board": """\
.K..
P...
....
....""",
            "expected": "Success",
        },
        {
            "name": "Success: Rook รุกในแนวนอน",
            "board": """\
....
R..K
....
....""",
            "expected": "Success",
        },
        {
            "name": "Success: Bishop รุกในแนวทแยง",
            "board": """\
B...
....
..K.
....""",
            "expected": "Success",
        },
        {
            "name": "Success: Queen รุกในแนวทแยง",
            "board": """\
...Q
....
.K..
....""",
            "expected": "Success",
        },
        {
            "name": "Success: กระดานขนาดใหญ่ (8x8) และ Rook เล็งตรงถึง King",
            "board": """\
........
...R...K
........
...B....
........
........
........
........""",
            "expected": "Success",
        },
        # --- FAIL CASES (ปลอดภัย / ไม่โดนรุก) ---
        {
            "name": "Fail: King ปลอดภัย หมากอยู่คนละแนว",
            "board": """\
R...
....
..K.
....""",
            "expected": "Fail",
        },
        {
            "name": "Fail: โดนหมากตัวอื่นบังทางเดินไว้ (Blocked)",
            "board": """\
R.BK
....
....
....""",
            "expected": "Fail",
        },
        {
            "name": "Fail: Pawn อยู่เหนือ King (Pawn กินลงล่างไม่ได้)",
            "board": """\
.P..
K...
....
....""",
            "expected": "Fail",
        },
        {
            "name": "Fail: King อยู่ตัวเดียวบนกระดาน",
            "board": """\
...
.K.
...""",
            "expected": "Fail",
        },
        # --- ERROR / EDGE CASES (กระดานผิดรูปแบบ) ---
        {
            "name": "Error: กระดานไม่เป็นสี่เหลี่ยมจัตุรัส (3x2)",
            "board": """\
...
...""",
            "expected": "Error",
        },
        {
            "name": "Error: ไม่มี King อยู่บนกระดาน",
            "board": """\
R...
....
....
....""",
            "expected": "Error",
        },
        {
            "name": "Error: มี King มากกว่า 1 ตัว",
            "board": """\
K...
...K
....
....""",
            "expected": "Error",
        },
        {
            "name": "Error: ข้อความว่างเปล่า (Empty Board)",
            "board": "",
            "expected": "Error",
        },
    ]

    print("=" * 60)
    print("เริ่มรัน Checkmate Test Cases")
    print("=" * 60)

    passed_count = 0

    for idx, test in enumerate(tests, 1):
        # ดักจับค่าที่ฟังก์ชัน print ออกมา
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            checkmate(test["board"])
            actual = captured_output.getvalue().strip()
        except Exception as e:
            actual = f"Crash ({e})"
        finally:
            sys.stdout = sys.__stdout__  # คืนค่า stdout

        status = "PASSED" if actual == test["expected"] else "FAILED"
        if status == "PASSED":
            passed_count += 1

        print(f"[{idx}/{len(tests)}] {test['name']}")
        print(f"  - คาดหวัง: {test['expected']}")
        print(f"  - ได้รับ:   {actual}")
        print(f"  - ผล:      {status}\n")

    print("=" * 60)
    print(f"สรุปผลการทดสอบ: ผ่าน {passed_count}/{len(tests)} เคส")
    print("=" * 60)
