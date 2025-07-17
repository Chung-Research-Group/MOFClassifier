from MOFClassifier import CLscore
import glob


# ### parallel
cifs = glob.glob("./*.cif")

results = CLscore.predict_batch(root_cifs=cifs, model="core")
print("CoRE:", results)

results = CLscore.predict_batch(root_cifs=cifs, model="qsp")
print("CoRE+QMOF:", results)

# ### serial

cifs = glob.glob("./*.cif")

for cif in cifs:
    result = CLscore.predict(root_cif=cif, model="core")
    print("CoRE:", result)

for cif in cifs:
    result = CLscore.predict(root_cif=cif, model="qsp")
    print("CoRE+QMOF:", result)

### test HMOF

cifs = ["tobmof-1.cif", "tobmof-2.cif", "tobmof-3.cif"]
results = CLscore.predict_batch(root_cifs=cifs, model="h")
print("H:", results)