from datetime import datetime, timedelta

print("=" * 50)
print("      WOMEN'S MENSTRUAL CYCLE TRACKER")
print("=" * 50)

# User Input
last_period = input("Enter first day of your last period (YYYY-MM-DD): ")
cycle_length = int(input("Enter your average cycle length (days): "))
period_duration = int(input("Enter your average period duration (days): "))

# Convert date
last_period_date = datetime.strptime(last_period, "%Y-%m-%d")

# Today's date
today = datetime.today()

# Calculations
next_period = last_period_date + timedelta(days=cycle_length)
ovulation_date = next_period - timedelta(days=14)

fertile_start = ovulation_date - timedelta(days=5)
fertile_end = ovulation_date + timedelta(days=1)

pms_start = next_period - timedelta(days=7)

current_cycle_day = (today - last_period_date).days + 1
days_until_period = (next_period - today).days

# Determine current phase
if current_cycle_day <= period_duration:
    phase = "Menstrual Phase"
elif current_cycle_day <= 13:
    phase = "Follicular Phase"
elif current_cycle_day <= 16:
    phase = "Ovulation Phase"
else:
    phase = "Luteal Phase"

# Results
print("\n" + "=" * 50)
print("               RESULTS")
print("=" * 50)

print("Last Period Start Date :", last_period_date.strftime("%d-%m-%Y"))
print("Next Expected Period   :", next_period.strftime("%d-%m-%Y"))
print("Ovulation Date         :", ovulation_date.strftime("%d-%m-%Y"))
print("Fertile Window Start   :", fertile_start.strftime("%d-%m-%Y"))
print("Fertile Window End     :", fertile_end.strftime("%d-%m-%Y"))
print("PMS May Start Around   :", pms_start.strftime("%d-%m-%Y"))
print("Current Cycle Day      :", current_cycle_day)
print("Days Until Next Period :", max(0, days_until_period))
print("Current Phase          :", phase)

print("\n" + "=" * 50)
print("HEALTH TIPS")
print("=" * 50)

if phase == "Menstrual Phase":
    print("\nDuring Menstruation:")
    print("✓ Stay hydrated")
    print("✓ Get enough rest")
    print("✓ Use a heating pad if needed")
    print("✓ Eat iron-rich foods")
    print("✓ Light exercise or walking")

    print("\nAvoid:")
    print("✗ Skipping meals")
    print("✗ Excess junk food")
    print("✗ Overexertion")
    print("✗ Lack of sleep")

elif phase == "Follicular Phase":
    print("\nDuring Follicular Phase:")
    print("✓ Focus on healthy nutrition")
    print("✓ Try new workouts")
    print("✓ Stay active")
    print("✓ Drink plenty of water")

    print("\nAvoid:")
    print("✗ Dehydration")
    print("✗ Excess processed food")

elif phase == "Ovulation Phase":
    print("\nDuring Ovulation:")
    print("✓ Maintain balanced nutrition")
    print("✓ Stay hydrated")
    print("✓ Monitor body changes")

    print("\nAvoid:")
    print("✗ Ignoring unusual symptoms")
    print("✗ Excessive stress")

else:
    print("\nDuring Luteal Phase:")
    print("✓ Eat magnesium-rich foods")
    print("✓ Prioritize sleep")
    print("✓ Manage stress")
    print("✓ Gentle exercise")

    print("\nAvoid:")
    print("✗ Too much caffeine")
    print("✗ High-sugar snacks")
    print("✗ Poor sleep habits")

print("\n" + "=" * 50)
print("IMPORTANT")
print("=" * 50)
print("This tracker provides estimates only.")
print("Actual cycle dates can vary from person to person.")
print("For medical concerns, consult a healthcare professional.")
print("=" * 50)
