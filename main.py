total = 0

for a in range(4):
    print(f"\nQuarter {a + 1}")

    sa1 = float(input("SA1: "))
    sa2 = float(input("SA2: "))
    fa1 = float(input("FA1: "))
    fa2 = float(input("FA2: "))

    sa = ((sa1 + sa2) / 2) * 0.70
    fa = ((fa1 + fa2) / 2) * 0.30

    tentative_grade = sa + fa
    total += tentative_grade

final_grade = total / 4

if final_grade >= 96:
    equiv, status = "1.00", "EXCELLENT"
elif final_grade >= 90:
    equiv, status = "1.25", "VERY GOOD"
elif final_grade >= 84:
    equiv, status = "1.50", "VERY GOOD"
elif final_grade >= 78:
    equiv, status = "1.75", "GOOD"
elif final_grade >= 72:
    equiv, status = "2.00", "GOOD"
elif final_grade >= 66:
    equiv, status = "2.25", "SATISFACTORY"
elif final_grade >= 60:
    equiv, status = "2.50", "SATISFACTORY"
elif final_grade >= 55:
    equiv, status = "2.75", "FAIR"
elif final_grade >= 50:
    equiv, status = "3.00", "FAIR"
elif final_grade >= 40:
    equiv, status = "4.00", "FAILED ON CONDITION"
else:
    equiv, status = "5.00", "FAILED"

print("\nRESULT")
print(f"FINAL GRADE: {final_grade:.2f}")
print(f"EQUIVALENT: {equiv}")
print(f"STATUS: {status}")
