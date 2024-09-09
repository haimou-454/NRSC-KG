import pycorrector
import time
import sys
sys.path.append("..")
from pycorrector.macbert.macbert_corrector import MacBertCorrector
start =time.clock()

input_file = open("aAjoint/dccrn_jff/5db/decode_asr_branchformer_normalize_output_wavtrue_enh_asr_model_valid.acc.best/dev/text_spk1", "r", encoding="utf-8")
output_file = open("aAjoint/dccrn_jff/5db/decode_asr_branchformer_normalize_output_wavtrue_enh_asr_model_valid.acc.best/dev/text_spk1_mac", "w", encoding="utf-8")

m = MacBertCorrector()

for line in input_file:
    line = line.strip()
    chinese_text = line.split(" ")[1]

    correct_sent, err = m.macbert_correct(chinese_text)
    if correct_sent == '':
        correct_sent = chinese_text

    correct_line = line.split(" ")[0] + " " +correct_sent
    output_file.write(correct_line+"\n")

input_file.close()
output_file.close()

end = time.clock()
runtime = end - start
print("spend time:", runtime)
print("finished")