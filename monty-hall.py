import random

HOLE_NUMBER = 3

def intro(correct):
    choices = list(range(HOLE_NUMBER))
    select = random.choice(choices)
    ## 蓋を開ける候補を抽出
    delete_candidate = list(range(HOLE_NUMBER))
    if correct in delete_candidate:
        delete_candidate.remove(correct)
    if select in delete_candidate:
        delete_candidate.remove(select)
    ## 蓋を開ける（選択肢から削除候補の内一つを除外）
    choices.remove(random.choice(delete_candidate))
    return select, choices

def no_change(correct):
    select, choices = intro(correct)
    return select

def change(correct):
    select, choices = intro(correct)
    return random.choice(choices)

LOOP_NUMBER = 1000

correct_number_nochange = 0
correct_number_change = 0
for cnt in range(LOOP_NUMBER):
    correct = random.randrange(HOLE_NUMBER)

    if no_change(correct) == correct:
        correct_number_nochange += 1
    if change(correct) == correct:
        correct_number_change += 1

print("選択を変えない場合の正答数：", correct_number_nochange, "    確率：", round(correct_number_nochange / LOOP_NUMBER * 100), "％")
print("選択を変えた場合の正答数：", correct_number_change, "    確率：", round(correct_number_change / LOOP_NUMBER * 100), "％")
    


