total_test_mark = 0
total_ass_mark = 0
for i in range(3):
    test_marks = int(input(f"enter a test {i+1} mark out of 100 :- "))
    pre = int((test_marks/100)*20)
    total_test_mark += pre
for i in range(2):
    ass_mark = int(input(f"enter assignment {i+1} mark out of 70 :- "))
    pre = int((ass_mark/100)*20)
    total_ass_mark += pre
total = total_ass_mark + total_test_mark 
if