from transform import Transformer

DATASET1 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset1_Python+P7.csv"
DATASET2 = r"C:\OPENCLASSROOMS\PROJET 7 Résolvez des problèmes en utilisant des algorithmes en Python\SECTION 3\dataset2_Python+P7.csv"

transformer = Transformer()

# ---- test dataset 1 ----
rows = transformer.action_loader_dataset(DATASET1)
actions = transformer.transform_data_dataset(rows)

print("DATASET 1")
print("Valides :", len(actions))
print("Rejetées :", len(transformer.rejected_action))

reasons_count = {}
for r in transformer.rejected_action:
    reason = r["reason"]
    reasons_count[reason] = reasons_count.get(reason, 0) + 1

print("Détail rejets :", reasons_count)
print("Exemples rejets :", transformer.rejected_action[:5])

# ---- test dataset 2 ----
rows2 = transformer.action_loader_dataset(DATASET2)
actions2 = transformer.transform_data_dataset(rows2)

print("\nDATASET 2")
print("Valides :", len(actions2))
print("Rejetées :", len(transformer.rejected_action))
print("Exemples rejets :", transformer.rejected_action[:5])


