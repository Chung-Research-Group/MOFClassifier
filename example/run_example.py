from MOFClassifier import CLscore
import glob


### parallel
cifs = glob.glob("./*.cif")

results = CLscore.predict_batch(root_cifs=cifs)
print(results)

### serial

cifs = glob.glob("./*.cif")

for cif in cifs:
    result = CLscore.predict(root_cif=cif)
    print(result)