import pycorrector
import sys
sys.path.append("..")
from pycorrector.macbert.macbert_corrector import MacBertCorrector

m = MacBertCorrector()

def Macneo4j(line1, line2, line3, line4, line5):
    # if line1 == None and line2 == None:
    line = line1 + line2 + line3 + line4 + line5
    flag = (pycorrector.correct(line))[-1]
    if flag:
        text_new = (pycorrector.correct(line))[0]
        text_new3 = text_new[(len(line1)+len(line2)):(len(line1)+len(line2)+len(line3))]

        corrected_item = list()
        begin_idx = list()
        end_idx = list()

        corrected_item3 = list()
        begin_idx3 = list()
        end_idx3 = list()

        for i in range((pycorrector.correct(line))[-2]):
            corrected_item.append(list(str(((pycorrector.correct(line))[2][i][0]))))  # corrected_item = list(str(((pycorrector.correct(line))[2][0])))
            begin_idx.append((pycorrector.correct(line))[2][i][1])  # begin_idx, end_idx = ((pycorrector.correct(line))[2][1]), ((pycorrector.correct(line))[2][2])
            end_idx.append((pycorrector.correct(line))[2][i][2])
        # begin_idx, end_idx = begin_idx, end_idx-1
        for j in range(len(begin_idx)):
            if begin_idx[j] >= len(line1) + len(line2) and begin_idx[j] < len(line1) + len(line2) + len(line3):
                corrected_item3.append(corrected_item[j])
                begin_idx3.append(begin_idx[j] - (len(line1) + len(line2)))
                end_idx3.append(end_idx[j] - (len(line1) + len(line2)))

        correct_sent, err = m.macbert_correct2(text_new3, corrected_item3, begin_idx3, end_idx3)

    else:
        correct_sent, err = m.macbert_correct(line3)

    return correct_sent

input_file = open("AAorg/clean/text_spk1", "r", encoding="utf-8")
output_file = open("AAorg/clean/text_spk1_neo4j", "w", encoding="utf-8")

lines = input_file.readlines()
total_lines = len(lines)

for i in range(total_lines):
    lines[i] = lines[i].strip()
    current_chinese_text = lines[i].split(" ")[1]
    if i == 0:
        line1, line2, line3, line4, line5 = '', '', current_chinese_text, lines[i+1].split(" ")[1], lines[i+2].split(" ")[1]
        corrected = Macneo4j(line1, line2, line3, line4, line5)

    elif i == 1:
        line1, line2, line3, line4, line5 = '', lines[i-1].split(" ")[1], current_chinese_text, lines[i+1].split(" ")[1], lines[i+2].split(" ")[1]
        corrected = Macneo4j(line1, line2, line3, line4, line5)

    elif i == total_lines-2:
        line1, line2, line3, line4, line5 = lines[i-2].split(" ")[1], lines[i-1].split(" ")[1], current_chinese_text, lines[i+1].split(" ")[1], ''
        corrected = Macneo4j(line1, line2, line3, line4, line5)

    elif i == total_lines-1:
        line1, line2, line3, line4, line5 = lines[i-2].split(" ")[1], lines[i-1].split(" ")[1], current_chinese_text, '', ''
        corrected = Macneo4j(line1, line2, line3, line4, line5)

    else:
        line1, line2, line3, line4, line5 = lines[i-2].split(" ")[1], lines[i-1].split(" ")[1], current_chinese_text, lines[i+1].split(" ")[1], lines[i+2].split(" ")[1]
        corrected = Macneo4j(line1, line2, line3, line4, line5)

    correct_line = lines[i].split(" ")[0] + " " + corrected
    output_file.write(correct_line+"\n")

input_file.close()
output_file.close()

print("finished")


